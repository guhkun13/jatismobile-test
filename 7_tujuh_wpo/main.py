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
  -> GET: /register/<username> [DONE]

2. user can buy product from tenants.  
  input   : username, total_price
  output  : invoice

  table : invoice

-> GET: /buy/<username>/<price> [DONE]

3. Customers can redeem invoice to get voucher, which value will be determined by the price in invoice.  
  input   : username, invoice_id
  output  : object Voucher

  table : voucher
-> GET: /redeem/invoice/<username>/<invoice_id> [WIP] => malah diset otomatis wkwk.

4. Customers can check how many voucher he/she has. 
  input   : username
  output  : list of Voucher 

-> GET: /vouchers/<username> [DONE]

5. Customers can use any voucher he/she owns only once when buy product with voucher applied. 
  Expired voucher or already used voucher will not be applied and return error to user. 

  input   : username, product_price, Voucher
  output  : Invoice

-> GET: /buy_with_voucher/<username>/<price>/<voucher_id> [WIP]

source/example : https://www.digitalocean.com/community/tutorials/how-to-use-an-sqlite-database-in-a-flask-application
"""

import datetime
import math
import os
import sqlite3
from flask import  Flask, jsonify
from dateutil.relativedelta import relativedelta

DB_NAME = 'database.db'
APP_ENV = os.getenv('APP_ENV')
SATU_JUTA = 1000000
GOCAP = 10000
YMDHIS = "%Y%m%d%H%M%S"
YMD_HIS = "%Y-%m-%d %H:%M:%S.%f"

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

  items = cur.execute('SELECT * FROM user').fetchall()
  conn.close()

  json_items = []
  for item in items:
    print(item)
    l_item  = {
      "id" : item[0],
      "username" : item[1],
      "total_paying" : item[2],
    }

    json_items.append(l_item)

  return jsonify(json_items)

@app.route("/invoices", methods=['GET'])
def list_invoices():
  conn = sqlite3.connect(DB_NAME)  
  cur = conn.cursor()

  items = cur.execute('SELECT * FROM invoice').fetchall()
  conn.close()

  json_items = []
  for item in items:
    print(item)
    l_item = item
    l_item  = {
      "id" : item[0],
      "username" : item[1],
      "price" : item[2],
      "voucher_id" : item[3],
      "voucher_value" : item[4],
      "final_price" : item[5],
    }

    json_items.append(l_item)

  return jsonify(json_items)


@app.route("/vouchers", methods=['GET'])
def list_vouchers():
  conn = sqlite3.connect(DB_NAME)  
  cur = conn.cursor()

  items = cur.execute('SELECT * FROM voucher').fetchall()
  conn.close()
  ret = ret_json_voucher(items)

  return jsonify(ret)

@app.route("/vouchers/<username>", methods=['GET'])
def list_user_vouchers(username):
  conn = sqlite3.connect(DB_NAME)  
  cur = conn.cursor()

  items = cur.execute('SELECT * FROM voucher WHERE username = ?', (username,)).fetchall()
  conn.close()

  ret = ret_json_voucher(items)

  return jsonify(ret)


def ret_json_voucher(items):
  resp = []
  for item in items:
    print(item)
    l_item = item
    l_item  = {
      "id" : item[0],
      "code" : item[1],
      "amount" : item[2],
      "invoice_id" : item[3],
      "username" : item[4],
      "status" : item[5],
      "created" : item[6],
      "expired" : item[7],
    }

    resp.append(l_item)
  
  return resp

# register user by username
@app.route("/register/<username>", methods=['GET'])
def register_user(username):
  print(f"username to be registered = {username}")
  try:
    with sqlite3.connect(DB_NAME) as conn:
      cur = conn.cursor()
      cur.execute('INSERT INTO user (username) VALUES (?)', (username,))

      conn.commit()
      msg = "Record successfully added"      
      ret = jsonify({'status': True, 'message': msg})
      return ret
  except Exception as e:
    print ('Exception : ', str(e))
    conn.rollback()
    ret = jsonify({'status': False, 'message': str(e)})

    return ret  

def get_registered_user(username):
  conn = sqlite3.connect(DB_NAME)  
  cur = conn.cursor()

  user = cur.execute('SELECT * FROM user where username = ?', (username,)).fetchone()
  conn.close()
  
  return user
  
@app.route("/buy/<username>/<price>", methods=['GET'])
def buy(username, price):
  return buying(username, price)

@app.route("/buy_with_voucher/<username>/<price>/<voucher_id>/", methods=['GET'])
def buy_with_voucher(username, price, voucher_id):
  return buying(username, price, voucher_id)

def get_voucher(id):
  print(f"get voucher by id {id}")

  try:
    with sqlite3.connect(DB_NAME) as conn:
      cur = conn.cursor()      
      item = cur.execute('SELECT * FROM voucher WHERE id = ? ', (id,)).fetchone()
      # print (f"item = {item}")      

    return item
  except Exception as e:
    print (f"Exc : {str(e)}")
    return None

def buying(username, price, voucher_id = None):
  price = int(price)
  if not voucher_id:
    final_price = price
    voucher_value = None
  else:
    # check if the voucher is valid!
    voucher = get_voucher(voucher_id)
    print (f"found = voucher {voucher}")

    v_amount = voucher[2]
    voucher_value = v_amount
    v_status = voucher[5]
    v_expired = voucher[7]
    print (f"v_expired type = {type(v_expired)}")
    
    if not v_status:
      return jsonify({'status':False, 'message': "voucher already used!"})
    
    c_date = datetime.datetime.now()
    x_date = datetime.datetime.strptime(v_expired, YMD_HIS)
    print(f"c date : {c_date} and x_date : {x_date}")

    if c_date > x_date:
      return jsonify({'status':False, 'message': f"voucher expired!"})
    
    # status aman dan belum expired, adjust final_price
    final_price = price - v_amount

  msg = (f"username {username} pay price {price}")  
  print(msg)

  user = get_registered_user(username)
  print(f"found user = {user}")

  if not user:
    ret = jsonify({'status':False, 'message': f"user {username} was not registered"})
    return ret
  else:
    total_paying = user[2]

  try:
    with sqlite3.connect(DB_NAME) as conn:
      cur = conn.cursor()
      
      cur.execute('INSERT INTO invoice (username, price, final_price, voucher_id, voucher_value) VALUES (?, ?, ?, ?, ?)', (username, price, final_price, voucher_id, voucher_value,))

      if voucher_id:
        cur.execute('UPDATE voucher SET status = 0 WHERE id = ? ', (voucher_id,))

      inv_id = cur.lastrowid
      print(f"new inv_id = {inv_id}")

      print(f" ttl paying = {total_paying} | price = {final_price}")
      new_total = total_paying + final_price
      cur.execute('UPDATE user SET total_paying = ? WHERE username = ? ', (new_total, username,))

      if final_price > SATU_JUTA:
        print("!!!price more than sejuta!!!")
        gocap_multiplier = math.floor(price / SATU_JUTA)
        amount = gocap_multiplier * GOCAP
        current_date = datetime.datetime.now()
        strymd = str(current_date.strftime(YMDHIS))
        expired = current_date + relativedelta(months=3)

        print(f"strymd = {strymd}")
        voucher_code = strymd + str(username) + str(inv_id)
        cur.execute('INSERT INTO voucher (code, amount, invoice_id, username, expired ) VALUES (?, ?, ?, ?, ?)', (voucher_code, amount, inv_id, username, expired, ))

      conn.commit()
      msg = "Record successfully added"

      ret = jsonify({'status': True, 'message': msg})
      return ret
  except Exception as e:
    print ('Exception : ', str(e))
    conn.rollback()
    ret = jsonify({'status': False, 'message': str(e)})

    return ret  

  ret = jsonify(msg)
  return ret

if __name__ == '__main__':
   app.run(debug = True)