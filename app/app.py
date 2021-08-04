from flask import Flask, Markup, render_template, make_response, request, jsonify
from logic import square_of_a_number_plus_nine
from forms import ContactForm, SignupForm

app = Flask(
    __name__,
    instance_relative_config=False,
    template_folder="templates",
    static_folder="static"
    )
app.config['SECRET_KEY']="1q2w3e4r5t6y7u8i9o0p"


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', title='Contact', form=form)


@app.route('/signup')
def signup():
    form = SignupForm()
    return render_template('signup.html', title='Sign Up Form', form=form)

# @app.route('/')
# def home():
#     value = square_of_a_number_plus_nine(5)
#     return 'Value is {}'.format(value)
#
#
# @app.route('/markup')
# def markup():
#     return Markup("<h1> Hello WORLD </h1>")
#
#
# @app.route('/index.html')
# def index():
#     return render_template("index.html")
#
#
# @app.route('/response')
# def response():
#     headers = {"Content-Type": "application/json"}
#     return make_response('it worked!', 200, headers)
#
#
# @app.route('/request', methods=['GET'])
# def request():
#     if request.method != 'GET':
#         return make_response('Malformed Request', 400)
#     headers = {"Content-Type": "application/json"}
#     return make_response('it worked!', 200, headers)
#
#
# @app.route('/jsonify', methods=['GET'])
# def jsonify():
#     if request.method != 'GET':
#         return make_response('Malformed request', 400)
#     my_dict = {'key':'dictionary_value'}
#     headers = {'Content-Type': 'application/json'}
#     return make_response(jsonify(my_dict), 200, headers)
# @app.route('/view/<int:city_id>', methods=['GET'])
# def record_view(city_id):
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM citiesData WHERE id=%s', city_id)
#     result = cursor.fetchall()
#     return render_template('view.html', title='View Form', city=result[0])
#
#
# @app.route('/edit/<int:city_id>', methods=['GET'])
# def form_edit_get(city_id):
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM citiesData WHERE id=%s', city_id)
#     result = cursor.fetchall()
#     return render_template('edit.html', title='Edit Form', city=result[0])
#
#
# @app.route('/edit/<int:city_id>', methods=['POST'])
# def form_update_post(city_id):
#     cursor = mysql.get_db().cursor()
#     inputData = (request.form.get('fldLatD'), request.form.get('fldLatM'), request.form.get('fldLatS'),
#                  request.form.get('fldNS'), request.form.get('fldLonD'), request.form.get('fldLonM'),
#                  request.form.get('fldLonS'), request.form.get('fldEW'), request.form.get('fldCity'),
#                  request.form.get('fldState'), city_id)
#     sql_update_query = """UPDATE citiesData t SET t.fldLatD = %s, t.fldLatM = %s, t.fldLatS = %s, t.fldNS =
#     %s, t.fldLonD = %s, t.fldLonM = %s, t.fldLonS = %s, t.fldEW = %s, t.fldCity = %s, t.fldState = %s WHERE t.id = %s """
#     cursor.execute(sql_update_query, inputData)
#     mysql.get_db().commit()
#     return redirect("/", code=302)
#
#
# @app.route('/cities/new', methods=['GET'])
# def form_insert_get():
#     return render_template('new.html', title='New Form')
#
#
# @app.route('/cities/new', methods=['POST'])
# def form_insert_post():
#     cursor = mysql.get_db().cursor()
#     inputData = (request.form.get('fldLatD'), request.form.get('fldLatM'), request.form.get('fldLatS'),
#                  request.form.get('fldNS'), request.form.get('fldLonD'), request.form.get('fldLonM'),
#                  request.form.get('fldLonS'), request.form.get('fldEW'), request.form.get('fldCity'),
#                  request.form.get('fldState'))
#     sql_insert_query = """INSERT INTO citiesData (fldLatD,fldLatM,fldLatS,fldNS,fldLonD,fldLonM,fldLonS,fldEW,fldCity,fldState) VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s,%s) """
#     cursor.execute(sql_insert_query, inputData)
#     mysql.get_db().commit()
#     return redirect("/", code=302)
#
#
# @app.route('/delete/<int:city_id>', methods=['POST'])
# def form_delete_post(city_id):
#     cursor = mysql.get_db().cursor()
#     sql_delete_query = """DELETE FROM citiesData WHERE id = %s """
#     cursor.execute(sql_delete_query, city_id)
#     mysql.get_db().commit()
#     return redirect("/", code=302)
#
#
# @app.route('/api/v1/cities', methods=['GET'])
# def api_browse() -> str:
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM citiesData')
#     result = cursor.fetchall()
#     json_result = json.dumps(result);
#     resp = Response(json_result, status=200, mimetype='application/json')
#     return resp
#
#
# @app.route('/api/v1/cities/<int:city_id>', methods=['GET'])
# def api_retrieve(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     cursor.execute('SELECT * FROM citiesData WHERE id=%s', city_id)
#     result = cursor.fetchall()
#     json_result = json.dumps(result);
#     resp = Response(json_result, status=200, mimetype='application/json')
#     return resp
#
#
# @app.route('/api/v1/cities/<int:city_id>', methods=['PUT'])
# def api_edit(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     content = request.json
#     inputData = (content['fldLatD'], content['fldLatM'], content['fldLatS'],
#                  content['fldNS'], content['fldLonD'], content['fldLonM'],
#                  content['fldLonS'], content['fldEW'], content['fldCity'],
#                  content['fldState'], city_id)
#     sql_update_query = """UPDATE citiesData t SET t.fldLatD = %s, t.fldLatM = %s, t.fldLatS = %s, t.fldNS =
#         %s, t.fldLonD = %s, t.fldLonM = %s, t.fldLonS = %s, t.fldEW = %s, t.fldCity = %s, t.fldState = %s WHERE t.id = %s """
#     cursor.execute(sql_update_query, inputData)
#     mysql.get_db().commit()
#     resp = Response(status=200, mimetype='application/json')
#     return resp
#
#
# @app.route('/api/v1/cities', methods=['POST'])
# def api_add() -> str:
#
#     content = request.json
#
#     cursor = mysql.get_db().cursor()
#     inputData = (content['fldLatD'], content['fldLatM'], content['fldLatS'],
#                  content['fldNS'], content['fldLonD'], content['fldLonM'],
#                  content['fldLonS'], content['fldEW'], content['fldCity'],
#                  content['fldState'])
#     sql_insert_query = """INSERT INTO citiesData (fldLatD,fldLatM,fldLatS,fldNS,fldLonD,fldLonM,fldLonS,fldEW,fldCity,fldState) VALUES (%s, %s,%s, %s,%s, %s,%s,%s,%s,%s) """
#     cursor.execute(sql_insert_query, inputData)
#     mysql.get_db().commit()
#     resp = Response(status=201, mimetype='application/json')
#     return resp
#
#
# @app.route('/api/v1/cities/<int:city_id>', methods=['DELETE'])
# def api_delete(city_id) -> str:
#     cursor = mysql.get_db().cursor()
#     sql_delete_query = """DELETE FROM citiesData WHERE id = %s """
#     cursor.execute(sql_delete_query, city_id)
#     mysql.get_db().commit()
#     resp = Response(status=200, mimetype='application/json')
#     return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
