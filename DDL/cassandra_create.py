from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

try:
    session.execute(
        """
        CREATE KEYSPACE IF NOT EXISTS loldb
        WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }
        """
    )
    session.set_keyspace('loldb')

    session.execute(
        """
        CREATE TABLE IF NOT EXISTS Performance (
            team TEXT,
            player TEXT,
            season INT,
            place TEXT,
            games_played INT,
            wins INT,
            loses INT,
            kills INT,
            deaths INT,
            assists INT,
            creep_score INT,
            gold INT,
            damage INT,
            PRIMARY KEY ((team, player, season, place))
        )
        """
    )

    rows = session.execute("SELECT * FROM system_schema.tables WHERE keyspace_name = 'loldb'")
    if rows:
        print('Tabelas no keyspace "loldb": ')
        for row in rows:
            print(row.table_name)
    else:
        print('Nenhuma tabela encontrada em "loldb".')

except Exception as e:
    print('Erro: ', e)

session.shutdown()
cluster.shutdown()