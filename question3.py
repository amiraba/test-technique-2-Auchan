import pandas as pd

def initialiser():
    order_lines = pd.read_csv('rsc/raw_data/order_lines.csv', names=['order_id', 'product_id', 'quantity'])
    products = pd.read_csv('rsc/raw_data/products.csv', names=['id', 'price', 'perc_promo'])
    products.set_index('id', inplace=True)
    return order_lines, products

def definir_produit_nb_achetes(order_lines, products):
    products_en_promo=products[products['perc_promo'] != 0]
    for i, row_product in products_en_promo.iterrows():
        products_en_promo.loc[i,'nb_achetes'] = round(order_lines.groupby('product_id').get_group(i)['quantity'].sum())
    return products_en_promo

def tri_selection(products_en_promo):
    products_en_promo.sort_values('nb_achetes', inplace=True)
    return products_en_promo.head(5)

def afficher(products_en_promo):
    print(products_en_promo)

def question3():
    order_lines, products=initialiser()
    products_en_promo= definir_produit_nb_achetes(order_lines, products)
    products_en_promo= tri_selection(products_en_promo)
    afficher(products_en_promo)

