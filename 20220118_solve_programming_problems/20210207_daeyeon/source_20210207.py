# File encoding: UTF-8

import datetime
import IPython.display
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf

mpl.rcParams['figure.figsize'] = (8, 6)
mpl.rcParams['axes.grid'] = False
mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['figure.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 20

# The store dataset #####################################################################################
df = pd.read_excel('data.xlsx')
date_time = pd.to_datetime(df.pop('date'), format='%d.%m.%Y %H:%M:%S')

df.head()

# plot_cols = ['sales', 'net sales', 'amount', 'mean_consumer_price', 'discount_rate', 'SKU', 'Store']
# plot_features = df[plot_cols]
# plot_features.index = date_time
# _ = plot_features.plot(subplots=True)

# Inspect and cleanup
count = df.describe().transpose()

# Feature engineering
timestamp_s = date_time.map(datetime.datetime.timestamp)

day = 24*60*60
year = 365.2425 * day

df['Day sin'] = np.sin(timestamp_s * (2 * np.pi / day))
df['Day cos'] = np.cos(timestamp_s * (2 * np.pi / day))
df['Year sin'] = np.sin(timestamp_s * (2 * np.pi / year))
df['Year cos'] = np.cos(timestamp_s * (2 * np.pi / year))

# plt.plot(np.array(df['Day sin'])[:50])
# plt.plot(np.array(df['Day cos'])[:50])
# plt.plot(np.array(df['Year sin']))
# plt.plot(np.array(df['Year cos']))
# plt.xlabel('Time [Day]')
# plt.title('Time of day signal')

# fft = tf.signal.rfft(df['amount'])
# f_per_dataset = np.arange(0, len(fft))
#
# n_samples_h = len(df['amount'])
# hours_per_year = 24*365.2524
# years_per_dataset = n_samples_h/hours_per_year

# f_per_year = f_per_dataset/years_per_dataset
# plt.step(f_per_year, np.abs(fft))
# plt.xscale('log')
# plt.ylim(0, 400000)
# plt.xlim([0.1, max(plt.xlim())])
# plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
# _ = plt.xlabel('Frequency (log scale)')

# choose the data
# total = ['sales', 'net sales', 'amount', 'mean_consumer_price', 'discount_rate', 'SKU', 'Store', 'Day sin', 'Day cos', 'Year sin', 'Year cos']
total = df
df = total[['net sales', 'Year sin', 'Year cos']]
target = 'net sales'

# split the data
column_indices = {name: i for i, name in enumerate(df.columns)}

n = len(df)
train_df = df[0:int(n*0.7)]
val_df = df[int(n*0.7):int(n*0.9)]
test_df = df[int(n*0.9):]


# num of features
num_features = df.shape[1]

# normalize data
train_mean = train_df.mean()
train_std = train_df.std()

train_df = (train_df - train_mean) / train_std
val_df = (val_df - train_mean) / train_std
test_df = (test_df - train_mean) / train_std

# input-set
input_df = df.tail(31)
input_df = (input_df - train_mean) / train_std
input_df = np.array(input_df, dtype=np.float32)
input_df = input_df.reshape(1, 31, 3)

# df_std = (df - train_mean) / train_std
# df_std = df_std.melt(var_name='Column', value_name='Normalized')
# plt.figure(figsize=(12, 6))
# ax = sns.violinplot(x='Column', y='Normalized', data=df_std)
# _ = ax.set_xticklabels(df.keys(), rotation=90)


# Data windowing #########################################################################
# 1. Indexes and offsets
class WindowGenerator:
    def __init__(self, input_width, label_width, shift, train_df=train_df, val_df=val_df, test_df=test_df,
                 label_columns=None):
        # Store the raw data.
        self.train_df = train_df
        self.val_df = val_df
        self.test_df = test_df

        # Work out the label column indices.
        self.label_columns = label_columns
        if label_columns is not None:
            self.label_columns_indices = {name: i for i, name in
                                          enumerate(label_columns)}
        self.column_indices = {name: i for i, name in
                               enumerate(train_df.columns)}

        # Work out the window parameters.
        self.input_width = input_width
        self.label_width = label_width
        self.shift = shift

        self.total_window_size = input_width + shift

        self.input_slice = slice(0, input_width)
        self.input_indices = np.arange(self.total_window_size)[self.input_slice]

        self.label_start = self.total_window_size - self.label_width
        self.labels_slice = slice(self.label_start, None)
        self.label_indices = np.arange(self.total_window_size)[self.labels_slice]

    def __repr__(self):
        return '\n'.join([
            f'Total window size: {self.total_window_size}',
            f'Input indices: {self.input_indices}',
            f'Label indices: {self.label_indices}',
            f'Label column name(s): {self.label_columns}'])

    def make_dataset(self, data):
        data = np.array(data, dtype=np.float32)
        ds = tf.keras.preprocessing.timeseries_dataset_from_array(
            data=data,
            targets=None,
            sequence_length=self.total_window_size,
            sequence_stride=1,
            shuffle=True,
            batch_size=32, )

        ds = ds.map(self.split_window)
        print('ds: %s' % ds)

        return ds

    def split_window(self, features):
        inputs = features[:, self.input_slice, :]
        labels = features[:, self.labels_slice, :]
        if self.label_columns is not None:
            labels = tf.stack(
                [labels[:, :, self.column_indices[name]] for name in self.label_columns],
                axis=-1)

        # Slicing doesn't preserve static shape information, so set the shapes
        # manually. This way the `tf.data.Datasets` are easier to inspect.
        inputs.set_shape([None, self.input_width, None])
        labels.set_shape([None, self.label_width, None])

        return inputs, labels

    def plot(self, model=None, plot_col=target, max_subplots=3):
        inputs, labels = self.example
        plt.figure(figsize=(12, 8))
        plot_col_index = self.column_indices[plot_col]
        max_n = min(max_subplots, len(inputs))
        for n in range(max_n):
            plt.subplot(3, 1, n + 1)
            plt.ylabel(f'{plot_col} [normed]')
            plt.plot(self.input_indices, inputs[n, :, plot_col_index],
                     label='Inputs', marker='.', zorder=-10)

            if self.label_columns:
                label_col_index = self.label_columns_indices.get(plot_col, None)
            else:
                label_col_index = plot_col_index

            if label_col_index is None:
                continue

            plt.scatter(self.label_indices, labels[n, :, label_col_index],
                        edgecolors='k', label='Labels', c='#2ca02c', s=64)
            if model is not None:
                predictions = model(inputs)
                plt.scatter(self.label_indices, predictions[n, :, label_col_index],
                            marker='X', edgecolors='k', label='Predictions',
                            c='#ff7f0e', s=64)

            if n == 0:
                plt.legend()

        plt.xlabel('Time [Day]')


w1 = WindowGenerator(input_width=24, label_width=1, shift=24,
                     label_columns=[target])
print(w1)

w2 = WindowGenerator(input_width=6, label_width=1, shift=1,
                     label_columns=[target])
print(w2)


# 2. Split
# Stack three slices, the length of the total window:
example_window = tf.stack([np.array(train_df[:w2.total_window_size]),
                           np.array(train_df[100:100+w2.total_window_size]),
                           np.array(train_df[200:200+w2.total_window_size])])


example_inputs, example_labels = w2.split_window(example_window)

print('All shapes are: (batch, time, features)')
print(f'Window shape: {example_window.shape}')
print(f'Inputs shape: {example_inputs.shape}')
print(f'labels shape: {example_labels.shape}')


# 3. Plot
w2.example = example_inputs, example_labels
# w2.plot()


# 4. Create tf.data.Datasets
@property
def train(self):
    return self.make_dataset(self.train_df)


@property
def val(self):
    return self.make_dataset(self.val_df)


@property
def test(self):
    return self.make_dataset(self.test_df)


@property
def example(self):
    """Get and cache an example batch of `inputs, labels` for plotting."""
    result = getattr(self, '_example', None)
    if result is None:
        # No example batch was found, so get one from the `.train` dataset
        result = next(iter(self.train))
        # And cache it for next time
        self._example = result
    return result


WindowGenerator.train = train
WindowGenerator.val = val
WindowGenerator.test = test
WindowGenerator.example = example

# Each element is an (inputs, label) pair
w2.train.element_spec

for example_inputs, example_labels in w2.train.take(1):
    print(f'Inputs shape (batch, time, features): {example_inputs.shape}')
    print(f'Labels shape (batch, time, features): {example_labels.shape}')


# (single part) #######################################################################################################
MAX_EPOCHS = 20
def compile_and_fit(model, window, patience=2):
    early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss',
                                                      patience=patience,
                                                      mode='min')

    model.compile(loss=tf.losses.MeanSquaredError(),
                  optimizer=tf.optimizers.Adam(),
                  metrics=[tf.metrics.MeanAbsoluteError()])

    history = model.fit(window.train, epochs=MAX_EPOCHS,
                        validation_data=window.val,
                        callbacks=[early_stopping])

    return history


