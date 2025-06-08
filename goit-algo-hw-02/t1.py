from queue import Queue

line = Queue()

def generate_requests():
    request = input("Enter your request: ")    
    line.put(request)
    print(line.queue)

def process_request():
    if not line.empty():
        request = line.get()
        print(f'Request "{request}" was done')
    else:        
        print(f'Queue is empty. Current state is {line.queue}')


if __name__ == "__main__":
    while True:
        command = input("Enter to create & process, 'process' to process only, or 'exit': ")
        if command.lower() == 'exit':
            break
        elif command.lower() == 'process':
            process_request()
        else:
            generate_requests()
            process_request()


# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги

# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста

# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок
