from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    is_status = db.Column(db.SmallInteger, default=0)

    def set_form_attr(self, form_data: dict):
        for k, v in form_data.items():
            if hasattr(self, k):
                setattr(self, k, v)


from .user_models import UserModel
