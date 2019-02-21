from flask import Flask, render_template, jsonify
from Rb.web.controllers import controllers
from flask_cors import CORS
from flask_caching import Cache


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
# cache = Cache(app, config={'CACHE_TYPE': 'filesystem'})
cache = Cache(app, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})


@app.route('/')
def main():
  c = controllers()
  return render_template('index.html')


@app.route("/api/v1/projects")
@cache.cached(timeout=50, key_prefix='all_projects')
def api_list_projects():
  c = controllers()
  return jsonify(c.project_list())

@app.route("/api/v1/project/<id>")
@cache.cached(timeout=50, key_prefix='a_project')
def api_a_project(id):
  c = controllers()
  return jsonify(c.project_detail(id))

@app.route("/api/v1/space/<id>/<rot>")
@cache.cached(timeout=50, key_prefix='a_space')
def api_a_space(id):

  c = controllers()
  return jsonify(c.space_detail(id))

@app.route('/about')
def about():
  return render_template('about.html')

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')

