# coding=utf8
import requests
from lxml import etree
import urllib
import urllib2
import cookielib


def test(username, password):
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    url = 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=4'
    html = requests.get(url=url).content
    selector = etree.HTML(html)
    pswname = selector.xpath('//input[@type="password"]/@name')[0]
    postdata = {}
    postdata['mobile'] = username
    postdata[pswname] = password
    postdata['remember'] = 'on'
    postdata['backURL'] = 'http%3A%2F%2Fweibo.cn%2F'  # http://weibo.cn/
    postdata['backTitle'] = '%E5%BE%AE%E5%8D%9A'  # 微博
    postdata['tryCount'] = ''

    vk = selector.xpath('//input[@name="vk"]/@value')[0]
    capId = selector.xpath('//input[@name="capId"]/@value')[0]

    postdata['vk'] = vk
    postdata['capId'] = capId
    postdata['submit'] = '%E7%99%BB%E5%BD%95'  # 登录

    postdata = urllib.urlencode(postdata)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
    req = urllib2.Request(
        url=url,
        data=postdata,
        headers=headers
    )
    result = urllib2.urlopen(req)
    text = result.read()
    # 这里之后原本可以得到想要的cookie的,但是现在被验证码挡住了 :(
    print text


if __name__ == '__main__':
    test('账号', '密码')
