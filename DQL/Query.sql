use loldb;

SELECT * from Team;
SELECT COUNT(team_id) AS number_of_Teams FROM Team;

SELECT * FROM Player;
SELECT COUNT(player_id) AS number_of_Players FROM Player;

SELECT * from Performance;

SELECT
    p.season_id,
    p.place_id,
    p.team_id,
    p.player_id,
    pl.nome AS player_name, -- Nome do jogador
    t.nome AS team_name, -- Nome do time
    p.games_played,
    p.wins,
    p.loses,
    p.kills,
    p.deaths,
    p.assists,
    p.creep_score,
    p.gold,
    p.damage,
    FORMAT((p.kills + p.assists) / NULLIF(p.deaths, 0), 2) AS kda, -- Calcula KDA
    FORMAT((p.wins / NULLIF(p.games_played, 0)) * 100, 2) AS win_rate -- Calcula win rate
FROM
    Performance p
JOIN
    Player pl ON p.player_id = pl.player_id -- Junção com a tabela Player
JOIN
    Team t ON p.team_id = t.team_id -- Junção com a tabela Team