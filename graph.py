import pandas as pd
from pandas import DataFrame

import datetime
import matplotlib.pyplot as plt

order_details = pd.read_csv('rsc/raw_data/order_details.csv')
order_details['mois']=order_details['date'].str[8:10] #[5:7] étant le vrai mois mais le graphe ne sera pas visualisable du fait que tout l'échantillon date de Juillet (7)
#print(order_details.head())

#for i, row in order_details.iterrows():

new = order_details.groupby('mois')['nb_products'].sum()
newnew= new.reset_index('mois')
newnew.columns = ['mois', 'pro_par_mois']
#print((newnew))

plt.bar(newnew['mois'], newnew['pro_par_mois'], color='c')

plt.xlabel('Mois')
plt.ylabel('Nombre de produits achetés')
plt.title('Nombre de produits achetés par mois')

plt.show()