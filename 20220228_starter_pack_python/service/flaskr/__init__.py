# File encoding: utf8

import os
from flask import Flask, jsonify
from . import env
from loguru import logger


@logger.catch()
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='test12345',
        DATABASE=env.PathFile.database,
    )
    logger.info('path_root: {}'.format(app.root_path))
    logger.info('path_instance: {}'.format(app.instance_path))
    logger.info('path_database: {}'.format(env.PathFile.database))

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    @app.route('/')
    def index():
        return "Flask API is running!"

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # REST API
    @app.route('/restapi')
    def get_dic_restapi():
        dic_restapi = {
            "name": "kangdaepyo",
            "links": {
                "self": {
                    "endpoint": "/restapi",
                    "method": "GET",
                },

                "binance_market": {
                    "endpoint": "/restapi/binance/market",
                    "method": "POST",
                    "description": "detail_candlestick, etc.",
                },
                "binance_account": {
                    "endpoint": "/restapi/binance/account",
                    "method": "POST",
                    "description": "balance, position, order, trade, etc.",
                },
                "binance_leverage": {
                    "endpoint": "/restapi/binance/account/leverage",
                    "method": "PUT",
                    "description": "update init leverage",
                },
                "binance_order": {
                    "endpoint": "/restapi/binance/account/order",
                    "method": "PUT",
                    "description": "send to binance from your order",
                },

                "gmail_send": {
                    "endpoint": "/restapi/gmail",
                    "method": "PUT",
                    "description": "send to everyone from your",
                },

                "management_request_tr": {
                    "endpoint": "/restapi/management/request_tr",
                    "method": "POST",
                    "description": "get db, gate_next_door transaction",
                },

                "tistory_message": {
                    "endpoint": "/restapi/tistory",
                    "method": "POST",
                    "description": "get user message",
                },

                "upbit_market": {
                    "endpoint": "/restapi/upbit/market",
                    "method": "POST",
                    "description": "detail_candlestick, etc.",
                },

                "upbit_account": {
                    "endpoint": "/restapi/upbit/account",
                    "method": "POST",
                    "description": "account_balance, etc.",
                },

                "upbit_order": {
                    "endpoint": "/restapi/upbit/account/order",
                    "method": "PUT",
                    "description": "send to upbit from your order",
                },
            }
        }
        return jsonify(dic_restapi), 200

    from .object import db
    db.init_app(app)

    from .routes import management
    app.register_blueprint(management.bp)

    from .routes import binance
    app.register_blueprint(binance.bp)

    from .routes import gmail
    app.register_blueprint(gmail.bp)

    from .routes import tistory
    app.register_blueprint(tistory.bp)

    from .routes import upbit
    app.register_blueprint(upbit.bp)

    return app
