.read data.sql

-- Q1
create table flight_costs as
with flight(day, price, pre) as(
  select 1, 20, 0         UNION
  select 2, 30, 20       UNION
  select 3, 40, 30       UNION
  select day + 1 ,  (price + pre) / 2 + 5 * ((day + 1) % 7), price from flight where day < 25 and day > 2
)
  select day, price from flight;

-- Q2
create table schedule as
with flight_possible(first, second, third, prices, path) as(
  select departure, arrival, NULL, price, departure || ", " || arrival || "|" || price from flights where departure = "SFO" and arrival = "PDX" union
  select a.departure, a.arrival, b.arrival, a.price + b.price, a.departure || ", " || a.arrival || ", " || b.arrival || "|" || (a.price + b.price) from flights as a, flights as b where a.departure = "SFO" and b.arrival = "PDX" and a.arrival != "PDX" and a.arrival = b.departure
)
  select path from flight_possible order by prices;

-- Q3
create table shopping_cart as
with shoppling_list(list, budget, pre) as(
  select item, 60 - price, price from supermarket where price <= 60 UNION
  select list || ", " || item, budget - price, price from shoppling_list, supermarket where price <= budget and pre <= price
)
  select list, budget from shoppling_list order by budget, list;

-- Q4
create table number_of_options as
  select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course as a, pies as b where a.calories + b.calories < 2500;

-- Q6
create table healthiest_meats as
with meats(meat_option, max_calories) as(
  select meat, max(a.calories + b.calories) from main_course as a, pies as b group by meat
)
  select meat_option, min(a.calories + b.calories) from meats, main_course as a, pies as b where max_calories < 3000 and meat_option = a.meat group by meat ;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select item, store, min(price)from inventory group by item;

-- Q9
create table shopping_list as
with best_deal(orde, category, store) as(
  select min(MSRP / rating), item ,lowest_prices.store from lowest_prices, products where item = name group by category
)
  select category, store from best_deal;

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as a, stores as b where a.store = b.store;
