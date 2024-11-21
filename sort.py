

    
def sortArray(List):
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if(List[i]>List[j]):
                List[i],List[j]=List[j],List[i]
               
    return List        


List = ['3', '2' ,'1' ,'6' ,'9']
print("Before sort")
print(List)
sort_list=sortArray(List)
print(sort_list)