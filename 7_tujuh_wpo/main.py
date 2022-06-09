"""_summary_
A mall wants to make a royalty program. 
For every 1.000.000 rupiahs spent on a mall tenant, will award a 10.000 rupiahs voucher to the registered customer. 
To get the voucher, the customers need to show the tenant invoice.
This invoice will have a unique transaction ID and can only be used once. 
This voucher has a unique code that can only be used once. 
Each voucher has expired time for 3 months. 

Make a program and database to distribute and redeem the voucher (including registration and transaction)
"""

"""notes 
The Program created will be in REST API format.
There are ? use cases : 
1. user can register. (registered users are called customers)
  input   : username, 
  output  : User object  

  table : user
  -> GET: /register/<username>

2. user can buy product from tenants. user get invoice.
  input   : username, total_price
  output  : invoice_id

  table : invoice

-> GET: /buy/<username>/<price>

3. Customers can redeem invoice to get voucher, which value will be determined by the price in invoice.
  input   : username, invoice_id
  output  : object Voucher

  table : voucher
-> GET: /redeem/invoice/<username>/<invoice_id>

4. Customers can check how many voucher he/she has. 
  input   : username
  output  : list of Voucher 

-> GET: /vouchers/<username>

5. Customers can use any voucher he/show owns only once when buy product with voucher applied
  input   : username, product_price, Voucher
  output  : Invoice

-> GET: /buy/<username>/<price>/<voucher_id>

source/example : https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
"""

import os
import json
import sqlite3
from flask import  Flask, jsonify

DB_NAME = 'database.db'
APP_ENV = os.getenv('APP_ENV')
app = Flask(__name__)
app.run(debug=True)

@app.route("/")
def welcome():
  return jsonify({"message":"Selamat datang di Toko TODOS"})

# list all users
@app.route("/users", methods=['GET'])
def list_user():
  conn = sqlite3.connect(DB_NAME)  
  cur = conn.cursor()

  items = cur.execute('SELECT * FROM users').fetchall()
  conn.close()
  json_items = []
  for item in items:
    print(item)
    l_item  = {
      "id" : item[0],
      "username" : item[1],
      "created" : item[2],
    }

    json_items.append(l_item)

  return jsonify(json_items)

# register user by username
@app.route("/register/<username>", methods=['GET'])
def register_user(username):
  print(f"username to be registered = {username}")
  try:
    with sqlite3.connect(DB_NAME) as conn:
      cur = conn.cursor()

      cur.execute('INSERT INTO users (username) VALUES (?)', (username,))

      conn.commit()
      msg = "Record successfully added"      
      ret = jsonify({'status': True, 'message': msg, 'data': username})
      return ret
  except Exception as e:
    print ('Exception : ', str(e))
    conn.rollback()
    ret = jsonify({'status': False, 'message': str(e), 'data': username})

    return ret  

if __name__ == '__main__':
   app.run(debug = True)