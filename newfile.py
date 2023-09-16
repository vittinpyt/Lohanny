from flask import Flask, render_template
import os

app = Flask(__name__)
foto_dir = 'https://github.com/vittinpyt/Lohanny/assets/145213798/da70f01f-ff3a-450c-80ef-8bd6a6987ff1'

@app.route('/')
def index():
    fotos = [f for f in os.listdir(foto_dir) if f.endswith('.jpg')]
    return render_template('index.html', fotos=fotos)

if __name__ == '__main__':
    app.run(debug=True)
