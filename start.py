import function_spr as fs
import globals as g
import edit_abonent as ea
import delit as dl
import search_abonent as sa
def print_help():
   
    print("""
Основной список
0 - Создать новую или очистить существующую книжку
1 - Создать новый контакт
2 - Показать все контакты
3 - Редактировать, удалить и поиск контакта
4 - Выход """)
def edit_help():
    print('''
    Редактировать, удалить и поиск контакта
    1 - Изменить фамилию
    2 - Изменить номер телефона
    3 - Изменить почту
    4 - Поиск контакта
    5 - Удалить контакт
    6 - Основной  список
    '''    )
def checklist():
    print_help()
    choice=command_selection()
    if choice < 0 or choice > 4:
          print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
          checklist()
    if choice == 0:
        fs.create_json()
    elif choice == 1:
        fs.add_abonent()
    elif choice == 2:
        fs.list_sprav()
    elif choice == 3:
        edit_help()
        choice=command_selection()
        if choice < 0 or choice > 5:
          print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
          checklist()
        if choice == 1:
            ea.edit_surname()
        elif choice == 2:
            ea.edit_phone_number()
        elif choice == 3:
            print("Данная команда в разработке")
            checklist()
        elif choice == 4:
            sa.search_abonent()
        elif choice == 5:
            dl.delete_abonent()
        elif choice==6:
            checklist()
    
    elif choice == 4:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()
    
def command_selection():
    try:
        choice = int(input('выберите действие'))
        return choice
    except ValueError:
        print('Это должно быть число\n')
        print_help()
        return command_selection()