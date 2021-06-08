from flask import Flask,  jsonify 
import os 
app = Flask(__name__)
@app.route('/')
def hello_world():
    return jsonify({
        'message': 'hello I am a developer my name is Seil Dulatkyzy',
        'environment': os.environ.get('ENVIRONMENT'),
        'ownner': 'sekolya',
        'namespace': os.environ.get('NAMESPACE')
    })
@app.route('/Sdulatkyzy')
def comming_soon():
    return jsonify({
        'message': 'This is my page Seil Dulatkyzy!!'
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)