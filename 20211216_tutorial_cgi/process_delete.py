#!/usr/bin/python3
# File encoding: UTF-8

import cgi
import os

form = cgi.FieldStorage()
id_page = form['title'].value

os.remove('data/{}'.format(id_page))

print('Location: index.py\n')

