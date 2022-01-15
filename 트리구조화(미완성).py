# -*- coding: utf-8 -*-

"""

"""
class dic:
    #POS - 태그, SC - 감정 점수, NAME-이모지,이모티콘 이름 , UNICODE - 유니코드
    data ={"i":{'POS':'PRP','SC':0},
          'am':{'POS':'VBP','SC':0},
          'sorry':{'POS':'JJ','SC':-0.7},
          'you':{'POS':'PRP','SC':0},
          'are':{'POS':'VBP','SC':0},
          'not':{'POS':'RB','SC':'nn'},
          'feeling':{'POS':'VBG','SC':0.1},
          'well':{'POS':'RB','SC':0.7},
          'Well':{'POS':'UH','SC':0.6},
          'know':{'POS':'VBP','SC':0},
          'what':{'POS':'WDT','SC':0},
          'mean':{'POS':'VRP','SC':0},
          'congratulations':{'POS':'UH','SC':0.9},
          'done':{'POS':'VBN','SC':0.1},
          'really':{'POS':'RB','SC':'*1.5'},
          'for':{'POS':'IN','SC':0},
          'have':{'POS':'MD','SC':0},
          'fun':{'POS':'JJ','SC':0.8},
          'during':{'POS':'RB','SC':0},
          'your':{'POS':'POS','SC':0},
          'lesson':{'POS':'NN','SC':0},
          'survived':{'POS':'VBD','SC':0.7},
          'but':{'POS':'CC','SC':0},
          'everything':{'POS':'NN','SC':0},
          'is':{'POS':'VBZ','SC':0},
          'hurting':{'POS':'VBH','SC':-0.7},
          'now':{'POS':'RB','SC':0},
          'it':{'POS':'PRP','SC':0},
          'took':{'POS':'VBD','SC':0},
          'over':{'POS':'RP','SC':0},
          '4':{'POS':'CD','SC':0},
          'hours':{'POS':'NNS','SC':0},
          'auts':{'POS':'UH','SC':-0.7},
          'bet':{'POS':'RPR','SC':0},
          'that':{'POS':'IN','SC':0},
          'tomorrow':{'POS':'NN','SC':0},
          'will':{'POS':'MD','SC':0},
          'be':{'POS':'VB','SC':0},
          'a':{'POS':'DT','SC':0},
          'better':{'POS':'JJR','SC':0.7},
          'day':{'POS':'NN','SC':0},
          '👏':{'POS':'EMO','SC':'POS','NAME':'CLAPPING','UNICODE':'U+1F44F'},
          '🙈':{'POS':'EMO','SC':'NEG','NAME':'SEENOEVIL','UNICODE':'U+1F648'},
          '🎷':{'POS':'EMO','SC':'NON','NAME':'SAXOPHONE','UNICODE':'U+1F3B7'},
          '😱':{'POS':'EMO','SC':'NEG','NAME':'SCREAMING','UNICODE':'U+1F631'},
          '😫':{'POS':'EMO','SC':'NEG','NAME':'DISTRAUGHT','UNICODE':'U+1F62B'},
          '😍':{'POS':'EMO','SC':'POS','NAME':'SMILING','UNICODE':'U+1F60D'},
          ':(':{'POS':'EMO','SC':'NEG','NAME':'UNSMILING','UNICODE':''},
          ';)':{'POS':'EMO','SC':'POS','NAME':'WINK','UNICODE':''},
          ',':{'POS':'PUNC','SC':'NON','NAME':'COMMA','UNICODE':''},
          '!':{'POS':'PUNC','SC':'NON','NAME':'EXCLAM','UNICODE':''}
          }

    rule = {
        'PRP':{'VRP': 'VP'},
        'PRP':{'VBP': 'VP'},
        'WDT':{'VP': 'VP'},
        'PUNC':{'VP': 'VP'},
        'RB':{'VP': 'VP'},
        'VP':{'VP': 'S'},
        'S':{'EMO': 'S'},
        'S':{'PUNC': 'S'}
    }
    
    def getPOS(self, token) :
        try:
            token=token.lower()
        except:
            pass
        try:
            return self.data[token]['POS']
        except:
            return
        
    def getSC(self, token) :
        return self.data[token]['SC']
        
    def getNAME(self, token) :
        return self.data[token]['NAME']
        
    def getUNICODE(self, token) :
        return self.data[token]['UNICODE']

    def getRuleBase(self, front, rear):
        try:
            return self.rule[front][rear]
        except:
            return None
    
    def searchDIC(self, token) :
        temp = token
        if (temp in self.data):
            return True
        else :
            return False
    
    def isEMO(self, token): # 주어진 토큰이 이모지인지 아닌지 구별함
        try:
            if self.getPOS(token) =='EMO':
                return True
        except:
            pass        
        return False

    def tokenizer(self, list) : #주어진 문장 리스트에서 한 문장씩 가져와 각 글자를 확인 후 토큰화함
        returnList = []
        token = []
        listPointer = 0
        for sentence in list:
            returnList.append([])
            letterPointer=0
            while(letterPointer != len(sentence)):
                if sentence[letterPointer] == ' ':
                    returnList[listPointer].append("".join(token))
                    token = []

                elif sentence[letterPointer] == '!':
                    returnList[listPointer].append("".join(token))
                    token = []
                    returnList[listPointer].append("!")
                
                elif sentence[letterPointer] == '.':
                    returnList[listPointer].append("".join(token))
                    token = []
                    while(sentence[letterPointer] == '.'):
                        token.append(sentence[letterPointer])
                        letterPointer += 1
                    returnList[listPointer].append("".join(token))
                    token = []

                elif sentence[letterPointer] == ',':
                    returnList[listPointer].append("".join(token))
                    token = []
                    returnList[listPointer].append(",")

                elif self.isEMO(sentence[letterPointer]) :
                    returnList[listPointer].append("".join(token))
                    token = []
                    returnList[listPointer].append(sentence[letterPointer])

                else:
                    token.append(sentence[letterPointer])
                letterPointer += 1
            returnList[listPointer].append("".join(token))
            token = []
            while('' in returnList[listPointer]):
                returnList[listPointer].remove('')
            listPointer += 1
        return returnList
    
    def tagger(self, list):
        returnList = []
        listPointer = 0
        for sentence in list:
            returnList.append([])
            for token in sentence:
                returnList[listPointer].append([token, self.getPOS(token)])
            
            listPointer += 1
        return returnList

    class Node:
        def __init__(self, front, rear, pos):
            self.front = front
            self.rear = rear
            self.pos = pos

    def make_tree(self, sentence):
        temp = []
        temp2 = []
        count = 0
        for token in sentence:
            temp.append(token[1])
        while(len(temp) != 1 & count !=100):
            print(temp)
            temp2 = []
            pointer = len(temp)-1
            while(pointer):
                key1 = temp[pointer-1]
                key2 = temp[pointer]
                pos = self.getRuleBase(key1, key2)
                print(key1, key2)
                if pos:
                    temp2.insert(0, pos)
                    pointer -= 1
                else:
                    temp2.insert(0, key2)
                pointer -= 1
            temp2.insert(0, key1)
            temp = temp2
            count += 1

        return 









S = [
'I am sorry you are not feeling well. :(',
'Well,you know what I mean ;) !',
'Congratulations! Well Done!👏',
'I am really sorry for what i have done 🙈',
'Have fun during your 🎷 lesson',
'I survived, but everything is hurting now. It took over 4 hours😱',
'Auts 😫 I bet that tomorrow will be a better day... 😍']


dictionary = dic()

tokenedList = dictionary.tokenizer(S)

taggedList = dictionary.tagger(tokenedList)
dictionary.make_tree(taggedList[1])
