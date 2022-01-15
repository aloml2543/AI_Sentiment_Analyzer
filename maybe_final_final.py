# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

POSLIST =['CC','CD','DT','EX','FW','IN','JJ','LS','MD','NN','RB','RP','TO','UH','VB','WP',
'WP$','WRB','VBD','VBG','VBN','VBP','VBZ','WDT','NNS','NNP','JJR','JJS','RBR','RBS','PDT',
'POS','PRP','PRP$','NNPS']
return_v=10

class dic:
    data ={"i":{'POS':'PRP','SC':0},
          'am':{'POS':'VBP','SC':0},
          'sorry':{'POS':'JJ','SC':-0.7},
          'you':{'POS':'PRP','SC':0},
          'are':{'POS':'VBP','SC':0},
          'not':{'POS':'RB','SC':'nn'},
          'feeling':{'POS':'VBG','SC':0.1},
          'well':{'POS':'RB','SC':0.7},
          'know':{'POS':'VBP','SC':0},
          'what':{'POS':'WP','SC':0},
          'mean':{'POS':'VBP','SC':0},
          'congratulations':{'POS':'UH','SC':0.9},
          'done':{'POS':'VBN','SC':0.1},
          'really':{'POS':'RB','SC':'*1.5'},
          'for':{'POS':'IN','SC':0},
            'have':{'POS':('VBP','VB'),'SC':0,'CON':'''global return_v\nif 'done' in token_list:\n    return_v=1\nelse:\n    return_v=0'''}, #조건  ... have... done....     ....have....
          'fun':{'POS':'NN','SC':0.8},
          'your':{'POS':'PRP$','SC':0},
          'lesson':{'POS':'NN','SC':0},
          'survived':{'POS':'VBD','SC':0.7},
          'but':{'POS':'CC','SC':0},
          'everything':{'POS':'NN','SC':0},
          'is':{'POS':'VBZ','SC':0},
          'hurting':{'POS':'VBG','SC':-0.7},
          'now':{'POS':'RB','SC':0},
          'it':{'POS':'PRP','SC':0},
          'took':{'POS':'VBD','SC':0},
          'over':{'POS':'IN','SC':0},
          '4':{'POS':'CD','SC':0},
          'hours':{'POS':'NNS','SC':0},
          'auts':{'POS':'UH','SC':-0.7},
          'bet':{'POS':'VB','SC':0},
          'that':{'POS':'IN','SC':0},
          'tomorrow':{'POS':'NN','SC':0},
          'will':{'POS':'MD','SC':0},
          'be':{'POS':'VB','SC':0},
          'a':{'POS':'DT','SC':0},
          'better':{'POS':'JJR','SC':0.7},
          'day':{'POS':'NN','SC':0},
          '?':{'POS':'PUC','SC':0},
          '!':{'POS':'PUC','SC':0},
          #'!!!!':{'POS':'UH','SC':0},         
          'during':{'POS':'IN','SC':0},
          '.':{'POS':'PUC','SC':0},
          ',':{'POS':'CC','SC':0},
          '...':{'POS':'PUC','SC':0},
          '👏':{'POS':'EMO','SC':'POS','NAME':'CLAPPING','UNICODE':'U+1F44F'},
          '🙈':{'POS':'EMO','SC':'NEG','NAME':'SEENOEVIL','UNICODE':'U+1F648'},
          '🎷':{'POS':'EMO','SC':'NON','NAME':'SAXOPHONE','UNICODE':'U+1F3B7'},
          '😱':{'POS':'EMO','SC':'NEG','NAME':'SCREAMING','UNICODE':'U+1F631'},
          '😫':{'POS':'EMO','SC':'NEG','NAME':'DISTRAUGHT','UNICODE':'U+1F62B'},
          '😍':{'POS':'EMO','SC':'POS','NAME':'SMILING','UNICODE':'U+1F60D'},
          ':(':{'POS':'EMO','SC':'NEG','NAME':'UNSMILING','UNICODE':''},
          ':)':{'POS':'EMO','SC':'NEG','NAME':'SMILING_emo','UNICODE':''},
          ';)':{'POS':'EMO','SC':'POS','NAME':'WINK','UNICODE':''}
          }
  
            
    def NEWgetPOS(self, token_list) :
        """
        토큰을 매개변수로 받아와서 POS를 리턴해주는 함수
        만약 토큰(키) 값이 사전에 없다면 사전에 추가하는 과정을 거쳐서 POS 리턴 가능
        
        """
        temp_str=""
        temp_list=[]
        for i in token_list:
           key_v=i.__str__().lower()
           
           if (self.data[key_v]['CON']!='') :
               
               temp_str=self.data[key_v]['CON']
             
               #print(temp_str)
               code = compile(temp_str, '<string>', 'exec')
               exec(code)
               #print(return_v)
               temp_list.append(self.data[key_v]['POS'][int(return_v)])
               #print("token : ",key_v," POS : ",self.data[key_v]['POS'])
           else:
               try :
                   temp_list.append(self.data[key_v]['POS'])
               except KeyError:
                    print("key error occured during taging")
                    in_error=input("do you want add token "+key_v+" to dictionary? (yes or no)")
                    newKEY=key_v
                    if in_error.lower() == 'yes':
                        newPOS=input("input new POS for new token \""+newKEY+"\" :")
                        while newPOS not in POSLIST:
                            newPOS=input("input new POS for new token \""+newKEY+"\" :")
                        
                        newSC=input("input new SC for new token \""+newKEY+"\" :")
                        
                        while int(newSC) not in range(-1,+1):
                            newSC=input("input correct new SC for new token \""+newKEY+"\" :")
                        newList={}
                        
                        newList.update(POS=newPOS)
                        
                        newList.update(SC=newSC)
                        
                        self.data.setdefault(newKEY,newList)
                        return self.data[key_v]['POS']
                        
                    elif  in_error.lower()=='no':
                        print("you selected no. program will be terminated")
                        exit()
               #print("token : ",key_v," POS : ",self.data[key_v]['POS'])
        #print(temp_list)
        return temp_list
       
    def getSC(self, token) :
        """
        토큰을 매개변수로 받아와서 감정 점수(SC)를 리턴해주는 함수
        만약 감정 점수(SC)값이 사전에 없다면 0으로 리턴
        
        """
        try:
            return self.data[token]['SC']
        except KeyError:
            return 0
        
    def getNAME(self, token) :
        """
        토큰을 매개변수로 받아와서 이모티콘/이모지의 이름(NAME)을 리턴해주는 함수
        만약 이모티콘/이모지의 이름(NAME)값이 사전에 없다면 'NULL' 로 리턴
        
        """
        try:
            return self.data[token]['NAME']
        except KeyError:
            return 'NULL'
        
    def getUNICODE(self, token) :
        """
        토큰을 매개변수로 받아와서 이모티콘/이모지의 유니코드를(UNICODE)을 리턴해주는 함수
        만약 이모티콘/이모지의 유니코드(UNICODE)값이 사전에 없다면 'NULL' 로 리턴
        
        """
        try:
            return self.data[token]['UNICODE']
        except KeyError:
            return 'NULL'
    
    def searchDIC(self, token) :
        """
        토큰을 매개변수로 받아와서 사전에 해당 키가 있는지 확인
        만약 키 값이 존재시 True / 없을 시 False 리턴
        
        """
        temp = token
        if (temp in self.data):
            return True
        else :
            return False
    

