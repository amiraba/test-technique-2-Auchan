import pandas as pd

def question2():
    order_details=pd.read_csv('rsc/raw_data/order_details.csv')
    #choice=input('Voulez-vous le panier moyen ou le panier moyen réduit? (Saisissez 1 pour le premier choix et 2 pour le deuxième\n')
    #if choice==str(1):
    print(round(order_details.groupby('date')['amount'].mean(),2))
    #elif choice==str(2):
    #    print(round(order_details.groupby('date')['billed_price'].mean(), 2))
    #else:
    #    print('Erreur. Veuillez réessayer, SVP.')