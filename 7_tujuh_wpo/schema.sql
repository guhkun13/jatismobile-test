DROP TABLE IF EXISTS user;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR UNIQUE NOT NULL,    
);

DROP TABLE IF EXISTS user_product;

CREATE TABLE invoice (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR NOT NULL,
  price INTEGER NOT NULL,  
  voucher_id INTEGER,
  voucher_value INTEGER,
  final_price INTEGER
)

CREATE TABLE voucher (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  code VARHCAR UNIQUE NOT NULL,
  invoice_id INTEGER NOT NULL,  
  username VARCHAR NOT NULL,  
  status INT NOT NULL DEFAULt 1,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
)