def tokenizer(sentence):
   
   """
   문장을 공백을 기준으로 분할->리스트로 저장
   분할된 덩어리 단위로, 정규식 이용하여 필요한 토큰 리스트로 저장 -> 영단어,특수문자(!,.?),이모지,이모티콘 단위로 분류
   정규식으로 토큰화 후에 정렬 필요 -> 딕셔너리(temp_dic)을 이용하여 토큰화 이전 위치 확인하여 위치:키 토큰:값 으로 저장
   정렬 사용하여 원래 위치로 저장
   """
   
   character_pattern=re.compile("[a-zA-Z]+",flags=re.UNICODE)
   puct_pattern=re.compile('[\U00000021\U0000002C\U0000002E\U0000003F]+', flags=re.UNICODE)
   emoji_pattern = re.compile("[\U0001F44F\U0001F648\U0001F3B7\U0001F631\U0001F62B\U0001F60D]+", flags=re.UNICODE)
   emoti_pattern = re.compile("[\U00000022-\U00000029\U0000002F-\U0000003B]+", flags=re.UNICODE)
   
   def sorter(character_pattern,temp_str,start,temp1,temp_split):
       if character_pattern.search(temp_str) != None:
         temp_split+=character_pattern.findall(temp_str) 
        
   
   temp=[]
   splited = sentence.split(' ')
   #print("splited : ", splited)
   for index in range(0,len(splited)):
      temp_str=splited[index].__str__()
      start=0
      temp1=[]   
      temp_split=[]
      temp_dic={}
      sorter(puct_pattern,temp_str,start,temp1,temp_split)    
      sorter(character_pattern,temp_str,start,temp1,temp_split)
      sorter(emoji_pattern,temp_str,start,temp1,temp_split)        
      sorter(emoti_pattern,temp_str,start,temp1,temp_split)  
               
      for j in range(0,len(temp_split)):
                 
        if temp_str.find(temp_split[j].__str__(),start) >=0:
            temp_dic.setdefault(temp_str.find(temp_split[j].__str__(),start),temp_split[j])
            if temp_str.count(temp_split[j])>=2:
                start=temp_str.find(temp_split[j].__str__(),start)+len(temp_split[j])
      
      sdict = sorted(temp_dic.items(), key= lambda item : item[0])
      
      for i in sdict:
          temp.append(i[1])
          
   return temp   


