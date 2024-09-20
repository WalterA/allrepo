-- Quali sono i voli (codice e nome della compagnia) la cui durata supera le 3 ore?
select v.codice, v.comp
from volo v
where v.durataminuti > 270
-- Quali sono le compagnie che hanno voli che superano le 3 ore?
select distinct v.comp
from volo v
where v.durataminuti > 270
-- Quali sono i voli (codice e nome della compagnia) che partono dall ’ aeroporto con codice ’CIA’?
select distinct v.codice ,v.comp
from volo v, arrpart arr
where arr.partenza = 'CIA' and v.codice = arr.codice
--Quali sono le compagnie che hanno voli che arrivano all ’ aeroporto con codice ’FCO’
select distinct v.comp
from volo v, arrpart arr
where arr.arrivo = 'FCO' and v.codice = arr.codice
--Quali sono i voli (codice e nome della compagnia) che partono dall ’
-- aeroporto ’FCO’ e arrivano all ’ aeroporto ’JFK’
select distinct v.codice, v.comp
from volo v, arrpart arr
where arr.arrivo = 'JFK' and v.codice = arr.codice and arr.partenza ='FCO'
-- Quali sono le compagnie che hanno voli che partono dall ’ aeroporto ’FCO’ e
--atterrano all ’ aeroporto ’JFK’
select distinct v.comp
from volo v, arrpart arr
where arr.arrivo = 'JFK' and v.codice = arr.codice and arr.partenza ='FCO'
-- Quali sono i nomi delle compagnie che hanno voli diretti dalla citta ’ di
 --’Roma’ alla citta ’ di ’New York ’
select distinct v.comp
from volo v, arrpart arr
where arr.arrivo = 'JFK' and v.codice = arr.codice and arr.partenza ='CIA' or arr.partenza = 'FCO'

-- Quali sono gli aeroporti (con codice IATA, nome e luogo) nei quali
 --partono voli della compagnia di nome ’MagicFly ’
select distinct arr.partenza, a.nome , la.citta
from arrpart arr , luogoaeroporto la, aeroporto a, volo v
where arr.comp='MagicFly' and la.aeroporto = arr.partenza and v.comp=arr.comp and arr.codice = arr.codice
    and a.codice = arr.partenza

-- Quali sono i voli che partono da un qualunque aeroporto della citta ’ di ’
 --Roma’ e atterrano ad un qualunque aeroporto della citta ’ di ’New York’?
 --Restituire : codice del volo , nome della compagnia , e aeroporti di
 --partenza e arrivo 
select distinct v.comp v.codice, arr.partenza, arr
from arrpart arr , luogoaeroporto la, aeroporto a, volo v
where la.citta = 'Roma' and la.citta='New York' and
