from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect('loldb')


result = session.execute("SELECT * FROM Performance LIMIT 10")
for row in result:
    print(row)

result = session.execute("SELECT team, player, season, place FROM Performance LIMIT 10")
for row in result:
    print(row.team, row.player, row.season, row.place)


session.shutdown()
cluster.shutdown()
