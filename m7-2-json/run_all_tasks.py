# Запуск всех задач по JSON

import subprocess
import sys
import os

def run_task(task_file, description):
    """Запускает задачу и показывает результат"""
    print(f"\n{'='*60}")
    print(f"ЗАПУСК: {description}")
    print(f"Файл: {task_file}")
    print('='*60)
    
    try:
        result = subprocess.run([sys.executable, task_file], 
                              capture_output=True, text=True, encoding='utf-8')
        
        if result.stdout:
            print("ВЫВОД:")
            print(result.stdout)
        
        if result.stderr:
            print("ОШИБКИ:")
            print(result.stderr)
            
        if result.returncode == 0:
            print("✓ ЗАДАЧА ВЫПОЛНЕНА УСПЕШНО")
        else:
            print("✗ ЗАДАЧА ЗАВЕРШИЛАСЬ С ОШИБКОЙ")
            
    except Exception as e:
        print(f"✗ ОШИБКА ЗАПУСКА: {e}")

def main():
    """Запускает все задачи по порядку"""
    
    tasks = [
        ("task1_expenses.py", "Задача 1: Анализатор расходов"),
        ("task2_validator.py", "Задача 2: Валидатор профиля пользователя"),
        ("task3_weather.py", "Задача 3: Трансформатор данных из API"),
        ("task4_config.py", "Задача 4: Генератор конфигурационного файла"),
        ("task5_library.py", "Задача 5: Поиск по JSON-базе данных")
    ]
    
    print("🚀 ЗАПУСК ВСЕХ ЗАДАЧ ПО JSON")
    print(f"Всего задач: {len(tasks)}")
    
    успешных = 0
    
    for task_file, description in tasks:
        if os.path.exists(task_file):
            run_task(task_file, description)
            # Простая проверка успешности (можно улучшить)
            if os.path.exists(task_file):
                успешных += 1
        else:
            print(f"\n✗ ФАЙЛ НЕ НАЙДЕН: {task_file}")
    
    print(f"\n{'='*60}")
    print(f"ИТОГИ: {успешных}/{len(tasks)} задач запущено")
    print('='*60)
    
    # Показываем созданные файлы
    print("\nСОЗДАННЫЕ ФАЙЛЫ:")
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]
    for file in sorted(json_files):
        size = os.path.getsize(file)
        print(f"  📄 {file} ({size} байт)")

if __name__ == "__main__":
    main()