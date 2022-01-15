# -*- coding: utf-8 -*-
#!/usr/bin/env python
import re

POSLIST =['CC','CD','DT','EX','FW','IN','JJ','LS','MD','NN','RB','RP','TO','UH','VB','WP',
'WP$','WRB','VBD','VBG','VBN','VBP','VBZ','WDT','NNS','NNP','JJR','JJS','RBR','RBS','PDT',
'POS','PRP','PRP$','NNPS']
"""
==POSLIST==
POSLIST is list about all of POS in peen treebank
usage : for adding new dictionary data in class dic when there are not proper data
NEWgetPOS use this list during error exception processing
"""
return_v=0

"""
==dic==
Class dic contain data bank of our system
dic
  | data = dictionary type data storage. it contain dataset for analyze sentence. 
  | NEWgetPOS = core funtion of this class. detail explain is below
  | getSC = function to get sentimental score in dataset for each token
  | getNAME = function for emoji and emoticon. it returns the name of emoji or emoticon in dataset for each token
  | getUNICODE = function for emoji. it returns the UNICODE of emoji from dataset in dictionary
  | searchDIC = search the key in dataset. it just check existence of key

usage : for tokenizer(), tagger use this class for parse sentence input

"""

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
          'really':{'POS':'RB','SC':'up'},
          'for':{'POS':'IN','SC':0},
          'have':{'POS':'VB','SC':0, 'IF': {'NEXT':{'done': {'POS':'MD','SC':0}}}},
          #'have':{'POS':('VB','VBP'),'SC':0,'CON':'''global return_v\nif 'done' in token_list:\n    return_v=1\nelse:\n    return_v=0'''}, 
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
          '👏':{'POS':'EMO','SC':1,'NAME':'CLAPPING','UNICODE':'U+1F44F'},
          '🙈':{'POS':'EMO','SC':-1,'NAME':'SEENOEVIL','UNICODE':'U+1F648'},
          '🎷':{'POS':'EMO','SC':0,'NAME':'SAXOPHONE','UNICODE':'U+1F3B7'},
          '😱':{'POS':'EMO','SC':-1,'NAME':'SCREAMING','UNICODE':'U+1F631'},
          '😫':{'POS':'EMO','SC':-1,'NAME':'DISTRAUGHT','UNICODE':'U+1F62B'},
          '😍':{'POS':'EMO','SC':1,'NAME':'SMILING','UNICODE':'U+1F60D'},
          ':(':{'POS':'EMO','SC':-1,'NAME':'UNSMILING','UNICODE':''},
          ':)':{'POS':'EMO','SC':-1,'NAME':'SMILING_emo','UNICODE':''},
          ';)':{'POS':'EMO','SC':1,'NAME':'WINK','UNICODE':''}
          }
   
    def getPOS(self, token ,rear) :
        """
        ==getPOS(self, token_list)==
        it reads data on dic. and parses token_list as input. it searchs all about token and if needed, it can modify dataset
        it gets key from token_list and modify it lowcase character(use low())
        it checks condition of token first. if there are condition for that token, it will try analyze condition,return proper POS
        there are no condition then just search key on dataset and return POS list
        
        error handling
        when there is not proper key in dataset
        try to add new key, and value from user
        if error can't be handled then i shows proper message and terminate program(use exit())
        
        usage : for tagger use this function for making new list contain tag information for token_list
        
        """
        try :
            if rear:
                if 'IF' in self.data[token.lower()]:
                    
                    value = self.data[token.lower()]['IF']
                    if 'NEXT' in value:
                        
                        for i in value['NEXT'].keys():
                            if rear == i:
                                return value['NEXT'][rear]['POS']
            return self.data[token.lower()]['POS']
        except KeyError:
            print("key error occured during taging")
               
            in_error=input("do you want add token "+token+" to dictionary? (yes or no)")
            newKEY=token
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
                return self.data[token]['POS']
                
            elif  in_error.lower()=='no':
                print("you selected no. program will be exit")
                quit()
            
                    
    def NEWgetPOS(self, token_list) :
        """
        ==NEWgetPOS(self, token_list)==
        it reads data on dic. and parses token_list as input. it searchs all about token and if needed, it can modify dataset
        it gets key from token_list and modify it lowcase character(use low())
        it checks condition of token first. if there are condition for that token, it will try analyze condition,return proper POS
        there are no condition then just search key on dataset and return POS list
        
        error handling
        when there is not proper key in dataset
        try to add new key, and value from user
        if error can't be handled then i shows proper message and terminate program(use exit())
        
        usage : for tagger use this function for making new list contain tag information for token_list
        
        """
        temp_str=""
        temp_list=[]
        for i in token_list:
           key_v=i.__str__().lower()
           try :
               if (self.data[key_v]['CON']!='') :
                   
                   temp_str=self.data[key_v]['CON']
             
                   #print(temp_str)
                   code = compile(temp_str, '<string>', 'exec')
                   exec(code)
                   #print(return_v)
                   temp_list.append(self.data[key_v]['POS'][int(return_v)])
                   #print("token : ",key_v," POS : ",self.data[key_v]['POS'])
               else:
                   temp_list.append(self.data[key_v]['POS'])
                    #print("token : ",key_v," POS : ",self.data[key_v]['POS'])
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
                        temp_list.append(self.data[key_v]['POS'])
                        
                    elif  in_error.lower()=='no':
                        print("you selected no. program will be terminated")
                        exit()    
                        print(temp_list)
        return temp_list
       
    def getSC(self, token) :
        """
        ==getSC(self, token)==

        function for getting sentimental score for analyze sentencies sentimental for check proper emoji/emoticon usages

        """
        try:
            return self.data[token]['SC']
        except KeyError:
            return 0
        
    def getNAME(self, token) :
        """
        ==getNAME(self, token)==
        
        function for getting Name of emoji and emoticon. it returns the name of emoji or emoticon in dataset for each token
        
        """
        try:
            return self.data[token]['NAME']
        except KeyError:
            return 'NULL'
        
    def getUNICODE(self, token) :
        """
        
        ==getUNICODE==
        
        function for emoji. it returns the UNICODE of emoji from dataset in dictionary
        
        """
        try:
            return self.data[token]['UNICODE']
        except KeyError:
            return 'NULL'
    
    def searchDIC(self, token) :
        """
        
        ==getUNICODE==
        
        getUNICODE = function for emoji. it returns the UNICODE of emoji from dataset in dictionary
        
        """
        temp = token
        if (temp in self.data):
            return True
        else :
            return False
    


