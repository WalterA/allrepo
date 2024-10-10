CREATE DOMAIN Reale_01 AS real
    CHECK (value >= 0 AND value <= 1);

CREATE DOMAIN Voto AS integer
    CHECK (value >= 0 AND value <= 5);

CREATE DOMAIN URL AS VARCHAR(255)
    CHECK (VALUE ~* '^https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9._-]*)*$');

CREATE TYPE Popolarita AS ENUM 
    ('bassa', 'media', 'alta');

CREATE DOMAIN IntegerGEZ AS INTEGER
    CHECK (value >= 0);

CREATE DOMAIN RealGEZ AS real
    CHECK (value >= 0);

CREATE DOMAIN RealGZ AS real
    CHECK (value > 0);

CREATE TYPE CondUsato AS ENUM
    ('ottimo', 'buono', 'discreto', 'da sistemare');



CREATE TABLE Utente (
    nome VARCHAR(255) NOT NULL,
    registrazione TIMESTAMP NOT NULL,
    affidabilità Reale_01,
    PRIMARY key (nome)
);
CREATE TABLE Privato(
    Utente VARCHAR(255)  NOT NULL,
    foreign key (Utente) references Utente(nome) 
);

CREATE TABLE VenditoreProf (
    Utente VARCHAR(255) NOT NULL,
    vetrina URL NOT NULL,
    popolarita Popolarita NOT NULL,
    foreign key (Utente) references Utente(nome) 
);

CREATE TABLE Bid (
    istante timestamp,
    prezzo RealGEZ NOT NULL,
    Privato VARCHAR(255) not null ,
    PostaAsta INT ,
    foreign key (PostaAsta) references PostAsta(Post)
    foreign key (Privato) references Privato(Utente) 
);
CREATE TABLE Post (
    descrizione TEXT ,
    pubblicazione TIMESTAMP NOT NULL,
    anni_garanzia IntegerGEZ NOT NULL,
    prezzo RealGEZ NOT NULL,
    ha_feedback BOOLEAN,
    voto Voto,
    commento TEXT,
    nuovo BOOLEAN,
    condizioni CondUsato ,
    id_post SERIAL,
    Utente VARCHAR(255) NOT NULL,
    MetodoPagamento VARCHAR(255) not null,
    Categoria VARCHAR(255),
    Valuta VARCHAR(255),
    primary key (id_post),
    foreign key (Valuta) references Valuta(nome)
    foreign key (Categoria) references Categoria(nome)
    foreign key (MetodoPagamento) references MetodoPagamento(nome),
    foreign key (Utente) references Utente(nome) 
);
CREATE TABLE PostAsta(
    rialzo RealGZ,
    scadenza timestamp,
    Post SERIAL,
    conclusa BOOLEAN,
    bid_aggiudicatario INT, 
    foreign key (Post) references Post(id_post)
);

CREATE TABLE MetodoPagamento (
    nome VARCHAR(255) NOT NULL,
    primary key (nome)
);

CREATE TABLE Categoria(
    nome VARCHAR(255) not null,
    primary key(nome)
);

CREATE TABLE Valuta (
    nome VARCHAR(255) not null,
    primary key (nome)
);

CREATE TABLE PostCompraloSubito(
     Post INT,
     foreign key (Post) references Post(id_post)
);

CREATE TABLE Acquirente(
    Privato VARCHAR(255),
    PostCompraloSubito INT,
    istante timestamp
    foreign key (Privato) references Privato(Utente),
    foreign key (PostCompraloSubito) references PostCompraloSubito(Post)
);



