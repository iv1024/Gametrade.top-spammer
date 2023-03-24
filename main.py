import requests

message1 = input("message1: ")
message2 = input("message2: ")
count = int(input("送信したい回数: "))

def launcher():
    session = requests.Session()
    response = session.get("https://gametrade.top")

    data = {"email": message1, "password": message2, "id": "00000000"}

    result = session.post("https://gametrade.top/signin", data=data, cookies=response.cookies, allow_redirects=True)

    if result.status_code == 401:
        return "Success"
    else:
        return "Failed"

for i in range(count):
    print(launcher())
