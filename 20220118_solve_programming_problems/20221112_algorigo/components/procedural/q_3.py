# File encoding: utf8

import tensorflow as tf
from tensorflow import feature_column
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split

from sklearn.cluster import KMeans

import pandas

from components.functional.base import Memory

from components.env import Name, PathDirectory


class Cluster:
    def __init__(self):
        self.ins_base_memory = Memory()

        self.ins_env_name = Name()
        self.ins_env_pathdirectory = PathDirectory()

    def run(self):
        # Load data
        data_unlabeled = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="unlabeled",
            extension="csv"
        )

        data_unlabeled = data_unlabeled.dropna(axis=0)
        data_unlabeled = self.__get_df_only_num(data_unlabeled)
        data_unlabeled.isnull().sum()

        self.create_label(data_unlabeled)
        self.__print_accuracy()

    def __print_accuracy(self):
        data_train = self.ins_base_memory.get_cumulate_recent_saved_data(
            len_now_time=12,
            directory=self.ins_env_pathdirectory.project_output,
            file_group_name="unlabeled_new",
            extension="csv"
        )

        data_test = self.ins_base_memory.get_cover_saved_data(
            directory=self.ins_env_pathdirectory.raw_data,
            file_name="test",
            extension="csv"
        )

        index = data_train.pop("index")
        idd = data_test.pop("id")

        data_train = data_train.dropna(axis=1)
        data_train = data_train.rename(columns={'Online boarding': 'Online_boarding'})
        data_train = data_train.rename(columns={'Inflight entertainment': 'Inflight_entertainment'})
        data_train = data_train.rename(columns={'Seat comfort': 'Seat_comfort'})
        data_train = data_train.rename(columns={'On-board service': 'On-board_service'})
        data_train = data_train.rename(columns={'Leg room service': 'Leg_room_service'})

        data_test = data_test.rename(columns={'Online boarding': 'Online_boarding'})
        data_test = data_test.rename(columns={'Inflight entertainment': 'Inflight_entertainment'})
        data_test = data_test.rename(columns={'Seat comfort': 'Seat_comfort'})
        data_test = data_test.rename(columns={'On-board service': 'On-board_service'})
        data_test = data_test.rename(columns={'Leg room service': 'Leg_room_service'})

        data_train = self.__get_df_only_num(data_train)
        data_test = self.__get_df_only_num(data_test)

        # Split data
        train, val = train_test_split(data_train, test_size=0.2)

        # Feature columns
        # numeric
        feature_columns = []
        for header in ['Online_boarding', 'Inflight_entertainment', 'Seat_comfort', 'On-board_service', 'Leg_room_service']:
            feature_columns.append(feature_column.numeric_column(header))

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

    def create_label(self, data_unlabeled):
        # ret, label, center = self.__get_r_l_c(data_unlabeled)
        data = data_unlabeled.iloc[:, 1:23]
        data = data.reset_index(drop=True)

        kmeans = KMeans(n_clusters=2)
        kmeans.fit(data)

        label = kmeans.labels_
        label = pandas.Series(label)

        df_new = pandas.concat([data, label], axis=1)
        df_new = df_new.rename(columns={0: 'satisfaction'})

        sum_0 = df_new["Online boarding"][df_new["satisfaction"]==0].sum()
        sum_1 = df_new["Online boarding"][df_new["satisfaction"]==1].sum()

        if sum_0 <= sum_1:
            pass
        else:
            index_0 = df_new["Flight Distance"][df_new["satisfaction"]==0].index
            index_1 = df_new["Flight Distance"][df_new["satisfaction"]==1].index

            for i in index_0:
                df_new.iloc[i, 22] = 1

            for i in index_1:
                df_new.iloc[i, 22] = 0

        self.ins_base_memory.create_cumulate_csv(
            directory=self.ins_env_pathdirectory.project_output,
            file_name="unlabeled_new",
            df=df_new
        )

    # 판다스 데이터프레임으로부터 tf.data 데이터셋을 만들기 위한 함수
    def df_to_dataset(self, dataframe, shuffle=True, batch_size=32):
        dataframe = dataframe.copy()
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
    ins = Cluster()
    ins.run()
