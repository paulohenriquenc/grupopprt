create database loldb;
use loldb;

CREATE TABLE Season (
    season_id INT AUTO_INCREMENT PRIMARY KEY,
    nome INT NOT NULL
);
CREATE TABLE Player (
    player_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);
CREATE TABLE Team (
    team_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);
CREATE TABLE Place (
    place_id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE Season_team_player (
    season_id INT NOT NULL,
    place_id INT NOT NULL,
    team_id INT NOT NULL,
    player_id INT NOT NULL,
    games_played INT,
    wins INT,
    loses INT,
    win_rate FLOAT,
    kills INT,
    deaths INT,
    assists INT,
    KDA FLOAT,
    creep_score INT,
    gold INT,
    damage INT,
    PRIMARY KEY (season_id, place_id, team_id, player_id),
    FOREIGN KEY (season_id) REFERENCES Season(season_id),
    FOREIGN KEY (place_id) REFERENCES Place(place_id),
    FOREIGN KEY (team_id) REFERENCES Team(team_id),
    FOREIGN KEY (player_id) REFERENCES Player(player_id)
);