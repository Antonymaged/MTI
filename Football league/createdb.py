from engine import engine
from sqlalchemy import text

connection = engine.connect().execution_options(isolation_level="AUTOCOMMIT")

s= text("""
    CREATE DATABASE league;
""")
connection.execute(s)

s = text("""
    USE league

CREATE TABLE clubs (
    cname VARCHAR(30) PRIMARY KEY,
    stadium VARCHAR(30),
    trophies VARCHAR(30),
    estyear VARCHAR(30),
    city VARCHAR(30),
    marketvalue INT,
    num_of_players INT
);

CREATE TABLE players (
    pname VARCHAR(30) PRIMARY KEY,
    origin VARCHAR(30),
    rating INT,
    salary INT,
    pnum INT,
    marketvalue INT,
    age INT,
    cname VARCHAR(30),
    position VARCHAR(30),
    FOREIGN KEY (cname) REFERENCES clubs(cname)
);

CREATE TABLE ltable (
    won INT,
    cname VARCHAR(30),
    points INT,
    ranks INT PRIMARY KEY,
    drawn INT,
    lost INT,
    played INT,
    goalsA INT,
    goalsD INT,
    goalsF INT,
    FOREIGN KEY (cname) REFERENCES clubs(cname)
);

CREATE TABLE matches (
    idmatch INT PRIMARY KEY,
    stadium VARCHAR(30),
    matchs VARCHAR(30),
    dates DATE,
    teams VARCHAR(30),
    hometeam VARCHAR(30),
    awayteam VARCHAR(30),
    attendance VARCHAR(30)
);

CREATE TABLE playersmatches (
    pname varchar(30),
	idmatch int,
	primary key(pname,idmatch),
	FOREIGN KEY (pname) REFERENCES players(pname),
	FOREIGN KEY (idmatch) REFERENCES matches(idmatch)
);

CREATE TABLE clubsmatches (
    cname varchar(30),
	idmatch int,
	primary key(cname,idmatch),
	FOREIGN KEY (cname) REFERENCES clubs(cname),
	FOREIGN KEY (idmatch) REFERENCES matches(idmatch)
);

""")

connection.execute(s)
connection.close()