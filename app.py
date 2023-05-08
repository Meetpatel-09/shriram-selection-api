from flask import Flask,jsonify,request
from flask_mysqldb import MySQL
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
mysql = MySQL(app)
import os

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'JackOTech@0078'
app.config['MYSQL_DB'] = 'shri_ram_selection'

uploads_dir = os.path.join(app.instance_path, 'uploads')
# os.makedirs(uploads_dir, exists_ok=True)

# app.config['MYSQL_HOST'] = 'aws.connect.psdb.cloud'
# app.config['MYSQL_USER'] = 'ugm3jqlhy86yv4p2r281'
# app.config['MYSQL_PASSWORD'] = 'pscale_pw_5A2RYV89OSU1vEyzWCjevwDlOyh92SnJQiqDTJR5Mki'
# app.config['MYSQL_DB'] = 'learning-flutter-v2'
# app.config['OPTIONS'] = 'learning-flutter-v2'
# app.config['MYSQL_DB'] = {'ssl': True}

# Delete => Delete Data
# GET => Select Data
# POST => Insert Data
# PUT => Update Data
@app.route("/product_image", methods=["POST"])
def process_image():
    file = request.files['image']
    product_id = request.form['prodcuct_id']
    # Read the image via file.stream
    # img = Image.open(file.stream)
    # return 'home page'
    path = os.path.join(uploads_dir, file.filename)
    file.save(path)
    # cur = mysql.connection.cursor()
    return jsonify({'msg': 'success', 'path': path, 'product_id': product_id})

@app.route('/',methods=['DELETE','GET','POST','PUT','PATCH', 'SEARCH'])
def home():
    method = request.method

    if method == "SEARCH":
        return 'Search Page'

    return 'home page'

