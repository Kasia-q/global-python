import json

tasks = []

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks.extend(json.load(file))
    except FileNotFoundError:
        pass

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def display_tasks():
    if len(tasks) == 0:
        print("Brak zapisanych zadań.")
    else:
        for task in tasks:
            print("ID:", task['id'])
            print("Tytuł:", task['title'])
            print("Termin wykonania:", task['due_date'])
            print()

def add_task():
    title = input("Podaj tytuł zadania: ")
    description = input("Podaj opis zadania: ")
    due_date = input("Podaj termin wykonania: ")

    task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'due_date': due_date
    }

    tasks.append(task)
    print("Zadanie dodane")

def delete_task():
    task_id = int(input("Podaj ID zadania do usunięcia: "))
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print("Zadanie usunięte")
            return
    print("Zadanie o podanym ID nie istnieje")

def update_task():
    task_id = int(input("Podaj ID zadania do aktualizacji: "))
    for task in tasks:
        if task['id'] == task_id:
            title = input("Podaj nowy tytuł zadania: ")
            description = input("Podaj nowy opis zadania: ")
            due_date = input("Podaj nowy termin wykonania: ")

            task['title'] = title
            task['description'] = description
            task['due_date'] = due_date

            print("Zadanie zaktualizowane")
            return
    print("Zadanie o podanym ID nie istnieje")

def save_tasks_to_file():
    save_option = input("Czy chcesz zapisać zadania do pliku? (tak/nie): ")
    if save_option.lower() == 'tak':
        save_tasks()
        print("Zadania zostały zapisane do pliku.")
    else:
        print("Anulowano zapis do pliku.")

def main():
    load_tasks()

    while True:
        print("******Zarządzanie zadaniami******")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Aktualizuj zadanie")
        print("5. Zapisz zadania do pliku")
        print("6. Wyjście z programu")

        choice = input("Wybierz opcję 1-6: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            update_task()
        elif choice == '5':
            save_tasks_to_file()
        elif choice == '6':
            break
        else:
            print("Niepoprawny wybór, spróbuj ponownie")

    save_tasks()

if __name__ == '__main__':
    main()
