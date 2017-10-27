#Question 1.1
x = input('Enter name: ')
print(x)

#Question 1.2

x = input('Enter your first name: ')
y = input('Enter your last name: ')
print(x,y)

#Question 1.3

m = input('Enter integer: ')
n = input('Enter integer: ')
m = int(m), n = int(n)
print(m+n)

#Question 1.4

n = input ('Enter integer: ')
nm = input('Enter name: ')
n = int(n)
print (nm*n)

#Question 1.5

n = input ('Enter integer: ')
nm = input('Enter name: ')
n = int(n)

sentence = " "*n + nm + ' is printing this ' + str(n) + ' times \n'
print(sentence*n)

#Question 1.6

def print_three(x):
    x = input('Enter a string: ')
    print (x*3)

x = input('Enter a name: ')
print_three(x)

#Question 2.1

m = int(input('Enter integer: '))
n = int(input('Enter integer: '))
p = int(input('Enter integer: '))
q = int(input('Enter integer: '))

print(p*(m-n)**5)

#Question 2.2

def my_computation(m,n,p,q):
    return (p*((m-n)**5))

#Question 2.3

def my_computation(m,n,p,q):
    if (m+n) == (p + q):
        print('Hurrah!')
    else:
        print('Sorry!')

#Question 3.1

try:
    x = int(input())
    print('is a number')
    if x%2 == 0:
        print('Even!')
    if x% 4 == 0:
        print('You got it!')
except ValueError:
    print('Sorry!')

#Question 3.2

x = int(input('Enter a number'))
result = 0
while x>0:
    result+=(x%10)
    x //= 10
print(result)

#Question 4

to_19 = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,3,6,6,5,5,5,7,6,6]
hundred = 7
thousand = 11
total = 0
for i in range(1,1000):
    u = i%10               #Find last digit
    t = int(((i%100)-u) /10)   #Find second last digit
    h = int(((i%1000)-(t*10)-u) /100)#Find first digit

    if i < 20:                                                          #the number is less than 20
        total += to_19[i]
    elif h != 0 and (t != 0 or u != 0):                #the number is over 100 but not a multiple of 100
        if t == 0 or t == 1:                                            #the number is between x01 and x19
            total += to_19[h] + hundred + 3 + to_19[(t * 10) + u]
        else:                                                           #the number is between x20 and x99
            total += to_19[h] + hundred + 3 + tens[t] + to_19[u]
    elif t == 0 and u == 0:                                             #the number is a multiple of 100
        total += to_19[h] + hundred
    else:                                                               #the number is between 20 and 99
        total +=  tens[t] + to_19[u]

print(total+thousand)
