#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:20:43 2018

@author: genebenneth
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import customer
from faker import Faker

fakegen = Faker()

def populate(N=5):
    
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()
        
        users = customer.objects.get_or_create(user_firstname=fake_first_name,
                                           user_lastname=fake_last_name,
                                           user_email=fake_email
                                           )[0]
        
if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')    