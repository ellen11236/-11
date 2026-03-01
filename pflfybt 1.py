#Выполнила студент 1-мд-35 Бабаян Эллен
from collections import Counter
import re

def get_top_ips(filename):
    ''' Функция для подсчёта топ-5 IP-адресов '''
    ip_counter = Counter()
    total_request = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                ip = line.split()[0]
                ip_counter[ip] += 1
                total_request += 1
    print("Топ-5 IP- адресов:")
    print("-" * 40)
    for ip, count in ip_counter.most_common(5):
        percentage = (count / total_request) * 100
        print(f"{ip} - {count} запросов ({percentage:.1f}%)")


get_top_ips('logs.txt')

#2
from collections import Counter

def get_status_codes(filename):
    """
    Функция для подсчета запросов по статус-кодам
    """
    status_counter = Counter()
    total_requests = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                # Разбиваем строку на части
                parts = line.split()

                status = parts[-2]
                status_counter[status] += 1
                total_requests += 1

    print("Статус-коды:")
    print("-" * 40)

    for status in sorted(status_counter.keys()):
        count = status_counter[status]
        percentage = (count / total_requests) * 100
        print(f"{status} - {count} запросов ({percentage:.1f}%)")


# Использование
get_status_codes('logs.txt')

# 3
from collections import Counter
import re


def get_top_paths(filename):
    """
    Функция для поиска самых популярных путей запросов
    """
    path_counter = Counter()

    path_pattern = re.compile(r'"[A-Z]+ ([^ ]+) HTTP')

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():
                match = path_pattern.search(line)
                if match:
                    path = match.group(1)  # group(1) - это то, что в скобках
                    path_counter[path] += 1

    print(" Самые популярные пути:")
    print("-" * 40)

    for path, count in path_counter.most_common(3):
        print(f"{path} - {count} запросов")


# Использование
get_top_paths('logs.txt')

#4
def get_total_size_fixed(filename):
    """
    Размер находится на позиции -2!
    """
    total_size = 0
    count = 0
    line_number = 0

    print("🔍 Анализ размеров ответов:")
    print("-" * 50)

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_number += 1
            line = line.strip()
            if not line:
                continue

            parts = line.split()

            size_str = parts[-2]

            size_str = size_str.strip('"')

            try:
                size = int(size_str)
                total_size += size
                count += 1
                print(f"✓ Строка {line_number:2d}: размер = {size:6d} байт")
            except ValueError:
                print(
                    f"✗ Строка {line_number:2d}: НЕ ЧИСЛО! '{size_str}' (индекс {parts.index(size_str) if size_str in parts else '?'})")
                print(f"  Все части: {parts}")
                break

    print("\n" + "=" * 50)
    print(f" Найдено размеров: {count}")
    print(f" Общий размер: {total_size:,} байт")

    if total_size > 0:
        if total_size > 1024 * 1024:
            print(f" Это: {total_size / (1024 * 1024):.2f} MB")
        elif total_size > 1024:
            print(f" Это: {total_size / 1024:.2f} KB")

    return total_size


# Запуск
get_total_size_fixed('logs.txt')