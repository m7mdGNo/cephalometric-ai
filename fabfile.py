import os
from fabric.api import *

env.hosts = ['ubuntu@34.227.67.212']
PROJECT_DIR = '/home/ubuntu/cephalometric'


def install_fixture(fixture):
    with prefix('cd {}'.format(PROJECT_DIR)):
        with prefix('source {}/venv/bin/activate'.format(PROJECT_DIR)):
            run('python3 manage.py loaddata {}'.format(fixture))


def createsuperuser():
    with prefix('cd {}'.format(PROJECT_DIR)):
        with prefix('source {}/venv/bin/activate'.format(PROJECT_DIR)):
            run ('python3 manage.py createsuperuser')


def manage(command):
    with prefix('cd {}'.format(PROJECT_DIR)):
        with prefix('source {}/venv/bin/activate'.format(PROJECT_DIR)):
            run ('python3 manage.py {}'.format(command))


def update():
    with prefix('cd {}'.format(PROJECT_DIR)):
        run('git pull')
        with prefix('source {}/venv/bin/activate'.format(PROJECT_DIR)):
            run('pip3 install --no-cache-dir -r requirements.txt')
            run('python3 manage.py migrate --noinput')
            run('python3 manage.py collectstatic --noinput')
        sudo('cp infrastructure/nginx.conf /etc/nginx/sites-available/')
        sudo('cp infrastructure/common.conf /etc/nginx/sites-available/')
        sudo('service nginx restart')

        sudo('cp infrastructure/gunicorn.conf /etc/supervisor/conf.d/')
        # sudo('cp infrastructure/celery.conf /etc/supervisor/conf.d/')
        sudo('supervisorctl reread')
        sudo('supervisorctl update')
        sudo('supervisorctl restart gunicorn')
        # sudo('supervisorctl restart celery')