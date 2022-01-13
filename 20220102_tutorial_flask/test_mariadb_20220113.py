import pymysql

db_mariadb = pymysql.connect(
        user='root',
        passwd='test',
        host='127.0.0.1',
        port=3306,
        db='flaskr',
        charset='UTF8'
    )
