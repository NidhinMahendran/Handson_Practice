from flask import Flask
from blueprint.render_page.views import page


app = Flask(__name__)
app.register_blueprint(page)

    
if __name__ == '__main__':
    app.run(debug=True,port=8000)

