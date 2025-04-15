from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return Response(
        render_template('index.html'),
        content_type='text/html; charset=utf-8'
    )

if __name__ == '__main__':
    app.run(debug=True)
