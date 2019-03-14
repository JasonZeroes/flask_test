from flask import Flask


def register_bp(app: Flask):
    from apps.cms import cms_bp
    app.register_blueprint(cms_bp)


def register_db(app: Flask):
    from apps.models import db
    db.init_app(app)


def create_app(config_str: str):
    """初始化创建app"""
    app = Flask(__name__)

    # 注册配置文件
    app.config.from_object(config_str)

    # 注册数据库
    register_db(app)

    # 注册;蓝图
    register_bp(app)

    return app
