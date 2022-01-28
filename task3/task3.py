"""На вход в качестве аргументов программы поступают два файла: tests.json и values.json
(в приложении к заданию находятся примеры этих файлов)
• values.json содержит результаты прохождения тестов с уникальными id
• tests.json содержит структуру для построения отчёта на основе прошедших тестов
(вложенность может быть большей, чем в примере)
Напишите программу, которая формирует файл report.json с заполненными полями value для структуры
tests.json на основании values.json.
Пример:
Часть структуры tests.json:
{"id": 122, "title": "Security test", "value": "", "values": [{"id": 5321, "title": "Confidentiality", "value": ""},
{"id": 5322, "title": "Integrity", "value": ""}]}
После заполнения в соответствии с values.json:
{"values": [{"id": 122, "value": "failed"}, {"id": 5321,"value": "passed"}, {"id": 5322,"value": "failed"}]}
Будет иметь следующий вид в файле report.json:
{"id": 122, "title": "Security test", "value": "failed", "values":
 [{"id": 5321, "title": "Confidentiality", "value": "passed"}, {"id": 5322, "title": "Integrity", "value": "failed"}]}
"""
import json
import sys


def parse_dict(test, values):
    for item in test:
        for elem in values:
            if item['id'] == elem['id']:
                item['value'] = elem['value']
            if 'values' in item.keys():
                parse_dict(item['values'], values)
    return tests_list


if __name__ == '__main__':
    tests_json = sys.argv[1]
    values_json = sys.argv[2]

    with open(tests_json) as f:
        tests = json.load(f)

    with open(values_json) as f:
        values = json.load(f)

    tests_list = tests['tests']
    values_list = values['values']

    parse_dict(tests_list, values_list)

    print(json.dumps(tests_list, indent=4, ensure_ascii=False))

    with open('report.json', 'w') as f:
        f.write(json.dumps(tests_list, indent=4, ensure_ascii=False))
