--1 Quanti sono gli strutturati di ogni fascia?
select a.posizione , count(a1.posizione)
from persona a, persona a1
where a.id = a1.id 
group by a.posizione,a1.posizione
order by a.posizione desc
-- 2) Quanti sono gli strutturati con stipendio>=40000?
select count (a.stipendio) as numero
from persona a
where a.stipendio >=40000
-- 3) Quanti sono i progetti gia ’ finiti che superano i l budget di 50000?
select count(pr.budget) as numero
from progetto pr
where pr.budget >50000
 --4) Qual e’ la media, i l massimo e i l minimo delle ore
-- delle attivita ’ relative al progetto "Pegasus"?
select avg(a.oredurata)as media , min(a.oredurata) as minimo , max(a.oredurata) as massimo
from attivitaprogetto a ,progetto p
where a.progetto = p.id and p.nome = 'Pegasus'
 -- 5) Quali sono le medie, i massimi e i minimi delle ore giornaliere
 --dedicate al progetto ’Pegasus ’ da ogni singolo docente?
select p.id, p.nome,p.cognome, avg(a.oredurata)as media , min(a.oredurata) as minimo , max(a.oredurata) as massimo
from attivitaprogetto a ,progetto pr, persona p
where a.progetto = pr.id and pr.nome = 'Pegasus' and a.persona = p.id
group by p.id,p.nome , p.cognome, a.oredurata
order by a.oredurata desc
--6) Qual e’ i l numero totale di ore dedicate alla didattica
--da ogni docente?
select distinct att.persona , p.nome , p.cognome, att.oredurata
from attivitanonprogettuale att ,persona p
where att.persona = p.id and att.tipo = 'Didattica'
group by att.persona , p.nome , p.cognome, att.oredurata
-- 7) Qual e’ la media , i l massimo e i l minimo degli stipendi dei ricercatori ?
select  avg(p.stipendio)as media , min(p.stipendio) as minimo , max(p.stipendio) as massimo
from persona p
where p.posizione = 'Ricercatore'
-- 8) Quali sono le medie , i massimi e i minimi degli stipendi
 --dei ricercatori , dei professori
 --associati e dei professori ordinari?
SELECT 
    p.posizione,
    AVG(p.stipendio) AS media,
    MIN(p.stipendio) AS minimo,
    MAX(p.stipendio) AS massimo
FROM 
    persona p
GROUP BY 
    p.posizione;
--Quante ore "Ginevra Riva" ha dedicato ad ogni progetto
-- nel quale ha lavorato?
SELECT 
    att.progetto , pr.nome , att.oredurata
FROM 
    persona p ,attivitaprogetto att, progetto pr
WHERE
	p.nome= 'Ginevra' and
	p.cognome = 'Riva'and
	p.id = att.persona and
	att.progetto = pr.id
--10) Qual e’ i l nome dei progetti su cui lavorano piu ’ di
--due strutturati ?
select p.id , p.nome
from attivitaprogetto a,progetto p
where p.id = a.progetto and a.persona >=3
group by p.id , p.nome
-- 11) Quali sono i professori associati che hanno lavorato
-- su piu ’ di un progetto?
SELECT distinct p.id , p.nome,p.cognome
FROM attivitaprogetto att , persona p
where p.posizione = 'Professore Associato' and p.id= att.persona
