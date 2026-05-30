
import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义53个用户的登录信息
users = {
    "user1": {"username": "yhhybbp@gmail.com", "password": "sunread601"},
    "user2": {"username": "bbbopxjj@gmail.com", "password": "sunread601"},
    "user3": {"username": "gohioon01@gmail.com", "password": "sunread601"},
    "user4": {"username": "kingpp8.69@gmail.com", "password": "123123123aQ####"},
    "user5": {"username": "vps601805@gmail.com", "password": "howto2356"},
    "user6": {"username": "amer008@gmail.com", "password": "sunread601"},
    "user7": {"username": "fff0090@gmail.com", "password": "123123123aQ####"},
    "user8": {"username": "amer6677@gmail.com", "password": "sunread601"},
    "user9": {"username": "ttt777hy@gmail.com", "password": "sunread601"},
    "user10": {"username": "ttt00902025@gmail.com", "password": "sunread601"},
    "user11": {"username": "bhgfffss0090@gmail.com", "password": "123123123aQ####"},
    "user12": {"username": "cbngg0090@googlemail.com", "password": "123456aW##yyyyy"},
    "user13": {"username": "china0090@gmail.com", "password": "123456aW##yyyyy"},
    "user14": {"username": "asdfg5561@gmail.com", "password": "123123123aQ###%"},
    "user15": {"username": "chinbhutt@gmail.com", "password": "1234512345aQ####"},
    "user16": {"username": "ouy0yt0w@gmail.com", "password": "1234512345aQ####"},
    "user17": {"username": "tgioklp@gmail.com", "password": "123456aW##@"},
    "user18": {"username": "ginmtf@gmail.com", "password": "123456aW##@"},
    "user19": {"username": "ghgh992a@gmail.com", "password": "123456aW##yyyyy"},
    "user20": {"username": "tttcopy60@gmail.com", "password": "123456aW##yyyyy"},
    "user21": {"username": "ytvttywztwvwjv@gmail.com", "password": "123123123aQ###%"},
    "user22": {"username": "wvv0wgswawztv@gmail.com", "password": "vSqDG21N"},
    "user23": {"username": "xs0smwynuytxv@gmail.com", "password": "123123123aQ###%"},
    "user24": {"username": "noioptty@gmail.com", "password": "123456aW##yyyyy"},
    "user25": {"username": "rrr970516@gmail.com", "password": "123456aW##yyyyy"},
    "user26": {"username": "dongiop866@gmail.com", "password": "123456aW##yyyyy"},
    "user27": {"username": "yuuusuxuitxtg@gmail.com", "password": "123123123aQ####"},
    "user28": {"username": "c0fgfbidig@gmail.com", "password": "123123123aQ####"},
    "user29": {"username": "kingpp869@gmail.com", "password": "123123123aQ####"},
    "user30": {"username": "goitgm@googlemail.com", "password": "123456aW##yyyyy"},
    "user31": {"username": "fcfknxx@googlemail.com", "password": "123456aW##yyyyy"},
    "user32": {"username": "fff009.0@googlemail.com", "password": "6IT09YCw"},
    "user33": {"username": "amer00.8@googlemail.com", "password": "6IT09YCw"},
    "user34": {"username": "eng8.87a@googlemail.com", "password": "tttgggT236"},
    "user35": {"username": "ghgh992.a@googlemail.com", "password": "459064612aA"},
    "user36": {"username": "ttt0090@gmail.com", "password": "123456aW##yyyyy"},
    "user37": {"username": "cnff0088@gmail.com", "password": "123123aE##"},
    "user38": {"username": "yyyppp888@gmail.com", "password": "123456aW##yyyyy"},
    "user39": {"username": "usaff1299@gmail.com", "password": "Y$359463073177od"},
    "user40": {"username": "ggiopyyt@gmail.com", "password": "123456aW##yyyyy"},
    "user41": {"username": "ytswvyttlsh0s@gmail.com", "password": "123123aQ#%"},
    "user42": {"username": "y0tfszuyztug@gmail.com", "password": "123456aW##yyyyy"},
    "user43": {"username": "x00vy0s0v0ycy0@gmail.com", "password": "123456aW##yyyyy"},
    "user44": {"username": "x0yhyx0syywyj@gmail.com", "password": "123456aW##yyyyy"},
    "user45": {"username": "wzsskxyy0xyx0u@gmail.com", "password": "123123123aQ####"},
    "user46": {"username": "y0sw0uyzstuh@gmail.com", "password": "123456aW##yyyyy"},
    "user47": {"username": "change260501@gmail.com", "password": "Qwe159369."},
    "user48": {"username": "change250503@gmail.com", "password": "123456aW##@"},
    "user49": {"username": "change260505@gmail.com", "password": "gggyhy67yY@"},
    "user50": {"username": "changehy26@gmail.com", "password": "gggyhy67yY@"},
    "user51": {"username": "fffcopy26@gmail.com", "password": "gggyhy67yY@"},
    "user52": {"username": "zjttcopy@gmail.com", "password": "111111222aA@"},
    "user53": {"username": "yststjyeswh@gmail.com", "password": "123456aW##yyyyy"}
}

# 遍历每个用户并尝试登录
for user, user_info in users.items():
    username = user_info["username"]
    password = user_info["password"]

    # 创建一个session对象
    session = requests.Session()

    # 设置User-Agent
    session.headers.update({'User-Agent': user_agent})

    # 获取登录页面
    response = session.get(login_url)

    # 获取CSRF token
    csrf_token = response.cookies['csrftoken']

    # 定义登录数据
    login_data = {
        'csrfmiddlewaretoken': csrf_token,
        'login': username,
        'password': password,
    }

    # 提交登录请求
    response = session.post(login_url, data=login_data, headers={'Referer': login_url})

    # 访问https://admin.alwaysdata.com/log
    response = session.get('https://admin.alwaysdata.com/log/', allow_redirects=False)

    # 检查响应状态
    if response.status_code == 200:
        print(f"用户 {user} 登录成功")
    elif response.status_code in [301, 302]:
        print(f"用户 {user} 登录失败，状态码：{response.status_code}")
    else:
        print(f"用户 {user} 未知状态，状态码：{response.status_code}")
    
    # 等待20秒
    time.sleep(20)
