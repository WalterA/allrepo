CREATE TABLE Operatori(
    id  SERIAL ,
    password VARCHAR(20) NOT NULL,
    primary key (id)

);
CREATE TABLE Cittadini(
    nome VARCHAR(20) NOT NULL,
    cognome VARCHAR(20) NOT NULL,
    data_di_nascita VARCHAR(20) NOT NULL,
    codice_fiscale VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL,
    PRIMARY KEY (codice_fiscale) 
);
psql -h 127.0.0.1 -U postgres postgres
