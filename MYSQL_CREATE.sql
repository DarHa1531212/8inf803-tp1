
DROP DATABASE IF EXISTS devoir; 
CREATE DATABASE devoir; 
USE devoir;
-- BD POUR DEVOIR BASES DE DONNÉES RÉPARTIES
-- CRÉÉE LE 24/09/2021 PAR Hans Darmstadt-Bélanger

-- Création de la bd

-- Table tblSpell
DROP TABLE IF EXISTS tblSpell; 

CREATE TABLE tblSpell(
	SpellId					Int 			NOT NULL UNIQUE AUTO_INCREMENT,
    SpellName				varchar (30)	NOT NULL UNIQUE,
	SpellLevel				Int 			NOT NULL,
    SpellComponents			varchar (18)	NOT NULL,
	SpellResistance			bit 			NOT NULL,
	PRIMARY KEY (SpellId)
);

