import csv

class qvartal:
    def __init__(self, profession, qv, vacancies):
        self.num_vacs = 0
        self.min_salary = None
        self.max_salary = None

        not_init = True
        for x in vacancies:
            if x['title'].lower().find(profession.lower()) != -1 and x['Квартал'] == qv:
                self.num_vacs += 1

                if not_init:
                    self.min_salary = int(x['min_salary'])
                    self.max_salary = int(x['max_salary'])
                    not_init = False
                elif int(x['min_salary']) < self.min_salary:
                    self.min_salary = int(x['min_salary'])
                elif int(x['max_salary']) > self.max_salary:
                    self.max_salary = int(x['max_salary'])

class profession:
    def __init__ (self, title, vacancies):
        self.title = title
        self.q_data = [
            qvartal(title, 'Кв. 1', vacancies), 
            qvartal(title, 'Кв. 2', vacancies), 
            qvartal(title, 'Кв. 3', vacancies), 
            qvartal(title, 'Кв. 4', vacancies)
            ]

    def qvartal_report_num_vacs(self, qv):
        if self.q_data[qv].num_vacs:
            print(f'\t{self.title} :\t {self.q_data[qv].num_vacs}')

    def report(self, num, year = 2019):
        print(f'{num}. По профессии \"{self.title}\"')
        for index in range(4):
            found = 'найдено'
            if int(self.q_data[index].num_vacs) % 100 > 10 and int(self.q_data[index].num_vacs) % 100 < 20:
                nword = 'вакансий'
            elif int(self.q_data[index].num_vacs) % 10 == 1:
                found = 'найдена'
                nword = 'вакансия'
            elif int(self.q_data[index].num_vacs) % 10 > 1 and int(self.q_data[index].num_vacs) % 10 < 5:
                nword = 'вакансии'
            else:
                nword = 'вакансий'
            print(f"\tПо профессии \"{self.title}\" по даным за {index+1} квартал {year} года {found} {self.q_data[index].num_vacs} {nword}, в исходных файлах к данной профессии есть требования к опыту, есть размер минимальной ({self.q_data[index].min_salary} рублей) и максимальной ({self.q_data[index].max_salary} рублей) заработной платы, профессиональный стандарт отсутствует.")
        
#def report(self, year = 2019):
        #print(f'По профессии \"{self.title}\"')
        #for index in range(4):
            #print(f'По даным за {index+1} квартал {year} года :')
            #print(f'{self.q_data[index].num_vacs} вакансий')
            #print(f'минимальная зп ({self.q_data[index].min_salary} рублей')
            #print(f'маскимальная зп ({self.q_data[index].max_salary} рублей\n')