# Multi-step models ##################################################################################################
OUT_STEPS = 31
multi_window = WindowGenerator(input_width=31,
                               label_width=OUT_STEPS,
                               shift=OUT_STEPS)

# multi_window.plot()
multi_window


# ready to performance
multi_val_performance = {}
multi_performance = {}


# Baselines
# class MultiStepLastBaseline(tf.keras.Model):
#     def call(self, inputs):
#         return tf.tile(inputs[:, -1:, :], [1, OUT_STEPS, 1])
#
#
# last_baseline = MultiStepLastBaseline()
# last_baseline.compile(loss=tf.losses.MeanSquaredError(),
#                       metrics=[tf.metrics.MeanAbsoluteError()])
#
# multi_val_performance['Last'] = last_baseline.evaluate(multi_window.val)
# multi_performance['Last'] = last_baseline.evaluate(multi_window.test, verbose=0)
# multi_window.plot(last_baseline)


class RepeatBaseline(tf.keras.Model):
    def call(self, inputs):
        return inputs


repeat_baseline = RepeatBaseline()
repeat_baseline.compile(loss=tf.losses.MeanSquaredError(),
                        metrics=[tf.metrics.MeanAbsoluteError()])

multi_val_performance['Baseline'] = repeat_baseline.evaluate(multi_window.val)
multi_performance['Baseline'] = repeat_baseline.evaluate(multi_window.test, verbose=0)
# multi_window.plot(repeat_baseline)


