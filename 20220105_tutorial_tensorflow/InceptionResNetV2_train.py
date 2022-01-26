import matplotlib.pyplot as plt
import numpy as np
import time
import glob
import tensorflow as tf
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import Callback

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# from keras.backend.tensorflow_backend import set_session
# config = tf.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.3
# set_session(tf.Session(config=config))


# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)


# try:
#     tf_gpus = tf.config.list_physical_devices('GPU')
#     for gpu in tf_gpus:
#         tf.config.experimental.set_memory_growth(gpu, True)
# except:
#     pass


# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#   # 텐서플로가 첫 번째 GPU에 1GB 메모리만 할당하도록 제한
#   try:
#     tf.config.experimental.set_virtual_device_configuration(
#         gpus[0],
#         [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=1024)])
#   except RuntimeError as e:
#     # 프로그램 시작시에 가상 장치가 설정되어야만 합니다
#     print(e)


# problem
# 하나의 데이터 폴더에서 train, valid, test 가 구분 될 수 있도록 수정 요망

# tensorflow-gpu-2.0.0
print('tensorflow:\t' + tf.version.VERSION)
print(tf.test.is_gpu_available())

# gpus = tf.config.list_physical_devices('GPU')
# if gpus:
#   # Restrict TensorFlow to only use the first GPU
#   try:
#     tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
#     logical_gpus = tf.config.experimental.list_logical_devices('GPU')
#     print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
#   except RuntimeError as e:
#     # Visible devices must be set before GPUs have been initialized
#     print(e)


# with tf.device('/GPU:0'):
weight_ver = '01'
img_size = 300
train_data_dir = r'/home/woong/20210205_project/20210205_data/20200526_train'
valid_data_dir = r'/home/woong/20210205_project/20210205_data/20200526_dev'

base_path = './weights/vae_classification_{0}_InceptionResNetV2_{1}.{2}'
base_path2 = './weights/vae_classification_{0}_InceptionResNetV2_{1}_{2}.{3}'
loss_path = base_path.format('loss', weight_ver, 'png')
acc_path = base_path.format('acc', weight_ver, 'png')
weights_path = base_path.format('weights', weight_ver, 'h5')

freeze_layers = 780 - 162
class_num = 2  # 11

train_image_count = len(glob.glob(f'{train_data_dir}/**/*.png'))
valid_image_count = len(glob.glob(f'{valid_data_dir}/**/*.png'))
batch_size = 4  # 64
epochs = 5
steps_per_epoch = train_image_count // batch_size
valid_steps_per = valid_image_count // batch_size
# steps_per_epoch = batch_size * 10
# valid_steps_per = batch_size * 10

# ==================== 모델 정의 ====================
base_model = InceptionResNetV2(
    weights='imagenet',
    input_shape=(img_size, img_size, 3),
    include_top=False)
# ==================== 분류 classification layer ====================
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(units=class_num, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

for layer in model.layers[:freeze_layers]:
    layer.trainable = False
# 레이어 가중치 동결 확인
for layer in model.layers:
    print(layer, layer.trainable)
# cost 정의
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['acc'])
# 저장된 weights 로드
# model.load_weights(weights_path)
# 레이어 확인
model.summary()
print('layers: ' + str(len(model.layers)))
# ==================== 모델 정의 END ====================

print('END')

# ==================== 학습데이터 정의 ====================
# 학습할 이미지 변형 설정 (회전, 줌 등등)
train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.7,
    zoom_range=[0.9, 2.2],
    channel_shift_range=10,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest'
)
# 검증할 이미지 변형 설정 (회전, 줌 등등)
valid_datagen = ImageDataGenerator(
    rescale=1. / 255
)
# 학습할 이미지 크기, 배치, 분류 설정
train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical')

# 검증할 이미지 크기, 배치, 분류 설정
valid_generator = valid_datagen.flow_from_directory(
    valid_data_dir,
    target_size=(img_size, img_size),
    batch_size=batch_size,
    class_mode='categorical')
# ==================== 학습데이터 정의 END ====================

# ==================== 학습 시작 ====================
start_time = time.time()


class Evaluate(Callback):
    def __init__(self):
        import os
        self.lowest = 1e10
        self.losses = []
        if not os.path.exists('weights'):
            os.mkdir('weights')

    def on_epoch_end(self, epoch, logs=None):
        save_path = base_path2.format('weights', weight_ver, epoch, 'h5')
        # 학습된 weights 저장
        model.save_weights(save_path)


evaluator = Evaluate()

history = model.fit(
    x=train_generator,
    epochs=epochs,
    steps_per_epoch=steps_per_epoch,
    validation_data=valid_generator,
    validation_steps=valid_steps_per,
    callbacks=[evaluator]
)

print("%s분" % ((time.time() - start_time) / 60))
# ==================== 학습 시작 END ====================

# 그래프 출력
# 손실
y_val_loss = history.history['val_loss']
y_loss = history.history['loss']

x_len_loss = np.arange(len(y_loss))
plt.plot(x_len_loss, y_val_loss, marker='.', c='red', label="valid loss")
plt.plot(x_len_loss, y_loss, marker='.', c='blue', label="train loss")

plt.legend(loc='upper right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.savefig(loss_path)
plt.show()

# 정확도
y_val_acc = history.history['val_acc']
y_acc = history.history['acc']
x_len_acc = np.arange(len(y_acc))
plt.plot(x_len_acc, y_val_acc, marker='.', c='red', label="valid acc")
plt.plot(x_len_acc, y_acc, marker='.', c='blue', label="train acc")

plt.legend(loc='lower right')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('acc')
plt.savefig(acc_path)
plt.show()

print('END')
