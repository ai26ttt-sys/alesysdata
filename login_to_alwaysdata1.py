import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {
        "username": "usatty222553@gmail.com",
        "password": "t56gv456eE#"
    },
    "user2": {
        "username": "gertanyioptty@gmail.com",
        "password": "gtyy6677Aa##%"
    },
    "user3": {
        "username": "hyiopybby12558@gmail.com",
        "password": "ggghhh6666A##{"
    },
    "user4": {
        "username": "gghuxxt1255@gmail.com",
        "password": "ghhu6667A##}"
    },
    "user5": {
        "username": "bbbiop125886@gmail.com",
        "password": "tyyu77777A###%"
    },
    "user6": {
        "username": "gerbuiop22255@gmail.com",
        "password": "hhuuuuvvg66A##%"
    },
    "user7": {
        "username": "hongiopyyt@tzhy.tk",
        "password": "hongiopyyttzhy.tk6677"
    },
    "user8": {
        "username": "goorm326@tzhy.tk",
        "password": "yyyy5tgyS#%"
    },
    "user9": {
        "username": "cxwwtu0txyvut0@gmail.com",
        "password": "yyy777D@@##"
    },
    "user10": {
        "username": "tbtosyxwvtbv@gmail.com",
        "password": "12356yhT@@@"
    },
    "user11": {
        "username": "gtatyiiiopty@gmail.com",
        "password": "yyhgg66665aA##"
    },
    "user12": {
        "username": "ttt009yiop22250@gmail.com",
        "password": "5ctt44fcArRt#"
    },
    "user13": {
        "username": "nssyx0xxynvtw@gmail.com",
        "password": "12356yhT@@@"
    },
    "user14": {
        "username": "chinabnjgg090@gmail.com",
        "password": "123123123aQ#G+"
    },
    "user15": {
        "username": "zj210606@gmail.com",
        "password": "tttt6666aW##%"
    },
    "user16": {
        "username": "yyyttb998@gmail.com",
        "password": "tttggh777S#%"
    },
    "user17": {
        "username": "msxv0xwxwxysst@gmail.com",
        "password": "12583?gTT@"
    },
    "user18": {
        "username": "cgbdfsdsa0090@gmail.com",
        "password": "66666sssss5555T##%"
    },
    "user19": {
        "username": "foybiop2355@gmail.com",
        "password": "yyy666W#}%"
    },
    "user20": {
        "username": "tgiopooooyy@gmail.com",
        "password": "123123123aQ##"
    },
    "user21": {
        "username": "hrwerwr3233r34222@gmail.com",
        "password": "555666777aA###"
    },
    "user22": {
        "username": "cfgfgterere90@gmail.com",
        "password": "yyyy5555gS##%"
    },
    "user23": {
        "username": "copy1105@tzhy.tk",
        "password": "123123123aW###"
    },
    "user24": {
        "username": "cnbjhy001@gmail.com",
        "password": "123456123456aR##%"
    },
    "user25": {
        "username": "haiopyy@ttt0090.tk",
        "password": "hhhtcRt555[]"
    },
    "user26": {
        "username": "zjhyh.xc2@gmail.com",
        "password": "123123123aA##%"
    },
    "user27": {
        "username": "ksts0aty@googlemail.com",
        "password": "1234512345aW##%%"
    },
    "user28": {
        "username": "cfgfgterere90@googlemail.com",
        "password": "55555ttttA##}%%"
    },
    "user29": {
        "username": "a541aa51@gmail.com",
        "password": "123456123456aW##"
    },
    "user30": {
        "username": "iunv0fytnwt@gmail.com",
        "password": "ggghy/?@12525R"
    },
    "user31": {
        "username": "zj210606@googlemail.com",
        "password": "ttttccffEe567##"
    },
    "user32": {
        "username": "ccc0090@gmail.com",
        "password": "678678gF##%"
    },
    "user33": {
        "username": "fff0090@googlemail.com",
        "password": "12341234aA###"
    },
    "user34": {
        "username": "dayday001@zjtz.tk",
        "password": "123123123aQ###"
    },
    "user35": {
        "username": "dayhowto@ttt0090.tk",
        "password": "5555gggggttt###"
    },
    "user36": {
        "username": "china0090hj@gmail.com",
        "password": "ttt666S#%#"
    },
    "user37": {
        "username": "back001@zjtz.tk",
        "password": "back001aA#"
    },
    "user38": {
        "username": "ytbntt0bos@gmail.com",
        "password": "12341234aQ###"
    },
    "user39": {
        "username": "hnoop103@gmail.com",
        "password": "12345612345aQ##%"
    },
    "user40": {
        "username": "cfdfgfgdfafda0@gmail.com",
        "password": "123456123456aQ##"
    },
    "user41": {
        "username": "goitgm@gmail.com",
        "password": "12341234aA###"
    },
    "user42": {
        "username": "u0txuuvyzsusdt@gmail.com",
        "password": "gggg22555?RY"
    },
    "user43": {
        "username": "cc0gidynfg@gmail.com",
        "password": "6666hhhhhhD#+%"
    },
    "user44": {
        "username": "viny23660@gmail.com",
        "password": "55555666tytyA#%"
    },
    "user45": {
        "username": "japanyy912@gmail.com",
        "password": "ddddd6666A##+="
    },
    "user46": {
        "username": "onemanager@tzhy.tk",
        "password": "666777888aA###"
    },
    "user47": {
        "username": "ystgtsgsn@gmail.com",
        "password": "gggguuuD@666777"
    },
    "user48": {
        "username": "wscut0susu00j@gmail.com",
        "password": "yyyfffR12345@@"
    },
    "user49": {
        "username": "hhyy88aa@gmail.com",
        "password": "1234512345aQ##"
    },
    "user50": {
        "username": "goorm320@tzhy.tk",
        "password": "123123123aQ##"
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
