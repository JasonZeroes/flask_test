import uuid
from flask import render_template, request, url_for, redirect
from flask_login import login_required, current_user
from apps.cms import cms_bp
from apps.forms.shop_forms import ShopForm
from apps.models import db
from apps.models.shop_models import ShopModel


@cms_bp.route("/show/", methods=["GET", "POST"], endpoint="商铺列表")
@login_required
def show_list():
    """查看商家列表"""
    user_id = current_user.id
    form = ShopModel.query.filter_by(seller_id=user_id).all()
    return render_template("shop-list.html", form=form)


@cms_bp.route("/add/", methods=["GET", "POST"], endpoint="商铺添加")
@login_required
def shop_add():
    """添加店铺"""
    form = ShopForm(request.form)
    if request.method == "POST" and form.validate():
        shop = db.session.query(ShopModel).filter_by(id=form.shop_name.data).first()
        if shop is None:
            shop = ShopModel()
            shop.set_form_attr(form.data)
            pub_id = ''.join(str(uuid.uuid4()).split("-"))[:16]
            shop.pub_id = pub_id
            shop.seller_id = current_user.id
            db.session.add(shop)
            db.session.commit()
            return redirect(url_for("cms.商铺列表"))
        form.shop_name.errors.append("该商家已经存在,请更换商家名")
    return render_template("shop-add.html", form=form, flags="添加")


@cms_bp.route("/update/<pub_id>", methods=["GET", "POST"])
@login_required
def update(pub_id):
    form = None
    if request.method == "GET":
        data = ShopModel.query.filter_by(pub_id=pub_id).first()
        form = ShopForm(data=dict(data))
    elif request.method == "POST":
        form = ShopForm(request.form)
        if form.validate():
            shop = ShopModel.query.filter_by(pub_id=pub_id).first()
            shop.set_form_attr(form.data)
            db.session.commit()
            return redirect(url_for("cms.商铺列表"))
    return render_template("shop-add.html", form=form, flags="更新")
