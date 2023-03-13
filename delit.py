import json
import start as st
import globals as g
ph_js='phones.json'
def delete_abonent():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')

    with open(ph_js, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in reversed(range(len(data))):
            if name==data[i]['Имя'] or name==data[i]['Фамилия']:
                del data[i]
               
        # if name not in data:
        #         print('Такого контакта нет')
    
    with open(ph_js, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4,ensure_ascii=False)
    print('\nКонтакт успешно  удалён!\n')
    st.checklist()

def delete():
    with open(ph_js, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        del data
    print("Телефонная книжка успешно удалена")
    data = []
    with open(ph_js, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4,ensure_ascii=False)
    print('\n Чистая телефонная книжка успешно создана!!\n')
    st.checklist()