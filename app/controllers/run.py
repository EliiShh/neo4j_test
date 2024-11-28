from flask import Flask
from app.controllers.phone_controller import phone_blueprint



app = Flask(__name__)


if __name__ == '__main__':
   app.register_blueprint(phone_blueprint, url_prefix="/")
   app.run()