@app.route('/customer',methods=['DELETE','GET','POST','PUT','PATCH'])
def customer():
    method = request.method
    match method:
        
        case "DELETE":
            customer_id = request.json['customer_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM customer_table WHERE customer_id=%s", (customer_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM customer_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                # print(user[0])
                # print(data)
                enter = {
                    "customer_id" : user[0], 
                    "first_name" : user[1],
                    "last_name" : user[2],
                    "gender" : user[3],
                    "mobile_1" : user[4],
                    "mobile_2" : user[5],
                    "customer_email" : user[6],
                    "customer_password" : user[7],
                    "remark" : user[8]
                }
                data.append(enter)
                count = count + 1

            return jsonify({"data": data})
        
        case "POST":    
            cur = mysql.connection.cursor()
            
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            gender = request.json['gender']
            mobile_1 = request.json['mobile_1']
            mobile_2 = request.json['mobile_2']
            customer_email = request.json['customer_email']
            customer_password = request.json['customer_password']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO customer_table (first_name, last_name, gender, mobile_1, mobile_2, customer_email,customer_password, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, gender, mobile_1, mobile_2, customer_email, customer_password, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT": 

            cur = mysql.connection.cursor()
            customer_id = request.json['customer_id']
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            gender = request.json['gender']
            mobile_1 = request.json['mobile_1']
            mobile_2 = request.json['mobile_2']
            customer_email = request.json['customer_email']
            remark = request.json['remark']

            result = cur.execute("UPDATE customer_table SET first_name = %s,last_name=%s,gender=%s,mobile_1=%s,mobile_2=%s,customer_email=%s,remark=%s WHERE customer_id=%s", (first_name,last_name,gender,mobile_1,mobile_2,customer_email,remark,customer_id))

            mysql.connection.commit()

            cur.close()
            if result == 1:
                data = {
                    "Status":"Successful",
                    "data": {
                        "customer_id": request.json['customer_id'],
                        "first_name": request.json['first_name'],
                        "last_name": request.json['last_name'],
                        "gender": request.json['gender'],
                        "mobile_1": request.json['mobile_1'],
                        "mobile_2": request.json['mobile_2'],
                        "customer_email": request.json['customer_email'],
                        "remark": request.json['remark']
                    }
                }
            
            else:
                data = {"Status":"Failed"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            customer_id = request.json['customer_id']
            cur.execute("SELECT * FROM customer_table WHERE customer_id=%s", (customer_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "customer_id" : user[0], 
                    "first_name" : user[1],
                    "last_name" : user[2],
                    "mobile_1" : user[3],
                    "mobile_2" : user[4],
                    "customer_email" : user[5],
                    "customer_password" : user[6],
                    "remark" : user[7]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)

@app.route('/login',methods=['PATCH'])
def login():
    method = request.method
    match method:
               
        case "PATCH":
            cur = mysql.connection.cursor()
            customer_email = request.json['customer_email']
            cur.execute("SELECT * FROM customer_table WHERE customer_email=%s", (customer_email,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "customer_id" : user[0], 
                    "first_name" : user[1],
                    "last_name" : user[2],
                    "gender" : user[3],
                    "mobile_1" : user[4],
                    "mobile_2" : user[5],
                    "customer_email" : user[6],
                    "customer_password" : user[7],
                    "remark" : user[8]
                }
                return jsonify({"status": 200, "data" : data})
            else:
                data = {"status": 401, 'message': 'User not found'}
                return jsonify(data)

@app.route('/product',methods=['DELETE','GET','POST','PUT','PATCH'])
def product():
    method = request.method
    match method:
        
        case "DELETE":
            product_id = request.json['product_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM product_table WHERE product_id=%s", (product_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "product_id" : user[0], 
                    "product_tittle" : user[1],
                    "product_details" : user[2],
                    "product_price" : user[3],
                    "product_brand" : user[4],
                    "product_quantity" : user[5],
                    "product_review" : user[6],
                    "category" : user[7],
                    "sub_category" : user[8],
                    "product_availability" : user[9],
                    "product_highlight" : user[10],
                    "remark" : user[11],
                    "image": [
                        "image1.png",
                        "image2.png"
                    ]
                }

                
                data.append(enter)
                count = count + 1

            return jsonify({"products": data})
        
        case "POST":    
            cur = mysql.connection.cursor()
            
            product_tittle = request.json['product_tittle']
            product_details = request.json['product_details']
            product_price = request.json['product_price']
            product_brand = request.json['product_brand']
            product_quantity = request.json['product_quantity']
            product_review = request.json['product_review']
            category = request.json['category']
            sub_category = request.json['sub_category']
            product_availability = request.json['product_availability']
            product_highlight = request.json['product_highlight']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO product_table (product_tittle, product_details, product_price, product_brand, product_quantity, product_review, category, sub_category, product_availability, product_highlight, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (product_tittle, product_details, product_price, product_brand, product_quantity, product_review, category, sub_category, product_availability, product_highlight, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":    
           
            cur = mysql.connection.cursor()
            product_id=request.json['product_id']
            product_tittle = request.json['product_tittle']
            product_details = request.json['product_details']
            product_price = request.json['product_price']
            product_brand = request.json['product_brand']
            product_quantity = request.json['product_quantity']
            product_review = request.json['product_review']
            category = request.json['category']
            sub_category = request.json['sub_category']
            product_availability = request.json['product_availability']
            product_highlight = request.json['product_highlight']
            remark = request.json['remark']
            
            cur.execute("UPDATE product_table SET product_tittle = %s,product_details=%s,product_price=%s,product_brand=%s,product_quantity=%s,product_review=%s,category=%s,sub_category=%s,product_availability=%s,product_highlight=%s,remark=%s WHERE product_id=%s", (product_tittle,product_details,product_price,product_brand,product_quantity,product_review,category,sub_category,sub_category,product_availability,product_highlight,remark,product_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}           
           
            # data = {"test":"PUT"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            product_id = request.json['product_id']
            cur.execute("SELECT * FROM customer_table WHERE product_table=%s", (product_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "product_id" : user[0], 
                    "product_tittle" : user[1],
                    "product_details" : user[2],
                    "product_price" : user[3],
                    "product_brand" : user[4],
                    "product_quantity" : user[5],
                    "product_review" : user[6],
                    "category" : user[7],
                    "sub_category" : user[8],
                    "product_availability" : user[9],
                    "product_highlight" : user[10],
                    "remark" : user[11]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)
            
            
@app.route('/employee',methods=['DELETE','GET','POST','PUT','PATCH'])
def employees():
    method = request.method
    match method:
        
        case "DELETE":
            employee_id = request.json['employee_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM employees_table WHERE employee_id=%s", (employee_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM employees_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "employee_id" : user[0], 
                    "first_name" : user[1], 
                    "last_name" : user[2], 
                    "mobile_1" : user[3], 
                    "mobile_2" : user[4], 
                    "email_id" : user[5], 
                    "password" : user[6], 
                    "date_of_birth" : user[7], 
                    "flat_house_no" : user[8], 
                    "locality" : user[9], 
                    "landmark" : user[10], 
                    "pincode" : user[11], 
                    "city" : user[12], 
                    "state" : user[13],
                    "department" : user[14], 
                    "salary" : user[15], 
                    "adharcard" : user[16], 
                    "remark" : user[17]
                }
                data.append(enter)
                count = count + 1

            return jsonify({"data": data})
        
        case "POST":    
            cur = mysql.connection.cursor()

            first_name =  request.json['first_name']
            last_name =  request.json['last_name']
            mobile_1 =  request.json['mobile_1']
            mobile_2 =  request.json['mobile_2']
            email_id =  request.json['email_id']
            password =  request.json['password']
            date_of_birth =  request.json['date_of_birth']
            flat_house_no =  request.json['flat_house_no']
            locality =  request.json['locality']
            landmark =  request.json['landmark'] 
            pincode =  request.json['pincode'] 
            city =  request.json['city'] 
            state =  request.json['state']
            department =  request.json['department'] 
            salary =  request.json['salary'] 
            adharcard =  request.json['adharcard'] 
            remark =  request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO employees_table (employee_id, first_name, last_name, mobile_1, mobile_2, email_id, password, date_of_birth, flat_house_no, locality, landmark, pincode, city, state, department, salary, adharcard, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (employee_id, first_name, last_name, mobile_1, mobile_2, email_id, password, date_of_birth, flat_house_no, locality, landmark, pincode, city, state, department, salary, adharcard, remark,employee_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":    

            cur = mysql.connection.cursor()
            employee_id =request.json['employee_id']
            first_name =  request.json['first_name']
            last_name =  request.json['last_name']
            mobile_1 =  request.json['mobile_1']
            mobile_2 =  request.json['mobile_2']
            email_id =  request.json['email_id']
            password =  request.json['password']
            date_of_birth =  request.json['date_of_birth']
            flat_house_no =  request.json['flat_house_no']
            locality =  request.json['locality']
            landmark =  request.json['landmark'] 
            pincode =  request.json['pincode'] 
            city =  request.json['city'] 
            state =  request.json['state']
            department =  request.json['department'] 
            salary =  request.json['salary'] 
            adharcard =  request.json['adharcard'] 
            remark =  request.json['remark']

            cur.execute("UPDATE employees_table SET first_name = %s,last_name=%s,gender=%s,mobile_1=%s,mobile_2=%s,customer_email=%s,customer_password=%s,remark=%s  WHERE employee_id=%s", (first_name,last_name,mobile_1,mobile_2,email_id,password,date_of_birth,flat_house_no,locality,landmark,pincode,city,state,department,salary,adharcard,remark,employee_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}

            data = {"test":"PUT"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            employee_id = request.json['employee_id']
            cur.execute("SELECT * FROM customer_table WHERE employees_table=%s", (employee_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "employee_id" : user[0], 
                    "first_name" : user[1], 
                    "last_name" : user[2], 
                    "mobile_1" : user[3], 
                    "mobile_2" : user[4], 
                    "email_id" : user[5], 
                    "password" : user[6], 
                    "date_of_birth" : user[7], 
                    "flat_house_no" : user[8], 
                    "locality" : user[9], 
                    "landmark" : user[10], 
                    "pincode" : user[11], 
                    "city" : user[12], 
                    "state" : user[13],
                    "department" : user[14], 
                    "salary" : user[15], 
                    "adharcard" : user[16], 
                    "remark" : user[17]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)
            
            
@app.route('/category',methods=['DELETE','GET','POST','PUT','PATCH'])
def category():
    method = request.method
    match method:
        
        case "DELETE":
            # delete()
            category_id = request.json['category_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM category_table WHERE category_id=%s", (category_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM category_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "category_id" : user[0], 
                    "category_tittle" : user[1],
                    "remark" : user[2]
                }
                data.append(enter)
                count = count + 1

            return jsonify(data)
        
        case "POST":    
            cur = mysql.connection.cursor()
            
            category_tittle = request.json['category_tittle']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO category_table (category_tittle, remark) VALUES (%s, %s)", (category_tittle, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":    

            cur = mysql.connection.cursor()
            category_id = request.json['category_id']
            category_tittle = request.json['category_tittle']
            remark = request.json['remark']

            cur.execute("UPDATE category_table SET category_tittle=%s,remark=%s WHERE category_id=%s", (category_tittle,category_tittle,remark,category_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            # data = {"test":"PUT"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            category_id = request.json['category_id']
            cur.execute("SELECT * FROM category_id WHERE category_table=%s", (category_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "category_id" : user[0], 
                    "category_tittle" : user[1],
                    "remark" : user[2]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)
            
            
@app.route('/cart',methods=['DELETE','GET','POST','PUT','PATCH'])
def cart():
    method = request.method
    match method:
        
        case "DELETE":
            cart_id = request.json['cart_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM  cart_table WHERE cart_id=%s", (cart_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM  cart_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "cart_id" : user[0], 
                    "user_id" : user[1],
                    "product_id" : user[2],
                    "quantity" : user[3],
                    "remark" : user[4]
                }
                data[count]= enter
                count = count + 1

            return jsonify(data)
        
        case "POST":    
            cur = mysql.connection.cursor()
            
            user_id = request.json['user_id']
            product_id = request.json['product_id']
            quantity = request.json['quantity']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO cart_table (user_id, product_id, quantity, remark) VALUES (%s, %s, %s, %s)", (user_id, product_id, quantity, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":   


            cur = mysql.connection.cursor()
            cart_id = request.json['cart_id']
            user_id = request.json['user_id']
            product_id = request.json['product_id']
            quantity = request.json['quantity']
            remark = request.json['remark']

            cur.execute("UPDATE cart_table SET user_id = %s,product_id=%s,quantity=%s,remark=%s WHERE cart_id=%s", (user_id,product_id,quantity,remark,cart_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            
            # data = {"test":"PUT"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            cart_id = request.json['cart_id']
            cur.execute("SELECT * FROM cart_table WHERE cart_id=%s", (cart_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "cart_id" : user[0], 
                    "user_id" : user[1],
                    "product_id" : user[2],
                    "quantity" : user[3],
                    "remark" : user[4]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)
            
            
@app.route('/wishlist',methods=['DELETE','GET','POST','PUT','PATCH'])
def wishlist():
    method = request.method
    match method:
        
        case "DELETE":
            wishlist_id = request.json['wishlist_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM wishlist_table WHERE customer_id=%s", (wishlist_id,))
            mysql.connection.commit()
            cur.close()
            data = {'message': 'User deleted successfully'}
            return jsonify(data)
        
        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM wishlist_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "wishlist_id" : user[0], 
                    "user_id" : user[1],
                    "product_id" : user[2],
                    "quantity" : user[3],
                    "remarks" : user[4]
                }
                data[count]= enter
                count = count + 1

            return jsonify(data)
        
        case "POST":    
            cur = mysql.connection.cursor()
            
            user_id = request.json['user_id']
            product_id = request.json['product_id']
            quantity = request.json['quantity']
            remark = request.json['remarks']
    
            
            #Insert Data   
            cur.execute("INSERT INTO wishlist_table(user_id, product_id, quantity, remarks) VALUES (%s, %s, %s, %s)", (user_id, product_id, quantity, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":   
            cur = mysql.connection.cursor()
            wishlist_id = request.json['wishlist_id']
            user_id = request.json['user_id']
            product_id = request.json['product_id']
            quantity = request.json['quantity']
            remark = request.json['remarks']
    
            cur.execute("UPDATE wishlist_table SET user_id=%s,product_id=%s,quantity = %s,remark=%s WHERE wishlist_id=%s", (user_id,product_id,quantity,remark,wishlist_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
           

            # data = {"test":"PUT"}
            return jsonify(data)
        
        case "PATCH":
            cur = mysql.connection.cursor()
            wishlist_id = request.json['wishlist_id']
            cur.execute("SELECT * FROM wishlist_table WHERE wishlist_id=%s", (wishlist_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "wishlist_id" : user[0], 
                    "user_id" : user[1],
                    "product_id" : user[2],
                    "quantity" : user[3],
                    "remarks" : user[4]
                }
                return jsonify(data)
            else:
                data = {'message': 'User not found'}
                return jsonify(data)
      

@app.route('/address',methods=['DELETE','GET','POST','PUT','PATCH'])
def address():
    method = request.method
    match method:
        
        case "DELETE":
            address_id = request.json['address_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM address_table WHERE customer_id=%s", (address_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM address_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "address_id" : user[0], 
                    "customer_id" : user[1],
                    "customer_address" : user[2],
                    "customer_city" : user[3],
                    "customer_state" : user[4],
                    "customer_pincode" : user[5],
                    "customer_street" : user[6],
                    "remark" : user[7],
                }
                data[count]= enter
                count = count + 1

            return jsonify(data)
            
        case "POST":
            cur = mysql.connection.cursor()
            
            customer_id = request.json['customer_id']
            customer_address = request.json['customer_address']
            customer_city = request.json['customer_city']
            customer_state = request.json['customer_state']
            customer_pincode = request.json['customer_pincode']
            customer_street = request.json['customer_street']
            remark = request.json['remark']
    
            
            #Insert Data   
            cur.execute("INSERT INTO address_table(customer_id, customer_address, customer_city, customer_state, customer_pincode, customer_street, remark) VALUES (%s, %s, %s, %s, %s, %s, %s)", (customer_id, customer_address, customer_city, customer_state, customer_pincode, customer_street, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        

        case "PUT":   
            cur = mysql.connection.cursor()
            address_id = request.json['address_id']
            customer_id = request.json['customer_id']
            customer_address = request.json['customer_address']
            customer_city = request.json['customer_city']
            customer_state = request.json['customer_state']
            customer_pincode = request.json['customer_pincode']
            customer_street = request.json['customer_street']
            remark = request.json['remark']
    
            
    
            cur.execute("UPDATE address_table SET customer_id=%s,customer_address=%s,customer_city = %s,customer_state=%s,customer_pincode=%s,customer_street=%s,remark=%s WHERE address_id=%s", (customer_id,customer_address,customer_city,customer_state,customer_pincode,customer_street,remark,address_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
           

            # data = {"test":"PUT"}
            return jsonify(data)

        case "PATCH":
            cur = mysql.connection.cursor()
            address_id = request.json['address_id']
            cur.execute("SELECT * FROM address_table WHERE address_id=%s", (address_id,))
            user = cur.fetchone()
            cur.close()
            if user:
                print(user)
                data = {
                    "address_id" : user[0], 
                    "customer_id" : user[1],
                    "customer_address" : user[2],
                    "customer_city" : user[3],
                    "customer_state" : user[4],
                    "customer_pincode" : user[5],
                    "customer_street" : user[6],
                    "remark" : user[7],
                }
                return jsonify(data)
            else:
                data = {'message': 'Not Found'}
                return jsonify(data)
        
        
@app.route('/admin',methods=['DELETE','GET','POST','PUT','PATCH'])
def admin():
    method = request.method
    match method:
        
        case "DELETE":
            admin_id = request.json['admin_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM admin_table WHERE customer_id=%s", (admin_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM admin_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "admin_id" : user[0], 
                    "first_name" : user[1],
                    "last_name" : user[2],
                    "mobile_1" : user[3],
                    "mobile_2" : user[4],
                    "email" : user[5],
                    "password" : user[6],
                    "profile_image" : user[7],
                    "remarks" : user[8]
                    
                }
                data[count]= enter
                count = count + 1
        
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "POST":
            cur = mysql.connection.cursor()
            
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            mobile_1 = request.json['mobile_1']
            mobile_2 = request.json['mobile_2']
            email = request.json['email']
            password = request.json['password']
            profile_image = request.json['profile_image']
            remarks = request.json['remarks']
    
            
            #Insert Data   
            cur.execute("INSERT INTO admin_table(first_name, last_name, mobile_1, mobile_2, email,password, profile_image, remarks) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (first_name, last_name, mobile_1, mobile_2, email,password, profile_image, remarks))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)
        
        case "PUT":   
            cur = mysql.connection.cursor()
            admin_id = request.json['admin_id']
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            mobile_1 = request.json['mobile_1']
            mobile_2 = request.json['mobile_2']
            email = request.json['email']
            password = request.json['password']
            profile_image = request.json['profile_image']
            remarks = request.json['remarks']
    
            cur.execute("UPDATE admin_table SET first_name= %s,last_name= %s,mobile_1 = %s,mobile_2=%s,email=%s,password=%s,profile_image=%s,remarks=%s WHERE admin_id=%s", (first_name,last_name,mobile_1,email,mobile_2,password,profile_image,remarks))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
        
            # data = {"test":"PUT"}
            return jsonify(data)


        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)

        
@app.route('/cancellation',methods=['DELETE','GET','POST','PUT','PATCH'])
def cancellation():
    method = request.method
    match method:
        
        case "DELETE":
            cancellation_id = request.json['cancellation_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM cancellation_table WHERE cancellation_id=%s", (cancellation_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM cancellation_table ")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "cancellation_id" : user[0], 
                    "invoice_id" : user[1],
                    "reason" : user[2],
                    "cancel_data" : user[3],
                    "cancel_status" : user[3],
                    "remark" : user[4]
                }
                data[count]= enter
                count = count + 1

            data = {"Status":"Successful"}
            return jsonify(data)

        case "POST":
            cur = mysql.connection.cursor()
            
            invoice_id = request.json['invoice_id']
            reason = request.json['reason']
            cancel_data = request.json['cancel_data']
            cancel_status = request.json['cancel_status']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO cancellation_table (invoice_id, reason, cancel_data, cancel_status, remark) VALUES (%s, %s, %s, %s, %s)", (invoice_id, reason, cancel_data, cancel_status, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PUT" :
            cur = mysql.connection.cursor()
            cancellation_id = request.json['cancellation_id']
            invoice_id = request.json['invoice_id']
            reason = request.json['reason']
            cancel_data = request.json['cancel_data']
            cancel_status = request.json['cancel_status']
            remark = request.json['remark']
            cur.execute("UPDATE cancellation_table SET invoice_id= %s,reason= %s,cancel_data = %s,cancel_status=%s,remark=%s WHERE cancellation_id=%s", (invoice_id,reason,cancel_data,cancel_status,remark,cancellation_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/feedback',methods=['DELETE','GET','POST','PUT','PATCH'])
def feedback():
    method = request.method
    match method:
        
        case "DELETE":
           feedback_id = request.json['feedback_id']
           cur = mysql.connection.cursor()
           cur.execute("DELETE FROM feedback WHERE feedback_id=%s", (feedback_id,))
           mysql.connection.commit()
           cur.close()
           data = {"Status":"Successful"}
           return jsonify(data)


        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT feedback.*, customer_table.first_name,customer_table.last_name FROM feedback INNER JOIN customer_table ON feedback.customer_id=customer_table.customer_id")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "feedback_id" : user[0], 
                    "customer_id" : user[1],
                    "feedback" : user[2],
                    "remark" : user[3],
                    "first_name" : user[4],    
                    "last_name" : user[5]    
                }
                data.append(enter)
                count = count + 1

            
            # data = {"Status":"Successful"}
            return jsonify({"data": data})



        case "POST":
            cur = mysql.connection.cursor()
            
            customer_id = request.json['customer_id']
            feedback = request.json['feedback']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO feedback (customer_id, feedback, remark) VALUES (%s, %s, %s)", (customer_id, feedback, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

 
        case "PUT":  
            cur = mysql.connection.cursor()
            feedback_id = request.json['feedback_id']
            customer_id = request.json['customer_id']
            feedback = request.json['feedback']
            remark = request.json['remark']
            cur.execute("UPDATE feedback SET customer_id = %s,feedback=%s,remark=%s WHERE feedback_id=%s", (customer_id,feedback,remark,feedback_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/banner',methods=['DELETE','GET','POST','PUT','PATCH'])
def banner():
    method = request.method
    match method:
        
        case "DELETE":
           banner_id = request.json['banner_id']
           cur = mysql.connection.cursor()
           cur.execute("DELETE FROM banner_table WHERE banner_id=%s", (banner_id,))
           mysql.connection.commit()
           cur.close()
           data = {"Status":"Successful"}
           return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM banner_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "banner_id" : user[0], 
                    "banner" : user[1],
                    "title" : user[2], 
                    "status" : user[3]    
                }
                data.append(enter)
                count = count + 1

            return jsonify({"data": data})

        case "POST":
            cur = mysql.connection.cursor()
            
            banner = request.json['banner']
            title = request.json['title']
            status = request.json['status']
            
            cur.execute("INSERT INTO banner_table (banner, title, status) VALUES (%s, %s, %s)", (banner, title, status))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

 
        case "PUT":  
            cur = mysql.connection.cursor()
            banner_id = request.json['banner_id']
            banner = request.json['banner']
            title = request.json['title']
            status = request.json['status']
            cur.execute("UPDATE banner_table SET banner = %s,title=%s,status=%s WHERE banner_id=%s", (banner, title, status))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
          
@app.route('/contact',methods=['DELETE','GET','POST','PUT','PATCH'])
def contact():
    method = request.method
    match method:
        
        case "DELETE":
           contact_id = request.json['contact_id']
           cur = mysql.connection.cursor()
           cur.execute("DELETE FROM contact_table WHERE contact_id=%s", (contact_id,))
           mysql.connection.commit()
           cur.close()
           data = {"Status":"Successful"}
           return jsonify(data)


        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM contact_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "contact_id" : user[0], 
                    "name" : user[1],
                    "email" : user[2],
                    "message" : user[3],
                    "remark" : user[4]  
                }
                data.append(enter)
                count = count + 1

            return jsonify({"data": data})



        case "POST":
            cur = mysql.connection.cursor()
            
            name = request.json['name']
            email = request.json['email']
            message = request.json['message']
            
            #Insert Data   
            cur.execute("INSERT INTO contact_table (name, email, message) VALUES (%s, %s, %s)", (name, email, message))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

 
        case "PUT":  
            cur = mysql.connection.cursor()
            contact_id = request.json['contact_id']
            name = request.json['name']
            email = request.json['email']
            message = request.json['message']
            cur.execute("UPDATE contact_table SET name = %s,email=%s,message=%s WHERE contact_id=%s", (name,email,message,contact_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/order',methods=['DELETE','GET','POST','PUT','PATCH'])
def order():
    method = request.method
    match method:
        
        case "DELETE":
            order_id = request.json['order_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM order_table WHERE order_id=%s", (order_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM order_table")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = []
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "order_id" : user[0], 
                    "product_id" : user[1],
                    "customer_id" : user[2],
                    "address_id" : user[3],
                    "invoice_id" : user[4],
                    "order_date" : user[5],
                    "order_status" : user[6],
                    "order_quantity" : user[7],
                    "remark" : user[8]
                }
                data.append(enter)
                count = count + 1

            return jsonify({"data": data})

        case "POST":
            cur = mysql.connection.cursor()
            
            product_id = request.json['product_id']
            customer_id = request.json['customer_id']
            address_id = request.json['address_id']
            invoice_id = request.json['invoice_id']
            order_date = request.json['order_date']
            order_status = request.json['order_status']
            order_quantity = request.json['order_quantity']
            remark = request.json['remark']
            
            #Insert Data   
            cur.execute("INSERT INTO order_table (product_id, customer_id, address_id, invoice_id, order_date, order_status,order_quantity, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (product_id, customer_id, address_id, invoice_id, order_date, order_status, order_quantity, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case"PUT":   
            cur = mysql.connection.cursor()
            order_id = request.json['order_id']
            product_id = request.json['product_id']
            customer_id = request.json['customer_id']
            address_id = request.json['address_id']
            invoice_id = request.json['invoice_id']
            order_date = request.json['order_date']
            order_status = request.json['order_status']
            order_quantity = request.json['order_quantity']
            remark = request.json['remark']
            cur.execute("UPDATE order_table SET product_id = %s,customer_id=%s,address_id=%s,invoice_id=%s,order_date=%s,order_status=%s,order_quantity=%s,remark=%s WHERE order_id=%s", (product_id,customer_id,address_id,invoice_id,order_date,order_status,order_quantity,remark,order_id))


            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/product_review',methods=['DELETE','GET','POST','PUT','PATCH'])
def product_review():
    method = request.method
    match method:
        
        case "DELETE":
            review_id = request.json['review_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM product_review WHERE customer_id=%s", (review_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM product_review ")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "review_id" : user[0], 
                    "product_id" : user[1],
                    "user_id" : user[2],
                    "rating" : user[3],
                    "review" : user[4],
                    "remark" : user[5]
                }
                data[count]= enter
                count = count + 1

        
            data = {"Status":"Successful"}
            return jsonify(data)

        case "POST":
            cur = mysql.connection.cursor()
            
            product_id = request.json['product_id']
            user_id = request.json['user_id']
            rating = request.json['rating']
            review = request.json['review']
            remark = request.json['remark']
           
            
            #Insert Data   
            cur.execute("INSERT INTO product_review (product_id, user_id, rating, review, remark) VALUES (%s, %s, %s, %s, %s)", (product_id, user_id, rating, review, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PUT":
            cur = mysql.connection.cursor()
            review_id = request.json['review_id']
            product_id = request.json['product_id']
            user_id = request.json['user_id']
            rating = request.json['rating']
            review = request.json['review']
            remark = request.json['remark']
            cur.execute("UPDATE product_review SET product_id = %s,user_id=%s,rating=%s,review=%s,remark=%s WHERE review_id=%s", (product_id,user_id,rating,review,remark,review_id))


            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/return_table',methods=['DELETE','GET','POST','PUT','PATCH'])
def return_table():
    method = request.method
    match method:
        
        case "DELETE":
            return_id = request.json['return_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM return_table WHERE customer_id=%s", (return_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)



        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM return_table ")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "return_id" : user[0], 
                    "invoice_id" : user[1],
                    "reason" : user[2],
                    "date" : user[3],
                    "status" : user[4],
                    "return_type" : user[5],
                    "remark" : user[6]
                }
                data[count]= enter
                count = count + 1
        
            data = {"Status":"Successful"}
            return jsonify(data)



        case "POST":
            cur = mysql.connection.cursor()
    
            invoice_id = request.json['invoice_id']
            reason = request.json['reason']
            date = request.json['genddateer']
            status = request.json['status']
            return_type = request.json['return_type']
            remark = request.json['remark']
          
            #Insert Data   
            cur.execute("INSERT INTO return_table (invoice_id, reason, date, status, return_type, remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (invoice_id, reason, date, status, return_type, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PUT":  
            cur = mysql.connection.cursor()
            return_id = request.json['return_id']
            invoice_id = request.json['invoice_id']
            reason = request.json['reason']
            date = request.json['date']
            status = request.json['status']
            return_type = request.json['return_type']
            remark = request.json['remark']
            cur.execute("UPDATE return_table SET invoice_id = %s,reason=%s,date=%s,status=%s,return_type=%s,remark=%s WHERE return_id=%s", (invoice_id,reason,date,status,return_type,remark,return_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/store',methods=['DELETE','GET','POST','PUT','PATCH'])
def store():
    method = request.method
    match method:
        
        case "DELETE":
            store_id = request.json['store_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM store_table WHERE customer_id=%s", (store_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM store_table ")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "store_id" : user[0], 
                    "store_name" : user[1],
                    "store_logo" : user[2],
                    "store_tagline" : user[3],
                    "store_address" : user[4],
                    "store_city" : user[5],
                    "store_state" : user[6],
                    "store_pincode" : user[7],
                    "mobile_num_1" : user[8],
                    "mobile_num_2" : user[9],
                    "open_timing" : user[10],
                    "close_timing" : user[11],
                    "remark" : user[12]
                }
                data[count]= enter
                count = count + 1
        
            data = {"Status":"Successful"}
            return jsonify(data)



        case "POST":
            cur = mysql.connection.cursor()
            
            store_name = request.json['store_name']
            store_logo = request.json['store_logo']
            store_tagline = request.json['store_tagline']
            store_address = request.json['store_address']
            store_city = request.json['store_city']
            store_state = request.json['store_state']
            store_pincode = request.json['store_pincode']
            mobile_num_1 = request.json['mobile_num_1']
            mobile_num_2 = request.json['mobile_num_2']
            open_timing = request.json['open_timing']
            close_timing = request.json['close_timing']
            remark = request.json['remark']

            #Insert Data   
            cur.execute("INSERT INTO store_table (store_name, store_logo, store_tagline, store_address, store_city, store_state,store_pincode, mobile_num_1,mobile_num_2,open_timing,close_timing,remark) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (store_name, store_logo, store_tagline, store_address, store_city, store_state, store_pincode, mobile_num_1,mobile_num_2,open_timing,close_timing,remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PUT":
            cur = mysql.connection.cursor()
            store_id = request.json['store_id']
            store_logo = request.json['store_logo']
            store_tagline = request.json['store_tagline']
            store_address = request.json['store_address']
            store_city = request.json['store_city']
            store_state = request.json['store_state']
            store_pincode = request.json['store_pincode']
            mobile_num_1 = request.json['mobile_num_1']
            mobile_num_2 = request.json['mobile_num_2']
            open_timing = request.json['open_timing']
            close_timing = request.json['close_timing']
            remark = request.json['remark']
            cur.execute("UPDATE store_table SET  store_logo=%s,store_tagline=%s,store_address=%s,store_city=%s,store_city=%s,store_state=%s,store_pincode=%s,mobile_num_1=%s,mobile_num_2=%s,open_timing=%s,close_timing=%s,remark=%s WHERE store_id=%s", (store_logo,store_tagline,store_address,store_city,store_state,store_pincode,mobile_num_1,mobile_num_2,open_timing,close_timing,remark,store_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)
        
@app.route('/subcategory',methods=['DELETE','GET','POST','PUT','PATCH'])
def subcategory():
    method = request.method
    match method:
        
        case "DELETE":
            subcategory_id = request.json['subcategory_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM subcategory WHERE customer_id=%s", (subcategory_id,))
            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)


        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM subcategory")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "subcategory_id" : user[0], 
                    "cat_id" : user[1],
                    "subcategory_tittle" : user[2],
                    "remark" : user[3]
                }
                data[count]= enter
                count = count + 1

            data = {"Status":"Successful"}
            return jsonify(data)


        case "POST":
            cur = mysql.connection.cursor()
            
            cat_id = request.json['cat_id']
            subcategory_tittle = request.json['subcategory_tittle']
            remark = request.json['remark']
           
            
            #Insert Data   
            cur.execute("INSERT INTO subcategory (cat_id, subcategory_tittle, remark) VALUES (%s, %s, %s)", (cat_id, subcategory_tittle, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PUT": 
            cur = mysql.connection.cursor()
            subcategory_id = request.json['subcategory_id']
            cat_id = request.json['cat_id']
            subcategory_tittle = request.json['subcategory_tittle']
            remark = request.json['remark']
            
            cur.execute("UPDATE subcategory SET cat_id = %s,subcategory_tittle= %s, remark=%s, WHERE subcategory_id=%s", (cat_id,subcategory_tittle,remark,subcategory_id))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
            return jsonify(data)

        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)

if __name__ == '__main__':
   app.run()