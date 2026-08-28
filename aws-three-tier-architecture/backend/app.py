from flask import Flask
import os
import pymysql

app = Flask(__name__)


def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USERNAME"),
        password=os.environ.get("DB_PASSWORD"),
        database=os.environ.get("DB_NAME"),
        port=3306,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.route("/")
def home():
    return "Backend Flask Application is Running Successfully"


@app.route("/api/")
def api():
    try:
        connection = get_db_connection()
        connection.close()

        return {
            "status": "success",
            "message": "Backend connected to RDS successfully"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
