from crypt import methods
from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask, jsonify, request
from dotenv import load_dotenv

load_dotenv()

SWAGGER_URL="/docs"
API_URL="/static/swagger.json"

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "Message": "App up and running successfully"
    })

@app.route("/access",methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server","server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Star Wars API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


