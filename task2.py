def crime():
  file=open('Crime.csv','r')
  list1=[]	
  list2=[]
  dict={}	
  for line in file:
    line.strip()
  for lines in line.split(','):
    list1.append(lines)
  for i in list1: 
    if(i not in dict): 
      dict[i]=1      
    else:
      dict[i]+=1   

  list3=list(dict.keys())
  for i in range(len(list1)):
    if list1[i] in list3:
      dict[list1[i]]=list1[i+1].strip()

  print ("{:<12} {:<29}".format('key','value')) 
  for key,value in dict.items():   
    crime_type=key
    crime_count=value
    print("{:<12} {:<19}".format(crime_type, crime_count))

crime()

