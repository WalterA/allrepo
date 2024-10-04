--1 Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
SELECT a.codice , a.nome, count(distinct arr.comp)
from aeroporto a, arrpart arr 
where arr.arrivo = a.codice or a.codice=arr.partenza
group by a.codice , a.nome

--2  Quanti sono i voli che partono dall ’aeroporto ’HTR’ e 
--hanno una durata di almeno 100 minuti?
SELECT count(arr.partenza) as "num_voli"
from arrpart arr, volo v
where arr.partenza = 'HTR' and arr.codice=v.codice and v.durataminuti<=100

--3  Quanti sono gli aeroporti sui quali opera la compagnia ’Apitalia ’ , per
--ogni nazione nella quale opera?
select distinct la.nazione , count( arr.codice)
from arrpart arr, luogoaeroporto la
where arr.comp= 'Apitalia'
group by arr.codice, la.nazione

--4) Qual e’ la media, i l massimo e i l minimo della durata dei voli effettuati
-- dalla compagnia ’MagicFly’?
SELECT avg(v.durataminuti), max(v.durataminuti), min(v.durataminuti)
FROM VOLO v
WHERE v.comp = 'MagicFly'

--5) Qual e’ l ’anno di fondazione della compagnia piu’ vecchia che opera in
-- ognuno degli aeroporti?
SELECT 
    a.codice AS codice_aeroporto,
    a.nome AS nome_aeroporto,
    MIN(c.annofondaz) AS anno_fondazione
FROM 
    Aeroporto a, 
    Compagnia c, 
    ArrPart ap
WHERE 
    (ap.arrivo = a.codice OR ap.partenza = a.codice)
    AND ap.comp = c.nome
GROUP BY 
    a.codice, a.nome
ORDER BY 
    a.codice;

