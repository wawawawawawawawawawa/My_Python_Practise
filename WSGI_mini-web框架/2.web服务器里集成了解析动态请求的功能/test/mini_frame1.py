# 支持WSGI协议
def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    return 'Hello world'
