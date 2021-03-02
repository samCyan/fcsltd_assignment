
from flask import Flask

from investors.load_data import init_db


def create_app():
    from investors import models, routes
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///investors/locations.db"
    app.config["DEBUG"] = True
    models.init_app(app)
    with app.app_context():
        init_db(models.db, models.investors.Investor)
    routes.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run()
