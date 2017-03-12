#!/bin/bash
psql -c "drop database fbb17;"
psql -c "create database fbb17;"

cat fields/players.txt | psql -d fbb17
cat fields/proj_bat_atc.txt | psql -d fbb17
cat fields/proj_bat_zips.txt | psql -d fbb17
cat fields/proj_bat_depthcharts.txt | psql -d fbb17
cat fields/proj_bat_steamer.txt | psql -d fbb17

cat data/players_clean.csv | psql -d fbb17 -c "COPY players FROM stdin DELIMITER ',' CSV HEADER;"
cat data/batters_fg_atc.csv | psql -d fbb17 -c "COPY proj_bat_atc FROM stdin DELIMITER ',' CSV HEADER;"
cat data/batters_fg_zips.csv | psql -d fbb17 -c "COPY proj_bat_zips FROM stdin DELIMITER ',' CSV HEADER;"
cat data/batters_fg_depthcharts.csv | psql -d fbb17 -c "COPY proj_bat_depthcharts FROM stdin DELIMITER ',' CSV HEADER;"
cat data/batters_fg_steamer.csv | psql -d fbb17 -c "COPY proj_bat_steamer FROM stdin DELIMITER ',' CSV HEADER;"
