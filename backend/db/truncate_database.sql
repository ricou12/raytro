-- Script de suppression de la base
---------------------------------------------------
-- Regrouper les requêtes par 'blocs' d'application (feedbacks, votes, etc.)


-- Supprime tous les éléments nécessaires auxdes feedbacks
DROP TABLE IF EXISTS Participations;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Feedbacks;

DROP TYPE IF EXISTS feedback_kind;


-- Supprime tous les éléments nécessaires aux votes
-- ... Plein de trucs qui suppriment !