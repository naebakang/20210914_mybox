FROM wsgi:latest_20220120
COPY flaskr/ /var/www/flaskr/
COPY flaskr/flaskr.conf /etc/apache2/sites-available/
COPY requirements.txt /var/www/flaskr/
WORKDIR /var/www/
RUN cd /etc/apache2/sites-available/ && a2dissite 000-default && a2ensite flaskr && cd /var/www/flaskr/ && apt-get install -y python3-pip && pip3 install -r requirements.txt && cd /var/www/ && export FLASK_APP=flaskr && flask init-db && service apache2 stop
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

