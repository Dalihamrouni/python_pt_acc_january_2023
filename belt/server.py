from flask_app import app

from flask_app.controllers import dojos ,ninjas
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja





if __name__ == "__main__":
    app.run(debug=True)
