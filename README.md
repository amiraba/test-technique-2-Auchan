# sql project

1. 
Je garde les mêmes identifiants entre la table order_details et orders du fait que la situation est modélisée par une relation un-à-un (une commande est unique et a un seul détail et de même les détails d'une commande n'appartiennet qu'à une et une seule commande)

nb_products, étant le nombre de produits distincts achetés dans la commande est assimilée en tant que le nombre des produits spécifiques de la commande (et donc distincts par leurs code à barre unique par exemple). S'il y a une ambiguité sur ce point dans un contexte à large envergure, on doit le comprendre et le valider avec le client ou le product owner au préalable.

Pour la colonne billed_price, dans ce cas, on évitera d'utiliser la solution triviale qui consiste à ajouter une colonne des prix réduits dans la table produits puisqu'il constitue un cumul d'espace de données gaspillé. On préviligiera, par contre, l'estimation en temps réel de ce champs calcul.
```
create table order_details as
select o.id, o.date, sum(l.quantity) as nb_products,  sum(p.price*l.quantity) as amount, ROUND(sum(l.quantity*p.price*(1-p.perc_promo*1.0/100)),2) as billed_price
from order_lines l, orders o, products p
where o.id=l.order_id AND p.id= l.product_id
group by o.id;
```
Dans cet exercice, il s'agit de l'initialisation de la table avec l'historique de nos commandes. Une fois que c'est fait, et en simulant le besoin d'un cas réel où cette table est générée en temps réel et mise à jour ligne par ligne selon les nouvelles commandes, on se rend compte qu'il faut privilégier une procédure stockée qui ajoute une nouvelle ligne dans la base order_details à chaque fois qu'une nouvelle commande est effectuée.

On peut aussi définir une procédure stockée qui permet d'archiver les prix des produits lorsqu'il est modifié afin de conserver la trace de l'information perdue dans la nouvelle table (les prix élémentaires historisés ou les anciens proucentages de promotions contenus dans la commande).

2.
```
select ROUND(AVG(amount),2) as panier_moyen, ROUND(AVG(billed_price),2) as panier_moyen_reduit
from order_details
group by date; 
```
3.
```
select l.product_id
from order_lines l, products p
where p.id=l.product_id AND p.perc_promo<>0
group by l.product_id
order by sum(l.quantity) asc
limit 5; 
```

question 1:

![capture1b](https://user-images.githubusercontent.com/23452983/33506362-e0da8f78-d6ef-11e7-9284-c89d9bcac99a.PNG)

![capture11](https://user-images.githubusercontent.com/23452983/33506372-ec68eb32-d6ef-11e7-8ca6-3551da0d38fe.PNG)

![capture111](https://user-images.githubusercontent.com/23452983/33506377-f2d1e686-d6ef-11e7-872f-daebc5ca6fbc.PNG)


question 2:

![capture2](https://user-images.githubusercontent.com/23452983/33506403-03cd5bdc-d6f0-11e7-8d13-e94adc3b799d.PNG)

![capture2b](https://user-images.githubusercontent.com/23452983/33506409-08ff480e-d6f0-11e7-913d-4c7edef8ce74.PNG)


question 3:

![capture3](https://user-images.githubusercontent.com/23452983/33506421-14a4e18c-d6f0-11e7-8cc0-ad6128cecc78.PNG)

![capture3b](https://user-images.githubusercontent.com/23452983/33506422-179cce0e-d6f0-11e7-85f8-0ad616ea8e29.PNG)


# pandas project

Used: Python, Pandas, Matplotlib, Pytest, Docker. 

```
docker build -t python-auchan . 
docker run python-auchan
```

question 1:

![1](https://user-images.githubusercontent.com/23452983/33506232-482ed892-d6ef-11e7-8357-f5786c516f7b.PNG)

question 2:

![2](https://user-images.githubusercontent.com/23452983/33506245-587886f8-d6ef-11e7-8e0b-27dd0cb72db6.PNG)

question 3:

![3](https://user-images.githubusercontent.com/23452983/33506254-607d9ca8-d6ef-11e7-82aa-d548820dcef8.PNG)

question graphe:

![graph](https://user-images.githubusercontent.com/23452983/33506267-6a1d7ae4-d6ef-11e7-8266-f71876bf3f8a.PNG)
