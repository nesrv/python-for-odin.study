# **Урок по `mypy` для новичков: статическая типизация в Python**  

`mypy` — это статический анализатор типов для Python, который помогает находить ошибки, связанные с типами данных, до запуска программы.  

В этом уроке разберём:  
1. Что такое `mypy` и зачем он нужен?  
2. Как установить и настроить `mypy`.  
3. Основы аннотаций типов в Python.  
4. Примеры использования `mypy`.  
5. Интеграция в IDE и CI/CD.  

---

## **1. Зачем нужен `mypy`?**  
Python — язык с динамической типизацией, но с версии **3.5** в нём появились **аннотации типов** (type hints). `mypy` проверяет, чтобы типы данных использовались правильно.  

**Проблемы, которые решает `mypy`:**  
❌ Ошибки в типах аргументов функций.  
❌ Несоответствие возвращаемых типов.  
❌ Опечатки в атрибутах классов.  

**Преимущества:**  
✅ Раннее обнаружение ошибок.  
✅ Улучшает читаемость кода.  
✅ Помогает в больших проектах.  

---

## **2. Установка и запуск**  

### **Установка**  
```bash
pip install mypy
```

### **Проверка файла**  
```bash
mypy ваш_файл.py
```

### **Проверка всей папки**  
```bash
mypy ваша_папка/
```

---

## **3. Основы аннотаций типов**  

### **Аннотации переменных**  
```python
name: str = "Alice"
age: int = 25
is_student: bool = True
```

### **Аннотации функций**  
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### **Сложные типы (из `typing`)**  
```python
from typing import List, Dict, Optional, Union

def process_data(data: List[int]) -> Dict[str, int]:
    return {"count": len(data)}

def get_user(id: int) -> Optional[str]:  # Может вернуть `str` или `None`
    return "Alice" if id == 1 else None

def parse_input(value: Union[str, int]) -> float:  # Принимает `str` или `int`
    return float(value)
```

---

## **4. Примеры работы `mypy`**  

### **❌ Код с ошибками (`bad_code.py`)**  
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(5, "10")  # Ошибка: передаётся строка вместо числа
```

### **Запуск `mypy`**  
```bash
mypy bad_code.py
```

### **Вывод:**  
```
bad_code.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

### **✅ Исправленный код**  
```python
def add(a: int, b: int) -> int:
    return a + b

result = add(5, 10)  # Теперь всё правильно
```

---

## **5. Настройка `mypy`**  

### **Конфигурационный файл (`mypy.ini` или `pyproject.toml`)**  
```ini
[mypy]
python_version = 3.10
ignore_missing_imports = True  # Игнорировать отсутствующие модули
strict = True  # Строгий режим (проверяет всё)
```

### **Игнорирование ошибок**  
```python
result = add(5, "10")  # type: ignore  # mypy пропустит эту строку
```

---

## **6. Интеграция**  

### **В VS Code**  
1. Установите расширение **Python** (Microsoft).  
2. Добавьте в `settings.json`:  
   ```json
   "python.linting.mypyEnabled": true,
   "python.linting.mypyArgs": [
       "--ignore-missing-imports",
       "--strict"
   ]
   ```

### **В CI/CD (GitHub Actions)**  
```yaml
- name: Run mypy
  run: |
    pip install mypy
    mypy .
```

---

## **Итог**  
✅ `mypy` помогает избегать ошибок типов.  
✅ Аннотации (`: type`, `-> type`) делают код понятнее.  
✅ Можно настраивать строгость проверки.  
✅ Интегрируется в IDE и CI/CD.  

**Дальше:**  
- [Документация mypy](https://mypy.readthedocs.io/)  
- `typing` модуль (`List`, `Dict`, `Optional`, и т. д.)  
- `dataclasses` + `mypy` для классов.  

Попробуйте добавить `mypy` в свой проект! 🚀