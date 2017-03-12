#!/bin/bash
curl -o data/players.csv 'http://crunchtimebaseball.com/master.csv'
iconv -f ISO-8859-15 -t UTF-8 data/players.csv > data/players_clean.csv
