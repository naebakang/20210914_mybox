# File encoding: UTF-8

import pymysql
import pandas


class BotMySQL:
    def __init__(self, server='name_server', schema='name_db'):
        self.server = server
        self.schema = schema

    def get_df(self, sql):
        open_db, cursor = self.__get_open_db_and_cursor()

        cursor.execute(sql)
        result = cursor.fetchall()
        result = pandas.DataFrame(result)

        open_db.commit()  # commit은 모든 작업을 정상적으로 잘 처리하겠다고 확정하는 명령어
        open_db.close()

        return result

    def run_insert_data(self, sql, list_file_path, list_id_product, list_category_display):
        open_db, cursor = self.__get_open_db_and_cursor()

        for i in range(len(list_file_path)):
            cursor.execute(sql,
                           (
                               list_file_path[i],
                               list_id_product[i],
                               list_category_display[i],
                           ))
        open_db.commit()  # commit은 모든 작업을 정상적으로 잘 처리하겠다고 확정하는 명령어
        open_db.close()

    def __get_open_db_and_cursor(self):
        if self.server == 'name_server':
            user = ''
            passwd = ''
            host = ''
            port = 3306
            db = self.schema

        else:
            user = ''
            passwd = ''
            host = ''
            port = 1706
            db = self.schema

        open_db = pymysql.connect(
            user=user,
            passwd=passwd,
            host=host,
            port=port,
            db=db,
            charset='UTF8'
        )

        cursor = open_db.cursor(pymysql.cursors.DictCursor)

        return open_db, cursor


if __name__ == '__main__':
    ins = BotMySQL()
    sql = "INSERT INTO laboratory_boundingbox_webcrawling (file_path, id_product, category_display) VALUES(%s, %s, %s);"
    sql = "UPDATE button SET number_of_holes=%s WHERE number_of_holes=%s;"
    sql = "SELECT * FROM laboratory_check_webcrawling WHERE (validation_boundingbox LIKE 'N') and (usage_image LIKE 'confirm');"
    sql = '''CREATE TABLE laboratory_boundingbox_customer (
              `id` BIGINT(20) NOT NULL AUTO_INCREMENT,
              `file_path` LONGTEXT NOT NULL,
              `category` VARCHAR(255) NULL DEFAULT NULL,
              `x` DOUBLE NULL DEFAULT NULL,
              `y` DOUBLE NULL DEFAULT NULL,
              `width` DOUBLE NULL DEFAULT NULL,
              `height` DOUBLE NULL DEFAULT NULL,
              `created_at` DATETIME(6) NULL DEFAULT NULL,
              `admin_user` VARCHAR(45) NULL DEFAULT NULL,
              `id_check` BIGINT(20) NOT NULL,
                PRIMARY KEY (`id`))
                DEFAULT CHARACTER SET = utf8
                ENGINE = InnoDB;'''
