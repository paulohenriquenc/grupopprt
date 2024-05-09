<h1> Tecnologia escolhida: </h1>
<div style="text-align: justify;">
<p>Optamos por usar o Cassandra como tecnologia para esse trabalho. O Cassandra é um banco de dados NoSQL distribuído, projetado para lidar com grandes volumes de dados e operações de alta velocidade. Ele é conhecido por sua escalabilidade e baixa latência, sendo amplamente utilizado em aplicações que exigem alto desempenho e tolerância a falhas.</p>
</div>
<hr>

<h1> League of Legends Worlds Stats </h1>
<div style="text-align: justify;">
<p> O dataset escolhido para realizar este trabalho foi o League of Legends Worlds (2011-2022) Stats, este banco possui diversos dados à respeito dos times e jogadores do Campeonato Mundial de League of Legends dos anos de 2011 até 2022.</p>
</div>

![Imagem League of Legends](https://github.com/paulohenriquenc/grupopprt/assets/83928123/f41c6c15-ac12-46c8-80dc-e1abd8d8d4df)
Link do dataset escolhido: [League of Legends Worlds (2011-2022) Stats](https://www.kaggle.com/datasets/pedrocsar/league-of-legends-worlds-20112022-stats)

<hr>

<h1> Modelo lógico </h1>

![Imagem League of Legends](https://raw.githubusercontent.com/paulohenriquenc/grupopprt/main/current_conceptual_model/model_image.png)

<hr>

<h1> Instalação </h1>
<div style="text-align: justify;">
<p>Inicie o docker e digite <code>docker-compose up -d</code> no diretorio raiz do projeto</p>

<p>o docker-compose criou o banco de dados e agora ele está na porta | 3307 |</p>

<p>execute o arquivo script.py, necessario ter python e instalar as bibliotecas pandas e mysql-connector-python</p>

<p><code>pip install pandaspip</code></p>
<p><code>pip install mysql-connector-python</code></p>

<p>Após isso digite <code>docker-compose exec mysql mysql -uroot -proot loldb</code> </p>

<p>Para consultar o banco de dados use: <code>use loldb;</code> e <code>show tables;</code> </p>
</div>
