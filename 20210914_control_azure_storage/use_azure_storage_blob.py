# File encoding: UTF-8

import os
from azure.storage.blob import BlobServiceClient


class BotAzureStorage:
    def __init__(self, container):
        # https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
        # Windows - cmd
        # setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"
        self.connection_str = os.environ['AZURE_STORAGE_CONNECTION_STRING']

        self.container = container
        self.list_file_path = []

    def get_list_file_path(self, prefix):
        service_client = BlobServiceClient.from_connection_string(self.connection_str)
        container_client = service_client.get_container_client(self.container)

        self.__get_file_path(container_client=container_client, prefix=prefix)

        return self.list_file_path

    def __get_file_path(self, container_client, prefix):
        ins = container_client.walk_blobs(name_starts_with=prefix)
        for i in ins:
            file_path = i.name
            if file_path[-1] == '/':
                self.__get_file_path(container_client=container_client, prefix=file_path)
            else:
                self.list_file_path.append(file_path)
                print(file_path)


if __name__ == '__main__':
    ins = BotAzureStorage(container='name_container')
    list_file_path = ins.get_list_file_path(prefix='name_folder/')
