from fastmcp import Client
import asyncio

async def interact_with_server():
    print("--- 클라이언트 생성 중 ---")

    # 옵션 1: `python my_server.py`를 통해 실행 중인 서버에 연결 (stdio 사용)
    # client = Client("my_server.py")

    # 옵션 2: `fastmcp run ... --transport sse --port 8080`를 통해 실행 중인 서버에 연결
    client = Client("http://localhost:7878/sse") # 정확한 URL/포트를 사용하십시오.

    print("--- 클라이언트 생성 완료 ---")

    try:
        async with client:
            print("--- 클라이언트 연결됨 ---")
            print(f"클라이언트의 도구 목록: {await client.list_tools()}")
            
            # 'describe_tools' 도구 호출
            # describe_result = await client.call_tool("describe_tools")
            # print(f"describe_tools 결과: {describe_result}")

            # 'query_mysql' 도구 호출
            # SQL 쿼리 예시: 테이블 구조를 확인하기 위한 쿼리
            query_result = await client.call_tool("query_mysql", {"sql": "show tables;"})
            print(f"query_mysql 결과: {query_result}")

            # 'fetch_api' 도구 호출
            # API URL 예시: 실제 API URL로 변경하십시오.
            api_result = await client.call_tool("fetch_api", {"url": "https://google.com"})
            print(f"fetch_api 결과: {api_result}")

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        print("--- 클라이언트 상호작용 완료 ---")

if __name__ == "__main__":
    asyncio.run(interact_with_server())