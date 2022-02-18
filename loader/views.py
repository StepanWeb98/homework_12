# loader / views.py

# Сперва импорттируем класс блюпринта
from flask import render_template, Blueprint, request
from functions import *

# Затем создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")

# Создаем вьюшку, страницы поста, подключаем шаблон
@loader_blueprint.route("/post", methods=["GET", "POST"])
def profile_page():
    return render_template("post_form.html")

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/search')
def category_page():
    suche = request.args.get('s')
    result_suche = suche_post(suche)
    return render_template("post_list.html", suche=suche, result_suche=result_suche)
