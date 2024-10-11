--1 Qual è media e deviazione standard degli stipendi per ogni categoria di strutturati?
select p.posizione, avg(p.stipendio), STDDEV(p.stipendio)
from persona p
group by p.posizione
--2  Quali sono i ricercatori ( tutti gli attributi ) con uno stipendio superiore alla media della loro categoria?
SELECT p.nome, p.cognome , p.posizione , p.stipendio
FROM persona p
join persona p2 on p2.posizione = 'Ricercatore'
WHERE p.posizione = 'Ricercatore'
group by p.nome, p.cognome , p.posizione , p.stipendio
having p.stipendio > AVG(p2.stipendio)

with m as (select avg(p.stipendio) as media_strip
from persona p 
WHERE p.posizione='ricercatore')
select
from persona p , m massimo
WHERE p.posizione ='ricerca' and p.stipendio > m.media
-- 3) Per ogni categoria di strutturati quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria?

with m as (select p.posizione as posizione,avg(p.stipendio) as media_strip,
STDDEV(p.stipendio) as deviazione_strip
from persona p 
group by p.posizione)

select p.posizione , count(*)
from persona p, M m 
where p.posizione= m.posizione and 
p.stipendio > m.media - m.STDDEV_strip and 
        p.stipendio <= m.media + m.STDDEV
group by p.posizione;


--5
with stats(
select avg(prog.fine - prog.inizio) 
from PRogetto prog
)
select prog.nome , prog fine - prog.inizio as durata
from progetto prog ,  stats s 
where prog.fine -prog.inizio > s.media