import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "hhhhudfc@cv.nn",
        "password": "hhhuT255+452"
    },
    "user2": {
        "username": "vggytrgh@yt.bb",
        "password": "hhhhY2563*85"
    },
    "user3": {
        "username": "fffvyubi@tt.bb",
        "password": "hhhY2555*25"
    },
    "user4": {
        "username": "bbbuhbg@yg.bn",
        "password": "hhyY255+456"
    },
    "user5": {
        "username": "uiijjnnbx@ff.bb",
        "password": "yyyyT58*25"
    },
    "user6": {
        "username": "yyyhbbbu@tg.bb",
        "password": "yyyT255+58"
    },
    "user7": {
        "username": "hinji@yh.jk",
        "password": "yhU2235+25"
    },
    "user8": {
        "username": "gvbyubbbydt@gmail.com",
        "password": "gggyhhhhT2556*0"
    },
    "user9": {
        "username": "yhbiuiui@gmail.com",
        "password": "yyyzyY255+-*"
    },
    "user10": {
        "username": "hinjioppo@gmail.com",
        "password": "yyyA1225*25"
    },
    "user11": {
        "username": "hujnnntyt@gmail.com",
        "password": "ccvvyyyR2253+*"
    },
    "user12": {
        "username": "hhhinopn@gmail.com",
        "password": "hhhY25568@@@"
    },
    "user13": {
        "username": "tyhhhbop0056@gmail.com",
        "password": "gggY3669@y"
    },
    "user14": {
        "username": "gtybuniin@gmail.com",
        "password": "xccvyyy@Y2553"
    },
    "user15": {
        "username": "frtgbiooou@gmail.com",
        "password": "gggT255《@33》"
    },
    "user16": {
        "username": "hinnnnhjm@gmail.com",
        "password": "yyyT25557+32"
    },
    "user17": {
        "username": "dangyijinv@gmail.com",
        "password": "gggY2555+5587y"
    },
    "user18": {
        "username": "yyyunnnbn@gmail.com",
        "password": "yyyY255+558"
    },
    "user19": {
        "username": "cccctgvbyuu@gmail.com",
        "password": "fffR255+558"
    },
    "user20": {
        "username": "bhnnnniuiu@gmail.com",
        "password": "yyyyaT588+58"
    },
    "user21": {
        "username": "gggujnjnj@gmail.com",
        "password": "yyyG255+583f"
    },
    "user22": {
        "username": "yhbnbnb@gmail.com",
        "password": "yyyY255+253hh"
    },
    "user23": {
        "username": "gojkolmnny@gmail.com",
        "password": "tttcccY366Y+523"
    },
    "user24": {
        "username": "gbinjuuu222@gmail.com",
        "password": "25558yyy:Y233"
    },
    "user25": {
        "username": "tytghbbbnb@gmail.com",
        "password": "tttuuuu2555T125"
    },
    "user26": {
        "username": "ttyhhbnopoplop@gmail.com",
        "password": "gghhY255+2563y"
    },
    "user27": {
        "username": "wz00800511@gmail.com",
        "password": "52858fG25+78"
    },
    "user28": {
        "username": "hhhnnniii253@gmail.com",
        "password": "ttt2536T2+53"
    },
    "user29": {
        "username": "hbbbghbbb23@gmail.com",
        "password": "tX25558*253ii"
    },
    "user30": {
        "username": "bbbinoopop@gmail.com",
        "password": "yyZ25557/36"
    },
    "user31": {
        "username": "cccuijnmmmopo@gmail.com",
        "password": "gggy/z(Z23366gy"
    },
    "user32": {
        "username": "fffyhhhbhji@gmail.com",
        "password": "tttT,yhh2563+253"
    },
    "user33": {
        "username": "gvbbbiuijnc@gmail.com",
        "password": "tttThhuu255*5852"
    },
    "user34": {
        "username": "hhhbnnyuuuc233@gmail.com",
        "password": "yydhhzT2361+96"
    },
    "user35": {
        "username": "ddtyhhhbh@gmail.com",
        "password": "tttsD255+258"
    },
    "user36": {
        "username": "frtgggvvv2365@gmail.com",
        "password": "yyyxR588+125"
    },
    "user37": {
        "username": "hhhyhbbbghty@gmail.com",
        "password": "tttR255*4523"
    },
    "user38": {
        "username": "ffiiijnmmmopo@gmail.com",
        "password": "hhhT5888yui"
    },
    "user39": {
        "username": "tytygvvvuy@gmail.com",
        "password": "ytygvvcfG2123"
    },
    "user40": {
        "username": "ghbiiiyu@gmail.com",
        "password": "tygvvR125*58i"
    },
    "user41": {
        "username": "vunimmm@gmail.com",
        "password": "fgbuY255*58c"
    },
    "user42": {
        "username": "vvubnni@gmail.com",
        "password": "yhbhyhH588uE"
    },
    "user43": {
        "username": "gvubiiiyu@gmail.com",
        "password": "tgvzF2558/25"
    },
    "user44": {
        "username": "fcybbbuyu@gmail.com",
        "password": "rfvuhbY8yhb"
    },
    "user45": {
        "username": "jpopop201@zjtt.tk",
        "password": "tygvgT/??"
    },
    "user46": {
        "username": "vvviopi@tgbi.tk",
        "password": "hhhTT525/+"
    },
    "user47": {
        "username": "gythbbb@tyg.tk",
        "password": "hhgfT@2536/*"
    },
    "user48": {
        "username": "vvvbujuj@tzg.tk",
        "password": "hhhhyyyE25557/+,"
    },
    "user49": {
        "username": "cccyhuij@tgy.tk",
        "password": "hjjuyttT@125+-"
    },
    "user50": {
        "username": "gbbbuiji@tg.tk",
        "password": "hhhyhb255/Y"
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
