############################################################
#                                                          #
#                     By Jason Wood                        #
#                                                          #
#                wujiecheng@bupt.edu.cn                    #
#                                                          #
############################################################
# encoding: utf-8

import sys
import os

from JasonWeiboCrawler import JasonWeiboCrawler
from JasonWeiboParser import JasonWeiboParser

reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    '''
        @description: Main function of the Weibo Crawler
        @:parameter1~4: Cookie. (must-have)
        @:parameter5: Function control, "k": keyword crawling, "u": user's weibos crawling. (must-have)
        @:parameter6: If the 5th parameter is "k", then this parameter should be the interested keyword, otherwise, interested uid. (must-have)
        @:parameter7: Thread control, "s": single thread, "m": multi thread. (only useful when parameter5 is "u", default "s")
        @:parameter8: This arg is for weibo gathering process, it's purpose is to tell whether this program to run in regular mode or test mode. (must-have, r/t, default r)
        @:parameter9: Try count, when attempt to download the same page exceeds try count, the thread simply gives up and returns. (default and recommended 20)
        @:parameter10: Multi-thread control, thread interval. (only useful when parameter4 is "m", default 10)
    '''

    if not (6 < len(sys.argv) < 12):
        print '''
        Usage:
            parameter1~4: Cookie. (must-have)
            parameter5: Function control, "k": keyword crawling, "u": user's weibos crawling. (must-have)
            parameter6: If the 5th parameter is "k", then this parameter should be the interested keyword, otherwise, interested uid. (must-have)
            parameter7: Thread control, "s": single thread, "m": multi thread. (only useful when parameter5 is "u", default "s")
            parameter8: This arg is for weibo gathering process, it's purpose is to tell whether this program to run in regular mode or test mode. (must-have, r/t, default r)
            parameter9: Try count, when attempt to download the same page exceeds try count, the thread simply gives up and returns. (default and recommended 20)
            parameter10: Multi-thread control, thread interval. (only useful when parameter4 is "m", default 10)
        '''
        os._exit(-1)
    else:
        cookie = sys.argv[1] + sys.argv[2] + sys.argv[3] + sys.argv[4]
        jasonCrawler = 0
        if sys.argv[5] == 'k':
            jasonCrawler = JasonWeiboCrawler(cookie, 'dummy')
            jasonCrawler.keywordcrawling(sys.argv[6])
        elif sys.argv[5] == 'u':
            jasonCrawler = JasonWeiboCrawler(cookie, sys.argv[6])
            if sys.argv[7] is not None:
                if sys.argv[7] == 's':
                    try:
                        trycount = int(sys.argv[9])
                    except:
                        trycount = 20
                    if sys.argv[8] == 't':
                        print jasonCrawler.startcrawling(trycount=trycount, istest=True)
                    else:
                        print jasonCrawler.startcrawling(trycount=trycount)
                elif sys.argv[7] == 'm':
                    try:
                        trycount = int(sys.argv[9])
                    except:
                        trycount = 20
                    try:
                        interval = int(sys.argv[10])
                    except:
                        interval = 10
                    if sys.argv[8] == 't':
                        print jasonCrawler.multithreadcrawling(interval=interval, trycount=trycount, istest=True)
                    else:
                        print jasonCrawler.multithreadcrawling(interval=interval, trycount=trycount)
                else:
                    print 'Argv7 should be either "s" or "m"'
                    os._exit(7)
            else:
                print jasonCrawler.startcrawling(trycount=20)
            jasonParser = JasonWeiboParser(sys.argv[6])
            jasonParser.startparsing()
            jasonParser.save()
            jasonParser.clean()
        else:
            print 'Argv6 should be either "k" or "u"'
            os._exit(6)
        print 'Done!'
