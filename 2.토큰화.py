# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

class dic:
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
          'mean':{'POS':'PRP','SC':0},
          'Congratulations':{'POS':'UH','SC':0.9},
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
          'Auts':{'POS':'UH','SC':-0.7},
          'bet':{'POS':'RPR','SC':0},
          'that':{'POS':'IN','SC':0},
          'tomorrow':{'POS':'NN','SC':0},
          'will':{'POS':'MD','SC':0},
          'be':{'POS':'VB','SC':0},
          'a':{'POS':'DT','SC':0},
          'better':{'POS':'JJR','SC':0.7},
          'day':{'POS':'NN','SC':0},
          '?':{'POS':'PUC','SC':0},
          '!':{'POS':'PUC','SC':0},
          '.':{'POS':'PUC','SC':0},
          '👏':{'POS':'EMO','SC':'POS','NAME':'CLAPPING','UNICODE':'U+1F44F'},
          '🙈':{'POS':'EMO','SC':'NEG','NAME':'SEENOEVIL','UNICODE':'U+1F648'},
          '🎷':{'POS':'EMO','SC':'NON','NAME':'SAXOPHONE','UNICODE':'U+1F3B7'},
          '😱':{'POS':'EMO','SC':'NEG','NAME':'SCREAMING','UNICODE':'U+1F631'},
          '😫':{'POS':'EMO','SC':'NEG','NAME':'DISTRAUGHT','UNICODE':'U+1F62B'},
          '😍':{'POS':'EMO','SC':'POS','NAME':'SMILING','UNICODE':'U+1F60D'},
          ':(':{'POS':'EMO','SC':'NEG','NAME':'UNSMILING','UNICODE':''},
          ';)':{'POS':'EMO','SC':'POS','NAME':'WINK','UNICODE':''}
          }
    
    def getPOS(self, token) :
        return self.data[token]['POS']
        
    def getSC(self, token) :
        return self.data[token]['SC']
        
    def getNAME(self, token) :
        return self.data[token]['NAME']
        
    def getUNICODE(self, token) :
        return self.data[token]['UNICODE']
    
    def searchDIC(self, token) :
        temp = token
        if (temp in self.data):
            return True
        else :
            return False
     
"""
dataofdic=dic()
print(dic.getPOS(dataofdic,'day'))
print('\n')
print(dic.getSC(dataofdic,'day'))
print('\n')
print(dic.getNAME(dataofdic,'👏'))
print('\n')
print(dic.getUNICODE(dataofdic,'👏'))
print('\n')

if dic.searchDIC(dataofdic,'day') :
    print("true\n")
else :
    print("false\n")

if dic.searchDIC(dataofdic,'day1') :
    print("true\n")
else :
    print("false\n")
   
   
#POS - 태그, SC - 감정 점수, NAME-이모지,이모티콘 이름 , UNICODE - 유니코드
"""

def tokenizer(sentence,select):
   emoji_pattern = re.compile('[\U00000021-\U0001F64F]+', flags=re.UNICODE)
   m=emoji_pattern.findall(sentence[select])
   index_temp = -1
   l=m[:]
   
   for i in l:
       index_temp+=1
       if l[index_temp].find(".")!=-1:
            temp = m[index_temp].__str__().replace('.','')
            del m[index_temp]
            m.insert(index_temp,temp)
            m.insert(index_temp+1,".")
            #print("case1",index_temp)
       elif l[index_temp].find("!")!=-1:
            temp = m[index_temp].__str__().replace('!','')
            del m[index_temp]
            m.insert(index_temp,temp)
            m.insert(index_temp+1,"!")
            
            #print("case2",index_temp)
       elif l[index_temp].find("?")!=-1:
            temp = m[index_temp].__str__().replace('?','')
            del m[index_temp]
            m.insert(index_temp,temp)
            m.insert(index_temp+1,"?")
           # print("case3",index_temp)
   return m

sentence =[]
f = open("source.txt", 'r',encoding='utf-8-sig')
while True:
    line = f.readline()    
    if not line: break
    line.rstrip('\n')
    sentence.append(line.rstrip('\n'))
    
print('inputed sentences\n')
index =-1

for i in sentence:
    if i:
        index +=1
        print(index,": ",i,'\n')        
    elif not i and index ==-1:
        print("empty file")
        break
    else:
        break
select=0
if index != -1 :
   print('select sentence to analyze',end="")

   while True:
        temp_input = input('input = ')
        if int(temp_input)>=0 and int(temp_input)<=len(sentence):
            select=int(temp_input)
            break;
        else:
            print("input correctly")
   
   print("selceted sentence : ",sentence[select])
   
   token_list=tokenizer(sentence, select)
   print(token_list)
   #print(m,"   ",index_temp)
   
   #emoji_pattern = re.compile('[(a-zA-Z)\U00000021-\U0001F64F]+', flags=re.UNICODE)


        
    
    