from time import sleep
from datetime import datetime
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

def run_threads(params):
    threads = [threading.Thread(target=write_words, args=param) for param in params]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

started_at = datetime.now()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
ended_at = datetime.now()
elapsed = ended_at - started_at
print(f'Работа потоков {elapsed}')

started_at = datetime.now()
params = [
    (10, 'example5.txt'),
    (30, 'example6.txt'),
    (200, 'example7.txt'),
    (100, 'example8.txt')
]
run_threads(params)
ended_at = datetime.now()
elapsed = ended_at - started_at
print(f'Работа потоков {elapsed}')