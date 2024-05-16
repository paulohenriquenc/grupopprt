import mysql.connector
from cassandra.cluster import Cluster

# Conecta ao mysql
try:
    conn_mysql = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        port= 3307, 
        password='root',
        database='loldb'
    )
    cursor_mysql = conn_mysql.cursor(dictionary=True)

    print('Conectado ao mySQL.')
except mysql.connector.Error as e:
    print('Erro ao conectar ao mySQL: ', e)
    exit()

# Conecta ao cassandra
try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('loldb')

    print('Conectado ao Cassandra.')
except Exception as e:
    print('Erro ao conectar ao Cassandra: ', e)
    exit()
    
# Copia os dados do mySQL
try:
    cursor_mysql.execute("""
        SELECT 
            Performance.*, Team.nome AS team_nome, Player.nome AS player_nome, Place.nome AS place_nome
        FROM 
            Performance
        JOIN 
            Team ON Performance.team_id = Team.team_id
        JOIN 
            Player ON Performance.player_id = Player.player_id
        JOIN 
            Place ON Performance.place_id = Place.place_id
    """)
    data_performance_mysql = cursor_mysql.fetchall()

    print('Dados da tabela "Performance" do MySQL copiados com sucesso.')
except mysql.connector.Error as e:
    print('Erro ao copiar os dados da tabela "Performance" do MySQL: ', e)
    exit()

# Insere os dados no cassandra
try:
    for data in data_performance_mysql:
        query = """
            INSERT INTO Performance (
                team, player, season, place,
                games_played, wins, loses, kills,
                deaths, assists, creep_score, gold, damage
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        session.execute(query, (
            data['team_nome'], data['player_nome'], data['season_id'], data['place_nome'],
            data['games_played'], data['wins'], data['loses'], data['kills'],
            data['deaths'], data['assists'], data['creep_score'], data['gold'], data['damage']
        ))

    print('Dados do MySQL inseridos com sucesso na tabela "Performance" do Cassandra.')
except Exception as e:
    print('Erro ao inserir os dados na tabela "Performance" do Cassandra: ', e)
    exit()

cursor_mysql.close()
conn_mysql.close()

session.shutdown()
cluster.shutdown()
