import shutil

from githubinformer.github_informer import GitHubInformer


def term_width():
    return shutil.get_terminal_size()[0]


def main():
    print(''.center(term_width(), '*'))
    print('Программа для вывода всех открытых репозиториев разработчиков на Github!'.center(term_width()))
    print(''.center(term_width(), '*'))
    user = input('Введите никнейм разработчика: ')
    github_informer = GitHubInformer(user=user)
    info = github_informer.get_all_info()
    if not info:
        print(''.center(term_width(), '-'))
        print('Репозитории данного пользователя не найдены!')
    else:
        choice = input('Выберете действие:\n'
                       'a: Вывести все репозитории;\n'
                       'c: Вывести колличество открытых репозиториев у разработчика.\n'
                       ': ')
        if choice in ['a', 'A', 'ф', 'Ф']:
            for n, repo in enumerate(info, 1):
                print(f'{n}) {repo["full_name"]}: {repo["html_url"]}')
        elif choice == 'c' or choice == 'C':
            print(f'Колличество открытых репозиториев у разработчика {user}:'
                  f' {github_informer.get_repositories_count()}')
        else:
            print('Вы ввели неверное значение!')
    print(''.center(term_width(), '='))
    print('Программа завершена!')


if __name__ == '__main__':
    main()
