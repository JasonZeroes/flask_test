from apps.models import UserModel
from . import BaseModel, db


class ShopModel(BaseModel):
    """商铺模型"""
    # 店铺外部id
    pub_id = db.Column(db.String(16), unique=True, index=True)
    # 店铺名称
    shop_name = db.Column(db.String(16), nullable=True, unique=True)
    # 店铺评分
    shop_rating = db.Column(db.Float, default=5.0)
    # 是否是品牌
    brand = db.Column(db.Boolean, default=False)
    # 是否准时送达
    on_time = db.Column(db.Boolean, default=True)
    # 是否是蜂鸟配送
    fengniao = db.Column(db.Boolean, default=True)
    # 是否是保险
    bao = db.Column(db.Boolean, default=True)
    # 是否有发票
    piao = db.Column(db.Boolean, default=True)
    # 是否准标识
    zhun = db.Column(db.Boolean, default=True)
    # 起送价格
    start_send = db.Column(db.Float, default=0)
    # 配送费
    send_cost = db.Column(db.Float, default=0)
    # 店铺图片
    shop_img = db.Column(db.String(128))
    # 店铺公告
    notice = db.Column(db.String(128), default='')
    # 优惠信息
    discount = db.Column(db.String(128), default='')
    # 店铺和商家的关系
    seller_id = db.Column(db.Integer, db.ForeignKey("user_model.id"))
    # 建立连接关系(反向查询)
    seller = db.relationship(UserModel, backref="shops")

    def keys(self):
        return ("shop_name", "shop_rating",
                "brand", "on_time", "fengniao",
                "bao", "piao", "zhun",
                "start_send", "send_cost", "shop_img",
                "notice", "discount")


class ShopCate(BaseModel):
    """商铺列表"""
    pass