# import pandas as pd
# from leki.models import ATC, NetherlandsDrug, PolandDrug


# def import_data_from_xslx(country: str, file_path: str) -> None:
#     df = pd.read_excel(file_path)
    
#     for _, row in df.iterrows():
#         ATCCode, _ = ATC.objects.get_or_create(name=row['active_substance'])
#         country_class = NetherlandsDrug if country == 'Netherlands' else PolandDrug
#         country_class.objects.create(
#             DrugName = row['NAZWA PRODUKTU'],
#             ATCCode = ATCCode,
#             ActiveSubstance =row['SKŁADNIKI AKTYWNY'],
#             RegistrationNumber = row['NUMER REJESTRACYJNY'],
#             ResponsibleEntity = row['PODMIOT ODPOWIEDZIALNY'],
#             PurchaseMode = row['STATUS DOSTAWY'],
#             DrugForm = row['FORMA LEKU'],
#             ApplicationForm = row['FORMA PODANIA']
#         )


# import_data_from_xslx('Netherlands', '../data/meta_netherlands.xlsx')

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:kamaszumi10@localhost:5433/leki_db')

df_pol = pd.read_csv(r'C:/Users/kamil/OneDrive - Politechnika Śląska/studia/mgr/semI/IP/pojekt/dane/polska.csv', sep=';', encoding='utf-8', header=0)
df_neth = pd.read_csv(r'C:/Users/kamil/OneDrive - Politechnika Śląska/studia/mgr/semI/IP/pojekt/dane/netherlands.csv', sep=';', encoding='unicode_escape', header=0)

df_pol.to_sql('PolandDrug', engine, if_exists='replace', index=False)
df_neth.to_sql('NetherlandsDrug', engine, if_exists='replace', index=False)