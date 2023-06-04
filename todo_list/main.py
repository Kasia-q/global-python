import json
import atexit

tasks = []
last_task_id = 0

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks.extend(json.load(file))
            update_last_task_id()
    except FileNotFoundError:
        pass

def save_tasks():
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def update_last_task_id():
    global last_task_id
    if len(tasks) > 0:
        last_task_id = max(task['id'] for task in tasks)

def display_tasks():
    if len(tasks) == 0:
        print("Brak zapisanych zadań.\n")
    else:
        for task in tasks:
            print("ID:", task['id'])
            print("Tytuł:", task['title'])
            print("Termin wykonania:", task['due_date'])
            print()

def show_task_description(task):
    print("Opis zadania:", task['description'])
    print()

def add_task():
    global last_task_id
    
    title = input("Podaj tytuł zadania: ")
    description = input("Podaj opis zadania: ")
    due_date = input("Podaj termin wykonania: ")

    last_task_id += 1
    task = {
        'id': last_task_id,
        'title': title,
        'description': description,
        'due_date': due_date
    }

    tasks.append(task)
    print("Zadanie dodane\n")

def delete_task():
    task_id = get_valid_input("Podaj ID zadania do usunięcia: ", int)
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            print("Zadanie usunięte\n")
            return
    print("Zadanie o podanym ID nie istnieje\n")

def update_task():
    task_id = get_valid_input("Podaj ID zadania do aktualizacji: ", int)
    for task in tasks:
        if task['id'] == task_id:
            title = input("Podaj nowy tytuł zadania: ")
            description = input("Podaj nowy opis zadania: ")
            due_date = input("Podaj nowy termin wykonania: ")

            task['title'] = title
            task['description'] = description
            task['due_date'] = due_date

            print("Zadanie zaktualizowane\n")
            return
    print("Zadanie o podanym ID nie istnieje\n")

def save_tasks_to_file():
    save_option = input("Czy chcesz zapisać zadania do pliku? (tak/nie): ")
    if save_option.lower() == 'tak':
        save_tasks()
        print("Zadania zostały zapisane do pliku.\n")
    else:
        print("Anulowano zapis do pliku.\n")

def get_valid_input(prompt, data_type):
    while True:
        try:
            user_input = data_type(input(prompt))
            return user_input
        except ValueError:
            print("Niepoprawne dane. Spróbuj ponownie.\n")

def on_exit():
    save_tasks()

def main():
    load_tasks()

    if len(tasks) > 0:
        print("Zapisane zadania:")
        display_tasks()
    else:
        print("Nie ma zapisanych zadań.\n")

    while True:
        print("******Zarządzanie zadaniami******")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Aktualizuj zadanie")
        print("5. Zapisz zadania do pliku")
        print("6. Wyjście z programu")

        choice = get_valid_input("\nWybierz opcję 1-6: ", str)

        if choice == '1':
            display_tasks()
            task_id = get_valid_input("\nPodaj ID zadania, aby zobaczyć opis (lub 0, aby wrócić do menu): ", int)
            if task_id != 0:
                for task in tasks:
                    if task['id'] == task_id:
                        show_task_description(task)
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
            print("Niepoprawny wybór, spróbuj ponownie\n")

    save_tasks()

if __name__ == '__main__':
    atexit.register(on_exit)
    main()
