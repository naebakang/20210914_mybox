# File encoding: utf8

"""
"""

from flaskr import create_app

from flaskr.function.logging import start_logger
from flaskr.function.monitor import run_monitoring_for_memory_to_client

from flaskr.env import PathDirectory, PathFile

path_dir_log = PathDirectory.logs
start_logger(path_dir_log)

app = create_app()
port = 5000
# run_monitoring_for_memory(app, port)  # 20250724, app.run 하기 전에는 port 생성이 안된서 PID 가 안찍힌다.
run_monitoring_for_memory_to_client()

if __name__ == '__main__':
    app.run(debug=False, port=port)
