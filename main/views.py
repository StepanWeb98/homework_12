# main / views.py

# Сперва импорттируем класс блюпринта
from flask import render_template, Blueprint, request
from functions import  *

# Затем создаем новый блюпринт, выбираем для него имя
main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

# Создаем вьюшку, главная страница, подключаем шаблон
@main_blueprint.route('/')
def profile_page():
    return render_template("index.html")

# Создаем вьюшку, страница поиска по слову, подключаем шаблон
@main_blueprint.route('/search')
def category_page():
    suche = request.args.get('s')
    result_suche = suche_post(suche)
    return render_template("post_list.html", suche=suche, result_suche=result_suche)
