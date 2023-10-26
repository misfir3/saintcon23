import os

from flask import Blueprint, redirect, render_template, g, request

not_settings = set(dir())
from memeapp.conf.config import *

settings = set(dir()) - not_settings - {"not_settings"}

bp = Blueprint("admin", __name__)


@bp.route("/admin", methods=["GET"])
def index():
    if g.user and not g.user.is_admin:
        return redirect("/home")
# that eval looks sus here. Check copilot chat log for suggestion, solutions
    return render_template("admin.html", environ=os.environ, user=g.user,
                          settings={name: eval(name) for name in settings if not name.startswith("__")})
    # settings = {name: getattr(module, name) for name in settings if not name.startswith("__")}
    # return render_template("admin.html", environ=os.environ, user=g.user, settings=settings)