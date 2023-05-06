from flask import Flask,jsonify
from flask_mysqldb import MySQL

def deleteData(id, mysql, table_name, column_name):
     cur = mysql.connection.cursor()
     cur.execute("DELETE FROM %s WHERE %s=%s", (table_name, column_name, id))
     mysql.connection.commit()
     cur.close()
     data = {'message': 'Deleted successfully'}
     return jsonify(data)