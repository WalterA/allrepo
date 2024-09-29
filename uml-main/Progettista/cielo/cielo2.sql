--1 Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
SELECT a.codice , a.nome, count(distinct arr.comp)
from aeroporto a, arrpart arr , arrpart arr1
where arr.arrivo = a.codice and a.codice=arr1.partenza
group by a.codice 

--2  Quanti sono i voli che partono dall ’aeroporto ’HTR’ e 
--hanno una durata di almeno 100 minuti?
SELECT count(arr.partenza) as "num_voli"
from arrpart arr, volo v
where arr.partenza = 'HTR' and arr.codice=v.codice and v.durataminuti<=100

--3  Quanti sono gli aeroporti sui quali opera la compagnia ’Apitalia ’ , per
--ogni nazione nella quale opera?
select *
from arrpart arr,luogoaeroporto la , aeroporto
where arr.comp= 'Apitalia' 
--group by la.nazione NON HO CAPITO DOVE OPERA IO HO FRANCIA OLTRE A QUELLI DELLA SOLUZIONE

--4) Qual e’ la media, i l massimo e i l minimo della durata dei voli effettuati
-- dalla compagnia ’MagicFly’?
SELECT avg(v.durataminuti), max(v.durataminuti), min(v.durataminuti)
FROM VOLO v
WHERE v.comp = 'MagicFly'