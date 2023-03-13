import json
import start as st
import globals as g
ph_js='phones.json'
g.data=[]
def create_json():
    json_book = []
    with open(ph_js,"w",encoding='UTF-8') as file:
        file.write(json.dumps(json_book, indent=4, ensure_ascii=False))
    print("Телефонная книжка успешно создана!")
    st.checklist()


def add_abonent():
    print("Заполняем новый контакт")
    surname = input('Введите Фамилию: ')
    name = input("Введите имя: ")
    mobil= input('Ваш мобильный телефон')
    home_phone = input('Есть домашний телефона? ')
    my_mail = input('Личная почта')
    work_mail=input('Рабочая почта')
    json_book = {
        'Фамилия': surname,
        'Имя': name,
        'Мобильный телефон': mobil,
        'Домашний телефон': home_phone,
        'Личная почта':my_mail,
        'Рабочяя почта': work_mail}
    with open('phones.json', 'r',encoding='UTF-8') as file:
        data = json.load(file)
   
   
    data.append(json_book)
    with open('phones.json', "w", encoding='UTF-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print('\nНовый контакт успешно добавлен!\n')
    st.print_help()
    st.checklist()

def list_sprav():
    with open("phones.json",'r',encoding="utf-8") as fl:
        data=json.load(fl)
        for i in range(0,len(data)):
            print(data[i]['Фамилия']," ",data[i]['Имя'],\
            "\Телефоны",data[i]['Мобильный телефон'],' ',data[i]['Домашний телефон']\
                ,"\Почта", data[i]['Личная почта'],' ',data[i]['Рабочяя почта'] )
           
        st.checklist()



# def first_save():
#     with open('phones.json',"w",encoding='UTF-8') as fl:
#         fl.write(json.dumps(ph_js, indent=4, ensure_ascii=False))
#     print("Телефонная книжка успешно создана!")
    
# def open_json():
#     with open(ph_js, 'r',encoding='UTF-8') as file:
#         data = json.load(file)

# def save():
#     with open(ph_js, 'w',encoding='UTF-8') as file:
#         json.dump(globals.data, file, indent=4, ensure_ascii=False)
  
# phone_number = ''
#     valid =False
#     while not valid:
#         try:
#             phone_number = input('Введите номер телефона: ')
#             if len(phone_number) != 11:
#                 print('В номере телефона должно быть 11 цифр.')
#             else:
#                 phone_number = int(phone_number)
#                 valid = True
#         except:
#             print('Номер телефона должен состоять только из цифр.'