# Single-shot models - linear
multi_linear_model = tf.keras.Sequential([
    # Take the last time-step.
    # Shape [batch, time, features] => [batch, 1, features]
    tf.keras.layers.Lambda(lambda x: x[:, -1:, :]),
    # Shape => [batch, 1, out_steps*features]
    tf.keras.layers.Dense(OUT_STEPS*num_features,
                          kernel_initializer=tf.initializers.zeros),
    # Shape => [batch, out_steps, features]
    tf.keras.layers.Reshape([OUT_STEPS, num_features])
])

history = compile_and_fit(multi_linear_model, multi_window)

IPython.display.clear_output()
multi_val_performance['Linear'] = multi_linear_model.evaluate(multi_window.val)
multi_performance['Linear'] = multi_linear_model.evaluate(multi_window.test, verbose=0)
# multi_window.plot(multi_linear_model)

# Single-shot models - dense
# multi_dense_model = tf.keras.Sequential([
#     # Take the last time step.
#     # Shape [batch, time, features] => [batch, 1, features]
#     tf.keras.layers.Lambda(lambda x: x[:, -1:, :]),
#     # Shape => [batch, 1, dense_units]
#     tf.keras.layers.Dense(512, activation='relu'),
#     # Shape => [batch, out_steps*features]
#     tf.keras.layers.Dense(OUT_STEPS*num_features,
#                           kernel_initializer=tf.initializers.zeros),
#     # Shape => [batch, out_steps, features]
#     tf.keras.layers.Reshape([OUT_STEPS, num_features])
# ])
#
# history = compile_and_fit(multi_dense_model, multi_window)
#
# IPython.display.clear_output()
# multi_val_performance['Dense'] = multi_dense_model.evaluate(multi_window.val)
# multi_performance['Dense'] = multi_dense_model.evaluate(multi_window.test, verbose=0)
# multi_window.plot(multi_dense_model)  # warning

# Single-shot models - cnn
CONV_WIDTH = 3
multi_conv_model = tf.keras.Sequential([
    # Shape [batch, time, features] => [batch, CONV_WIDTH, features]
    tf.keras.layers.Lambda(lambda x: x[:, -CONV_WIDTH:, :]),
    # Shape => [batch, 1, conv_units]
    tf.keras.layers.Conv1D(256, activation='relu', kernel_size=(CONV_WIDTH)),
    # Shape => [batch, 1,  out_steps*features]
    tf.keras.layers.Dense(OUT_STEPS*num_features,
                          kernel_initializer=tf.initializers.zeros),
    # Shape => [batch, out_steps, features]
    tf.keras.layers.Reshape([OUT_STEPS, num_features])
])

history = compile_and_fit(multi_conv_model, multi_window)

IPython.display.clear_output()

multi_val_performance['CNN'] = multi_conv_model.evaluate(multi_window.val)
multi_performance['CNN'] = multi_conv_model.evaluate(multi_window.test, verbose=0)
# multi_window.plot(multi_conv_model)

# Single-shot models - rnn
multi_lstm_model = tf.keras.Sequential([
    # Shape [batch, time, features] => [batch, lstm_units]
    # Adding more `lstm_units` just overfits more quickly.
    tf.keras.layers.LSTM(32, return_sequences=False),
    # Shape => [batch, out_steps*features]
    tf.keras.layers.Dense(OUT_STEPS*num_features,
                          kernel_initializer=tf.initializers.zeros),
    # Shape => [batch, out_steps, features]
    tf.keras.layers.Reshape([OUT_STEPS, num_features])
])

