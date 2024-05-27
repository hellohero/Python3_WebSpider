# -*- coding:utf-8 -*-

import json
import time
import logging
from security import safe_requests

def get_ip_port(url):
    """
    获取API返回的JSON数据
    :param url: 代理API
    :return: 有效IP
    """
    time.sleep(1)
    response = safe_requests.get(url)
    response = json.loads(response.text)
    result = response['RESULT']
    agent = ''
    for i in range(len(result)):
        agent = 'https://{}:{}/'.format(result[i]['ip'], result[i]['port'])
        logging.debug(agent)
    return agent

if __name__ == '__main__':
    # 测试 - 这里我购买了讯代理的"优质代理"，通过API生成提取链接来提取ip. 测试有效！
    url = ''
    agent = get_ip_port(url=url)
