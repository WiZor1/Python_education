ind_info = {'имя': '', 'фамилию': '', 'год рождения': '', 'город проживания': '', 'email': '', 'телефон': ''}


def info_output(name, surname, birth_year, city, email, phone):
    while True:
        try:
            int(birth_year)
            break
        except Exception as err:
            birth_year = input('Дата рождения должна быть числом:\n')
    print('Пользователь:', surname, name, end='')
    print(' родился в', birth_year, 'году, в настоящее время проживает в г.', city + '.', end='')
    print(' Способы связи: тел.:', phone, ' email:', email)


for i in list(ind_info.keys()):
    ind_info.update({i: input('Укажите ' + i + ':\n')})

info_output(name=ind_info.get('имя'), surname=ind_info.get('фамилию'), birth_year=ind_info.get('год рождения'),
            city=ind_info.get('город проживания'), email=ind_info.get('email'), phone=ind_info.get('телефон'))
