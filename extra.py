
@app.route('/wishlist_table',methods=['DELETE','GET','POST','PUT','PATCH'])
def wishlist_table():
    method = request.method
    match method:
        
        case "DELETE":

            wishlist_id = request.json['wishlist_id']
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM wishlist_table WHERE wishlist_id=%s", (wishlist_id,))
            mysql.connection.commit()
            cur.close()

            data = {"Status":"Successful"}
            return jsonify(data)



        case "GET":
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


