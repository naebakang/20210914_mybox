#!/usr/bin/python3
# File encoding: UTF-8

import cgi
import html_sanitizer

form = cgi.FieldStorage()
title = form['title'].value
description = form['description'].value

sanitizer = html_sanitizer.Sanitizer()
title = sanitizer.sanitize(title)
description = sanitizer.sanitize(description)

with open('data/'+title, 'w') as wb:
    wb.write(description)

print('Location: index.py?id={}\n'.format(title))

