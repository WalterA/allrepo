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
-- 3) Per ogni categoria di strutturati quante sono le persone con uno stipendio che differisce di al massimo una deviazione standard dalla media della loro categoria?