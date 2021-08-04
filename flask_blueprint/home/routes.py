from flask import Blueprint, render_template
from flask import current_app as app
from flask_blueprint_tutorial.api import fetch_products



# Blueprint Configuration
home_bp = Blueprint(
    'home_bp', __name__,
    static_folder='flask_blueprint_tutorial/home/static',
    template_folder='flask_blueprint_tutorial/home/templates'
)


@home_bp.route('/home7', methods=['GET'])
def home():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        'index.jinja2',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
        products=products
    )
