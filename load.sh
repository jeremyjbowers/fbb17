#!/bin/bash
psql -c "drop database fbb17;"
psql -c "create database fbb17;"
cat fields/players.txt | psql -d fbb17
cat data/players_clean.csv | psql -d fbb17 -c "COPY players FROM stdin DELIMITER ',' CSV HEADER;"
