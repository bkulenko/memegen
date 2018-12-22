#! /usr/bin/bash

su - postgres
createuser root -s
psql -f initdb/1-create-database-and-table.sql
