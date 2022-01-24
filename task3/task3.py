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
