import os
from flask import Flask
from werkzeug import secure_filename

import controllers

# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder = 'templates')

# Register the controllers
app.register_blueprint(controllers.api)

# Listen on external IPs
# For us, listen to port 3000 so you can just run 'python app.py' to start the server
if __name__ == '__main__':
	# listen on external IPs
	app.run(host = '0.0.0.0', port = 3000, debug = True)
