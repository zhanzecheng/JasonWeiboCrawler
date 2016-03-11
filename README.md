#JasonWeiboCrawler

###提供cookies爬取特定用户或关键词的爬虫
-----------------
author:Jason Wood

email:wujiecheng@bupt.edu.cn

------------------
开发环境：

* Mac OSX 10.11.3
* Python 2.7

依赖库：

* lxml
* urllib
* request

安装方法：
sudo pip install lxml urllib request

-----------------
### 使用方法
	python main.py _T_WM=xxx; SUHB=xxx; SUB=xxx; gsid_CTandWM=xxx (u/k) (displayID/keyword) (m/s) [(trycount) (thread control)]

参数解释：

1. argv[0]:文件名（必填）
2. argv[1]~argv[4]:四个cookie键值对（必填）。获取方法是，在登录[新浪微博手机版](weibo.cn)前打开浏览器开发者工具，查看网页选项卡，填写账号、密码（、验证码）后登录，搜索浏览器数据包请求头，如下图所示
3. argv[5]:爬虫模式。u表示爬取用户微博，k表示爬取关键词（必填）
4. argv[6]:若爬取用户微博，则提供用户的displayID，该ID在该用户主页上有显示，注意displayID不是登录账号；若爬取关键词，则提供所需关键词，中英文都可，emoji/形如[xx]的微博表情不可（必填）
5. argv[7]:线程模式，m代表多线程，s代表单线程（必填）
6. argv[8]:尝试阈值，同一尝试次数超过该阈值时线程退出，防止程序陷入死循环（选填，默认为20）
7. argv[9]:多线程控制，仅在argv[7]为m时有用，用于指定多线程中单个线程下载的微博页面数（选填，默认为10）

![获取cookies](http://img.blog.csdn.net/20160311094731995)

----------------------
本来这个程序不怎么需要输出信息的，但是开发前期觉得不输出点什么感觉程序好像陷入了死循环，所以就每爬取一个页面就显示完成进度。

另外，程序最后会输出两行，一行显示True或者False。True表示爬取过程很顺利，没有丢失页面，否则显示False；第二行是Done！表示程序结束。

解析的结果将存在/Weibo_parsed/文件夹里，以用户displayID为命名的.txt文件；关键词结果存在/keyword/文件夹里，以关键词为命名的.txt文件。

-------------------
写在后面：

使用他人的劳动成果时最好先征得他人的同意，但是如果你觉得我比较帅，就可以不用征得我的同意啦hhh
如果您觉得好用，请给与我鼓励，如果您觉得不好用，或者爬虫已经失效，请发邮件告诉我。
