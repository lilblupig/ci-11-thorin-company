# Import standard OS library to access environment information.
import os
# Import Flask class.
from flask import Flask

# Create instance of Flask class and store ina variable called app.
# __name__ is a built in variable so Flask can find templates and static files.
app = Flask(__name__)


# Decorator triggers index function below when root directory "/" is accessed.
@app.route("/")
def index():
    return "Hello, World"


# Use os module to get environment variables, or set a default if not found.
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
