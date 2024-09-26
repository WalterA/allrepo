--1 Quante sono le compagnie che operano (sia in arrivo che in partenza) nei diversi aeroporti?
SELECT a.codice, a.nome, COUNT(DISTINCT arr.comp) AS num_companies
FROM aeroporto a, arrpart arr, arrpart arr1
where  a.codice = arr.arrivo AND a.codice = arr1.partenza
GROUP BY a.codice, a.nome;

--2  Quanti sono i voli che partono dall ’aeroporto ’HTR’ e 
--hanno una durata di almeno 100 minuti?
SELECT count(arr.partenza) as "num_voli"
from arrpart arr, volo v
where arr.partenza = 'HTR' and arr.codice=v.codice and v.durataminuti<=100

--3  Quanti sono gli aeroporti sui quali opera la compagnia ’Apitalia ’ , per
--ogni nazione nella quale opera?
