import pandas as pd

def lire():
    colnames=['id','date']
    orders= pd.read_csv('rsc/raw_data/orders.csv', names=colnames)
    orders.set_index('id', inplace=True)

    colnames=['order_id', 'product_id', 'quantity']
    order_lines= pd.read_csv('rsc/raw_data/order_lines.csv', names=colnames)

    colnames=['id', 'price', 'perc_promo']
    products= pd.read_csv('rsc/raw_data/products.csv', names=colnames)
    products.set_index('id', inplace=True)

    return orders, order_lines, products

def initialiser():
    order_details= pd.DataFrame(columns=['order_id', 'date', 'nb_products', 'amount', 'billed_price'])
    order_details.set_index('order_id', inplace=True)
    return order_details

def remplir(order_details, orders, order_lines, products):

    order_ids=[]
    dates=[]
    nb_products=[]

    for i, row_order in orders.iterrows():
        order_id=i
        date= orders.loc[i, 'date']
        lines_of_order = order_lines[order_lines['order_id'] == i]

        nb_products=0
        amount=0
        billed_price=0

        for j, order_line in lines_of_order.iterrows():
            product_in_order = order_line['product_id']

            quantity_of_product = order_line['quantity']
            nb_products += quantity_of_product

            product_row= products[ products.index == product_in_order ]

            price_of_product=product_row.loc[product_in_order,'price']

            perc_promo_of_product=product_row.loc[product_in_order,'perc_promo']

            amount_elem= price_of_product * quantity_of_product
            amount += amount_elem

            billed_price+= amount_elem*(1-perc_promo_of_product/100)

            #print('-   -    -  next product  -    -    -')

        order_details.loc[i]=[date,nb_products,amount, round(billed_price,2)]
        #print('------------- next order --------------')

    return order_details

def ecrire(order_details):
    print(order_details)
    order_details.to_csv('rsc/raw_data/order_details.csv')

def question1():
    orders, order_lines, products= lire()
    order_details=initialiser()
    order_details=remplir(order_details, orders, order_lines, products)
    ecrire(order_details)
