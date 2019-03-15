from flask import render_template, url_for, redirect, session, current_app
from flask_login import current_user, login_required

from apps.cms import cms_bp


# @cms_bp.route("/", endpoint="首页")
# # @login_required
# def index():
#     if current_user.is_authenticated:
#         # print(current_user.username)
#         return render_template("index.html")
#     else:
#         return redirect(url_for("cms.登录"))


@cms_bp.route("/", endpoint="首页")
@login_required
def index():
    return render_template("index.html")
