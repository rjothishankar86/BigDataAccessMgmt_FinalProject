#!/bin/bash

sudo apt-get install wget

# remove older copy of file, if it exists
rm -f ny_shooting_inc.csv

# download latest data from USGS
wget https://data.cityofnewyork.us/api/views/833y-fsy8/rows.csv -O ny_shooting_inc.csv