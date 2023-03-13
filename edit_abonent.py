import json
import start as st
import function_spr as fs
import globals as g
ph_js='phones.json'
g.data=[]
def edit_surname():  
    name = input('Редактируем имя или фамилию абонента, наберите его  ')
   
    with open(ph_js, 'r',encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):  
            if name == data[i]['Имя'] or name == data[i]['Фамилия']:
                print( data[i]['Фамилия']) 
                data[i]['Фамилия'] = input('Фамилия :')
                print( data[i]['Имя']) 
                data[i]['Имя'] = input('Имя: ')
                
            # else: 
            #      print('Такого контакта нет')
            #      st.checklist()
            
    with open(ph_js, 'w',encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('\n Фамилия и имя изменёны!\n')
    st.checklist()
    
def edit_phone_number():  
    name = input('Наберите имя или фамилию абонента, чей номер будем редактировать:  ')
    # fs. open_json():
    with open(ph_js, 'r',encoding='UTF-8') as file:
        data = json.load(file)
    for i in range(0, len(data)):  
            if name == data[i]['Имя'] or name == data[i]['Фамилия']:
                print( data[i]['Мобильный телефон']) 
                data[i]['Мобильный телефон'] = input('Новый телефон: ')
                print( data[i]['Домашний телефон']) 
                data[i]['Домашний телефон'] = input('Новый телефон: ')
            
            # else: 
            #      print('Такого контакта нет')
            #      st.checklist()   
    with open(ph_js, 'w',encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('\nНомера изменёны!\n')
    st.checklist()


