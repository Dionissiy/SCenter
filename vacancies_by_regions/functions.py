def set_fields(sheet, professions, regions):
    sheet.write(0, 0, 'Название профессии')
    for i in range(len(professions)):
        sheet.write(i + 1, 0, professions[i])
    for i in range(len(regions)):
        sheet.write(0, i + 1, regions[i])

def count(data, profession, region):
    sum = 0
    for x in data:
        if x['name'] == profession and x['region'] == region:
            sum += (int)(x['number'])
    return sum

def fill_cells(sheet, data, professions, regions):
    for i in range(len(professions)):
        for j in range(len(regions)):
            sheet.write(i + 1, j + 1, count(data, professions[i], regions[j]))

def make_report(sheet, data, professions, regions):
    set_fields(sheet, professions, regions)
    fill_cells(sheet, data, professions, regions)
            
