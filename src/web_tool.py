from src.mcp_instance import mcp
import requests

@mcp.tool()
def fetch_api(url: str):
    # """
    # 주어진 URL에 GET 요청을 보내고 응답을 반환합니다.
    # """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        # URL에 GET 요청을 보냅니다.
        response = requests.get(url, headers=headers)
        # 응답 상태 코드가 200(성공)이 아닐 경우 예외를 발생시킵니다.
        response.raise_for_status()  # HTTP 오류 발생 시 예외 발생
        return response.text
    except requests.RequestException as e:
        print(f"[request_url] 예외 발생: {e}")
        return {"error": str(e)}

