import json
from json import JSONDecodeError
from pprint import pprint
import logging

def load_posts(file):
    posts = []
    with open(file, "r", encoding="utf-8") as load_file:
        posts = json.load(load_file)
    return posts

# функция поиска введенного слова ?s="слово"
def suche_post(key_wort):
    try:
        posts = load_posts("posts.json")
        list_suche = []
        for post in posts:
            if key_wort in post['content']:
                list_suche.append(post)
        return list_suche
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print("Файл не найден")


def save_picture(picture):
    filename = picture.filename
    file_type = filename.split(".")[-1]

    if file_type in ["jpeg", "svg", "jpg", "png"]:
        picture.save(f"./uploads/images/{filename}")
        return f"uploads/images/{filename}"
    else:
        return False


def save_post(posts, file="posts.json"):
    with open(file, "w", encoding="utf-8") as write_file:
        json.dump(posts, write_file)

def add_post(post):
    posts = load_posts("posts.json")
    posts.append(post)
    save_post(posts)
