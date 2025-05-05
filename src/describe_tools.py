from src.mcp_instance import mcp

@mcp.tool()
def describe_tools() -> str:
    """사용 가능한 도구 목록과 사용법을 설명합니다."""
    return """
    다음 도구들을 사용할 수 있습니다:

    1. query_mysql(sql: str) → 주어진 SQL 쿼리를 실행합니다.
       예시: query_mysql("SELECT * FROM users LIMIT 10;")
    
    2. fetch_api(url: str) → 주어진 URL로 HTTP GET 요청을 보냅니다.
       예시: fetch_api("https://api.example.com/data")
    
    도구들을 사용해 데이터를 조회하고, 필요한 정보를 분석하여 결과를 도출하세요.
    """

