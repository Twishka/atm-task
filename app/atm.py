from flask import jsonify, request, abort
from app import app
import json
from werkzeug.exceptions import HTTPException, Forbidden
from math import isnan

# 1. gitignore (venv in git)
# 2. Flask in venv missing
# 3. do not use Tab
# 4. clear unused modules
# 5. #!flask/bin/python ?


@app.route('/atm/api/money', methods=['GET'])
def get_balance():
    balance = json.loads(open("balance.txt").read())["amount"]	 # separate, json.load
    return jsonify({"amount" : balance}) # amount -> amount?


@app.route('/atm/api/money', methods = ['POST'])    
def post_cash():
    try:
        amount = request.json["amount"]		# if not json but header json?  if {} - Crash!!!
    except TypeError:
        return jsonify({"error": "The sum wasn't entered"}), 403
    try:
        float(amount) 						# move it up, float?, if 0.000001
    except ValueError:
        return jsonify({'error':'You can only use digits'}), 403
    if amount < 0 :		# if == 0
        return jsonify({'error':'You have entered a negative number'}), 403
    balance = json.loads(open("balance.txt").read())["amount"]		# separate function for balance load
    if amount > balance :
        return jsonify({'error': "You don't have enough money"}), 403
    dict_data = {}			# logic block
    balance -= amount											# 1000 - 0.001 = ...
    for banknote in (100, 50, 20, 10, 5, 1):
        b_count = amount // banknote	# divmod
        amount -= b_count * banknote
        dict_data[str(banknote) + "$"] = b_count
    with open('balance.txt', 'w') as outfile :					# separate function for balance save
        json.dump({"amount" : balance}, outfile, indent = 4)
    return jsonify({"cash" : dict_data})
