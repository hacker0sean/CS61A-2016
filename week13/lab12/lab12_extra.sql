.read lab12.sql

CREATE TABLE sp16favnum AS
  select number, COUNT(*) AS count from sp16students group by number order by count desc limit 1;


CREATE TABLE sp16favpets AS
  select pet, count(*) as count from sp16students group by pet order by count desc limit 10;


CREATE TABLE fa16favpets AS
  select pet, count(*) as count from students group by pet order by count desc limit 10;


CREATE TABLE fa16dragon AS
  select pet, count(*) from students where pet = "dragon" ;


CREATE TABLE fa16alldragons AS
  SELECT pet, COUNT(*) FROM students WHERE pet LIKE '%dragon%';


CREATE TABLE obedienceimage AS
  select seven, denero, count(*) from students where seven = "7" GROUP BY denero;

CREATE TABLE smallest_int_count AS
  SELECT smallest, COUNT(*) FROM students WHERE smallest >= 1 GROUP BY smallest;
