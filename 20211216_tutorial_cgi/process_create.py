#!/usr/bin/python3
# File encoding: UTF-8

import cgi

form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

with open('data/'+title, 'w') as wb:
    wb.write(description)

print('Location: index.py?id={}\n'.format(title))

