class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented')


def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

# 这里SearchEngineBase作为基类可以被继承，继承的类分别代表不同的算法引擎，每一个引擎都应该实现process_corpus()和
# search()两个函数，对应索引器和检索器，mian()函数提供搜索器和用户接口，这样一个简单的包装界面就产生了

# 具体来看这段代码
# add_corpus()函数负责读取文件内容，将文件路径作为ID，连同内容一起送到process_corpus中
# process_corpus需要对内容进行处理，然后文件路径为ID，将处理后的内容保存下来，处理后的内容，就叫做索引(index)
# search则给定一个询问，处理询问，在通过索引检索，然后返回


class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}

    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

search_engine = SimpleEngine()
main(search_engine)

# Bag Of Word
# 词袋模型，将文本转换为不考虑语法，句法，段落，词汇顺序等，只将这个文本看做这些词汇的集合
# 因此只需要存单词而不是全部文章，也不用考虑顺序
import re


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_words = {}

    def process_corpus(self, id, text):
        self.__id_to_words[id] = self.parse_text_to_words(text)

    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, word in self.__id_to_words.items():
            if self.query_match(query_words, word):
                results.append(id)
        return results

    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True

    @staticmethod
    def parse_text_to_words(text):
        text = re.sub(r'[^\w]', ' ', text)  # 去掉标点符号和换行
        text = text.lower()
        word_list = text.split(' ')
        word_list = filter(None, word_list)  # 去除空白字符
        return set(word_list)

search_engine = BOWEngine()
main(search_engine)















