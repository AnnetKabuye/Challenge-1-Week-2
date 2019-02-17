from datetime import datetime

def age_groups (x):
    x=input("Enter the year in which you were born")
    z = int(datetime.now().year)
    y = (z-(int(x)))
    if (y<=18): print ("You are a  minor")
    elif (18<y<36): print ("You are a youth")
    else: print ("You are an elder")
        
age_groups(2018)
