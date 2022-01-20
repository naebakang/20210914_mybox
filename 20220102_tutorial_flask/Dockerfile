FROM wsgi:latest_20220120
COPY cudnn-11.2-linux-x64-v8.1.0.77.tgz /home
WORKDIR /home/
RUN tar xvzf cudnn-11.2-linux-x64-v8.1.0.77.tgz && cp cuda/include/cudnn*.h /usr/local/cuda-11.2/include && cp -P cuda/lib64/libcudnn* /usr/local/cuda-11.2/lib64 && chmod a+r /usr/local/cuda/include/cudnn*.h /usr/local/cuda-11.2/lib64/libcudnn*

