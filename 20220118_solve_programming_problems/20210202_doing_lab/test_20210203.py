import tensorflow as tf
import PIL.Image
import numpy

from mrcnn import visualize
import mrcnn.model
from Mask_RCNN.samples.balloon import balloon


config = balloon.BalloonConfig()


# Override the training configurations with a few
# changes for inferencing.
class InferenceConfig(config.__class__):
    # Run detection on one image at a time
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
config.display()


def test_mask_rcnn(weights_path, test_image_path):
    # Create model in inference mode
    DEVICE = "/gpu:0"  # /cpu:0 or /gpu:0
    with tf.device(DEVICE):
        model = mrcnn.model.MaskRCNN(mode="inference", model_dir='./logs',
                                     config=config)

    # Load weights
    print("Loading weights ", weights_path)
    model.load_weights(weights_path, by_name=True, exclude=[ "mrcnn_class_logits", "mrcnn_bbox_fc", "mrcnn_bbox", "mrcnn_mask"])

    # Run object detection
    image = PIL.Image.open(test_image_path)
    image = numpy.array(image)
    results = model.detect([image], verbose=1)

    # Display results
    r = results[0]
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'],
                                ['BG', 'balloon'], r['scores'], ax=None,
                                title="Predictions", figsize=(16, 16),
                                show_mask=False)


weights_path = 'model_weight.h5'
test_image_path = 'test1.jpg'
test_mask_rcnn(weights_path, test_image_path)
