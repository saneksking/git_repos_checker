# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Program for show open repositories on GitHub."""
import shutil
from githubinformer.github_informer import GitHubInformer


def term_width():
    return shutil.get_terminal_size()[0]


def main():
    print(''.center(term_width(), '*'))
    print('GitHub Repos Checker'.center(term_width()))
    print(''.center(term_width(), '*'))
    print('Program for show open repositories on GitHub.'.center(term_width()))
    print(''.center(term_width(), '-'))
    user = input('Input a nickname of GitHub developer: ')
    github_informer = GitHubInformer(user=user)
    info = github_informer.get_all_info()
    if not info:
        print(''.center(term_width(), '-'))
        print('Repositories of this developer is not found!')
    else:
        choice = input('Chose action:\n'
                       'a: Show all repositories;\n'
                       'c: Show a count of developer repositories.\n'
                       ': ')
        if choice in ['a', 'A', 'ф', 'Ф']:
            for n, repo in enumerate(info, 1):
                print(f'{n}) {repo["full_name"]}: {repo["html_url"]}')
        elif choice == 'c' or choice == 'C':
            print(f'A count of developer repositories {user}:'
                  f' {github_informer.get_repositories_count()}')
        else:
            print('You entered the wrong symbol!')
    print(''.center(term_width(), '-'))
    print('https://github.com/saneksking/'.center(term_width()))
    print(''.center(term_width(), '='))


if __name__ == '__main__':
    main()
