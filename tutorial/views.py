# tutorial/views.py

from pyramid.view import view_config

@view_config(route_name="hello", renderer="string")
def hello_world(request):
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'
