def cut_useless_fields(vacancies):
    for x in vacancies:
        x.pop('\ufeffconditions', None)
        x.pop('Год', None)
        x.pop('Месяц', None)
        x.pop('industry', None)
        x.pop('education', None)
        x.pop('requirements', None)
        x.pop('responsibilities', None)