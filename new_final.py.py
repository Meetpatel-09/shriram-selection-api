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
            cur.execute("INSERT INTO wishlist_table(customer_id, customer_address, customer_city, customer_state, customer_pincode, customer_street, remark) VALUES (%s, %s, %s, %s, %s, %s, %s)", (customer_id, customer_address, customer_city, customer_state, customer_pincode, customer_street, remark))

            mysql.connection.commit()
            cur.close()
            data = {"Status":"Successful"}
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
            data = {"Status":"Successful"}
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
            cur.execute("DELETE FROM cancellation_table WHERE customer_id=%s", (cancellation_id,))
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
           cur.execute("DELETE FROM feedback WHERE customer_id=%s", (feedback_id,))
           mysql.connection.commit()
           cur.close()
           data = {"Status":"Successful"}
           return jsonify(data)



        case "GET":
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM feedback ")
            users = cur.fetchall()
            cur.close()
            count = 1
            # print(users)
            data = {}
            for user in users:
                print(user[0])
                print(data)
                enter = {
                    "feedback_id" : user[0], 
                    "customer_id" : user[1],
                    "feedback" : user[2],
                    "remark" : user[3]
                }
                data[count]= enter
                count = count + 1

            
            data = {"Status":"Successful"}
            return jsonify(data)



        case "POST":
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
            cur.execute("DELETE FROM order_table WHERE customer_id=%s", (order_id,))
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
            data = {}
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
                data[count]= enter
                count = count + 1

            data = {"Status":"Successful"}
            return jsonify(data)



        case "POST":
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
            data = {"Status":"Successful"}
            return jsonify(data)



        case "PATCH":
            if data:
                data = {"Status":"Successful"}
            else:
                data = {'message': 'User not found'}
            return jsonify(data)