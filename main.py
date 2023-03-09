from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from domain.question import question_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    # "http://127.0.0.1:5173",    # 또는 "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# @app.get("/hello")
# def hello():
#     return {"message": "안녕하세요 파이보"}

app.include_router(question_router.router)




# # 샘플 Python 스크립트입니다.
#
# # ⌃R을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# # 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 ⇧ 두 번을(를) 누릅니다.
#
#
# def print_hi(name):
#     # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.
#     print(f'Hi, {name}')  # 중단점을 전환하려면 ⌘F8을(를) 누릅니다.
#
#
# # 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
