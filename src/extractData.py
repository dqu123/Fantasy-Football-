#!/usr/bin/env python
import os
url = 'http://www.fantasyfootballnerd.com/service/'
ffn_id = 'json/pyxyugixjvn4/'
services = ['players', 'byes', 'injuries']
json_dir = '../json/'

def extract_from(service, ext, file_ext):
    os.system('wget ' + url + service + '/' + ffn_id  \
            + ext + ' -O ' + json_dir + service + file_ext + '.json')
    return

for s in services:
    os.system('wget ' + url + s + '/' + ffn_id + ' -O ' + json_dir + s + '.json') 
os.system('wget ' + url + 'nfl-teams/json/pyxyugixjvn4/ -O ../json/nfl-teams.json')

for i in range(9):
    extract_from('weekly-rankings', 'all/' + str(i + 1) + '/1', \
            '_all_wk' + str(i + 1))
