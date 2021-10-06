import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
college = [
    {'id': 0,
     'name': 'Shruti',
     'section': 'C'},
    {'id': 1,
     'name': 'Sanju',
     'section': 'A'},
    {'id': 2,
     'name': 'Rajashri',
     'section': 'B'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>college</h1>
<p>list of students data.</p>'''


@app.route('/api/college/all', methods=['GET'])
def api_all():
    return jsonify(college)


@app.route('/api/college', methods=['GET'])
def api_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []

    for student in college:
        if student['id'] == id:
            results.append(student)
    return jsonify(results)




app.run(debug=True, host='0.0.0.0', port=5000)