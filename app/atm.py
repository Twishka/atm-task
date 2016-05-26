from flask import jsonify, request, abort
from app import app
import json
from werkzeug.exceptions import HTTPException, Forbidden
from math import isnan

@app.route('/atm/api/money', methods = ['GET'])
def get_balance():
	balance = json.loads(open("balance.txt").read())["amount"]
	return jsonify({"amount" : balance})
	
@app.route('/atm/api/money', methods = ['POST'])	
def post_cash():
	try :
		amount = request.json["amount"]
	except TypeError:
		return jsonify({"error":"The sum wasn't entered"}), 403
	try :
		float(amount)
	except ValueError:
		return jsonify({'error':'You can only use digits'}), 403
	if amount < 0 :
		return jsonify({'error':'You have entered a negative number'}), 403
	balance = json.loads(open("balance.txt").read())["amount"]
	if amount > balance :
		return jsonify({'error': "You don't have enough money"}), 403
	dict_data = {}
	balance -= amount
	for banknote in (100, 50, 20, 10, 5, 1):
		b_count = amount // banknote
		amount -= b_count * banknote
		dict_data[str(banknote) + "$"] = b_count
	with open('balance.txt', 'w') as outfile :
		json.dump({"amount" : balance}, outfile, indent = 4)
	return jsonify({"cash" : dict_data})
