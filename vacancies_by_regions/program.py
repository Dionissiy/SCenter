from data import regions, professions_metallurgy, professions_food, professions_media
from functions import make_report
import xlwt
import csv

f = open('dataProfessionInFourIndustries.csv', 'r', encoding='UTF-8')
input_file = csv.DictReader(f)
data = list(input_file)

book = xlwt.Workbook('Data')

sheet = book.add_sheet('metallurgy')
make_report(sheet, data, professions_metallurgy, regions)

sheet = book.add_sheet('food')
make_report(sheet, data, professions_food, regions)

sheet = book.add_sheet('media')
make_report(sheet, data, professions_media, regions)

book.save('vacancies.xls')