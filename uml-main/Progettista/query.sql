-- 1) Quali sono i cognomi distinti di tutti gli strutturati?
select distinct cognome
from persona
-- 2) Quali sono i Ricercatori (con nome e cognome)?
select nome,  cognome
from persona
where persona.posizione = 'Ricercatore'
-- 3) Quali sono i Professori Associati i l cui cognome comincia con la lettera ’V’?
select nome,  cognome
from persona
where persona.posizione = 'Professore Associato' and cognome like 'V%'
-- 4) Quali sono i Professori (sia Associati che Ordinari) i l cui cognome comincia con la lettera ’V’?
select id, nome,  cognome
from persona
where  persona.posizione IN ('Professore Ordinario', 'Professore Associato') and cognome like 'V%'
-- 5) Quali sono i Progetti gia ’ terminati alla data odierna?
select *
from progetto
where  fine < current_date
-- 6) Quali sono i nomi di tutti i Progetti ordinati in ordine crescente di data di inizio?
select nome
from progetto
order by inizio asc
-- 7) Quali sono i nomi dei WP ordinati in ordine crescente ( per nome)?
select nome
from wp
order by nome asc
-- 8) Quali sono ( distinte ) le cause di assenza di tutti gli strutturati ?
select distinct tipo
from assenza
-- 9) Quali sono ( distinte ) le tipologie di attivita ’ di progetto di tutti gli strutturati?
select distinct tipo
from attivitaprogetto
--10) Quali sono i giorni distinti nei quali del personale ha effettuato attivita ’ non progettuali di tipo ’Didattica ’? Dare i l risultato in ordine crescente .
select distinct giorno
from attivitanonprogettuale
where attivitanonprogettuale.tipo = 'Didattica'
order by giorno asc

--Quali sono il nome, la data di inizio e la data di fine dei WP del progetto di nome ‘Pegasus’?
select WP.nome, WP.inizio , WP.fine
from WP , Progetto
where Progetto.id = WP.progetto and Progetto.name ='Pegasus';
--Quali sono il nome, il cognome e la posizione degli strutturati che hanno almeno una attività nel progetto ‘Pegasus’, ordinati per cognome decrescente?
select distinct p.nome , p.cognome , p.posizione
from  progetto pr , AttivitaProgetto att, Persona p 
where pr.nome = 'Pegasus' and att.persona = p.id and att.progetto = pr.id 
order by cognome desc 

--Quali sono il nome, il cognome e la posizione degli strutturati che hanno più di una attività nel progetto ‘Pegasus’ ?
select distinct p.nome , p.cognome , p.posizione
from Persona p ,attivitaprogetto att ,attivitaprogetto att1 , Progetto pr
where pr.nome = 'Pegasus' and p.id =att.persona and p.id = att2.persona and pr.id=att.progetto and pr.id =att2.progetto and att.id<>att2.id;

--Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto almeno una assenza per malattia?
select distinct p.nome , p.cognome , p.posizione, a.tipo
from Persona p , assenza a 
where a.tipo = 'Malattia' and p.posizione = 'Professore Ordinario'and p.id=a.persona

--Quali sono il nome, il cognome e la posizione dei Professori Ordinari che hanno fatto più di una assenza per malattia?
select distinct p.nome , p.cognome , p.posizione, a.tipo
from Persona p , assenza a , assenza a1
where a.tipo = 'Malattia' and p.posizione = 'Professore Ordinario'
    and p.id=a.persona
    and a.giorno <> a1.giorno
	and a.persona = a1.persona

--Quali sono il nome, il cognome e la posizione dei Ricercatori che hanno almeno un impegno per didattica?
select distinct p.nome , p.cognome , p.posizione
from Persona p, attivitanonprogettuale attn
where p.posizione = 'Ricercatore' and attn.persona = p.id

--