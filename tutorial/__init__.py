# todo/__init__.py

from pyramid.config import Configurator

def main(global_config, **settings):
    """Returns a Pyramid WSGI application."""
    config = Configurator(settings=settings)
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
