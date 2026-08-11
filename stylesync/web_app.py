from wsgiref.simple_server import make_server

def web_app(environ, start_response):
    products = [
        {'name': 'Sock', 'value': 7499.99},
        {'name': 'Chair', 'value': 150.55},
        {'name': 'Ball', 'value': 50.10},
        {'name': 'Computer', 'value': 5000.50}
    ]

    html_lines = ''
    for product in products:
        html_lines += f'<li>{product['name']} - R${product['value']}</li>'

    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    final_html = html.replace(f'{{products}}', html_lines)

    return [final_html.encode('utf-8')]

make_server('', 5000, web_app).serve_forever()