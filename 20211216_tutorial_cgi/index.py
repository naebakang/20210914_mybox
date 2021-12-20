#!/usr/bin/python3
# File encoding: UTF-8
print('content-type: text/html; charset=UTF-8\n')

import cgi
import view

descrip_basic = 'The World Wide Web (abbreviated WWW or the Web) is an information space where documents and other web resources are identified by Uniform Resource Locators (URLs), interlinked by hypertext links, and can be accessed via the Internet.[1] English scientist Tim Berners-Lee invented the World Wide Web in 1989. He wrote the first web browser computer program in 1990 while employed at CERN in Switzerland.[2][3] The Web browser was released outside of CERN in 1991, first to other research institutions starting in January 1991 and to the general public on the Internet in August 1991.'
form = cgi.FieldStorage()
if 'id' in form:
    id_page = form['id'].value
    with open('data/'+id_page, 'r') as rb:
        descrip = rb.read()

    update_link = '''<a href='update.py?id={}'>update</a>'''.format(id_page)
    delete_action = '''
    <form action='process_delete.py' method='post'>
        <input type='hidden' name='title' value='{id_page}'>
        <input type='submit' value='delete'>
    </form>
        '''.format(id_page=id_page)
else:
    id_page = 'WEB'
    descrip = descrip_basic
    update_link = ''
    delete_action = ''

print(1+1)
print('''
        <!doctype html>
        <html>
            <head>
                <title>WEB1 - Welcome</title>
                <meta charset="utf-8">
            </head>
            <body>
                <h1><a href='index.py'>WEB</a></h1>
                <ol>{html_page}</ol>
                <a href='create.py'>create</a>
                {update_link}
                {delete_action}
                <h2>{title}</h2>
                <p>{desc}</p>
            </body>
        </html>
        '''.format(html_page=view.get_list(), update_link=update_link, delete_action=delete_action,title=id_page, desc=descrip))

