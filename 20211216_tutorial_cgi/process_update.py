#!/usr/bin/python3
# File encoding: UTF-8

import cgi
import os
import html_sanitizer

form = cgi.FieldStorage()
title = form['title'].value
title_new = form['title_new'].value
description = form['description'].value

sanitizer = html_sanitizer.Sanitizer()
title_new = sanitizer.sanitize(title_new)
description = sanitizer.sanitize(description)

os.rename('data/{}'.format(title), 'data/{}'.format(title_new))

with open('data/{}'.format(title_new), 'w') as wb:
    wb.write(description)

print('Location: index.py?id={}\n'.format(title_new))

