import pandas as pd
import mysql.connector

db_config = {
    'host': 'localhost',
    'user': 'root',
    'port': '3307',
    'password': 'root',
    'database': 'loldb'
}

# Conectar ao banco de dados
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

df = pd.read_csv('players_stats.csv')

# Troca os espaços vazios por "0"
df = df.fillna(0)

def get_or_insert(table_name, column_name, value):
    cursor.execute(f"SELECT {table_name}_id FROM {table_name} WHERE nome = %s", (value,))
    result = cursor.fetchone()
    if result:
        return result[0]
    else:
        cursor.execute(f"INSERT INTO {table_name} (nome) VALUES (%s)", (value,))
        conn.commit()
        return cursor.lastrowid

for index, row in df.iterrows():
    season_id = get_or_insert('Season', 'nome', row['season'])
    
    place_id = get_or_insert('Place', 'nome', row['event'])
    
    team_id = get_or_insert('Team', 'nome', row['team'])
    
    player_id = get_or_insert('Player', 'nome', row['player'])
    
    cursor.execute(
        """
        INSERT INTO Season_team_player (
            season_id, place_id, team_id, player_id,
            games_played, wins, loses, win_rate, kills,
            deaths, assists, KDA, creep_score, gold, damage
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            season_id, place_id, team_id, player_id,
            row['games_played'], row['wins'], row['loses'],
            row['win_rate'], row['kills'], row['deaths'],
            row['assists'], row['kill_death_assist_ratio'],
            row['creep_score'], row['gold'], row['damage']
        )
    )

conn.commit()
cursor.close()
conn.close()