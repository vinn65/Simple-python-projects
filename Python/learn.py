str = "learn"
print(str[0:-1])

"""
String Slicing
Create a output like

Master
Master has tried
beginner has failed
failed
more
"""
# Use slicing and string concatenation
Str = '''Master has failed more,
than the beginner has tried'''
print(Str[0:6])
print(Str[0:10]+ Str[-6:])
print(Str[-18:-9]+ Str[7:17])
print(Str[11:17])
print(Str[18:22])

print(chr(88))
print(ord('Z'))

num1, num2, num3 = 1, 2, 3 + 3j
sum = num3+num2
print(type(sum))
num = 24 + 7j
# print(type(num.imag))
print(num.imag)
"""
Create a dictionary from the following tuple

tpl = ( 'Set', 'VRAM', 'Slots')
and assign values to the keys in the following order and print the dictionary (:

B550
8g
4
"""
tpl = ( 'Set', 'VRAM', 'Slots')
values = ('B550', '8g', 4)
my_dict = dict(zip(tpl, values))
print(my_dict)

"""If statements Exercise - 3
Create a total variable which will store the total value done in shopping and a discount variable (with 0 value as starting) and in create a if statement where

if the total is over 500 give 5% of discount or if the promotional item is bought give 10% of discount or if the total is over 1000 give 10% of discount else no discount.

Calculate the total and print the total and discount% and discount value for the following total like

Discount : discount% OFF -discount
Total : total"""
total = 760
promo_item_bought = True

discount = 0 
percentage_disc = 0

if total > 500:
    percentage_disc = 5
    discount = 500 * 0.05
    total = total - discount
    print(f"Discount : {percentage_disc}% OFF -{discount}")
    print(f"Total : {total}")
elif total > 1000 or promo_item_bought:
    percentage_disc = 10
    discount = 500 * 0.1
    total = total - discount
    print(f"Discount : {percentage_disc}% OFF -{discount}")
    print(f"Total : {total}")

else:
    print(f"Discount : {percentage_disc}% OFF -{discount}")
    print(f"Total : {total}")


"""

While loops
Create a program to clear the lst list

lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]
Using while loop and pop() function only.

Also print the empty list
"""

### Do not use the list.clear() method
lst = [ 1, 4, 56, 2, 4 , 12,  6, 89 ,11, 0]
i =len(lst)
# print(type(lengh))

while i > 0:
    lst.pop()
    i -= 1
    
print(lst)

"""
Create a for loop to remove the duplicates in the following list :

lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']
Do not use set() function
"""

# Use for loop to create uniques list and print it!
lst = [ 'red', 'blue', 'yellow', 'black', 'red', 'blue', 'green', 'black', 'blue']

unique_lst = []

for c in lst:
    if c in unique_lst:
        continue
    unique_lst.append(c)

print(unique_lst)

"""
In a shopping mart, a person bought items of following prices,

lst = [ 110, 65, 245, 80, 200, 115, 455]
use a for loop to calculate the sum of the elements using the + operator in the list and print it

*without using sum() function
"""
lst = [ 110, 65, 245, 80, 200, 115, 455]

total = 0
for i in lst:
    total += i

print(total)

"""
Arbitrary keyword arguments (**kwargs)

"""

def info(**kw):
    for n,a in kw.items():
        print(n,":" ,a)

info(name='vin',age=23, salary =0)

"""
Creating a functions to smartly round decimal points in a result of addition
"""

def sum_r(*n):
    sm = 0
    d= []

    for num in n:
        sm += num
        Num = str(num).split('.')
        d.append(len(Num[1]))

        min_d = min(d)
        return round(sm, min_d)

print(sum_r(11.90,12.36))

"""
Create a function dsort() to sort a list in descending order, taking a list as argument and returning it

Use the following list and print it!
"""

lst = [ 5, 6, 7, 23 ,12 ,3, 3, 4 ,5, 12, 34]

def dsort(*n):
    lst.sort(reverse=True)
    return lst
    
print(dsort(lst))

"""
Create a str_rev() function to print a reversed version of a string passed to the function as argument like,

'Word'  : 'Dorw'
Note that the output is capitalized and the last letter which may be upper or lower should be lower and also note it's format Word : Reversed

Perform the function on the following strings :
"""
Str1 = 'Desserts'
Str2 = "Live" 
Str3 = 'Pals'
Str4 = 'God'
Str5 = 'Raw'

def str_rev(word):
    rev_word = word[::-1]
    cap_word = rev_word.capitalize()
    
    lower_word = cap_word[:-1] + cap_word[-1].lower()
    
    return lower_word

print(Str1 + " : " + str_rev(Str1))
print(Str2 + " : " + str_rev(Str2))
print(Str3 + " : " + str_rev(Str3))
print(Str4 + " : " + str_rev(Str4))
print(Str5 + " : " + str_rev(Str5))


        