create type Strutturato as enum ('Ricercatore', 'Professore Associato','Professore Ordinario');
create type LavoroProgetto as enum ('Ricerca e Sviluppo','Dimostrazione','Management','Altro');
create type LavoroNonProgettuale as enum ('Didattica','Ricerca','Missione','Incontro Dipartimentale','Incontro Accademico','Altro');
create type CausaAssenza as enum ('Chiusura Universitaria','Maternita','Malattia');
create domain PosInteger as integer
    CHECK (VALUE >= 0);
create domain StringaM as varchar(100);
create domain NumeroOre as integer
   CHECK (VALUE >= 0 and VALUE <= 8);
create domain Denaro as real
    CHECK (VALUE >= 0);
create table Persona(id PosInteger not null,
                    nome StringaM NOT NULL,
                    cognome  StringaM not NULL,
                    posizione Strutturato not NULL,
                    stipendio Denaro not NULL,
                    primary key (id));
create table Progetto (id PosInteger not null,
                nome StringaM NOT NULL,
                inizio date not null,
                fine date not null,
                budget Denaro,
                CHECK (inizio<fine),
                primary key (id),
                unique (nome));

create table WP (progetto  PosInteger NOT NULL,
                id PosInteger NOT NULL,
                nome StringaM NOT NULL,
                inizio date NOT NULL,
                fine date NOT NULL,
				primary key (progetto, id),
                CHECK (inizio<fine),
                unique (progetto, nome),
                foreign key (progetto) references Progetto (id));

create table AttivitaProgetto (id  PosInteger NOT NULL,
                            persona PosInteger NOT NULL,
                            progetto PosInteger NOT NULL,
                            wp PosInteger NOT NULL,
                            giorno date NOT NULL,
                            tipo LavoroProgetto NOT NULL,
                            oreDurata NumeroOre NOT NULL,
                            foreign key (persona) references Persona (id),
                            foreign key (progetto, wp) references WP (progetto,id));

create table AttivitaNonProgettuale(id PosInteger NOT NULL,
                                    persona PosInteger NOT NULL,
                                    tipo LavoroNonProgettuale NOT NULL,
                                    giorno date NOT NULL,
                                    oreDurata NumeroOre NOT NULL,
                                    foreign key (persona) references Persona(id));
                                    
create table Assenza(id PosInteger NOT NULL,
                    persona PosInteger NOT NULL,
                    tipo CausaAssenza NOT NULL,
                    giorno date NOT NULL,
                    unique(persona, giorno),
                    foreign key (persona) references Persona(id));


