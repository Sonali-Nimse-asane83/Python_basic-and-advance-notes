'''

Flow control:-

Flow control describe the order in which statements will be executed at runtime.



There 3 types of flow control.(statements)

1.Conditional St.(if, elif, else)
2.Interative St.(for , while)
3.Transfer St. (break, continue, pass)


Conditional St:-
indentation:- it's a block of code, here we wrote the statements.



what is if?

Ans:- If condition is true then statements will be executed, if condition is false then statement will be executed
       never executed.


syntax:-
if condition:
    statement

or


if condition:
    statement_1
    statement_2
    statement_3
    ...
'''

# if ka example
'''a = 10
b = 20

if a>b :
    print(a, 'is smaller one')'''


#2 if-else:- if condition is true thr 'if ststement' will be executed otherwise 'else statement' will be


'''city = ['Nurse','Lawer','Police']

if 'doctor' in city:
    print('mein med leke aunga doctor se')

else:
    print('med clinc se leke ayunga')'''


# if-elif or if-elif-else

'''city = ['Nurse','Lawer','Police']


if 'doctor' in city:
    print('Med take from doc')

elif 'Compounder' in city:
    print('Med take from Compounder')

else:
    print('Med take from  Clinic')'''


#Ternary Opeartor :- Special condition of if

'''
if condiotion is True then firstValue will be considered else secondValue will be considered

Syntax:-

variable = firstValue if condition else secondvalue
'''

#ex

a = int(input("Enter your first no."))
b = int(input("Enter your second no."))

x =  a if a>b else b
print(x)



# write a program to find biggest of given 3 numbers.

'''n1 = int(input("Enter your first no."))
n2 = int(input("Enter your sec no."))
n3 = int(input("Enter your third no."))

if n1>n2 and n1>n3:
    print(n1, 'is biggest no.')
elif n2>n3:
    print(n2, 'is biggest no.')
else:
    print(n3, 'is biggest no.')
'''