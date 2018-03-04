INSERT INTO test1 (timestamp, weight, calorie, sugar, sodium, carbs, fat, blood_pressure, diets, workout, health) VALUES ('1', '12', '1200', '321', '1233', '12313', '1231', '345', '5235', '253', '2335');

INSERT INTO test1 (timestamp, weight, calorie, sugar, sodium, carbs, fat, blood_pressure, diets, workout, health) VALUES ('2', '10', '1200', '321', '1233', '12313', '1231', '345', '5235', '253', '2335');




INSERT INTO test4 (timestamp, weight, calorie, diets）VALUES ('0', '100', '1200', '421');
INSERT INTO test4 (timestamp, weight, calorie, diets） VALUES ('test',  'test', 'test', 'test');



CREATE TABLE test3 (timestamp TEXT, weight TEXT, calorie TEXT, diets TEXT);
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('1', '90', '1200', '200');
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('2', '85', '1200', '250');
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('3', '90', '1200', '200');
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('4', '85', '1200', '150');
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('5', '70', '1300', '0');
INSERT INTO test3 (timestamp, weight, calorie, diets) VALUES ('6', '100', '1200', '421');



 SELECT * FROM test4; //show table

 GRANT <privileges> ON database.tracking TO 'roote'@'localhost' IDENTIFIED BY '12345';


Working example!!
 #!/usr/bin/env python
import pymysql
import pymysql.cursors

# Connect to the database
conn = pymysql.connect(host='localhost', user='root', password='12345', db='tracking', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
cur = conn.cursor()

#selecting files
cur.execute("SELECT * FROM test2;")
results = cur.fetchall()
cur.execute("SELECT weight FROM test2;")
x=cur.fetchall()

# convert unicode into int in a dictionary
results= [dict([a, int(x)] for a, x in b.items()) for b in results]

# output testing 
print(cur.description) 
print(results)
print(x)
print()

cur.close()
conn.close()