import requests
import json
import unittest
from flask import jsonify, Flask

url = 'http://localhost:5000/atm/api/money'

class ATMTest(unittest.TestCase) :
	def setUp(self):
		global app
		app = Flask(__name__)
		self.app_context = app.app_context()
	   	self.app_context.push()

	def tearDown(self):
		self.app_context.pop()

	def test_get(self) :
		r = requests.get(url)
		body = json.loads(r.text)
		self.assertEqual(r.status_code, 200)
		self.assertIn('amount', body)

	def test_post(self) :
		cash_out = json.dumps({'amount':20})
		r = requests.post(url, data=cash_out, headers={'Content-Type':'application/json'})
		body = json.loads(r.text)
		self.assertEqual(r.status_code, 200)
		self.assertIn('cash', body)

	def test_not_enough(self):
		cash_out = json.dumps({'amount':200000})
		r = requests.post(url, data=cash_out, headers={'Content-Type':'application/json'})
		self.assertEqual(r.status_code, 403)
		body = json.loads(r.text)['error']
		self.assertIn('enough', body)

	def test_no_json(self):
		cash_out = json.dumps({'amount':456})
		r = requests.post(url, data=cash_out)
		self.assertEqual(r.status_code, 403)
		body = json.loads(r.text)['error']
		self.assertIn('entered', body)

	def test_negative(self):
		cash_out = json.dumps({'amount':-100})
		r = requests.post(url, data=cash_out, headers={'Content-Type':'application/json'})
		self.assertEqual(r.status_code, 403)
		body = json.loads(r.text)['error']
		self.assertIn('negative', body)

	def test_isnan(self):
		cash_out = json.dumps({'amount':'abc'})
		r = requests.post(url, data=cash_out, headers={'Content-Type':'application/json'})
		self.assertEqual(r.status_code, 403)
		body = json.loads(r.text)['error']
		self.assertIn('digits', body)

if __name__ == "__main__" :
	unittest.main()
