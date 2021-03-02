from .investors import investors_bp


def init_app(app):
    app.register_blueprint(investors_bp)
