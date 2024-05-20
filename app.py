import requests
import json
from githubinformer.github_informer import GitHubInformer


def main():
    print('Программа для вывода всех открытых репозиториев разработчиков на Github!')
    print(''.center(86, '-'))
    user = input('Введите никнейм разработчика: ')
    github_informer = GitHubInformer(user=user)
    info = github_informer.get_all_info()
    if not info:
        print('Такого пользователя несуществует!')
    else:
        choice = input('Выберете действие:\n'
                       'a: Вывести все репозитории;\n'
                       'c: Вывести колличество открытых репозиториев у разработчика.\n'
                       ': ')
        if choice == 'a' or choice == 'A':
            for repo in info:
                print(f'{repo["full_name"]}: {repo["html_url"]}')
        elif choice == 'c' or choice == 'C':
            print(f'Колличество открытых репозиториев у разработчика {user}:'
                  f' {github_informer.get_repositories_count()}')
        else:
            print('Вы ввели неверное значение!')
    print('Программа завершена!')


if __name__ == '__main__':
    main()
