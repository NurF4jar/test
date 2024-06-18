from flask import Flask, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "password"
app.config["MYSQL_DB"] = "neo"
mysql = MySQL(app)


# main route
@app.route("/")
def main():
    return "Neo Test"


# GET ALL USERS UPDATE data endpoint
@app.route("/user", methods=["GET"])
def get_data():
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM users""")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


# GET data by ID UPDATE data endpoint
@app.route("/user/<int:id>", methods=["GET"])
def get_data_by_id(id):
    cur = mysql.connection.cursor()
    cur.execute("""SELECT * FROM users WHERE id = %s""", (id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


# POST data endpoint
@app.route("/user", methods=["POST"])
def add_data():
    cur = mysql.connection.cursor()
    email = request.json["email"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    cur.execute(
        """INSERT INTO users (email, first_name, last_name) VALUES (%s, %s)""",
        (email, first_name, last_name),
    )
    mysql.connecetion.commit()
    cur.close()
    return jsonify({"message": "Data added successfully"})


# UPDATE data endpoint
@app.route("/user/<int:id>", methods=["PUT"])
def update_data(id):
    cur = mysql.connection.cursor()
    email = request.json["email"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    cur.execute(
        """UPDATE users SET email = %s, first_name = %s, last_name = s% WHERE id = %s""",
        (email, first_name, last_name, id),
    )
    mysql.connecetion.commit()
    cur.close()
    return jsonify({"message": "Data Updated successfully"})


# DELETE data endpoint
@app.route("/user/<int:id>", methods=["DELETE"])
def delete_data(id):
    cur = mysql.connection.cursor()
    cur.execute("""DELETE FROM users WHERE id = %s""", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({"message": "Data deleted successfully"})


if __name__ == "__main__":
    app.run(debug=Trus)
