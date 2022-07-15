def is_two(x):
    x=(int(x))
    if x==2:
        return True
    else:
        return False



def is_vowel(x):
   
    if len(x)==1 and type(x) == str:
        x=x.lower()
        vowels=['a','e','i','o','u']
        for v in vowels:
            if x==v:
                x=True
                return x
            else:
                x=False
                return x

def is_consonant(x):
    return not is_vowel(x)


def capital_cosonant(x):
    if type(x) == str and is_consonant(x[0]):
        x=x[0].upper()+x[1:]
        return x




def calculate_tip(bill,tip_percent=.2):
    if tip_percent>=0 and tip_percent<=1:
        tip=bill*tip_percent
        return tip

def apply_discount(price,discout_percent=0.0):
    applied_dis= price(1-discout_percent)
    return applied_dis



def count_commas(x):
    commas=[i for i in x if i==',']
    return len(commas)

 



def handle_commas(x):
    x=int(x.replace(',',''))
    
    return x,type(x)





def get_letter_grade(x):
    a=any( [i for i in range(88,101)if x==i])
    b=any( [i for i in range(80,88)if x==i])
    c=any( [i for i in range(67,80)if x==i])
    d=any( [i for i in range(60,67)if x==i])
    f=any( [i for i in range(0,60)if x==i])

    if a:
        return 'A'
    elif b:
        return 'B'
    elif c:
        return 'C'
    elif d:
        return 'D'
    elif f:
        return 'F'


def remove_vowels(x):
    if type(x)== str:
        vowels_to_remove=[x[i] for i in range(len(x)) if is_vowel(x[i])]
        for v in vowels_to_remove:
            x=x.replace(v,'')
        return x
    else:
        return "Not a string"
x='RichardMacken'


def normalize_name(x):
    x=str(x)
    x=x.strip()
    x=x.lower()
    x=x.replace(" ","_")
    chars=[str(chr(i)) for i in range(97,123)]
    chars.append(str('_'))
    nums=[str(i) for i in range(0,10)]
    chars=chars+nums
    to_remove=[i for i in range(len(x)) if (any(c for c in chars if x[i]==c)==False)]
   

    for t in to_remove:
        x=x.replace(x[t],' ')
        x=x.strip()
        x=x.replace(" ","_")

    
    while x[0].isnumeric() and len(x)>=0:
        x=x[1:]
        

    return x




def cumulative_sum(x):
    sum_x=0
    n_list=[]
    for i in x:
        sum_x+=i
        n_list.append(sum_x)
    return n_list



def cumulative_sum(x):
    n_list=[sum(x[:i])for i in x]
    return n_list




#strip of the pm/am from the string if pm add 12
def twelveto24(x):
    x=x.lower()
    am_index=x.find("am")
    pm_index=x.find("pm")
    if am_index >=0:
        x=x[:am_index]
        return x
    elif pm_index >=0:
        x=x[:pm_index]
        #00:00
        hour= int(x[:2])
        min=(x[3:5])
        hour+=12
        hour=str(hour)
        mil_time= hour + ':'+min
        return mil_time


#if greater than 12 hour mod 12 add pm
def mil_to_civ_time(x):
    hour= int(x[:2])
    c=':'
    if hour >12:
        hour=str(hour%12)
        time= hour+c+ x[3:6]+ 'pm'
        return time
    elif hour == 12:
        hour=str(hour)
        time= hour+c+ x[3:6]+ 'pm'
        return time
    else:
        hour=str(hour)
        time= hour+c+ x[3:6]+ 'am'
        return time





def col_index():
    user_imp=input('Enter a column index in the form of A or B or ... or AA or ... or AZ etc')
    x=[]
    count=0
    unicode_array=[i for i in range(97,123)]
    adder= [i for i in range(0,26)]
    for im in user_imp:
        im=im.lower()
        im=ord(im)
        for a in adder:
            if im==unicode_array[a]:
                x.append(adder[a]+1)#remember that you don't save append to a variable you just call it
                count+=1
    if count == 1:
        x=x[0]
        return x
    else:
        for i in range(1,len(x)):
            x[i]=x[i]+26
        x=sum(x)-count+1
        return x
