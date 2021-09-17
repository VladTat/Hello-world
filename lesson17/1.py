# Cinema site (Russiain users).

def is_film_exist(film_list, your_film):
    for film in film_list:
        if film == your_film:
            return True
    else:
        return False

films = [

    'Крепкий орешек', 'Назад в будущее', 'Таксист',

    'Леон', 'Богемская рапсодия', 'Город грехов',

    'Мементо', 'Отступники', 'Деревня',

    'Проклятый остров', 'Начало', 'Матрица'

]

user_films = []
while True:
    print('\nВаш текущий топ фильмов:', user_films)
    new_film = input('Название фильма: ')
    if is_film_exist(films, new_film):
        print('Команды: добавить, вставить, удалить.')
        command = input('Введите команду: ')
        if command == 'вставить':
            place = input('На какое место?')
            user_films.insert(place - 1, new_film)