.read sp16data.sql
.read fa16data.sql

CREATE TABLE obedience AS
  SELECT seven, denero FROM STUDENTS;

CREATE TABLE smallest_int AS
  SELECT time, smallest FROM STUDENTS WHERE smallest > 8 ORDER BY smallest LIMIT 20;

CREATE TABLE greatstudents AS
  select this.date, this.number, this.pet, this.color, last.color from sp16students as last, students as this where this.date = last.date and this.number = last.number and this.pet = last.pet;

CREATE TABLE sevens AS
  select a.seven from students as a, checkboxes as b where a.number = 7 and b.'7' = "True" and a.time = b.time;

CREATE TABLE matchmaker AS
  select a.pet, a.song, a.color, b.color from students as a, students as b where a.time != b.time and a.pet = b.pet and a.song = b.song;
