-- Script de création de notre base
----------------------------------------------------------
-- Création des tables, types et insertion des enregistrements nécessaires
-- Certaines requêtes sont encapsulées dans des transactions
-- pour gérer les cas d'artefacts déjà existants (utilisateurs, types, etc.)

-- Table des utilisateurs de l'application
CREATE TABLE IF NOT EXISTS USERS (
    id SERIAL PRIMARY KEY,
    firstName VARCHAR(30) UNIQUE NOT NULL,
    email VARCHAR(90) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL,
    isAdmin BOOLEAN DEFAULT FALSE
);

-- Table de suivi des participations aux feedbacks par semaine
CREATE TABLE IF NOT EXISTS PARTICIPATIONS (
    "year" integer NOT NULL check ("year" > 2018),
    week integer NOT NULL check (week > 0 AND week <= 52),
    user_id INTEGER NOT NULL,
    PRIMARY KEY (week, user_id),
    CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Création du type indiquant la nature du feedback
DO $$ BEGIN
    CREATE TYPE feedback_kind AS ENUM ('liked', 'disliked');
EXCEPTION
    WHEN duplicate_object THEN null;
END $$;

-- Table des feedbacks : un utilisateurs = n feedbacks par semaine
CREATE TABLE IF NOT EXISTS FEEDBACKS (
    id SERIAL PRIMARY KEY,
    "year" integer NOT NULL CHECK ("year" > 2018),
    week integer NOT NULL CHECK (week > 0 AND week <= 52),
    type feedback_kind NOT NULL,
    message varchar(250)
);

-- Création d'un utilsiateur admin pour
DO $$ BEGIN
    INSERT INTO USERS
        (firstName, email, password, isAdmin)
        VALUES ('Administrateur', 'administrator@asciiparait.fr',
        '$2b$12$TEzkaLLTEzKL/n83g959juE3DYrufDUTWA1CFqc85n1dRP/VFRSZq', true);
EXCEPTION
    WHEN unique_violation THEN null;
END $$;