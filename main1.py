from flask import Flask, request, jsonify, current_app

# from multiprocessing.pool import ThreadPool
# from app import app

app = Flask(__name__)


@app.route('/')
def home():
    return 'Home page running'


languages = [{'name': 'c'}, {'name': 'java'}, {'name': 'python'}]


@app.route('/get', methods=['GET'])
def test():
    return jsonify({'msg': 'its working'})


@app.route('/lang', methods=['GET'])
def returnAll():
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['GET'])
def returnone(name):
    langs = [language for language in languages if language['name'] == name]
    return jsonify({'language': langs[0]})


@app.route('/lang', methods=['POST'])
def addone():
    language = {'name': request.json['name']}
    languages.append(language)
    return jsonify({'languages': languages})


@app.route('/lang/<string:name>', methods=['PUT'])
def modifyone(name):
    langs = [language for language in languages if language['name'] == name]
    langs[0]['name'] = request.json['name']
    return jsonify({'language': langs[0]})


@app.route('/updateall', methods=['PUT'])
def modifyall():
    # langs = [language for language in languages if language['name'] == name]
    for lang in languages:
        lang['name'] = request.json['name']
    return jsonify({'language': languages})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
