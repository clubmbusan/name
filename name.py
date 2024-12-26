import tkinter as tk

def register():
    username = entry.get()
    if username in registered_users:
        label_result.config(text="이미 존재하는 아이디입니다.")
    else:
        registered_users.append(username)
        label_result.config(text=f"{username} 등록 성공!")

# 회원 데이터 저장
registered_users = []

# Tkinter 창 설정
root = tk.Tk()
root.title("회원 등록 시스템")

# 위젯 추가
label = tk.Label(root, text="아이디를 입력하세요:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="등록", command=register)
button.pack()

label_result = tk.Label(root, text="")
label_result.pack()

# 메인 루프 실행
root.mainloop()
