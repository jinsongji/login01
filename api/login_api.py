import requests

def login(jsonData):

    response = requests.post(url="http://ihrm-test.itheima.net/api/sys/login",
                             json= jsonData,
                             headers={"Content-Type": "application/json"})
    return response


if __name__ == '__main__':
    json = {"mobile":"13800000002","password":"123456"}
    aa = login(json)
    print(aa.json())