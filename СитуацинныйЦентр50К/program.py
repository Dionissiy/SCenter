import csv
from cut_useless_fields import cut_useless_fields
from pprint import pprint as pp

list_of_tables = ['январь.csv', 'февраль.csv', 'март.csv', 'апрель.csv', 'май.csv', 'июнь.csv', 'июль.csv', 'август.csv', 'сентябрь.csv', 'октябрь.csv']
current_folder = 'Металлургия/'

#create list of all vacancies of all CSV files
total_list = []
for x in list_of_tables:
    with open(current_folder + x, encoding = 'UTF-8') as f:
        reader = csv.DictReader(f)
        vacancies = list(reader)
        cut_useless_fields(vacancies)
        total_list += vacancies

#count number of all vacancies
with open('all_vacancies_metallurgy.csv', 'w', encoding = 'UTF-8') as f:
    fieldnames = ['Квартал', 'experience', 'max_salary', 'min_salary', 'title']
    writer =  csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for x in total_list:
        writer.writerows({'Квартал' : x['Квартал'], 'experience' : x['experience'], 'max_salary' : x['max_salary'], 'min_salary' : x['min_salary'], 'title' : x['title']})
        

    