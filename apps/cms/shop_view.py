import uuid
from flask import render_template, request, url_for, redirect, session
from flask_login import login_required, current_user
from apps.cms import cms_bp
from apps.forms.shop_forms import ShopForm, MenuCateForm, MenusForm
from apps.models import db
from apps.models.shop_models import ShopModel, MenuCateModel, MenusModel
from apps.tools.tools import check_shop_pid


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


@cms_bp.route("/update/<pub_id>", methods=["GET", "POST"], endpoint="商铺更新")
@login_required
def shop_update(pub_id):
    """商铺更新"""
    form = None
    if request.method == "GET":
        data = check_shop_pid(pub_id)
        form = ShopForm(data=dict(data))
    elif request.method == "POST":
        form = ShopForm(request.form)
        if form.validate():
            shop = ShopModel.query.filter_by(pub_id=pub_id).first()
            shop.set_form_attr(form.data)
            db.session.commit()
            return redirect(url_for("cms.商铺列表"))
    return render_template("shop-add.html", form=form, flags="更新")


@cms_bp.route("/cate_list/<pub_id>", methods=["GET", "POST"], endpoint="菜品分类展示")
def cate_list(pub_id):
    form = MenuCateModel.query.filter_by(shop_pid=pub_id).all()
    return render_template("cate_list.html", form=form, pub_id=pub_id)


@cms_bp.route("/cate_add/<pub_id>", methods=["GET", "POST"], endpoint="菜品分类添加")
@login_required
def cate_add(pub_id):
    form = MenuCateForm(request.form)
    if request.method == "POST" and form.validate():
        cate = MenuCateModel()
        cate.shop_pid = pub_id
        cate.set_form_attr(form.data)
        db.session.add(cate)
        db.session.commit()
        return redirect(url_for("cms.商铺列表"))
    return render_template("shop-add.html", form=form, flags="分类添加")


@cms_bp.route("/menus_list/<pub_id>", methods=["GET", "POST"], endpoint="菜品列表")
def menus_list(pub_id):
    form = MenusModel.query.filter_by(shop_id=pub_id).all()
    return render_template("menus_list.html", form=form, pub_id=pub_id)


@cms_bp.route("/menus_add/<pub_id>", methods=["GET", "POST"], endpoint="菜品添加")
@login_required
def menus_add(pub_id):
    shop = ShopModel.query.filter_by(pub_id=pub_id).first()
    form = MenusForm(shop, request.form)
    if request.method == "POST" and form.validate():
        menu = MenusModel()
        menu.shop_id = pub_id
        menu.set_form_attr(form.data)
        db.session.add(menu)
        db.session.commit()
        return redirect(url_for("cms.商铺列表"))
    return render_template("shop-add.html", form=form, flags="菜品添加")
