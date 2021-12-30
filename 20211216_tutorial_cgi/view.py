#!/usr/bin/python3
# File encoding: UTF-8

import os


def get_list():
    list_page = os.listdir(r'data/')
    html_page = ''
    for i in list_page:
        html_page += '''<li><a href="index.py?id={name}">{name}</a></li>'''.format(name=i)

    return html_page

