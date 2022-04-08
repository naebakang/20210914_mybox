# File encoding: UTF-8

import os
import shutil
from absl import app, flags, logging
from absl.flags import FLAGS
import tensorflow as tf

# Control GPU before yolov4
physical_devices = tf.config.experimental.list_physical_devices('GPU')
assert len(physical_devices) > 0, "Not enough GPU hardware devices available"
tf.config.experimental.set_memory_growth(physical_devices[0], True)

from core.yolov4 import YOLO, decode, filter_boxes
import core.utils as utils
from core.config import cfg

from env import Directory

ins_env_directory = Directory()
dir_model = ins_env_directory.project_output_ground + r'/models'
if os.path.exists(dir_model):
    pass
else:
    os.mkdir(dir_model)

# flags.DEFINE_string('weights', './data/yolov4.weights', 'path to weights file')
# flags.DEFINE_string('weights', "./checkpoints/yolov4_advancement_1_20211001", 'path to weights file')
flags.DEFINE_string('weights', r"/D_drive/20200619_research_data/20210702_yolov4_without_darknet/20211103_advancement_8/weights/yolo-obj_final.weights", 'path to weights file')
flags.DEFINE_string('output', r'{}'.format(dir_model), 'path to output')
flags.DEFINE_boolean('tiny', False, 'is yolo-tiny or not')
flags.DEFINE_integer('input_size', 416, 'define input size of export model')
flags.DEFINE_float('score_thres', 0.2, 'define score threshold')
flags.DEFINE_string('framework', 'tf', 'define what framework do you want to convert (tf, trt, tflite)')
flags.DEFINE_string('model', 'yolov4', 'yolov3 or yolov4')


def save_tf():
    STRIDES, ANCHORS, NUM_CLASS, XYSCALE = utils.load_config(FLAGS)

    input_layer = tf.keras.layers.Input([FLAGS.input_size, FLAGS.input_size, 3])
    feature_maps = YOLO(input_layer, NUM_CLASS, FLAGS.model, FLAGS.tiny)
    bbox_tensors = []
    prob_tensors = []
    if FLAGS.tiny:
        for i, fm in enumerate(feature_maps):
            if i == 0:
                output_tensors = decode(fm, FLAGS.input_size // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FLAGS.framework)
            else:
                output_tensors = decode(fm, FLAGS.input_size // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FLAGS.framework)
            bbox_tensors.append(output_tensors[0])
            prob_tensors.append(output_tensors[1])
    else:
        for i, fm in enumerate(feature_maps):
            if i == 0:
                output_tensors = decode(fm, FLAGS.input_size // 8, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FLAGS.framework)
            elif i == 1:
                output_tensors = decode(fm, FLAGS.input_size // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FLAGS.framework)
            else:
                output_tensors = decode(fm, FLAGS.input_size // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, FLAGS.framework)
            bbox_tensors.append(output_tensors[0])
            prob_tensors.append(output_tensors[1])
        pred_bbox = tf.concat(bbox_tensors, axis=1)
        pred_prob = tf.concat(prob_tensors, axis=1)
    if FLAGS.framework == 'tflite':
        pred = (pred_bbox, pred_prob)
    else:
        boxes, pred_conf = filter_boxes(pred_bbox, pred_prob, score_threshold=FLAGS.score_thres, input_shape=tf.constant([FLAGS.input_size, FLAGS.input_size]))
        pred = tf.concat([boxes, pred_conf], axis=-1)
    model = tf.keras.Model(input_layer, pred)

    # utils.load_weights(model, FLAGS.weights, FLAGS.model, FLAGS.tiny)
    if FLAGS.weights.split(".")[len(FLAGS.weights.split(".")) - 1] == "weights":
        utils.load_weights(model, FLAGS.weights, FLAGS.model, FLAGS.tiny)  # for name.weight
    else:
        latest = tf.train.latest_checkpoint(ins_env_directory.weights_pretrained)
        model.load_weights(latest)  # for checkpoint

    model.summary()
    model.save(FLAGS.output)


def main(_argv):
    save_tf()


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
