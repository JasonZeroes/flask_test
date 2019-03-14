from apps.models import db
from . import BaseModel


class UserModel(BaseModel):
    """创建用户模型表"""
    username = db.Column(db.String(32), unique=True, nullable=True, index=True)
    password = db.Column(db.String(128), nullable=True)
