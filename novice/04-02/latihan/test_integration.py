from flask import request
import unittest

from webapp import app, db

class TestIntegration(unittest.TestCase):
	"""docstring for TestIntegration"""
	def setUp(self):
		app.config.from_object('webapp.config.Testing')
		db.init_app(app)
		self.app = app.test_client()

	def tearDown(self):
		for collection in db.session.db.collection_names()[1:]:
			db.session.db.drop_collection(collection)

	def test_root(self):
		rv = self.app.get('/')
		assert 'Hello world!' in rv.data

	def test_params(self):
		with app.test_request_context('/?name=Daniel'):
			assert request.path == '/'
			assert request.args['name'] == 'Daniel'


@app.route('/')
def root():
	return 'Hello world! What a beautiful day'

@app.route('/<name>')
def name(name):
	return 'Hello'