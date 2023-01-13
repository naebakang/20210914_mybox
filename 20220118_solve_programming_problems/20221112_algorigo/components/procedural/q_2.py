# File encoding: utf8

import tensorflow as tf
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

from components.functional.base import Memory

from components.env import Name, PathDirectory


class Test:
    def __init__(self):
        self.ins_base_memory = Memory()

        self.ins_env_name = Name()
        self.ins_env_pathdirectory = PathDirectory()

    def run(self):
        # Load data
        data_train = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="train",
            extension="csv"
        )

        data_test = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="test",
            extension="csv"
        )

        data_unlabeled = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="unlabeled",
            extension="csv"
        )

        data_train = data_train.dropna(axis=1)
        data_train = data_train.rename(columns={'Flight Distance': 'Flight_Distance'})
        data_train = data_train.rename(columns={'Inflight wifi service': 'Inflight_wifi_service'})
        data_train = data_train.rename(columns={'Gate location': 'Gate_location'})
        data_train = data_train.rename(columns={'Type of Travel': 'Type_of_Travel'})
        data_train = data_train.rename(columns={'Customer Type': 'Customer_Type'})
        data_train = data_train.rename(columns={'Food and drink': 'Food_and_drink'})
        data_train = data_train.rename(columns={'Ease of Online booking': 'Ease_of_Online_booking'})
        data_train = data_train.rename(columns={'Departure/Arrival time convenient': 'Departure/Arrival_time_convenient'})

        data_test = data_test.rename(columns={'Flight Distance': 'Flight_Distance'})
        data_test = data_test.rename(columns={'Inflight wifi service': 'Inflight_wifi_service'})
        data_test = data_test.rename(columns={'Gate location': 'Gate_location'})
        data_test = data_test.rename(columns={'Type of Travel': 'Type_of_Travel'})
        data_test = data_test.rename(columns={'Customer Type': 'Customer_Type'})
        data_test = data_test.rename(columns={'Food and drink': 'Food_and_drink'})
        data_test = data_test.rename(columns={'Ease of Online booking': 'Ease_of_Online_booking'})
        data_test = data_test.rename(columns={'Departure/Arrival time convenient': 'Departure/Arrival_time_convenient'})

        data_train = self.__get_df_only_num(data_train)
        data_test = self.__get_df_only_num(data_test)
        data_unlabeled = self.__get_df_only_num(data_unlabeled)

        # Split data
        train, val = train_test_split(data_train, test_size=0.2)

        # Feature columns
        # numeric
        feature_columns = []
        for header in ['Age', 'Flight_Distance', 'Inflight_wifi_service', 'Departure/Arrival_time_convenient', 'Ease_of_Online_booking', 'Food_and_drink']:
            feature_columns.append(feature_column.numeric_column(header))
        # for header in ['Age']:
        #     feature_columns.append(feature_column.numeric_column(header))

        # categorical
        gender = feature_column.categorical_column_with_vocabulary_list(
            'Gender', [0, 1])
        gender_one_hot = feature_column.indicator_column(gender)
        feature_columns.append(gender_one_hot)

        customer_type = feature_column.categorical_column_with_vocabulary_list(
            'Customer_Type', [0, 1])
        customer_type_one_hot = feature_column.indicator_column(customer_type)
        feature_columns.append(customer_type_one_hot)

        type_of_travel = feature_column.categorical_column_with_vocabulary_list(
            'Type_of_Travel', [0, 1])
        type_of_travel_one_hot = feature_column.indicator_column(type_of_travel)
        feature_columns.append(type_of_travel_one_hot)

        class_d = feature_column.categorical_column_with_vocabulary_list(
            'Class', [0, 1, 2])
        class_d_one_hot = feature_column.indicator_column(class_d)
        feature_columns.append(class_d_one_hot)

        gate_location = feature_column.categorical_column_with_vocabulary_list(
            'Gate_location', [1, 2, 3, 4, 5])
        gate_location_one_hot = feature_column.indicator_column(gate_location)
        feature_columns.append(gate_location_one_hot)

        feature_layer = tf.keras.layers.DenseFeatures(feature_columns)

        # Input pipeline
        batch_size = 32
        train_ds = self.df_to_dataset(train, batch_size=batch_size)
        val_ds = self.df_to_dataset(val, shuffle=False, batch_size=batch_size)
        test_ds = self.df_to_dataset(data_test, shuffle=False, batch_size=batch_size)

        # Model
        model = tf.keras.Sequential([
            feature_layer,
            layers.Dense(128, activation='relu'),
            layers.Dense(128, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])

        model.compile(optimizer='adam',
                      loss='binary_crossentropy',
                      metrics=['accuracy'])

        model.fit(train_ds,
                  validation_data=val_ds,
                  epochs=5)

        loss, accuracy = model.evaluate(test_ds)
        print("Accuracy", accuracy)

        a = model.predict(test_ds)

    # tf.data
    def df_to_dataset(self, dataframe, shuffle=True, batch_size=32):
        dataframe = dataframe.copy()
        idd = dataframe.pop('id')
        labels = dataframe.pop('satisfaction')
        ds = tf.data.Dataset.from_tensor_slices((dict(dataframe), labels))
        if shuffle:
            ds = ds.shuffle(buffer_size=len(dataframe))
        ds = ds.batch(batch_size)

        return ds

    def __get_df_only_num(self, df):
        for key, value in self.ins_env_name.dic_total.items():
            df = df.replace(key, value)

        df_only_num = df

        return df_only_num


if __name__ == "__main__":
    ins = Test()
    ins.run()
