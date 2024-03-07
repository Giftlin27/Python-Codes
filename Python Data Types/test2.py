t = 'Prtestint only the words that start with s in this sentence'
s = t.split()
print(s)
for item in s:
    if item[0]=='s':
        print(item)


for num in range(0, 10):
    print(num)

lis = [num for num in range(1, 50) if (num % 3) == 0]
    

su = 'Print every word in this sentence that has an even number of letters'
f = su.split()
for item in s:
    x = len(item)
    if x %2==0:
        print(item)


for num in range(1, 100):
    if(num%3 == 0 and num%5==0):
        print('FizzBuzz')
    elif(num%3==0):
        print('Fizz')
    elif(num%5==0):
        print('Buzz')
    else:
        print(num)

st = 'Create a list of the first letters of every word in this string'
li = [item[0] for item in st.split()]
print(li)