history = compile_and_fit(multi_lstm_model, multi_window)

IPython.display.clear_output()

multi_val_performance['LSTM'] = multi_lstm_model.evaluate(multi_window.val)
multi_performance['LSTM'] = multi_lstm_model.evaluate(multi_window.test, verbose=0)
# multi_window.plot(multi_lstm_model)


# Advanced: Autoregressive model - rnn
# class FeedBack(tf.keras.Model):
#     def __init__(self, units, out_steps):
#         super().__init__()
#         self.out_steps = out_steps
#         self.units = units
#         self.lstm_cell = tf.keras.layers.LSTMCell(units)
#         # Also wrap the LSTMCell in an RNN to simplify the `warmup` method.
#         self.lstm_rnn = tf.keras.layers.RNN(self.lstm_cell, return_state=True)
#         self.dense = tf.keras.layers.Dense(num_features)
#
#     def warmup(self, inputs):
#         # inputs.shape => (batch, time, features)
#         # x.shape => (batch, lstm_units)
#         x, *state = self.lstm_rnn(inputs)
#
#         # predictions.shape => (batch, features)
#         prediction = self.dense(x)
#         return prediction, state
#
#     def call(self, inputs, training=None):
#         # Use a TensorArray to capture dynamically unrolled outputs.
#         predictions = []
#         # Initialize the lstm state
#         prediction, state = self.warmup(inputs)
#
#         # Insert the first prediction
#         predictions.append(prediction)
#
#         # Run the rest of the prediction steps
#         for n in range(1, self.out_steps):
#             # Use the last prediction as input.
#             x = prediction
#             # Execute one lstm step.
#             x, state = self.lstm_cell(x, states=state,
#                                       training=training)
#             # Convert the lstm output to a prediction.
#             prediction = self.dense(x)
#             # Add the prediction to the output
#             predictions.append(prediction)
#
#         # predictions.shape => (time, batch, features)
#         predictions = tf.stack(predictions)
#         # predictions.shape => (batch, time, features)
#         predictions = tf.transpose(predictions, [1, 0, 2])
#         return predictions
#
#
# feedback_model = FeedBack(units=32, out_steps=OUT_STEPS)
# prediction, state = feedback_model.warmup(multi_window.example[0])
# prediction.shape
#
# print('Output shape (batch, time, features): ', feedback_model(multi_window.example[0]).shape)
#
# history = compile_and_fit(feedback_model, multi_window)
#
# IPython.display.clear_output()
#
# multi_val_performance['AR LSTM'] = feedback_model.evaluate(multi_window.val)
# multi_performance['AR LSTM'] = feedback_model.evaluate(multi_window.test, verbose=0)
# multi_window.plot(feedback_model)


# Performance
x = np.arange(len(multi_performance))
width = 0.3


metric_name = 'mean_absolute_error'
metric_index = multi_lstm_model.metrics_names.index('mean_absolute_error')
val_mae = [v[metric_index] for v in multi_val_performance.values()]
test_mae = [v[metric_index] for v in multi_performance.values()]

plt.bar(x - 0.17, val_mae, width, label='Validation')
plt.bar(x + 0.17, test_mae, width, label='Test')
plt.xticks(ticks=x, labels=multi_performance.keys(),
           rotation=45)
plt.ylabel(f'MAE (average over all times and outputs)')
_ = plt.legend()

output = pd.DataFrame()
for name, value in multi_performance.items():
    print(f'{name:8s}: {value[1]:0.4f}')

    dff = pd.DataFrame([[name,
                         value[1]]],
                       columns=['name',
                                'value'])

    output = output.append(dff)

output.to_excel('output.xlsx',
                sheet_name='sheet1',
                index=True,
                index_label='section',
                float_format='%.4f'
                )


def translate_prediction(aa):
    bb = aa*train_std[0] + train_mean[0]
    bb = np.rint(bb)
    bb = (bb[0][:, 0]).astype(np.int64)
    bb = pd.Series(bb)
    return bb


cc = pd.concat([translate_prediction(multi_linear_model.predict(input_df)),
                translate_prediction(multi_conv_model.predict(input_df)),
                translate_prediction(multi_lstm_model.predict(input_df))],
               axis=1)

cc.to_excel('prediction_2.xlsx',
            sheet_name='sheet1',
            index=True,
            index_label='section',
            float_format='%.4f'
            )
