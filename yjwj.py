import json
import time

import requests

from utils import send


def getxcxtoken():
    headers = {
        'Host': 'ccc.hi.163.com',
        'Connection': 'keep-alive',
        'charset': 'utf-8',
        'User-Agent': "Mozilla/5.0 (Linux; Android 14; 22021211RC Build/UKQ1.231207.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240102 MMWEBID/9184 MicroMessenger/8.0.48.2580(0x2800309D) WeChat/arm64 Weixin Android Tablet NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'content-type': 'application/json',
        'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WyJvcDd2NzVGYWNNX1dtT1J4cWVUcFVuNVVycUJFIiwidGJXVElacWZ1UDFnb3ZUMU5mbExVZz09IiwxNzA4NTgxNzk2ODU3XQ.d4QqV7Jb1D1T8VDKgdgcuxROMWQXO7Tffs5Mtlvkpgc',
        'Referer': 'https://servicewechat.com/wx7c45a544886d9e69/85/page-frame.html',
    }

    params = {
        'activity_id': '28',
    }

    response = requests.get('https://ccc.hi.163.com/d90/mp/group-rank/auth/token', params=params, headers=headers)
    response_data = response.json()  # 将响应数据解析为JSON格式
    token = response_data["data"]["token"]  # 获取code字段的值
    # print(token)
    return token


def getxcxtoken_m():
    url = "https://ccc.hi.163.com/d90/mp/group-rank/auth/token"

    params = {
        'activity_id': "89"
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 14; 22021211RC Build/UKQ1.231207.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240102 MMWEBID/9184 MicroMessenger/8.0.48.2580(0x2800309D) WeChat/arm64 Weixin Android Tablet NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
        'Accept-Encoding': "gzip,compress,br,deflate",
        'charset': "utf-8",
        'content-type': "application/json",
        'token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WyJvcDd2NzVGYWNNX1dtT1J4cWVUcFVuNVVycUJFIiwiZUZoT2g0SXlabDkrZy8wMzdiQ2lpUT09IiwxNzI5MTU1MjMxNzgxXQ.cI9fRbD_MsmIB5GawlUuifywaN8IQj0J8kfV_usIobc",
        'Referer': "https://servicewechat.com/wx7c45a544886d9e69/121/page-frame.html"
    }

    response = requests.get(url, params=params, headers=headers)

    response_data = response.json()  # 将响应数据解析为JSON格式
    token = response_data["data"]["token"]  # 获取code字段的值
    # print(token)
    return token


headers = {
    'Host': 'api.yjwujian.cn',
    'Connection': 'keep-alive',
    'charset': 'utf-8',
    'User-Agent': "Mozilla/5.0 (Linux; Android 14; 22021211RC Build/UKQ1.231207.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240102 MMWEBID/9184 MicroMessenger/8.0.48.2580(0x2800309D) WeChat/arm64 Weixin Android Tablet NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    'content-type': 'application/json',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'xcxtoken': getxcxtoken()
}

headers_m = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 14; 22021211RC Build/UKQ1.231207.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260117 MMWEBSDK/20240102 MMWEBID/9184 MicroMessenger/8.0.48.2580(0x2800309D) WeChat/arm64 Weixin Android Tablet NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    'Accept-Encoding': "gzip,compress,br,deflate",
    'charset': "utf-8",
    'content-type': "application/json",
    'xcxtoken': getxcxtoken_m()
}

headers_s = {
    'User-Agent': "Mozilla/5.0 (Linux; Android 14; 23117RK66C Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/126.0.6478.188 Mobile Safari/537.36 XWEB/1260213 MMWEBSDK/20240102 MMWEBID/9184 MicroMessenger/8.0.48.2580(0x2800309D) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    'Accept-Encoding': "gzip,compress,br,deflate",
    'Content-Type': "application/json",
    'charset': "utf-8",
    'token': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.WyJvcDd2NzVGYWNNX1dtT1J4cWVUcFVuNVVycUJFIiwiSFBMclhMMXpVNXNOSC9wK1VWdm54QT09IiwxNzMxNTEyODc5NTUyXQ.MBTX9H8o1TA2HYXhi3FIp8cnnlq4LN69th3y3Ux3fiI",
    'Referer': "https://servicewechat.com/wx7c45a544886d9e69/127/page-frame.html"
}


def handle_response(response, name):
    data = response.json()
    if data['code'] == 0 or 1004:
        print(response.text)
    else:
        send.sc_send('YJWJ出现未知错误！', name + '：' + data['message'])
        print(response.text)


def sign():
    response = requests.post('https://api.yjwujian.cn/yjwj/xcx_store/sign/do', headers=headers)
    handle_response(response, '登录')


def task1():
    data = '{"taskId":"readNews"}'
    response = requests.post('https://api.yjwujian.cn/yjwj/xcx_store/task/do', headers=headers, data=data)
    handle_response(response, 'readNews')


def task2():
    # 前置模拟分享卡片
    url_1 = "https://ccc.hi.163.com/d90/mp/group-rank/user/card/share"
    payload_1 = json.dumps({})
    response1 = requests.post(url_1, data=payload_1, headers=headers_s).json()
    # print(response1)
    code = response1['code']
    if code != 0:
        send.sc_send('yjwj', '出现未知错误')
    time.sleep(2)

    data = '{"taskId":"shareCard"}'
    url = "https://api.yjwujian.cn/yjwj/xcx_store/task/do"
    response = requests.post(url, headers=headers, data=data)
    handle_response(response, 'shareCard')

def task3():
    data = '{"taskId":"loginGame"}'
    response = requests.post('https://api.yjwujian.cn/yjwj/xcx_store/task/do', headers=headers, data=data)
    handle_response(response, 'loginGame')


def sign_m():
    url = "https://mapi.yjwujian.cn/yjwjm/xcx_store/sign/do"
    response = requests.post(url, headers=headers_m)
    handle_response(response, '登录')


def task1_m():
    data = '{"taskId":"readNews"}'
    url = "https://mapi.yjwujian.cn/yjwjm/xcx_store/task/do"
    response = requests.post(url, headers=headers_m, data=data)
    handle_response(response, 'readNews')


def task2_m():
    # 前置模拟分享卡片
    url_1 = "https://ccc.hi.163.com/d90/mp/group-rank/user/m/card/share"
    payload_1 = json.dumps({})
    response1 = requests.post(url_1, data=payload_1, headers=headers_s).json()
    # print(response1)
    code = response1['code']
    if code != 0:
        send.sc_send('yjwj', '出现未知错误')
    time.sleep(2)

    data = '{"taskId":"shareCard"}'
    url = "https://mapi.yjwujian.cn/yjwjm/xcx_store/task/do"
    response = requests.post(url, headers=headers_m, data=data)
    handle_response(response, 'shareCard')


def task3_m():
    data = '{"taskId":"loginGame"}'
    url = "https://mapi.yjwujian.cn/yjwjm/xcx_store/task/do"
    response = requests.post(url, headers=headers_m, data=data)
    handle_response(response, 'loginGame')

if __name__ == '__main__':
    print('######端游部分签到开始######')
    sign()
    task1()
    task2()
    task3()
    time.sleep(2)
    print('######手游部分签到开始######')
    sign_m()
    task1_m()
    task2_m()
    task3_m()
