from flask import render_template
from apps.cms import cms_bp


@cms_bp.route("/", endpoint="首页")
def index():
    return render_template("index.html")

