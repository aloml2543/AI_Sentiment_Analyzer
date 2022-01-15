
    output = [[pos,[]] for pos in sentence]
    count = 0
    
    point_F, point_R = len(sentence)-2, len(sentence)-1
    pre_output_len = len(output)
    
    while(len(output) != 1):
        count +=1
        try:
            if ('VP' in [output[point_F][0], output[point_R][0]]) or ('S' in [output[point_F][0], output[point_R][0]]):
                if 'EMO' in [output[point_F][0], output[point_R][0]]:
                    if (output[point_F][1] > 0 and output[point_R][1] > 0) or (output[point_F][1] < 0 and output[point_R][1] < 0):
                        print('true')
                    elif output[point_F][1] == 0 or output[point_R][1] == 0:
                        pass
                    else:
                        print('false')
                        
            
            sum_pos = rule[output[point_F][0]][output[point_R][0]]
            if 'nn' in [output[point_F][1],output[point_R][1]]:
                sum_SC = output[point_F][1]*-1
            else:
                sum_SC = output[point_F][1]+output[point_R][1]
            output[point_F][0] = sum_pos
            output[point_F][1] = sum_SC
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
S = [
'I am sorry you are not feeling well. :(',
'Well,you know what I mean ;) !',
'Congratulations! Well Done!👏',
'I am really sorry for what i have done 🙈',
'Have fun during your 🎷 lesson',
'I survived, but everything is hurting now. It took over 4 hours😱',
'Auts 😫 I bet that tomorrow will be a better day... 😍']


for sentence in S:
   print("\n\nselceted sentence : ",sentence)
   
   token_list=tokenizer(sentence)
   print(token_list)
   print(tagger(token_list))
   make_tree(tagger(token_list))
 
   
   
   
   
  
   


        
    
    