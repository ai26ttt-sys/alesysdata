import time
import requests

# 定义登录信息
login_url = "https://admin.alwaysdata.com/login/"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"

# 定义多个用户的登录信息
users = {
    "user1": {"username": "baidu@tzhy.tk", "password": "123123123aA@@@"},
    "user2": {"username": "add@tzhy.tk", "password": "123123123aA@@@"},
    "user3": {"username": "cool@tzhy.tk", "password": "123123123aA@@@"},
    "user4": {"username": "ggg12345@zjtz.tk", "password": "1234512345aA@@"},
    "user5": {"username": "cnzj1699@tzhy.tk", "password": "123123125888@aA"},
    "user6": {"username": "yyyyopopop@gmail.com", "password": "12351235aW@@"},
    "user7": {"username": "ythiopp5225@tzhy.tk", "password": "yyhhhG1255*+/"},
    "user8": {"username": "github2405@tzhy.tk", "password": "yyytttT1255+-*"},
    "user9": {"username": "jpoop24005@tzhy.tk", "password": "yyyhhhbbb235T@"},
    "user10": {"username": "hkgythh@tzhy.tk", "password": "yyyyfffT1255/**"},
    "user11": {"username": "canada0217@tzhy.tk", "password": "yyyuuuiii123123A#"},
    "user12": {"username": "yn0217@tzhy.tk", "password": "yyyyttttD123@[]"},
    "user13": {"username": "yyyypop@tzhy.tk", "password": "123123123125aA@"},
    "user14": {"username": "five@wpv08.onmicrosoft.com", "password": "123123123aA@@@"},
    "user15": {"username": "hhh240302@tzhy.tk", "password": "123123123aA@@@"},
    "user16": {"username": "dweeazz323@gmail.com", "password": "123123123aA@@@"},
    "user17": {"username": "ssyywywd@gmail.com", "password": "123123123aQ@@@"},
    "user18": {"username": "vgy7777r@gmail.com", "password": "123123123aQ@@@"},
    "user19": {"username": "zjhyhxc@gmail.com", "password": "123123123aQ@@@"},
    "user20": {"username": "blank@tzhy.tk", "password": "123123123aQ@@@"},
    "user21": {"username": "howtogo@tzhy.tk", "password": "123123123aA@@@"},
    "user22": {"username": "cywucktg0w@gmail.com", "password": "123123123aA@@@"},
    "user23": {"username": "eee0090@gmail.com", "password": "123123123aA@@@"},
    "user24": {"username": "hai240330@tzhy.tk", "password": "123123123aA@@@"},
    "user25": {"username": "hk240330@tzhy.tk", "password": "123123123aA@@@"},
    "user26": {"username": "yyyadd@tzhy.tk", "password": "123123123aA@@@"},
    "user27": {"username": "hhhiii@tzhy.tk", "password": "123123123aA@@@"},
    "user28": {"username": "gothinhg@tzhy.tk", "password": "123123123aA@@@"},
    "user29": {"username": "bankop@tzhy.tk", "password": "123123123aA@@@"},
    "user30": {"username": "gobank@tzhy.tk", "password": "123123123aQ@@@"},
    "user31": {"username": "sss240404@tzhy.tk", "password": "ssstttyyy444S"},
    "user32": {"username": "kkkonno@tzhy.tk", "password": "yyyhhhhbbb@iTT"},
    "user33": {"username": "min0022@tzhy.tk", "password": "tttgggG1235#"},
    "user34": {"username": "hkfivetty@tzhy.tk", "password": "yhyhyh@1235A"},
    "user35": {"username": "hrty123555@tzhy.tk", "password": "yyyhhhT1255/"},
    "user36": {"username": "jptty240505@tzhy.tk", "password": "ygyg12555#/T"},
    "user37": {"username": "yyyiop240503@tzhy.tk", "password": "ccctttt123E:@"},
    "user38": {"username": "bbb240407@tzhy.tk", "password": "hhhyyyy/:YY123"},
    "user39": {"username": "jpop20255@tzhy.tk", "password": "yyyzzzT@[]"},
    "user40": {"username": "ghost240505@tzhy.tk", "password": "yyyybbbbT1235#+@"},
    "user41": {"username": "fnang2536@zjtz.tk", "password": "yyy1222/#S"},
    "user42": {"username": "vujnfff@zjtz.tk", "password": "yyyubbbT12-+*"},
    "user43": {"username": "wangopone@tzhy.tk", "password": "yhb2536*Y63"},
    "user44": {"username": "wangyuioi@zjtz.tk", "password": "gggyT@[iop]"},
    "user45": {"username": "wanghyuhb@tzhy.tk", "password": "gghhy2255*TY"},
    "user46": {"username": "wangtthvbi@tzhy.tk", "password": "hhhhh2555/+*@U"},
    "user47": {"username": "wanfrtguuu@zjtz.tk", "password": "yyyyy2222/*[G]"},
    "user48": {"username": "wagfttgbb@tzhy.tk", "password": "yyy2222/*UUU"},
    "user49": {"username": "wagtyffghb@tzhy.tk", "password": "uuuu2555/*+-UF"},
    "user50": {"username": "wagunss@zjtz.tk", "password": "yyyy2555**HH"},
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
