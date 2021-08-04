"""Initialize Flask app."""
#  import profile
from flask import compile_static_assets
from flask import Flask
from .home import routes
from .profile import routes
from .products import routes
from flask_assets import Environment


def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our application
        from .home import routes
        from .profile import routes
        from .products import routes

        # Register Blueprints
        app.register_blueprint(home.routes.home_bp)
        app.register_blueprint(products.routes.products_bp)
        app.register_blueprint(profile.routes.profile_bp)

        # Compile static assets
        compile_static_assets(assets)   # executes logic



        return app
