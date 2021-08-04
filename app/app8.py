from flask import Flask
#  from flask_assets import Environment
from sqlalchemy.orm import Bundle

app = Flask(__name__, instance_relative_config=False)
assets = Environment(app)

style_bundle = Bundle(
    'src/less/*.less',
    filters='less,cssmin',
    output='dist/css/style.min.css',
    extra={'rel': 'stylesheet/css'}
)

js_bundle = Bundle(
    'src/js/main.js',
    filters='jsmin',
    output='dist/js/main.min.js'
)


# Register style bundle
assets.register('main_styles', style_bundle)
assets.register('main_js', js_bundle)

# Build LESS styles
style_bundle.build()
js_bundle.build()
