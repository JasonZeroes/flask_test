from flask import request, render_template, redirect, url_for, session

from apps.cms import cms_bp
from apps.forms.user_forms import RegisterForm, LoginForm
from apps.models import UserModel, db


@cms_bp.route("/register/", methods=["GET", "POST"], endpoint="注册")
def register():
    """实现用户注册"""
    form = RegisterForm(request.form)
    if request.method == "POST" and form.validate():
        # 将数据保存到数据库当中
        u = UserModel()
        u.username = form.username.data
        u.password = form.password.data
        db.session.add(u)
        db.session.commit()
        return redirect(url_for("cms.登录"))
    return render_template("reg-log.html", form=form, flags="注册")


@cms_bp.route("/login/", methods=["GET", "POST"], endpoint="登录")
def login():
    """实现用户登录"""
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        # 到数据库查验用户的合法性
        username = form.username.data
        password = form.password.data
        try:
            user = db.session.query(UserModel).filter_by(username=username).first()
            if user.password == password:
                # 设置cookie和session
                response = redirect(url_for("cms.首页"))
                response.set_cookie("username", username)
                response.set_cookie("password", password)
                session["username"] = username
                return response
            else:
                return render_template("reg-log.html", form=form, flags="登录")
        except AttributeError:
            return render_template("reg-log.html", form=form, flags="登录")
    return render_template("reg-log.html", form=form, flags="登录")


@cms_bp.route("/logout/", methods=["GET", "POST"], endpoint="退出")
def logout():
    response = redirect(url_for("cms.登录"))
    response.delete_cookie("username")
    session.pop("username")
    return response
