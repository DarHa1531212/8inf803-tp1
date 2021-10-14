
DROP DATABASE IF EXISTS devoir; 
CREATE DATABASE devoir; 
USE devoir;
-- BD POUR DEVOIR BASES DE DONNÉES RÉPARTIES
-- CRÉÉE LE 24/09/2021 PAR Hans Darmstadt-Bélanger

-- Création de la bd

-- Table tblSpell
DROP TABLE IF EXISTS spell

create table spell
(
    id               int          not null,
    components       text         null,
    level            int          not null,
    name             varchar(255) not null,
    spell_resistance text         not null,
    constraint final_final_id_uindex
        unique (id),
    constraint final_final_name_uindex
        unique (name)
);

