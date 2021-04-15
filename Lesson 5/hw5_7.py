import json
data=[]
some_list=[]
some_dict={}
dict_aver_prof={}
sum=0
out_list=[]
try:
    with open(r'file_hw5_7.txt', encoding='utf-8') as f:
        #data=f.readlines()
        for data in f:
            strk=data.split()
            some_dict[strk[0]]=int(strk[2])-int(strk[3])
            #print(data)
            #print(strk)
    print(some_dict)
    for val in some_dict.values():
        sum+=val
    print(sum/len(some_dict))
    dict_aver_prof['average_profit']=sum/len(some_dict)
    out_list=[some_dict, dict_aver_prof]
    print(out_list)
    with open(r'file_hw5_7.txt', 'a') as f:
        json.dump(out_list,f)
except IOError:
        print('No such file in directory')
