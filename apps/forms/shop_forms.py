from wtforms import Form, validators, StringField, DecimalField, BooleanField


class ShopForm(Form):
    # 店铺名称
    shop_name = StringField(
        label="店铺名称:",
        validators=[
            validators.DataRequired(message="店铺名称必须填写!"),
            validators.Length(min=4, max=16, message="店铺名称最短4个字符, 最长16个字符")
        ],
        render_kw={"class": "layui-input lens", "placeholder": "请输入店铺名称"}
    )
    # 是否是品牌
    brand = BooleanField(label="是否品牌:", default=False)
    on_time = BooleanField(label="准时送达:", default=False)
    fengniao = BooleanField(label="蜂鸟速递:", default=False)
    piao = BooleanField(label="是否发票:", default=False)
    bao = BooleanField(label="是否保险:", default=False)
    zhun = BooleanField(label="是否标识:", default=False)

    # 起送价格
    start_send = DecimalField(
        label="起送价格:",
        validators=[
            validators.DataRequired(message="必须填写起送价格")
        ],
        render_kw={"class": "layui-input lens"}
    )
    # 配送费
    send_cost = DecimalField(
        label="配送价格:",
        validators=[
            validators.DataRequired(message="配送费必须填写!")
        ],
        render_kw={"class": "layui-input lens"}
    )
    # 店铺公告
    notice = StringField(
        label="店铺公告:",
        validators=[
            validators.Length(min=10, max=128, message="最短10个字符, 最长128个字符")
        ],
        render_kw={"class": "layui-input lens"}
    )
    # 优惠信息
    discount = StringField(
        label="优惠信息:",
        validators=[
            validators.Length(min=10, max=128, message="最短10个字符, 最长128个字符")
        ],
        render_kw={"class": "layui-input lens"}
    )

    # 自定义验证器,验证起送价格和运送费
    def validate_start_send(self, obj):
        obj.data = float('{:.2f}'.format(obj.data))

    def validate_send_cost(self, obj):
        obj.data = float("{:.2f}".format(obj.data))
