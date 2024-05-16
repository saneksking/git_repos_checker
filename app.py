import requests
import json


def main():
    print('Программа для вывода всех открытых репозиториев разработчиков на Github!')
    print(''.center(86, '-'))
    user = input('Введите никнейм разработчика: ')
    api_url = f'https://api.github.com/users/{user}/repos'
    response = requests.get(api_url)
    if response.status_code == 200:
        repositories = response.json()
        for repo in repositories:
            print(f'{repo["full_name"]}: {repo["html_url"]}')
    else:
        print(f'Ошибка! Код ответа {response.status_code}')
    print('Программа завершена!')


if __name__ == '__main__':
    main()
