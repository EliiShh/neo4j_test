from flask import Flask
from app.controllers.device_controller import device_blueprint
from app.controllers.interaction_controller import interaction_blueprint
from app.controllers.simulator_controller import simulator_blueprint




app = Flask(__name__)
app.register_blueprint(simulator_blueprint, url_prefix="/")
app.register_blueprint(device_blueprint, url_prefix="/")
app.register_blueprint(interaction_blueprint, url_prefix="/")


if __name__ == '__main__':
   app.run()




