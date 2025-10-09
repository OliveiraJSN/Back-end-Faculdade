from flask import Flask
from controllers.cinema_controller import configure_routes

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')

configure_routes(app)

if __name__ == '__main__':
  app.run(debug=True)