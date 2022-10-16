from flask import (Blueprint, render_template, abort)
from jinja2 import TemplateNotFound


admin_bp: Blueprint = Blueprint(
    'admin_bp', __name__, template_folder='templates')


@admin_bp.route('/admin', methods=["GET", "POST"])
def admin() -> None:
    try:
        return render_template('admin/index.html')
    except TemplateNotFound:
        abort(404)
