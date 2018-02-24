create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select name, size from dogs as a, sizes as b where height > min and height <= max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select a.name from dogs as a, parents as b, dogs as c where b.child = a.name and c.name = b.parent order by c.height DESC;

-- Sentences about siblings that are the same size
create table sentences as
with silibings(first, second) as(
  select a.child, b.child from parents as a, parents as b where a.parent = b.parent and a.child < b.child
)
  select first || " and " || second || " are " || size || " siblings" from silibings, dogs as a, dogs as b, sizes where a.name = first and b.name = second and a.height > min and a.height <= max and b.height > min and b.height <= max;


-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
with dog_domain(first, second, third, fourth, total_size) as (
  select a.name, b.name, c.name, d.name, a.height + b.height + c.height + d.height as total from dogs as a, dogs as b, dogs as c, dogs as d where a.height + b.height + c.height + d.height >= 170 and a.height < b.height and b.height < c.height and c.height < d.height order by total
)
  select first || ', ' || second || ', ' || third || ', ' || fourth || '|' || total_size  from dog_domain;

-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
with parents_relation(first, second) as (
  select parent, child from parents UNION
  select first, child from parents_relation, parents where second = parent
),
silibings(first, second) as(
  select a.child, b.child from parents as a, parents as b where a.parent = b.parent
)

  select a.name, b.name from dogs as a, dogs as b, parents as c, parents as d where a.name = c.parent and d.name = d.parent and parent != s;

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  with chart(x, y, z) as (
    select a.n, b.n, a.n * b.n from ints as a, ints as b where a.n * b.n <= 100
  )
  select c.z as n, count(*) as k from chart as c group by c.z;


create table primes as
    select n from divisors where k = 2 ;
