import datetime


class Weibo:
    def __init__(self):
        self.id = 'default'
        self.content = ''
        self.time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.isrepost = False
        self.repostreason = ''
