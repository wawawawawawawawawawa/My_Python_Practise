# 支持WSGI协议并对应页面
def index():
    return "这个是登录页面"


def register():
    return "这是注册页面"


def application(env, start_response):
    start_response("200 OK", [('Content-Type', 'text/html;charset=utf-8')])
    filename = env['PATH_INFO']
    if filename == "/index.py":
        return index()
    elif filename == "/register.py":
        return register()
    else:
        return "HEllo"
