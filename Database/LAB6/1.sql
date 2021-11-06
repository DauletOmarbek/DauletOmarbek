--a
select *
from client, dealer;

--b
select *
from client inner join dealer on client.dealer_id = dealer.id;

--c
select *
from client inner join  dealer on client.city = dealer.location;

--d
select sell.id, amount, client.name, city
from sell inner join client on sell.client_id = client.id
where 100 < sell.amount and sell.amount < 500;

--e
--???

--f
select client.name, city, dealer.name,charge
from client inner join dealer on client.dealer_id = dealer.id;

--g
select client.name, city, dealer.name, charge
from client inner join  dealer on client.dealer_id = dealer.id
where dealer.charge > 0.12;

--h
select client.name, city, sell.id, date, amount, dealer.name, charge
from (sell inner join client on sell.client_id = client.id) inner join dealer on sell.dealer_id = dealer.id;
--???
--i
select client.name, priority, dealer.name, sell.id, amount
from (dealer inner join client on dealer.id = client.dealer_id) inner join sell on (dealer.id = sell.dealer_id and client.id = sell.client_id)
where amount >=2000;
--???

