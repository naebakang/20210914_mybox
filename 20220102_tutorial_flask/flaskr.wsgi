<VirtualHost *:80>
    ServerName jdlab_ai_test

    WSGIDaemonProcess app threads=5
    WSGIScriptAlias / /var/www/flaskr/flaskr.wsgi

    <Directory /var/www/flaskr>
        WSGIProcessGroup yourapplication
        WSGIApplicationGroup %{GLOBAL}
        Order deny,allow
        Allow from all
    </Directory>
	ErrorLog /var/www/flaskr/logs/error.log
	LogLevel warn
	CustomLog /var/www/flask/logs/access.log combined
</VirtualHost>

