'''
作者: weimo
创建日期: 2021-01-01 15:10:20
上次编辑时间: 2021-01-01 17:21:44
一个人的命运啊,当然要靠自我奋斗,但是...
'''

from ..mpditem import MPDItem


class AdaptationSet(MPDItem):
    def __init__(self, name: str):
        super(AdaptationSet, self).__init__(name)
        self.id = None
        self.contentType = None # type: str
        self.lang = None
        self.segmentAlignment = None
        self.maxWidth = None
        self.maxHeight = None
        self.frameRate = None
        self.par = None
        self.width = None
        self.height = None
        self.mimeType = None
        self.codecs = None

    def get_contenttype(self):
        if self.contentType is not None:
            return self.contentType
        if self.mimeType is not None:
            return self.mimeType.split('/')[0].title()

    def get_suffix(self):
        return '.' + self.mimeType.split('/')[0].split('-')[-1]