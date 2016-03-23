from flask import *

api = Blueprint('api', __name__, template_folder = 'views')

@api.route('/api/true', methods = ['GET'])
def trueFunction():
	return True

@api.route('/api/false', methods = ['GET'])
def falseFunction():
	return False

@api.route('/api', methods = ['GET', 'PUT'])
def apiFunction():
	return 1
