import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "hhhiuuuyh@gmail.com",
        "password": "tgvY23680"
    },
    "user2": {
        "username": "fffiopioon@gmail.com",
        "password": "tgvgtY2587U"
    },
    "user3": {
        "username": "uuuuhbghyhy@gmail.com",
        "password": "tgvvRvvv233"
    },
    "user4": {
        "username": "yyyybbhhhy@gmail.com",
        "password": "yhhbhuuu258T"
    },
    "user5": {
        "username": "hhhiopopo@gmail.com",
        "password": "ygvgG2537Y"
    },
    "user6": {
        "username": "hhujnhjhvv@gmail.com",
        "password": "hhhyhDxc231"
    },
    "user7": {
        "username": "vvvytgvbbg@gmail.com",
        "password": "ttgggD807R"
    },
    "user8": {
        "username": "ggiiujjhbbn@gmail.com",
        "password": "uuuhhDxc236"
    },
    "user9": {
        "username": "hhhopiojhb@gmail.com",
        "password": "iiiyuhDx258"
    },
    "user10": {
        "username": "nnnhbhuiuyu@gmail.com",
        "password": "tttggvF5870"
    },
    "user11": {
        "username": "gggvyuhbbb@gmail.com",
        "password": "rfcfcF5870"
    },
    "user12": {
        "username": "ffcgvvyty@gmail.com",
        "password": "hhhbbbzR23689"
    },
    "user13": {
        "username": "gggvbuiiu@gmail.com",
        "password": "hbbbbD253I"
    },
    "user14": {
        "username": "hhhiujnjn@gmail.com",
        "password": "gi1KiYD0"
    },
    "user15": {
        "username": "ggvvbbhhy@gmail.com",
        "password": "gi1KiYD0"
    },
    "user16": {
        "username": "vbbuijnhgtc@gmail.com",
        "password": "gi1KiYD0"
    },
    "user17": {
        "username": "gbgggyhbh@gmail.com",
        "password": "ggvvvRg253"
    },
    "user18": {
        "username": "ffftgvgbhy@gmail.com",
        "password": "tttggvDmgv2"
    },
    "user19": {
        "username": "jjjnhjnbfg@gmail.com",
        "password": "tyyggDxcT252"
    },
    "user20": {
        "username": "vvvyhhbg@gmail.com",
        "password": "ttggvcfgfdD2360"
    },
    "user21": {
        "username": "ggghbgvgc@gmail.com",
        "password": "tggvczxR253"
    },
    "user22": {
        "username": "ghbhghbbg@gmail.com",
        "password": "tgvgF580U"
    },
    "user23": {
        "username": "bbbuyhjyh@gmail.com",
        "password": "vgyhbgT236R"
    },
    "user24": {
        "username": "hhbbhygbb@gmail.com",
        "password": "hhyhhhzY236U"
    },
    "user25": {
        "username": "hhhiujhbn@gmail.com",
        "password": "ggvvgD,2367"
    },
    "user26": {
        "username": "gggvbuyhj@gmail.com",
        "password": "tygDfc2310"
    },
    "user27": {
        "username": "ttgvgfcvf@gmail.com",
        "password": "iiiuhhR32580"
    },
    "user28": {
        "username": "bbbuyydfrt@gmail.com",
        "password": "kkkuiAz2362"
    },
    "user29": {
        "username": "vvbtyguhb@gmail.com",
        "password": "yyyghhR247"
    },
    "user30": {
        "username": "vvvuyhblo@gmail.com",
        "password": "bbbgggS236"
    },
    "user31": {
        "username": "vvvyhbddt@gmail.com",
        "password": "yyyggDc212"
    },
    "user32": {
        "username": "hhhuyuhj@gmail.com",
        "password": "tttgggT236"
    },
    "user33": {
        "username": "cccytgbgh@gmail.com",
        "password": "tttgggT236"
    },
    "user34": {
        "username": "ggyhbbbuy@gmail.com",
        "password": "asdasdE233"
    },
    "user35": {
        "username": "vvviujnjhj@gmail.com",
        "password": "yyyhhhgS212"
    },
    "user36": {
        "username": "gyhhbhghv@gmail.com",
        "password": "ggttgvgfgR23"
    },
    "user37": {
        "username": "vuhjnjnj@gmail.com",
        "password": "ttgghzT2147"
    },
    "user38": {
        "username": "gujjjklkio@gmail.com",
        "password": "ggyhbbbxcE321"
    },
    "user39": {
        "username": "gvuuuyuhj@gmail.com",
        "password": "ttggvcvxW236"
    },
    "user40": {
        "username": "cfyxuuxxksvy@gmail.com",
        "password": "tttfffS236"
    },
    "user41": {
        "username": "china0090gvv@gmail.com",
        "password": "tttfffS236"
    },
    "user42": {
        "username": "nkm008a1@gmail.com",
        "password": "tttfffS236"
    },
    "user43": {
        "username": "zzz0090@gmail.com",
        "password": "tttfffS236"
    },
    "user44": {
        "username": "bgf0yccexfbw@gmail.com",
        "password": "t567567Y@yu"
    },
    "user45": {
        "username": "china0bv090@gmail.com",
        "password": "gyy67876T@"
    },
    "user46": {
        "username": "d0ywv0s0ytnz@gmail.com",
        "password": "yyyhgR@yu67"
    },
    "user47": {
        "username": "asdfg055a@gmail.com",
        "password": "yyyghR567@"
    },
    "user48": {
        "username": "zzz0091@gmail.com",
        "password": "yhhbbz@gtU77"
    },
    "user49": {
        "username": "cnbjhy016@gmail.com",
        "password": "yhhbbz@gtU77"
    },
    "user50": {
        "username": "eng887a@gmail.com",
        "password": "hhh6766T@67"
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
