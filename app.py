from flask import Flask, render_template
import main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.get('/')
def index ():
    return render_template(
        'index.html'
   )

if __name__ == '__main__':
    app.run(debug=True)