def tagger(token_list):
    """
    토큰 리스트를 매개변수로 받아와서 튜플로 임시 저장
    튜플에 저장된 토큰을 이용하여 getPOS 클래스 메소드를 이용하여 POS 리스트 작
    """
    dic1=dic()
    temp=[]
    
    temp+=dic.NEWgetPOS(dic1, token_list)
    
    return temp


def make_tree(sentence):
    rule = {
        'NN':{'VP':'VP'},
        'DT':{'NP': 'NP'},
        'VP':{'VP': 'VP', 'PUC': 'VP', 'PP': 'VP','EMO': 'VP','SBAR':'VP','VBG':'VP','RB':'VP','CP':'VP'},
        'VB':{'NN': 'VP','NP':'VP','PP': 'VP'},
        'VBD':{'PP': 'VP'},
        'VBZ':{'VBG': 'VP'},
        'VBP':{'VBN': 'VP','ADJP':'VP','JJ':'VP','RB':'VP'},
        'PRP':{'VRP': 'VP','VBP': 'VP','VP':'S','VBD':'S',},
        'PRP$':{'NP': 'NP'},
        'WDT':{'VP': 'VP'},
        'MD':{'VP': 'VP'},
        'WP':{'S':'SBAR','VP':'SBAR'},
        'CC':{'VP': 'CP','CC':'CC','CP':'CP'},
        'CP':{'VBD': 'VP','CC':'CP'},
        'CD':{'NNS':'NP'},
        'JJR':{'NN':'NP'},
        'UH':{'PUC':'S','EMO':'S'},
        'RB':{'VP': 'VP', 'VBN': 'VP','JJ':'ADJP','RP':'PP','CP':'VP'},
        'EMO':{'NN': 'NP'},
        'IN':{'NP': 'PP','SBAR':'PP','VP':'PP'},
        'S':{'EMO': 'S','CP':'S','S':'S','VP':'S'}
    }
    output = [pos for pos in sentence]
    count = 0
    
    point_F, point_R = len(sentence)-2, len(sentence)-1
    pre_output_len = len(output)
    
    while(len(output) != 1):
        count +=1
        try:
            sum_pos = rule[output[point_F]][output[point_R]]
            output[point_F] = sum_pos
            del output[point_R]
            if pre_output_len != len(output):
                print(output)
                pre_output_len = len(output)
                count = 0
            point_F, point_R = len(output)-2, len(output)-1
            for i in output:
                if i not in ['VP', 'S']:
                    continue
            for i in output:
                i = 'S'

        except:
            pass
        point_F -= 1
        point_R -= 1
        if count == 1000: break
        if len(output) == 1 and output[0] == 'VP':
            output[0] = 'S'
            print(output)

    return output
          
          
"""
메인모듈
파일에 필요한 문장을 입력
선택후에 자동으로 토큰화 및 태깅 진행
"""
sentence =[]
dic1=dic()
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
   
   token_list=tokenizer(sentence[select])
   
   
   print("token list : ",token_list)
   print("tag list  : ",tagger(token_list))
 
   
   
   
   
  
   


        
    
    