import json
from pprint import pprint

def load_posts(file):
    posts = []
    with open(file, "r", encoding="utf-8") as load_file:
        posts = json.load(load_file)
    return posts

# функция поиска введенного слова ?s="слово"
def suche_post(key_wort):
    posts = load_posts("posts.json")
    list_suche = []
    for post in posts:
        if key_wort in post['content']:
            list_suche.append(post)
    return list_suche


# def addition_post(file):
#     with open(file, "w", encoding="utf-8") as write_file:

