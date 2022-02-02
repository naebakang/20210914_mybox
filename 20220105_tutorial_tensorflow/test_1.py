import tensorflow as tf
import tensorflow.keras.layers as layers
import numpy as np

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

x = np.random.normal(size=(100, 28, 28, 1)).astype(np.float32)
y = np.zeros([100, 10], dtype=np.float32)
y[:, 1] = 1.

train_ds = tf.data.Dataset.from_tensor_slices((x, y)).shuffle(buffer_size=100).batch(32)
num_classes = 10

model = tf.keras.Sequential([
    layers.Conv2D(16, 3, padding='same', activation='relu'),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(num_classes)
])
model.compile(optimizer='adam',
    loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'])
epochs=10
history = model.fit(
    train_ds,
    epochs=epochs
)
