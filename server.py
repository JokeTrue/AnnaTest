import aiohttp_jinja2
import jinja2
from aiohttp import web

from routes import routes

app = web.Application()

for route in routes:
    app.router.add_route(route[0], route[1], route[2], name=route[3])

# Static
app.router.add_static('/static', 'static', name='static')

# Templates
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

web.run_app(app, port=9000)


