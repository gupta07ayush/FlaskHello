from flask import Flask, jsonify

# Create a Flask application
app = Flask(__name__)




@app.route("/")
def home():
    return "I am home. Go to /about"

@app.route("/about")
def about():
    return "I am about. Go to /"


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
