import os
import time
import mysql.connector
from flask import Flask

app = Flask(__name__)

def get_connection():
    for _ in range(30):
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "db"),
                user=os.getenv("DB_USER", "root"),
                password=os.getenv("DB_PASSWORD", "root"),
                database=os.getenv("DB_NAME", "practica7"),
            )
        except mysql.connector.Error:
            time.sleep(2)
    raise RuntimeError("No se pudo conectar a la base de datos")

@app.route("/")
def hola():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT 'Hola mundo desde MySQL!'")
    mensaje = cur.fetchone()[0]
    cur.close()
    conn.close()
    return f"<h1>{mensaje}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)