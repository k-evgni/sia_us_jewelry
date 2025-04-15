from flask import Flask, render_template, Response, request

app = Flask(__name__)

@app.after_request
def add_cache_control(response):
    # Статика (CSS/JS/изображения) — кеш на 1 год
    if request.path.startswith('/static/'):
        response.headers['Cache-Control'] = 'public, max-age=31536000, immutable'
    # HTML и API — не кешировать
    else:
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/')
def home():
    return Response(
        render_template('index.html'),
        content_type='text/html; charset=utf-8'
    )

if __name__ == '__main__':
    app.run(debug=True)
