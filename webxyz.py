from flask import Flask
from Rb.web.controllers import controllers


app = Flask(__name__)

@app.route('/')
def main():
    c = controllers()
    return c.project_list()
