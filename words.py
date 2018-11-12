import re

pattern = re.compile(r'[a-zA-Z]+')

def GetTheWords(path):

    file = open(path,'r')
    words = []
    for line in file.readlines():
        wordLine = pattern.findall(line)
        #print(wordLine)
        words.extend(wordLine)

    file.close()
    return words

def CalculateTheWords(words):
    words_dict = dict()
    for word in words:
        words_dict[word] = words_dict.get(word,0) + 1
    return words_dict

def deal():
    words = list()
    words_dict = dict()
    path = 'article.txt'
    words_list = GetTheWords(path)
    words_dict = CalculateTheWords(words_list)
    file =  open("words_dict.txt",'w')
    for word,num in words_dict.items():
        res = (word,num)
        file.write(str(res))
    file.close()
    print(words_list)
    print(words_dict)

if __name__ == '__main__':
    deal()
