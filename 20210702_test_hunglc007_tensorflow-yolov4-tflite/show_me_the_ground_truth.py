# File encoding: UTF-8

from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import os
import shutil
import numpy as np
import copy

import change_coordinate

from core.yolov4 import filter_boxes
from tensorflow.python.saved_model import tag_constants
import core.utils as utils
from core.config import cfg

# flags.DEFINE_string('weights', './checkpoints/yolov4-416',
#                     'path to weights file')
flags.DEFINE_string('weights', './checkpoints/yolov4_5',
                    'path to weights file')
flags.DEFINE_string('framework', 'tf', 'select model type in (tf, tflite, trt)'
                    'path to weights file')
flags.DEFINE_string('model', 'yolov4', 'yolov3 or yolov4')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
# flags.DEFINE_string('annotation_path', "./data/dataset/val2017.txt", 'annotation path')
flags.DEFINE_string('annotation_path', "./data/dataset/train.txt", 'annotation path')
flags.DEFINE_string('write_image_path', "./data/detection/", 'write image path')
flags.DEFINE_float('iou', 0.5, 'iou threshold')
flags.DEFINE_float('score', 0.25, 'score threshold')


def main(_argv):
    INPUT_SIZE = FLAGS.size
    STRIDES, ANCHORS, NUM_CLASS, XYSCALE = utils.load_config(FLAGS)
    CLASSES = utils.read_class_names(cfg.YOLO.CLASSES)

    path_file = './data/show_ground_truth/'
    if os.path.exists(path_file): shutil.rmtree(path_file)
    os.mkdir(path_file)

    # # Build Model
    # if FLAGS.framework == 'tflite':
    #     interpreter = tf.lite.Interpreter(model_path=FLAGS.weights)
    #     interpreter.allocate_tensors()
    #     input_details = interpreter.get_input_details()
    #     output_details = interpreter.get_output_details()
    #     print(input_details)
    #     print(output_details)
    # else:
    #     pass

    num_lines = sum(1 for line in open(FLAGS.annotation_path))
    with open(cfg.TEST.ANNOT_PATH, 'r') as annotation_file:
        boxes_kjw = np.zeros((1, 50, 4), dtype=np.float32)
        scores = np.zeros((1, 50), dtype=np.float32)
        classes = np.zeros((1, 50), dtype=np.float32)
        for num, line in enumerate(annotation_file):
            annotation = line.strip().split()
            image_path = annotation[0]
            image_name = image_path.split('/')[-1]
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            root, _ = os.path.splitext(image_path)
            idx, _ = os.path.splitext(image_name)
            with open(root + ".txt") as fd:
                boxes = fd.readlines()
                boxes_clean = []
                for i in boxes:
                    boxes_clean.append(i.rstrip('\n'))
            bbox_data_gt = np.array([list(map(float, box.split())) for box in boxes_clean])

            if len(bbox_data_gt) == 0:
                bboxes_gt = []
                classes_gt = []
            else:
                classes_gt, bboxes_gt = bbox_data_gt[:, :1], bbox_data_gt[:, 1:5]
                classes_gt = classes_gt.astype(np.int)


            print('=> ground truth of %s:' % image_name)
            num_bbox_gt = len(bboxes_gt)
            image_h, image_w, _ = image.shape
            for i in range(num_bbox_gt):
                boxes_kjw[:, i, :] = bboxes_gt[i]
                scores[:, i] = 0.99
                classes[:, i] = classes_gt[i][0]

            valid_detections = np.array([num_bbox_gt], dtype=np.int32)
            # boxess = copy.deepcopy(boxes_kjw)
            boxess = change_coordinate.get_bunch_min_max_coor(boxes_kjw)

            # # temporary
            # import pickle
            # with open('kjw,pickle', 'rb') as rb:
            #     kjw = pickle.load(rb)


            # boxes, scores, classes, valid_detections = [boxes_kjw.numpy(), scores.numpy(), classes.numpy(), valid_detections.numpy()]
            # image_result = utils.draw_bbox(np.copy(image), [kjw[0], kjw[1], kjw[2], kjw[3]])
            image_result = utils.draw_bbox(np.copy(image), [boxess, scores, classes, valid_detections])
            cv2.imwrite(path_file + image_name, image_result)

            print(num, num_lines)


if __name__ == '__main__':
    try:
        app.run(main)
    except SystemExit:
        pass
