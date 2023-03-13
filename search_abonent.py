import json
import start as st
ph_js='phones.json'
def search_abonent():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')

    with open(ph_js, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in reversed(range(len(data))):
            if name==data[i]['Имя'] or name==data[i]['Фамилия']:
                 print(data[i]['Фамилия']," ",data[i]['Имя'],\
            "\Телефоны",data[i]['Мобильный телефон'],' ',data[i]['Домашний телефон']\
                ,"\Почта", data[i]['Личная почта'],' ',data[i]['Рабочяя почта'] )


    # with open(ph_js, 'w', encoding='UTF-8') as file:
    #     json.dump(data, file, indent=4,ensure_ascii=False)
    #     print('\nКонтакт успешно  найден!\n')
        st.checklist()