import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {"username": "wagninio@tzhy.tk", "password": "uuuuyuu.bjA(."},
    "user2": {"username": "wagfgyhy@zjtz.tk", "password": "uuu.nji2555*S"},
    "user3": {"username": "watyghuiii@zjtz.tk", "password": "uuuu.nnn,fff/T"},
    "user4": {"username": "fgggyhbbbu@tzhy.tk", "password": "hhh.,ghF2536"},
    "user5": {"username": "jjjjjyhhbbghtyt@gmail.com", "password": "hhh.,fgY/[255]"},
    "user6": {"username": "twyuijjjyhgt@gmail.com", "password": "yuhbb...,2555R"},
    "user7": {"username": "buijnnnnhjytyg@gmail.com", "password": "yyy5588.,@\"+-"},
    "user8": {"username": "hingopmkk@tzgyn.tk", "password": "ggggYyy/@@"},
    "user9": {"username": "jpopop201@zjtt.tk", "password": "tygvgT/??"},
    "user10": {"username": "vvviopi@tgbi.tk", "password": "hhhTT525/+"},
    "user11": {"username": "cccyhuij@tgy.tk", "password": "hjjuyttT@125+-"},
    "user12": {"username": "vvvbujuj@tzg.tk", "password": "hhhhyyyE25557/+,"},
    "user13": {"username": "gythbbb@tyg.tk", "password": "hhgfT@2536/*"},
    "user14": {"username": "gggyhbcv@ty.tk", "password": "hhhT22555*-+#"},
    "user15": {"username": "gbbbuiji@tg.tk", "password": "hhhyhb255/Y"},
    "user16": {"username": "yyyybhubb@tg.tk", "password": "hhhh/T12555"},
    "user17": {"username": "dc971@tzz.tk", "password": "hyhuhT12555*+-"},
    "user18": {"username": "vvvino@tzz.tk", "password": "hhhyyxA222"},
    "user19": {"username": "uiuiui@tvv.tk", "password": "hhhuuuuT255"},
    "user20": {"username": "gfgfgv@tygh.tk", "password": "hhhzzz14745*"},
    "user21": {"username": "nnnikop@tyb.yk", "password": "hhhuuzEr/222"},
    "user22": {"username": "hijnopo@tgg.tk", "password": "yyyhhh255*"},
    "user23": {"username": "vvvyhb@tyg.yk", "password": "gggT22212-"},
    "user24": {"username": "gggyhy@ghy.yk", "password": "hhhh/T2333"},
    "user25": {"username": "hbybbbn@yhh.yk", "password": "hhhY2555*"},
    "user26": {"username": "jjjiopui@yhn.tk", "password": "hhhhRrr255R("},
    "user27": {"username": "gggvgyu@tgtg.yk", "password": "hhhhT123+"},
    "user28": {"username": "hbhyuxx@yuy.yk", "password": "hhhhY2555+-"},
    "user29": {"username": "tygbbbi@yuu.yk", "password": "yyyyY1225*+"},
    "user30": {"username": "bbbiopity@tyty.tk", "password": "hhhyyyT25558/"},
    "user31": {"username": "jjjjuyuyu@tyty.yu", "password": "gghgdddR23698*"},
    "user32": {"username": "eeetytyg@yh.yk", "password": "yuuuYyy2555/"},
    "user33": {"username": "ggfgvbby@tyb.yk", "password": "yuhhT25578/"},
    "user34": {"username": "aastytygh@yu.yi", "password": "uuuuYt2333*"},
    "user35": {"username": "gggbyuhu@yh.hj", "password": "yuuuzty2555/"},
    "user36": {"username": "hhhijnhji@yuj.yk", "password": "hhhY2557/+"},
    "user37": {"username": "baibai@yuy.tk", "password": "yyytttT123+"},
    "user38": {"username": "vvvubopt@tyg.yh", "password": "yyytttG,1238"},
    "user39": {"username": "hbyuyyy@tyt.yj", "password": "hhhtttR12366*"},
    "user40": {"username": "gyhbbbb@ty.bi", "password": "yyygggY/233"},
    "user41": {"username": "jjjopio@yh.nj", "password": "hhh/2336T"},
    "user42": {"username": "bbbyyuhuy@ty.bi", "password": "vvvyyyR12555/+"},
    "user43": {"username": "twdfvbbio@ty.hh", "password": "hhhyyyT1222*/*"},
    "user44": {"username": "ninmopuy@ty.bb", "password": "yyygyyT255+-*"},
    "user45": {"username": "rtgvuyu@tyt.nn", "password": "yyyzzzR122-+*45"},
    "user46": {"username": "wafgbyu@ty.bbi", "password": "gguuhbR255*+"},
    "user47": {"username": "hhhhyctg@tg.bi", "password": "hhhS25-*25"},
    "user48": {"username": "ggtgvvvc@tg.vv", "password": "yyyY256*456"},
    "user49": {"username": "touiokl@yh.jj", "password": "yyhfT2566*111"},
    "user50": {"username": "nnniuuhbg@gg.vv", "password": "yyyyG255*-456"},
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
    csrf_token = response.cookies.get('csrftoken')

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
