--1
select stores_name,store_id,products.product_name, products.upc_code, count(all_orders.upc_code)
from (all_orders inner join stores on all_orders.store_id = stores.stores_id) inner join products on products.upc_code = all_orders.upc_code
group by stores_name,store_id,products.product_name, products.upc_code
order by stores_name,store_id,count(products.upc_code) desc,products.product_name;



--2
select (stores.address).city, product_name, count(products.upc_code)
from (all_orders inner join stores on all_orders.store_id = stores.stores_id) inner join products on products.upc_code = all_orders.upc_code
group by products.upc_code,(stores.address).city
order by (stores.address).city ,count(products.upc_code) desc


--3
select stores_name, sum(price)
from all_orders inner join stores on all_orders.store_id = stores.stores_id
where all_orders.time between '2020-12-31'::date and '2022-01-01'
group by stores_name
order by sum(price) desc
limit 1

--4

--5

