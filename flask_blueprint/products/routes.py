from flask import Blueprint, render_template
from flask import current_app as app
from flask_blueprint_tutorial.api import fetch_products



# Blueprint Configuration
products_bp = Blueprint(
    'products_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@products_bp.route('/product', methods=['GET'])
def product():
    """Homepage."""
    products = fetch_products(app)
    return render_template(
        'index.jinja2',
        title='Flask Blueprint Demo',
        subtitle='Demonstration of Flask blueprints in action.',
        template='home-template',
        products=products
    )
