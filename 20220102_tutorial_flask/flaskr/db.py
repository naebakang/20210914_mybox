# File encoding: utf8

import pymysql

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db(passwd):
    if 'db' not in g:
        db_mariadb = pymysql.connect(
            user='root',
            passwd=passwd,
            host='172.0.0.1',
            port='3306',
            db='flaskr',
            charset='UTF8'
        )
        g.db = db_mariadb.cursor(pymysql.cursors.DictCursor)

    return g.db


def close_db(passwd):
    db_mariadb = pymysql.connect(
        user='root',
        passwd=passwd,
        host='127.0.0.1',
        port=3306,
        db='flaskr',
        charset='UTF8'
    )
    db_mariadb.close()


def init_db(passwd):
    db = get_db(passwd)

    with current_app.open_resource('schema.sql') as f:
        db.execute(f.read().decode('utf8'))


@click.command("init-db")
@click.option('--passwd')
@with_appcontext
def init_db_command(passwd):
    """Clear existing data and create new tables."""
    # init_db(passwd)
    click.echo("Initialized the database.")


def init_app(app, passwd):
    app.teardown_appcontext(close_db(passwd))
    app.cli.add_command(init_db_command)


if __name__ == '__main__':
    print(1234)
