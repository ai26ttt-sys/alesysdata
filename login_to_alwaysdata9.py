import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "bbbiuiuiu@gmail.com",
        "password": "gyhhhF5880U"
    },
    "user2": {
        "username": "nnniophuopo@gmail.com",
        "password": "yyhhhyT583"
    },
    "user3": {
        "username": "twdftgtybu@gmail.com",
        "password": "tgvuhbT2536"
    },
    "user4": {
        "username": "enhuiopop@gmail.com",
        "password": "tgvdG2457"
    },
    "user5": {
        "username": "tytyghyhnm@gmail.com",
        "password": "tgvG25780"
    },
    "user6": {
        "username": "gggyhuyuy@gmail.com",
        "password": "gvgyT5278/80"
    },
    "user7": {
        "username": "tuyuioioi@gmail.com",
        "password": "gyyyggvD5870"
    },
    "user8": {
        "username": "bbbiuiuiop@gmail.com",
        "password": "ygtgR2536U"
    },
    "user9": {
        "username": "janpoioiiov@gmail.com",
        "password": "ygyg2588aY"
    },
    "user10": {
        "username": "twfghtyhyvb@gmail.com",
        "password": "tgyyytFb236"
    },
    "user11": {
        "username": "janopopijuj@gmail.com",
        "password": "yyhhbhT258/80"
    },
    "user12": {
        "username": "jhujuiiiui@gmail.com",
        "password": "tgvuytU7805"
    },
    "user13": {
        "username": "grtgyhbbhyh@gmail.com",
        "password": "fgvvyI5870/23"
    },
    "user14": {
        "username": "vuyuhnhhjh@gmail.com",
        "password": "fgvtU8052"
    },
    "user15": {
        "username": "hhhuiuiuyu@gmail.com",
        "password": "ffggyU8702"
    },
    "user16": {
        "username": "jjjujijiuio@gmail.com",
        "password": "cvhytfT7801"
    },
    "user17": {
        "username": "hhhuyhyhyg@gmail.com",
        "password": "ffffT85072"
    },
    "user18": {
        "username": "fgtgvghghgh@gmail.com",
        "password": "hhhuyfcF8078"
    },
    "user19": {
        "username": "vvvyhyhghbh@gmail.com",
        "password": "gggyhybgG780/25"
    },
    "user20": {
        "username": "bbbuiuiuyu@gmail.com",
        "password": "gytgxF857T"
    },
    "user21": {
        "username": "ggyhybvbghf@gmail.com",
        "password": "ggggdfS857/80"
    },
    "user22": {
        "username": "vvyhyhbhjui@gmail.com",
        "password": "vvvyhggsS780/25"
    },
    "user23": {
        "username": "vvvgytygyhy@gmail.com",
        "password": "gggAzcgY253"
    },
    "user24": {
        "username": "ccctygvghbg@gmail.com",
        "password": "gvytY2536I"
    },
    "user25": {
        "username": "bbbuiuiuhjyu@gmail.com",
        "password": "gtgvbhgT58/78"
    },
    "user26": {
        "username": "huyuhjuyuy@gmail.com",
        "password": "gtgG8057/25"
    },
    "user27": {
        "username": "gyhytytycvt@gmail.com",
        "password": "fgtyDc41/78"
    },
    "user28": {
        "username": "giokpopo@gmail.com",
        "password": "tygv2587TY"
    },
    "user29": {
        "username": "hhyuhjuju@gmail.com",
        "password": "gyty858/RT"
    },
    "user30": {
        "username": "tgyhbbhjg@gmail.com",
        "password": "tgvFH2536"
    },
    "user31": {
        "username": "gyhujgygvby@gmail.com",
        "password": "gtgvFG2587"
    },
    "user32": {
        "username": "hhhyuhggcc@gmail.com",
        "password": "ggggytR528/E"
    },
    "user33": {
        "username": "niopopocv@gmail.com",
        "password": "ggyhtT258Y"
    },
    "user34": {
        "username": "bbbioujhbg@gmail.com",
        "password": "ggvfT2577"
    },
    "user35": {
        "username": "iuyhujyuyc@gmail.com",
        "password": "vvvytD580"
    },
    "user36": {
        "username": "hhuybbtty@gmail.com",
        "password": "gggtZ253"
    },
    "user37": {
        "username": "bbuiuiunn@gmail.com",
        "password": "jjyuybyY233"
    },
    "user38": {
        "username": "bbiopopom@gmail.com",
        "password": "vvytS52U"
    },
    "user39": {
        "username": "ggyuhyhbh@gmail.com",
        "password": "gggyttR258E"
    },
    "user40": {
        "username": "hhyuhbby@gmail.com",
        "password": "vvvythG58G"
    },
    "user41": {
        "username": "yyhgvgbg@gmail.com",
        "password": "gggtT253O"
    },
    "user42": {
        "username": "hhyunniop@gmail.com",
        "password": "ggtybgh@236"
    },
    "user43": {
        "username": "vvyhbjuf@gmail.com",
        "password": "vvgytzZ245"
    },
    "user44": {
        "username": "hhuyjuygf@gmail.com",
        "password": "hhyyT258"
    },
    "user45": {
        "username": "bbyuhytyb@gmail.com",
        "password": "ffgtg258A"
    },
    "user46": {
        "username": "hhhuyhbhy@gmail.com",
        "password": "gggtgbbT"
    },
    "user47": {
        "username": "bbniopopi@gmail.com",
        "password": "gvtyY258E"
    },
    "user48": {
        "username": "jjiuyhbvyt@gmail.com",
        "password": "gggtvF528"
    },
    "user49": {
        "username": "ghyuhhbb@gmail.com",
        "password": "ggtggF528"
    },
    "user50": {
        "username": "hhyhygvhv@gmail.com",
        "password": "gggytR587"
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
