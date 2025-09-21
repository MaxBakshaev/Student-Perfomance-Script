# Тестовое задание: Анализ успеваемости студентов

### 📖 Описание:

Скрипт читает файлы с данными об успеваемости студентов и формирует отчет student-performance. 
Он включает в себя список студентов и среднюю оценку студента, среднее считается по всем предметам, студенты сортируются по успеваемости. Название файлов и название отчета передается в виде параметров --files и --report.

## ⚙️ Установка и запуск:

### 🔹 1. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
```

Для Linux или macOS:
```
source venv/bin/activate
```
Для Windows:
```
venv\Scripts\activate
```

### 🔹 2. Установите зависимости:
```
pip install -r requirements.txt
```

### 🔹 3. Примеры запуска скрипта:
```
python main.py --files students1.csv --report students-performance
python main.py --files students1.csv students2.csv --report students-performance
python main.py --files students1.csv students2.csv students3.csv students4.csv students5.csv --report students-performance
```

## 📊 Добавление новых отчетов на примере `teachers-performance`:



### 1. Добавить в `config.py` название отчета:

self.allowed_reports = [..., "teachers-performance",]


### 2. Добавить в `table.py`:
```
class TeachersTable(BaseTable):
    headers = "ваше_значение"
    tablefmt = "ваше_значение"
    colalign = "ваше_значение"
```

### 3. Создать файл `teachers-report.py`, в котором нужно написать логику аналогично students-report.py:
Функция `get_teachers_some_params_table` будет получать на вход список из списков параметров строк из файлов .csv, и возвращать объект TeachersTable(table), в который передается аргумент table - отсортированный по нужным параметрам список кортежей;

### 4. Добавить в `report.py`:
```
class TeachersPerformanceReport(BaseReport):
    def build_table(self, rows_list):
        return get_teachers_some_params_table(rows_list)

class ReportGenerator:
    def report_generator(self):
        elif parced_args.report == "teachers-performance":
            rg = TeachersPerformanceReport()
```