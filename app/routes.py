# from flask import (
#     Flask,
#     url_for,
#     render_template,
#     redirect
# )
# from forms import ContactForm, SignupForm
#
#
# app = Flask(__name__, instance_relative_config=False)
# app.config.from_object('config.Config')
#
#
# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     """Standard `contact` form."""
#     form = ContactForm()
#     if form.validate_on_submit():
#         return redirect(url_for("success"))
#     return render_template(
#         "contact.jinja2",
#         form=form,
#         template="form-template"
#     )