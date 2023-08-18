import csv

def add_contact(name, email):
    with open('contacts.csv', 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([name, email])
    print(f'Контакт {name} з електронною адресою {email} додано.')
    
def list_contacts():
    with open('contacts.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        print('Список контактів:')
        for row in csvreader:
            print(f"Ім'я: {row[0]}, Електронна адреса: {row[1]}")
            
while True:
    print('\nОберіть опцію:')
    print('1. Додати контакт')
    print('2. Вивести список контактів')
    print('3. Вийти')
    
    choice = input('Ваш вибір: ')
    
    if choice == '1':
        name = input("Введіть ім'я контакту: ")
        email = input("Введіть електронну адресу контакту: ")
        add_contact(name, email)
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        print("Програма завершує роботу.")
        break
    else:
        print('Невірний вибір. Спробуйте ще раз.')