import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "howtocopy1111@zjtz.tk",
        "password": "12341234aQ##"
    },
    "user2": {
        "username": "tw123123cp@ttt0090.tk",
        "password": "1234512345aQ##"
    },
    "user3": {
        "username": "cbbvccx0090@gmail.com",
        "password": "1234512345aQ##"
    },
    "user4": {
        "username": "kyswssuug0vww@gmail.com",
        "password": "1252558?WE"
    },
    "user5": {
        "username": "yiop12345@ttt0090.tk",
        "password": "1234512345aQ###"
    },
    "user6": {
        "username": "tw001001cp@zjtz.tk",
        "password": "12341234aQ##"
    },
    "user7": {
        "username": "hong1125@tzhy.tk",
        "password": "12341234aQ###"
    },
    "user8": {
        "username": "ttthjjersterd43@gmail.com",
        "password": "5555ggggT[]"
    },
    "user9": {
        "username": "jp2503669@outlook.com",
        "password": "1234512345aQ###"
    },
    "user10": {
        "username": "fcfknxx@gmail.com",
        "password": "12341234aQ####"
    },
    "user11": {
        "username": "ggg0090@gmail.com",
        "password": "1234512345aQ###"
    },
    "user12": {
        "username": "zjhy333333@gmail.com",
        "password": "1234512345aQ###"
    },
    "user13": {
        "username": "bbgg8880@gmail.com",
        "password": "1234512345aQ###"
    },
    "user14": {
        "username": "jjjiopbbb168@tzhy.tk",
        "password": "1234512345aQ###"
    },
    "user15": {
        "username": "tww240101@zjtz.tk",
        "password": "5555666yY%%%"
    },
    "user16": {
        "username": "bnjy6778655@gmail.com",
        "password": "yyyyddddDF555@@@"
    },
    "user17": {
        "username": "twtw231202@tzhy.tk",
        "password": "1234512345aQ###"
    },
    "user18": {
        "username": "chibbvfcdf090@gmail.com",
        "password": "gghhhyy6666@@@"
    },
    "user19": {
        "username": "cnzj1688@tzhy.tk",
        "password": "123123123aA@@@"
    },
    "user20": {
        "username": "ttthjjerster3@zjtz.tk",
        "password": "tttuuuu2555T125"
    },
    "user21": {
        "username": "hkk008369@tzhy.tk",
        "password": "hkk008369aQ###"
    },
    "user22": {
        "username": "hkopop0056@tzhy.tk",
        "password": "hkopop0056aA###"
    },
    "user23": {
        "username": "hhyy.88aa@gmail.com",
        "password": "hhyy88aaaA##"
    },
    "user24": {
        "username": "yyytgopop@tzhy.tk",
        "password": "yyytgopopaA###"
    },
    "user25": {
        "username": "svtdtsa0ktz@gmail.com",
        "password": "6786787yFt#%#@"
    },
    "user26": {
        "username": "tw24001@tzhy.tk",
        "password": "tw24001tzhy.tkaA%%%"
    },
    "user27": {
        "username": "tttryop123@tzhy.tk",
        "password": "tttryop123tzhy.tkaA%%"
    },
    "user28": {
        "username": "gaoman006@tzhy.tk",
        "password": "gaoman006tzhy.tkaA%%"
    },
    "user29": {
        "username": "jjjopop123@tzhy.tk",
        "password": "jjjopop123tzhy.tkaA%"
    },
    "user30": {
        "username": "tw240101@zjtz.tk",
        "password": "yyyy6666EtkaA##%"
    },
    "user31": {
        "username": "vuwyyvupouxisx@gmail.com",
        "password": "12356yhT@@@"
    },
    "user32": {
        "username": "zjhy130777@gmail.com",
        "password": "yyyyT@/125636"
    },
    "user33": {
        "username": "newhk001@tzhy.tk",
        "password": "123123123aA###"
    },
    "user34": {
        "username": "zjhy130713@gmail.com",
        "password": "1234512345aQ#@@"
    },
    "user35": {
        "username": "kysdu0yzu0i@gmail.com",
        "password": "qwert123123aW#"
    },
    "user36": {
        "username": "tawe240116@tzhy.tk",
        "password": "tyyggR12358!"
    },
    "user37": {
        "username": "vvvopkijny@tzhy.tk",
        "password": "123582aW/@@"
    },
    "user38": {
        "username": "gogyhbbbp@tzhy.tk",
        "password": "hyue2222[@]"
    },
    "user39": {
        "username": "ttxts0xzsxjv00@gmail.com",
        "password": "hhhyyyE/@2533"
    },
    "user40": {
        "username": "tzulwu0ysyz@gmail.com",
        "password": "6666yyyyY@@@@"
    },
    "user41": {
        "username": "koyeb333@tzhy.tk",
        "password": "hhuu7777@@T"
    },
    "user42": {
        "username": "jwsztvhvtod@gmail.com",
        "password": "yyuggg@@@@Ttt"
    },
    "user43": {
        "username": "u0uwyzutatwz@gmail.com",
        "password": "yyyytA123@#@"
    },
    "user44": {
        "username": "skype309@tzhy.tk",
        "password": "yyyy5555@Y7778"
    },
    "user45": {
        "username": "onedriophh@zjtz.tk",
        "password": "yyyygggAA12355@@@"
    },
    "user46": {
        "username": "du0syurduls@gmail.com",
        "password": "ttt666ST@@@"
    },
    "user47": {
        "username": "free123@ttt0090.tk",
        "password": "1235812358aA@"
    },
    "user48": {
        "username": "tttyyy123@tzhy.tk",
        "password": "123123123aA#@@"
    },
    "user49": {
        "username": "ban0217@tzhy.tk",
        "password": "111222333999aA#"
    },
    "user50": {
        "username": "hk0217@tzhy.tk",
        "password": "tttyyyhhhD1235@"
    },
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
    # 等待30秒
    time.sleep(20)
