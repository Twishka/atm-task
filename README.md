This is my solution of a test task with the following conditions:

Objective:
   Implement web-service for ATM using python3 and Flask web-framework.
The result of this task should be two files atm.py and test.py. First contains API implementation, second unittests for this API.

Description:
   User can check balance and withdraw cash using API. API provided by Flask-server via HTTP. Communication based on JSON format: user and server send JSONs to each other.   

Requirements:
ATM for one user (no authorization required)
ATM has unlimited amount of cash.
Values of bills: 100$, 50$, 20$, 10$, 5$, 1$
Server keeps information about users balance in text file.
Implement API (application public interface) which consists of two methods:
GET balance
url: /atm/api/money
read information about balance from file
return JSON:
{
        “balance”: int
}
POST withdraw
url: /atm/api/money
calculate quantity of each bill (1, 2, 5, ...) depends on requested by user amount. If users balance less than requested amount return error: “You don’t have enaught money.” and HTTP status 403 Forbidden. 
receive JSON:
{
        “amount”: int
    }
return JSON:
    {
        “cash”: {
    “100$”: int,      // if zero can be omitted
    “50$”: int,
    “20$”: int,
    “10$”: int,
    “5$”:int,
    “1$”:int
}
    }
if error return JSON:
    {
        “error”: “message”
}

Unittests:
Cover implemented methods by unittests. Place them into tests.py file.

Example:
> GET http://localhost:5000/atm/api/money
< 200 OK { “balance”: 500 }

> POST http://localhost:5000/atm/api/money
> { “amount”: “357” }
< 200 OK {
    “cash”: {
        “100$”: 3,
        “50$”: 1,
        “5$”: 1,
        “1$”: 2,
}
}

> GET http://localhost:5000/atm/api/money
< 200 OK { “balance”: 143 }

> POST http://localhost:5000/atm/api/money
> { “amount”: “200” }
< 403 Forbidden { “error”: “You don’t have enaught money.” }

Hints:
For development use JetBrains PyCharm IDE (Community edition is free!)
Install new frameworks and libraries using IDE: File/Preferences/ProjectInterpreter ...
Use an official Flask doc: http://flask.pocoo.org/
Place your API methods in different functions. Use ‘route’ decorators parameter ‘method’ to specify which request it handle POST or GET (read the docs for more info).
For easier testing divide your program into small separate methods which are responsible for undivided pieces of work.
To parse and serialize JSONs use standard pythons module “json”.

Good luck!
