# coding=utf-8
from lxml import etree
import sys
import os
from Weibo import Weibo
import re
import datetime
import json

reload(sys)
sys.setdefaultencoding("utf-8")

def deletefilesorfolders(src):
    '''
    delete files or folders
    '''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc=os.path.join(src,item)
            deletefilesorfolders(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass

class JasonWeiboParser:
    '''
    This class is used to extract weibo texts from plain html page texts stored in file system.
    The extracted weibo are stored in json form in /Weibo_parsed/(uid).txt.
    '''

    def __init__(self, uid):
        self.uid = uid
        self.weibos = []

    def startparsing(self, parsingtime=datetime.datetime.now()):
        basepath = sys.path[0] + '/Weibo_raw/' + self.uid
        for filename in os.listdir(basepath):
            if filename.startswith('.'):
                continue
            path = basepath + '/' + filename
            f = open(path, 'r')
            html = f.read()
            selector = etree.HTML(html)
            weiboitems = selector.xpath('//div[@class="c"][@id]')
            for item in weiboitems:
                weibo = Weibo()
                weibo.id = item.xpath('./@id')[0]
                cmt = item.xpath('./div/span[@class="cmt"]')
                if len(cmt) != 0:
                    weibo.isrepost = True
                    weibo.content = cmt[0].text
                else:
                    weibo.isrepost = False
                ctt = item.xpath('./div/span[@class="ctt"]')[0]
                if ctt.text is not None:
                    weibo.content += ctt.text
                for a in ctt.xpath('./a'):
                    if a.text is not None:
                        weibo.content += a.text
                    if a.tail is not None:
                        weibo.content += a.tail
                if len(cmt) != 0:
                    reason = cmt[1].text.split(u'\xa0')
                    if len(reason) != 1:
                        weibo.repostreason = reason[0]
                ct = item.xpath('./div/span[@class="ct"]')[0]
                time = ct.text.split(u'\xa0')[0]
                weibo.time = self.gettime(self, time, parsingtime)
                self.weibos.append(weibo.__dict__)
        f.close()

    @staticmethod
    def gettime(self, timestr, parsingtime):
        timeregex = '\d{1,4}-\d{1,2}-\d{1,2} \d{1,2}:\d{1,2}:\d{1,2}'
        pattern = re.compile(timeregex)
        match = pattern.search(timestr)
        if match is not None:
            return match.group(0)

        timeregex = u'\d{1,2}月\d{1,2}日 \d{1,2}:\d{1,2}'
        pattern = re.compile(timeregex)
        match = pattern.search(timestr)
        if match is not None:
            month = match.group(0).split('月')[0]
            day = match.group(0).split('日')[0].split('月')[1]
            time = match.group(0).split(' ')[1]
            return str(parsingtime.year) + '-' + month + '-' + day + ' ' + time + ':00'

        timeregex = '\d{0,2}:\d{0,2}'
        pattern = re.compile(timeregex)
        match = pattern.search(timestr)
        if match is not None:
            return str(parsingtime.year) + '-' + str(parsingtime.month) + '-' + str(parsingtime.day) + ' ' + \
                   match.group(0) + ':00'

        timeregex = u'\d{1,2}分钟前'
        pattern = re.compile(timeregex)
        match = pattern.search(timestr)
        if match is not None:
            num = match.group(0).split('分')[0]
            return str(parsingtime - datetime.timedelta(minutes=int(num)))

    def save(self):
        f = open(sys.path[0] + '/Weibo_parsed/' + self.uid + '.txt', 'w')
        jsonstr = json.dumps(self.weibos, indent=4, ensure_ascii=False)
        f.write(jsonstr)
        f.close()

    def clean(self):
        '''
        delete the raw files and folder
        '''
        src=sys.path[0] + '/Weibo_raw/' + self.uid
        deletefilesorfolders(src)


if __name__ == '__main__':
    parser = JasonWeiboParser('dummy');
    parser.startparsing()
    parser.save()
