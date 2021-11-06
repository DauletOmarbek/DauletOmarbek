--a
create view a (date, unique_clients, ave, tot) as
    select date, count(client_id), avg(amount), sum(amount)
    from sell
    group by date
    order by sum(amount) desc;
--b
create view b (date) as
    select date
    from sell
    group by date
    order by sum(amount) desc
    limit 5;
--c
create view c (dealer_id, dealer_name, sales, ave, tot) as
    select dealer.id, dealer.name, count(client_id), avg(amount), sum(amount)
    from sell inner join dealer on sell.dealer_id = dealer.id
    group by dealer.id;
--d
create view d (location, profit) as
    select location, charge*sum(amount)
    from sell inner join dealer on sell.dealer_id = dealer.id
    group by location,charge;
--e
create view e (location,sales, ave, tot) as
    select location, count(sell.id), avg(amount), sum(amount)
    from dealer inner join sell on dealer.id = sell.dealer_id
    group by location;
--f
create view f (city,sales, ave, tot) as
    select city, count(sell.id), avg(amount), sum(amount)
    from client inner join sell on client.id = sell.client_id
    group by city;
--g
create view g (city) as
    select city
    from e inner join f on e.location = f.city
    where e.tot<f.tot;

drop view a;
drop view b;
drop view c;
drop view d;
drop view g;
drop view e;
drop view f;

