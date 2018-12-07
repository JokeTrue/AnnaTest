from views import WebSocket, IndexView

routes = [
    ('GET', '/', IndexView, 'main'),
    ('GET', '/ws', WebSocket, 'chat'),
]
