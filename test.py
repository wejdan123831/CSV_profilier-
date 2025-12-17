#I = ['Ali', 'sara', 'adam ']

#list(reversed(I))
#for i in I :
   # print( i)
    
 I = ['1', '2', '3']
    reversed_list=list( reversed(I))
    # 1
    reversed_int_list=[]
    for x in reversed_list:
        result= int(x)
      reversed_int_list.append(int(x))
      
      #2
       reversed_int_list=[
           int(x)
           for x in reversed_list
       ]
       # 3 
       list(map(int,reversed_list))