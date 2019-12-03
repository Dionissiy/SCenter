#this script creates one CSV file, which contains all vacancies during current year with corresponding params
import csv

list_of_tables = ['январь.csv', 'февраль.csv', 'март.csv', 'апрель.csv', 'май.csv', 'июнь.csv', 'июль.csv', 'август.csv', 'сентябрь.csv', 'октябрь.csv']

current_folder = 'СМИ/'

output_file_name = 'all_vacancies_media.csv'

current_year = '2019'

fieldnames = ['Квартал', 'experience', 'max_salary', 'min_salary', 'title']

output_file = csv.DictWriter(open(output_file_name, 'w', encoding = 'UTF-8'), fieldnames = fieldnames)
output_file.writeheader()

for month in list_of_tables:
    input_file = csv.DictReader(open(current_folder + month, encoding = 'UTF-8'))
    vacancies = list(input_file)
    for x in vacancies:
        temp = {
            'Квартал' : x['Квартал'], 
            'experience' : x['experience'], 
            'max_salary' : x['max_salary'], 
            'min_salary' : x['min_salary'], 
            'title' : x['title']
        }
        if 'Год' in x:
            if x['Год'] == current_year:
                output_file.writerow(temp)
        else:
            output_file.writerow(temp)
        
        

