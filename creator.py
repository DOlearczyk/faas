# coding=utf-8
#!/bin/bash python
import os

from models import Json, Owner, Account, Client

if not os.path.exists('owners'):
    os.makedirs('owners')
if not os.path.exists('clients'):
    os.makedirs('clients')

owner = Owner('Sample Owner Company', '43-190 Mikołów\nul. Fajna 66', 1111111111,
              Account('Cool bank', '33 5555 5555 5555 5555 5555 5555'))

client = Client('Sample client company', '43-190 Mikołów\nul. Fajna 77', 2222222222, 60, 14)

deliver_to = Client('Sample deliver company', '43-190 Mikołów\nul. Fajna 77', 3333333333, 20, 0)


def create(file_name, source):
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as new_file:
            new_file.write(source.to_json())

create('owners/owner.json', owner)
create('clients/client.json', client)
create('clients/delivery.json', deliver_to)
