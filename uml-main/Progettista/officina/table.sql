create TABLE nazione (
    nome varchar not null,
    primary key  (nome)
);
create TABLE regione (
    nome varchar not null ,
    nazione varchar not null,
    primary key (nome, nazione),
    foreign key (nazione) references nazione(nome)
);
create TABLE citta (
    nome varchar not null,
    regione varchar not null ,
    nazione varchar not null,
    primary key  (nome, regione, nazione),
    foreign key (regione, nazione) references regione(nome, nazione),
);

create TABLE marca ( nome varchar not null,
primary key (nome)
);

create TABLE tipoveicolo(nome varchar not null,
    primary key (nome)
);

create TABLE modello(
    nome varchar not null ,
    marca varchar not null,
    tipoveicolo varchar not null,
    primary  key (nome),
    foreign key (marca) references marca(nome),
    foreign key (tipoveicolo) references tipoveicolo(nome)
);


create TABLE veicolo (
    targa Targa not null,
    immatricolazione integer not null,
    modello varchar  not null,
    marca varchar not null,
    primary key(targa),
    foreign key (modello,marca) references modello(nome, marca)
);

create TABLE officina ( 
    nome varchar not nulla,
    indirizzo Indirizzo not null ,
    id integer not null ,

    citta varchar not null ,
    regione varchar not null,
    regione varchar not null,
    primary key (id),
    foreign  key (citta, regione, nazione) references ciita(nome, nazione, regione)
);

create TABLE riparazione (
    riconsegna timestamp,
    codice integer not null,
    officina integer not null
    primary key (codice)
    foreign key (officina) references officina (id)
);

create TABLE persona (
    cf codFis not null
)




