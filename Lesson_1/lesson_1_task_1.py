import requests
import json


def save_repo(username):
    req = requests.get(f'https://api.github.com/users/{username}/repos')
    with open('saved_repo.txt', 'w', encoding='utf-8') as file:
        json.dump(req.json(), file, indent=4)
        print(f"JSON вывод сохранен в файл \"{file.name}\"")


def get_repo(username):
    req = requests.get(f'https://api.github.com/users/{username}/repos')
    print("Список репозиториев пользователя", username, ":")
    for repo_name in req.json():
        print(repo_name['name'])


user = input('Введите имя пользователя для поиска репозиториев: ')
get_repo(user)
save_repo(user)
