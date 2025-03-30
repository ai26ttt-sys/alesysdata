import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {"username": "hbbuyuyu@gmail.com", "password": "tgvytT587/853"},
    "user2": {"username": "buyuhjhjh@gmail.com", "password": "gtgvD25*452"},
    "user3": {"username": "njuijjjjfc@gmail.com", "password": "gtgvzF45/7825"},
    "user4": {"username": "hujnnnyu@gmail.com", "password": "tgvG7/251"},
    "user5": {"username": "yuyuhghh@gmail.com", "password": "yuuaF/457gG"},
    "user6": {"username": "vuhbhhhyghty@gmail.com", "password": "gghyu6777@R"},
    "user7": {"username": "bijunnntgy@gmail.com", "password": "yhyhyhF14*72/Y"},
    "user8": {"username": "ccvtyghgfgcv@gmail.com", "password": "zxS14/417Y"},
    "user9": {"username": "rrrfcftghhhv@gmail.com", "password": "ztgvzy47/25I"},
    "user10": {"username": "ccctygyhy005@gmail.com", "password": "xtgS457/253U"},
    "user11": {"username": "vijnjnjmkop@gmail.com", "password": "tyutyuD7/25*25"},
    "user12": {"username": "tyghbbbghfg@gmail.com", "password": "tygF7/58/8"},
    "user13": {"username": "monuiyuttyg@gmail.com", "password": "rtuuS/2578/8Y"},
    "user14": {"username": "bbbujujhjh@gmail.com", "password": "zxxxdS7/725I"},
    "user15": {"username": "bijkllkk125@gmail.com", "password": "ghyghD54*782"},
    "user16": {"username": "nijjkkjuhjh225@gmail.com", "password": "ytfDzx*457/5"},
    "user17": {"username": "bbujijuj@gmail.com", "password": "tgvF425*528"},
    "user18": {"username": "bbuhjujuju@gmail.com", "password": "tygtG457/7852"},
    "user19": {"username": "gyhbbbhyhty@gmail.com", "password": "tygvF7/5842*"},
    "user20": {"username": "gvuuuyuyuy@gmail.com", "password": "tguhvH78/583"},
    "user21": {"username": "njijkjkljg@gmail.com", "password": "tygD/7823*"},
    "user22": {"username": "vuyhhhyhyh@gmail.com", "password": "yhuhyS578/583"},
    "user23": {"username": "nkmiopopop@gmail.com", "password": "tygyD78/7823"},
    "user24": {"username": "bhujjjuj12358@gmail.com", "password": "yytG7/7825"},
    "user25": {"username": "yyyhuhuyyy@gmail.com", "password": "uuuiiyhS/758/2"},
    "user26": {"username": "binkopiopo@gmail.com", "password": "tgvfgdA47/583Y"},
    "user27": {"username": "gyhiuiui@gmail.com", "password": "tZD47/582/U"},
    "user28": {"username": "vvvinopop@gmail.com", "password": "tgvF7/858@"},
    "user29": {"username": "bbbtytygoo@gmail.com", "password": "vvvgyhQ@1234E"},
    "user30": {"username": "vunopopop@gmail.com", "password": "tgDfD14*253"},
    "user31": {"username": "byuhjujuj@gmail.com", "password": "tgvFDx14*253"},
    "user32": {"username": "gtygvbbhgh@gmail.com", "password": "yuuytyF7/458/72"},
    "user33": {"username": "bhujujujyu@gmail.com", "password": "tgvgtDzx47/582"},
    "user34": {"username": "tadgbhbhbgh@gmail.com", "password": "tygZx@152*58"},
    "user35": {"username": "hbujnjnj@gmail.com", "password": "tgvD78/782"},
    "user36": {"username": "gbghvbhyuy@gmail.com", "password": "tgyD/74858/"},
    "user37": {"username": "yyyghghtg@gmail.com", "password": "fffDG/807U"},
    "user38": {"username": "jinopopii@gmail.com", "password": "gvgtyyE1257Y"},
    "user39": {"username": "gyhhhujuju@gmail.com", "password": "yyyhzdE125"},
    "user40": {"username": "nijuiopbb@gmail.com", "password": "ttggtgG/725"},
    "user41": {"username": "tttyuhujuiu@gmail.com", "password": "tgvygT2587/82"},
    "user42": {"username": "nnniopop@gmail.com", "password": "gyhhH458/78"},
    "user43": {"username": "vvvuiuiui@gmail.com", "password": "gytyDx1258*"},
    "user44": {"username": "vvvuiuiuini@gmail.com", "password": "tgvfS748/23"},
    "user45": {"username": "jhjnjuiuiu@gmail.com", "password": "yyyttF/582"},
    "user46": {"username": "bbbyuyyyy@gmail.com", "password": "ttggF78/08"},
    "user47": {"username": "tgyhyhhhbhyu@gmail.com", "password": "uiiijyD/2@uU"},
    "user48": {"username": "tbyuuyuywer@gmail.com", "password": "yhbYcv257U"},
    "user49": {"username": "gyhuiiiuiu@gmail.com", "password": "tyuuytF78/2I"},
    "user50": {"username": "vvvuyuyubn@gmail.com", "password": "yuiiiT,255/R"},
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
