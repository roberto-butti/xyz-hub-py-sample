from flask import Flask, render_template, jsonify
from Rb.web.controllers import controllers
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/')
def main():
  c = controllers()
  return render_template('index.html')

@app.route("/api/v1/projects")
def api_list_projects():
  c = controllers()
  return jsonify(c.project_list())


@app.route('/about')
def about():
  return render_template('about.html')

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

