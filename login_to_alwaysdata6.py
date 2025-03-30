import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {"username": "yyyybhubb@tg.tk", "password": "hhhh/T12555"},
    "user2": {"username": "gggyhbcv@ty.tk", "password": "hhhT22555*-+#"},
    "user3": {"username": "dc971@tzz.tk", "password": "hyhuhT12555*+-"},
    "user4": {"username": "uiuiui@tvv.tk", "password": "hhhuuuuT255"},
    "user5": {"username": "gfgfgv@tygh.tk", "password": "hhhzzz14745*"},
    "user6": {"username": "nnnikop@tyb.yk", "password": "hhhuuzEr/222"},
    "user7": {"username": "hijnopo@tgg.tk", "password": "yyyhhh255*"},
    "user8": {"username": "vvvyhb@tyg.yk", "password": "gggT22212-"},
    "user9": {"username": "gggyhy@ghy.yk", "password": "hhhh/T2333"},
    "user10": {"username": "hbybbbn@yhh.yk", "password": "hhhY2555*"},
    "user11": {"username": "jjjiopui@yhn.tk", "password": "hhhhRrr255R("},
    "user12": {"username": "gggvgyu@tgtg.yk", "password": "hhhhT123+"},
    "user13": {"username": "hbhyuxx@yuy.yk", "password": "hhhhY2555+-"},
    "user14": {"username": "tygbbbi@yuu.yk", "password": "yyyyY1225*+"},
    "user15": {"username": "bbbiopity@tyty.tk", "password": "hhhyyyT25558/"},
    "user16": {"username": "jjjjuyuyu@tyty.yu", "password": "gghgdddR23698*"},
    "user17": {"username": "eeetytyg@yh.yk", "password": "yuuuYyy2555/"},
    "user18": {"username": "ggfgvbby@tyb.yk", "password": "yuhhT25578/"},
    "user19": {"username": "aastytygh@yu.yi", "password": "uuuuYt2333*"},
    "user20": {"username": "gggbyuhu@yh.hj", "password": "yuuuzty2555/"},
    "user21": {"username": "hhhijnhji@yuj.yk", "password": "hhhY2557/+"},
    "user22": {"username": "baibai@yuy.tk", "password": "yyytttT123+"},
    "user23": {"username": "vvvubopt@tyg.yh", "password": "yyytttG,1238"},
    "user24": {"username": "hbyuyyy@tyt.yj", "password": "hhhtttR12366*"},
    "user25": {"username": "ghokikmnty@gmail.com", "password": "rfvyhY255+36"},
    "user26": {"username": "gvybbbbiyu@gmail.com", "password": "yhbiknT58*583"},
    "user27": {"username": "gggtygvb@gmail.com", "password": "gbuiuuyT+1523"},
    "user28": {"username": "hinjujujyt@gmail.com", "password": "tgvrfcT25+458/"},
    "user29": {"username": "cyghbyuyy@gmail.com", "password": "rfvtgvD54*25"},
    "user30": {"username": "trfggvvgt@gmail.com", "password": "gyhbbR588/25+5"},
    "user31": {"username": "guhbbbyuy@gmail.com", "password": "vbuhyU255/78"},
    "user32": {"username": "hhhyuhbbbh@gmail.com", "password": "azxT588@dft2"},
    "user33": {"username": "ghubbbnjnn@gmail.com", "password": "gtgvzTY255/856"},
    "user34": {"username": "gyhbbbyuy@gmail.com", "password": "tygtR255+78/"},
    "user35": {"username": "gyhbbbtyty@gmail.com", "password": "ghbbyuR255*458"},
    "user36": {"username": "vvvujnjmj@gmail.com", "password": "gyhbbbbvbhbU255*58"},
    "user37": {"username": "ddtygvhuyu@gmail.com", "password": "ujnjujnjY78/25"},
    "user38": {"username": "vyhbbbghg@gmail.com", "password": "xdtyF588/78"},
    "user39": {"username": "fffyhbhbhb@gmail.com", "password": "werdfcD54*782"},
    "user40": {"username": "vbbijnnnuh@gmail.com", "password": "ghyhbF87/58Y"},
    "user41": {"username": "v27705604@gmail.com", "password": "123123123aQ?*"},
    "user42": {"username": "tgyhbghghg@gmail.com", "password": "edcfdxdfT71*487/"},
    "user43": {"username": "vijnnnnjnjn@gmail.com", "password": "ygT805/253U"},
    "user44": {"username": "bijnjkmk@gmail.com", "password": "vgyF588/6932"},
    "user45": {"username": "vbhnnnju@gmail.com", "password": "xcvT858gJ"},
    "user46": {"username": "ttgvhhbgh@gmail.com", "password": "gyhvbb@gT/567"},
    "user47": {"username": "vybhuuuyuy@gmail.com", "password": "ctygH255*58"},
    "user48": {"username": "fftyghbhbh@gmail.com", "password": "hyuhS5887/362"},
    "user49": {"username": "ghyuhbbb@gmail.com", "password": "tcT@yuu676@"},
    "user50": {"username": "hijnjnhjg@gmail.com", "password": "25888/858vH2"}
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
