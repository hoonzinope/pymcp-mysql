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
def describe_tools() -> str:
    """사용 가능한 도구 목록과 사용법을 설명합니다."""
    return """
    다음 도구들을 사용할 수 있습니다:

    1. query_mysql(sql: str) → 주어진 SQL 쿼리를 실행합니다.
    예시: query_mysql("SELECT * FROM users LIMIT 10;")
    
    도구들을 사용해 테이블 구조를 파악하고 데이터를 조회한 뒤, 그 내용을 분석해 결과를 도출하세요.
    """

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

