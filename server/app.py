from flask import Flask
from Routes import user
app = Flask(__name__)

def home():
    return "This is a flask server for the Technica 2024 Hackathon"

app.add_url_rule('/','home-page',home,methods=['GET'])

#REVIEW - Register Blueprint
app.register_blueprint(user)

if __name__ == "__main__":
    app.run(debug=True)