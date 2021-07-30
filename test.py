import csv

list_dicts = [
    {
    'name': 'Alan',
    'lastname': 'Wong',
    'age': 29
    },
    {
    'name': 'Beth',
    'lastname': 'Summer',
    'age': 35
    },
    {
    'name': 'Jerry',
    'lastname': 'Smith',
    'age': 39
    }
]

list_dicts_read = []

with open('./test.csv', 'w') as file:
    writer = csv.DictWriter(file, list_dicts[0].keys())
    writer.writeheader()
    writer.writerows(list_dicts)
    
with open('./test.csv', 'r') as file:
    reader = csv.DictReader(file)
    for line in reader:
        list_dicts_read.append(line)
        # ordered_dict_from_csv = list(reader)[line]
        # print(f'ordered_dict_from_csv: {ordered_dict_from_csv}')
        # dict_from_csv = dict(ordered_dict_from_csv)
        # print(dict_from_csv)

print(list_dicts_read)
print(type(list_dicts_read[0]))