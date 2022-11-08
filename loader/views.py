# loader / views.py

# Сперва импорттируем класс блюпринта
from flask import render_template, Blueprint, request
from functions import *
import logging


# Затем создаем новый блюпринт, выбираем для него имя
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder="templates")
logging.basicConfig(filename="basic.log", level=logging.INFO)

# Создаем вьюшку, страницы поста, подключаем шаблон
@loader_blueprint.route("/post")
def profile_page():
    return render_template("post_form.html")

# Создаем вьюшку, используя в декораторе блюпринт вместо app
@loader_blueprint.route('/post', methods=["POST"])
def category_page():
    picture = request.files.get('picture')
    content = request.form.get('content')

    picture_url = save_picture(picture)

    if picture_url is False:
        logging.info(f"{picture_url} не изображение")
        return "Не то изображение"

    add_post({"pic": picture_url, "content": content})


    return render_template("post_uploaded.html", picture_url=picture_url, content=content)
