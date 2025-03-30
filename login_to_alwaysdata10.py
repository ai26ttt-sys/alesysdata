import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "bbbioujhbg@gmail.com",
        "password": "ggvfT2578"
    },
    "user2": {
        "username": "hhyutytbb@gmail.com",
        "password": "ttysS253"
    },
    "user3": {
        "username": "hhhyuhjhjn@gmail.com",
        "password": "tyygtF2580"
    },
    "user4": {
        "username": "hujnhjugvby@gmail.com",
        "password": "tttggvgfgD253"
    },
    "user5": {
        "username": "bbuiuyhyhy@gmail.com",
        "password": "hhhuyYcv255"
    },
    "user6": {
        "username": "jjuhuhbhgy@gmail.com",
        "password": "gvvtygtS,253"
    },
    "user7": {
        "username": "bbbiyhjhnj@gmail.com",
        "password": "ttgtfgD2580"
    },
    "user8": {
        "username": "hhuhjhyub@gmail.com",
        "password": "ttgvgY2580T"
    },
    "user9": {
        "username": "hhyhbhyhb@gmail.com",
        "password": "tgvgtygvV253"
    },
    "user10": {
        "username": "uuuyhyhbh@gmail.com",
        "password": "tgtvgR2536A"
    },
    "user11": {
        "username": "uuuniujkjhn@gmail.com",
        "password": "tgygR2536T"
    },
    "user12": {
        "username": "vvyhbhyxc@gmail.com",
        "password": "tttgFG257"
    },
    "user13": {
        "username": "hujnjiopj@gmail.com",
        "password": "tgvT580E"
    },
    "user14": {
        "username": "guhbhbhbv@gmail.com",
        "password": "cvtyD858U"
    },
    "user15": {
        "username": "hhhijijnmn@gmail.com",
        "password": "cvvtT258U"
    },
    "user16": {
        "username": "vvyuhbhyu@gmail.com",
        "password": "yygggD2536E"
    },
    "user17": {
        "username": "huijujnhb@gmail.com",
        "password": "fcfvfgG580O"
    },
    "user18": {
        "username": "bbuijnjnjn@gmail.com",
        "password": "rfcfd258SS"
    },
    "user19": {
        "username": "bbbyuhbhbhg@gmail.com",
        "password": "fgtF807C"
    },
    "user20": {
        "username": "bbbiopopokl@gmail.com",
        "password": "hhhujc7G"
    },
    "user21": {
        "username": "hhhyughbvbg@gmail.com",
        "password": "gggtyyfD587/T"
    },
    "user22": {
        "username": "hhyuhbhghv@gmail.com",
        "password": "tgvgF2587G"
    },
    "user23": {
        "username": "yytgvbhgv@gmail.com",
        "password": "tgvgF258U"
    },
    "user24": {
        "username": "bbbiuhgfcvx@gmail.com",
        "password": "ggvxD580E"
    },
    "user25": {
        "username": "gvgvgvbcvxd@gmail.com",
        "password": "tgvcfcxD5803"
    },
    "user26": {
        "username": "hjuijnjhj@gmail.com",
        "password": "ggvgvF58697"
    },
    "user27": {
        "username": "hhhyhbhbh@gmail.com",
        "password": "tgvgvcvF582"
    },
    "user28": {
        "username": "yhbhyhhbvbc@gmail.com",
        "password": "tgvgzS2583"
    },
    "user29": {
        "username": "hhujnjujn@gmail.com",
        "password": "tgvgF2580U"
    },
    "user30": {
        "username": "bbbyuhyhbh@gmail.com",
        "password": "tgvtgfF2536"
    },
    "user31": {
        "username": "buyhbghvbc@gmail.com",
        "password": "tgvtgT23696"
    },
    "user32": {
        "username": "ddd0090@googlemail.com",
        "password": "123123123aQ@@@"
    },
    "user33": {
        "username": "hhhuijnmkoio@gmail.com",
        "password": "gvghyR25367T"
    },
    "user34": {
        "username": "gggyhbhjuyv@gmail.com",
        "password": "tgvgD2536/8"
    },
    "user35": {
        "username": "gyhbhhuijut@gmail.com",
        "password": "tgvzSx587/aT"
    },
    "user36": {
        "username": "bbbiujnmjh@gmail.com",
        "password": "gtttftE2531"
    },
    "user37": {
        "username": "vvvytgfgvg@gmail.com",
        "password": "yyytgDc5878"
    },
    "user38": {
        "username": "vvvyuhnhnh@gmail.com",
        "password": "gggtgS2536"
    },
    "user39": {
        "username": "bbuiujujuv@gmail.com",
        "password": "uuiiuTvgv236"
    },
    "user40": {
        "username": "jjiopopop@gmail.com",
        "password": "tgvgTv2368"
    },
    "user41": {
        "username": "hhhujnnmi@gmail.com",
        "password": "ggvvDggg233"
    },
    "user42": {
        "username": "ghbbbyubyyt@gmail.com",
        "password": "yhhbbT25870"
    },
    "user43": {
        "username": "guiiihbgopo@gmail.com",
        "password": "ggghFgxcv233"
    },
    "user44": {
        "username": "yyhhbvbmmm@gmail.com",
        "password": "yyhbbhgT2536"
    },
    "user45": {
        "username": "gikjkmnjbbb@gmail.com",
        "password": "yyyy666zT/a"
    },
    "user46": {
        "username": "bvbuiopoigh@gmail.com",
        "password": "yyyfffSF236"
    },
    "user47": {
        "username": "ggiiopoibb@gmail.com",
        "password": "yyyiioiuyG5630"
    },
    "user48": {
        "username": "hhhiopoiuy@gmail.com",
        "password": "yyghbbE2534/Y"
    },
    "user49": {
        "username": "cccytghbghh@gmail.com",
        "password": "tttyFc2536"
    },
    "user50": {
        "username": "vvvujhjjuh@gmail.com",
        "password": "yyyyGyhh2531"
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
    # 等待20秒
    time.sleep(20)