def tokenizer(sentence):
   
   """
   ==tokenizer(sentence)==
    
    it splits sentence. save that as list
    user regexp, split token detaily.(using sorter(...) )
    it returns token list of sentence
    splited by blank and alphabet character corpus, UNICODE which express punctuation, EMOJI ,EMOTICON)
    
    kind of token
    1. alphabet : ex ) [i] [will]
    2. punctuation corpus : ex) [...] [!!!] [,] [?]
    3. EMOJI or EMOTICON
    
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
    ==tagger(token_list)==
    
    it makes tag list of token_list
    it needs dic instance, so make local object of dic(dic1) and call NEWgetPOS function with token_list
    all of process is on NEWgetPOS. because NEWgetPOS access dataset befor tagger, so we did feature centralization for simplfy

    In addition, we included emotional scores.
    We put token and emotional scores in one list and put them in order in the temp.

    
    """
    dic1=dic()
    tuple1=()+tuple(token_list)
    temp=[]
    
    
    for i in range(0,len(token_list)):
        if i >= len(token_list)-2:
            if dic.getSC(dic1,tuple1[i].lower())!='nn' and dic.getSC(dic1,tuple1[i].lower())!='up':
                temp.append([dic.getPOS(dic1, tuple1[i],None), round(float(dic.getSC(dic1,tuple1[i].lower())),4)])
        else:
            if dic.getSC(dic1,tuple1[i].lower())!='nn'and dic.getSC(dic1,tuple1[i].lower())!='up':
                temp.append([dic.getPOS(dic1, tuple1[i],tuple1[i+1]),round(float(dic.getSC(dic1,tuple1[i].lower())),4)])  
    
    return temp

