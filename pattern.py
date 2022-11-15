def function_name(arg: type) -> type:
    ...


def function2_name(arg: type, arg2: type) -> type:
    ...


# Название функций через _, у принимаемых аргументов указываем тип данных (там где он понятен),
# указываем тип того что возвращает функция
# При написании функций, если она получается многофункциональной,
# то делим на под функции, по хорошему чтобы функция делала 1 действие
# При написании таблиц используем django-tables2
# Между функциями вне класса 2 пустых строчки, в классе 1 строчка
# Запись словаря:
# dict = {
#     'key': value,
# }
# Запись листа:
# list = [value1, value2]
# Запуск 
# cd app -> python ./manage.py runserver
# При создании страницы не забываем делать миграции
# cd app -> python ./manage.py migrate  
# пример отправки данных на страницу
# world = 'World'
# context = {
#     'world': world,
# }
# return render(request=request, template_name='exchange_app/_.html', context=context)
