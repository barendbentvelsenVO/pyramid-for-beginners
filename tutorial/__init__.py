# tutorial/__init__.py

import os
from pyramid.config import Configurator

SQLALCHEMY_URL = os.environ.get('DATABASE_URL', '')

def main(global_config, **settings):
    """Returns a Pyramid WSGI application."""
    settings['sqlalchemy.url'] = SQLALCHEMY_URL
    config = Configurator(settings=settings)
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
