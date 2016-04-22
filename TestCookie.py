import requests
import json
import base64

def login(username, password):
    username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    res = session.post(loginURL, data = postData)
    jsonStr = res.content.decode('gbk')
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        print('succeed')
        cookies = session.cookies.get_dict()
        cookies = [key + "=" + value for key, value in cookies.items()]
        cookies = "; ".join(cookies)
    else:
        print('fail: %s' % info["reason"])
    return cookies

if __name__ == '__main__':
    cookies = login('username', 'psw')