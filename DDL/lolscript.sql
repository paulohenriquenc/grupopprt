CREATE DATABASE IF NOT EXISTS loldb;
USE loldb;

CREATE TABLE IF NOT EXISTS Player (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS Team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);
CREATE TABLE IF NOT EXISTS Place (
    place_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Performance (
    season_id INT NOT NULL,
    place_id INT NOT NULL,
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    games_played INT,
    wins INT,
    loses INT,
    kills INT,
    deaths INT,
    assists INT,
    creep_score INT,
    gold INT,
    damage INT,
    PRIMARY KEY (season_id, place_id, team_id, player_id),
    FOREIGN KEY (place_id) REFERENCES Place(place_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);
