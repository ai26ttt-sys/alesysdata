import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "vubhhhyuty@gmail.com",
        "password": "gtgvyhhG255*36"
    },
    "user2": {
        "username": "fffytyghbh@gmail.com",
        "password": "258878/2558gY*"
    },
    "user3": {
        "username": "nnnuiuijujh@gmail.com",
        "password": "25367/85yY+5"
    },
    "user4": {
        "username": "guijuhbbty@gmail.com",
        "password": "cfttR788tY"
    },
    "user5": {
        "username": "cyuhbbhbh@gmail.com",
        "password": "255678/25yU"
    },
    "user6": {
        "username": "buijjjjjxc@gmail.com",
        "password": "tgvyhH5887/85"
    },
    "user7": {
        "username": "byhhhuyuyu@gmail.com",
        "password": "tgvyhuJ588/863"
    },
    "user8": {
        "username": "twouuioyuy@gmail.com",
        "password": "vyhbH7/528K"
    },
    "user9": {
        "username": "kkkmkmiopoi@gmail.com",
        "password": "gyhGv87/253"
    },
    "user10": {
        "username": "cnvvviopgh@gmail.com",
        "password": "123123123aQ@@@"
    },
    "user11": {
        "username": "gyhbbbiui@gmail.com",
        "password": "gyhvT255*58"
    },
    "user12": {
        "username": "gujbnnnuj@gmail.com",
        "password": "xcfgG858/58"
    },
    "user13": {
        "username": "buijnjmklk@gmail.com",
        "password": "gtgvG58yuT"
    },
    "user14": {
        "username": "buijjjnjn@gmail.com",
        "password": "gygvF255+253Y"
    },
    "user15": {
        "username": "guyhbbbhju@gmail.com",
        "password": "tfcgF588/25Ju"
    },
    "user16": {
        "username": "vujnkopopiug@gmail.com",
        "password": "zxdfcG584*78/Y"
    },
    "user17": {
        "username": "cccinmkml@gmail.com",
        "password": "tgvdfgdF588/25"
    },
    "user18": {
        "username": "vyhbhhhghg@gmail.com",
        "password": "tygygF578/23"
    },
    "user19": {
        "username": "guhjnjn@gmail.com",
        "password": "tygygG255*258"
    },
    "user20": {
        "username": "vtyyyghbhbh@gmail.com",
        "password": "yuhbhbgF255/80i"
    },
    "user21": {
        "username": "vuyuuuhjy@gmail.com",
        "password": "dfgtyG7/25"
    },
    "user22": {
        "username": "chghbhyuu@gmail.com",
        "password": "tygvT255*587/"
    },
    "user23": {
        "username": "gyhbbbytya@gmail.com",
        "password": "xcfgG74/25+"
    },
    "user24": {
        "username": "fffytyghbg@gmail.com",
        "password": "fgvbhD25*586"
    },
    "user25": {
        "username": "iujnnnhjg@gmail.com",
        "password": "uyuyhzt255*58"
    },
    "user26": {
        "username": "cvyfgggcvtyg@gmail.com",
        "password": "fgvfG588/25"
    },
    "user27": {
        "username": "bhyuhjujnh@gmail.com",
        "password": "tyutyS475/25"
    },
    "user28": {
        "username": "mmmiopopoi@gmail.com",
        "password": "ghbvG587/56"
    },
    "user29": {
        "username": "nnniopopo@gmail.com",
        "password": "tyutyF587/25"
    },
    "user30": {
        "username": "hhhujujbnhj@gmail.com",
        "password": "fgtgF78/58"
    },
    "user31": {
        "username": "vbghyhbhy@gmail.com",
        "password": "tygvG85/85"
    },
    "user32": {
        "username": "tttrtfgvgvg@gmail.com",
        "password": "rtfcGx725/87"
    },
    "user33": {
        "username": "gyhhhbhb@gmail.com",
        "password": "tgvTy7/708"
    },
    "user34": {
        "username": "njiiiuiyuy@gmail.com",
        "password": "gtygF78/582"
    },
    "user35": {
        "username": "ffftgyhyhb@gmail.com",
        "password": "tgvtFg74/253"
    },
    "user36": {
        "username": "uuuijknmjk@gmail.com",
        "password": "tgvtF7/758/"
    },
    "user37": {
        "username": "nijnmkiop@gmail.com",
        "password": "tgvgtgF47*25"
    },
    "user38": {
        "username": "nnjtgvhgh@gmail.com",
        "password": "tgygtyzT45/78"
    },
    "user39": {
        "username": "buhhhjnhnh@gmail.com",
        "password": "rfcgF78/782"
    },
    "user40": {
        "username": "vvvybhuhu@gmail.com",
        "password": "tgytgfgS47/58"
    },
    "user41": {
        "username": "eertftgyhgh@gmail.com",
        "password": "tygtG58/78"
    },
    "user42": {
        "username": "buijijkm@gmail.com",
        "password": "tgvgD58/782/"
    },
    "user43": {
        "username": "bbbiuijnjm@gmail.com",
        "password": "tygyS/254/78"
    },
    "user44": {
        "username": "bujnnnjmjh@gmail.com",
        "password": "tgvgSF7/758"
    },
    "user45": {
        "username": "honhjuijkmmj@gmail.com",
        "password": "tygvgD7/85"
    },
    "user46": {
        "username": "gvuyuhbjnj@gmail.com",
        "password": "tfRf58/782"
    },
    "user47": {
        "username": "bhuyuyuy@gmail.com",
        "password": "tgyF47/582+"
    },
    "user48": {
        "username": "nnuijujhj@gmail.com",
        "password": "tgvytS/72580"
    },
    "user49": {
        "username": "buhjjjujzd@gmail.com",
        "password": "tgvG725/8587"
    },
    "user50": {
        "username": "bujnnnjhu@gmail.com",
        "password": "tgvgD47/582+"
    }
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
