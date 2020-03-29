# Каталог документов хранится в следующем виде:

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "invoice", "number": "5453"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит

def people_by_doc_number(documents):
    doc_number = input('Введите номер документа ')
    for register in documents:
        if doc_number == register['number']:
            print(register['name'])
            return
    print('Документа с таким номером нет')


# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"

def list_of_docs(documents):
    if bool(documents):
        for register in documents:
            print(f"""{register['type']} \"{register['number']}\" \"{register['name']}\"""")
    else:
        print('Список пуст')


# Перечень полок, на которых находятся документы, хранится в следующем виде:

# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится

def shelf_by_doc_number(directories):
    doc_number = input('Введите номер документа ')
    for number, shelf in directories.items():
        if doc_number in shelf:
            print(number)
            return
    print('Документа с таким номером нет')


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.

def add_new_doc():
    new_register = {}

    print('Введите номер документа')
    doc_number = input()
    print('Введите тип документа, например passport')
    doc_type = input()
    print('Введите имя владельца, например Иван Иванов')
    doc_name = input()
    print('Введите номер полки (1, 2 или 3)')
    shelf_number = input()

    new_register.update({"type": doc_type, "number": doc_number, "name": doc_name})
    documents.append(new_register)

    directories[shelf_number].append(doc_number)

    print(f'Документ {new_register} успешно добавлен на полку {shelf_number}')

# n — names — команда, которая выводит имена всех владельцев документов


def show_all_names(documents):
    try:
        for register in documents:
            print(register['name'])
    except KeyError:
        print('В документе нет поля name')


def main():
    while True:
        print(
            'Введите\n p, чтобы найти имя по номеру документа;\n l, чтобы посмотреть список всех документов;\n s, чтобы по номеру документа узнать полку, на которой он лежит;\n a, чтобы добавить новый документ в каталог и в перечень полок;\n n, чтобы посмотреть имена всех владельцев документов;\n q, чтобы выйти')
        user_input = input()
        if user_input == 'p':
            people_by_doc_number(documents)
        elif user_input == 'l':
            list_of_docs(documents)
        elif user_input == 's':
            shelf_by_doc_number(directories)
        elif user_input == 'a':
            add_new_doc()
        elif user_input == 'n':
            show_all_names(documents)
        elif user_input == 'q':
            break
        else:
            print('Неверный ввод')


main()