def sum_token(front, rear):
    #Rules of conbining
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
        'MD':{'VP': 'VP','VBN':'VP'},
        'WP':{'S':'SBAR','VP':'SBAR'},
        'CC':{'VP': 'CP','CC':'CC','CP':'CP'},
        'CP':{'VBD': 'VP','CC':'CP'},
        'CD':{'NNS':'NP'},
        'JJR':{'NN':'NP'},
        'UH':{'PUC':'S','EMO':'S'},
        'RB':{'VP': 'VP', 'VBN': 'VP','JJ':'ADJP','RP':'PP','CP':'VP'},
        'EMO':{'NN': 'NP'},
        'IN':{'NP': 'PP','SBAR':'PP','VP':'PP'},
        'S':{'EMO': 'S','CP':'S'}
    }
    output = []#Because sentence consists of [POS, CS]
    #If the given front and back words are in the rule, add combine value to output.
    if front[0] in rule: 
        if rear[0] in rule[front[0]]:
            output.append(rule[front[0]][rear[0]])
            """
            When combined, compare the two values.
            Add if both are positive or negative.
            Multiply the reversal for 'nn' and 1.5 for 'up'
            If one is negative, make the other negative and add it.
            """
            if 'nn' in [front[1], rear[1]]:
                for i in [front, rear]:
                    if i[1] != 'nn':
                        output.append(round(float(i[1]*-1)),4)
            elif 'up' in [front[1], rear[1]]:
                for i in [front, rear]:
                    if i[1] != 'up':
                        output.append(round(float(i[1]*1.5),4))
            elif (front[1]>=0 and rear[1]>=0) or(front[1]<=0 and rear[1]<=0):
                output.append(round(float(front[1]+rear[1]),4))
            else:
                if front[1]<0:
                    output.append(round(float(front[1] + (rear[1]*-1)),4))
                else:
                    output.append(round(float(rear[1] + (front[1]*-1)),4))
    return output



def make_tree(sentence): #Take a sentence and output an array of final 'S' only.
    #Initializing
    output = [pos for pos in sentence]
    point_F, point_R = len(sentence)-2, len(sentence)-1 #Start with the last two words
    
    while(True):
        #If configured only with S or VP, replace VP with S and stop.
        temp = 0
        for token in output:
            if token[0] not in ['S','VP']:
                temp += 1
        if temp == 0:
            for token in range(len(output)):
                if output[token][0] == 'VP':
                    output[token][0] = 'S'
                    print(output)
            return output

        
        sum_V= sum_token(output[point_F], output[point_R])#If there is a result of combining the two words, output it, and if not, output None.
        #If it can be combined, put it in the first word, delete the last word, and start over with the last word again.
        if sum_V:
            output[point_F] = sum_V 
            del output[point_R]
            print(output)
            point_F, point_R = len(output)-2, len(output)-1
            continue
        #If it can't be combined, slide the word forward one space.
        else:
            point_F -= 1
            point_R -= 1
          

S = [
'I am sorry you are not feeling well. :(',
'Well,you know what I mean ;) !',
'Congratulations! Well Done!👏',
'I am really sorry for what i have done 🙈',
'Have fun during your 🎷 lesson',
'I survived, but everything is hurting now. It took over 4 hours😱',
'Auts 😫 I bet that tomorrow will be a better day... 😍']


 
for sentence in S:
    print("="*100)
    print("\nselceted sentence : ",sentence)
    token_list=tokenizer(sentence)
    print("\n\nToken List: ",token_list)
    tagged_list = tagger(token_list)
    print("\n\ntagged sentence : ",tagged_list)
    print("\n\nTree Building....  ")
    tree=make_tree(tagged_list)
    print("")
    for s in range(len(tree)):
        print(str(s+1)+"'s Sentiment Score: "+ str(tree[s][1]))
    print("="*100)



"""
==main module==

get sentence from sentence set 
all of sentence treated as UNICODE character set(we recommend utf-8-sig for text file accessing.  )
print message for processing(show sentence input, token list, tagged list and so on)

"""
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
 """