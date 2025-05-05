from src.mcp_instance import mcp
import mysql.connector
import os
ENV = os.environ.get("APP_ENV", "local")

if ENV == "local":
    from src.env import MYSQL_CONFIG
else:
    from src.env_dev import MYSQL_CONFIG

def get_connection():
    return mysql.connector.connect(**MYSQL_CONFIG)

@mcp.tool()
def query_mysql(sql: str):
    """
    Execute a SQL query and return the result.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except mysql.connector.Error as err:
        print(f"[query_mysql] 예외 발생: {err}")
        return {"error": str(err)}

