# Bryce Davitt qqn2ya
s ="{: >5d} times {: >5.2f} is {: >5.2f}"
print ( s. format ( 1, 3.75 , 1 * 3.75 ) )
print ( s. format ( 2, 3.75 , 2 * 3.75 ) )
print ( s. format ( 3, 3.75 , 3 * 3.75 ) )
print ( s. format ( 4, 3.75 , 4 * 3.75 ) )
print ( s. format ( 5, 3.75 , 5 * 3.75 ) )

a = 3.75
print ( f"{2: >5d} times {a: >5.2f} is {2* a: >5.2f}" )

from math import sqrt as squareroot
print ( squareroot ( 4 ) )

print ( "1.", 2 < 5 )
print ( "2.", 2 <= 5 )
print ( "3.", 3 > 3 )
print ( "4.", 3 >= 3 )
print ( "5.", 3 == 3.0 )
print ( "6.", 3 == "3" )
print ( "7."
,
" syntax "
==
" syntax " )
print ( "8."
,
" syntax "
==
" semantics " )
print ( "9."
,
" syntax "
==
" syntax " )
print ( "10."
,
" Python " != " rubbish " )
print ( "11."
,
" Python " > " Perl " )
print ( "12."
,
" banana " < " orange " )
print ( "13."
,
" banana " < " Orange " )

a = 2
match a:
    case 1:
        print ( "a is 1" )
    case 2:
        print ( "a is 2" )
    case 3:
        print ( "a is 3" )
    case others :
        print ( "a is not 1, 2, or 3" )

x = 5
y = 0
match (x,y):
    case (0 ,0):
        print ( "x and y are both 0" )
    case (0,_):
        print ( "x is 0" )
    case (_ ,0):
        print ( "y is 0" )
    case other :
        print ( " neither x nor y is 0" )


#Create a loop that lets the user enter some numbers until he enters zero, and
#then prints their total and their average. Make sure you test the loop with no numbers
#entered, and with several copies of the same number entered.

#num = int(input("what is ur number, enter zero to stop"))
#total = 0
#enters = 0


#while num != 0:
 #   enters +=1
  #  total += num
   # avg = total / enters
    #print(f"total:{total} and avg:{avg}")
    #num = int(input("what is ur number, enter zero to stop"))

fruit =" banana "
for letter in fruit :
    print ( letter )
    if letter =="n":
        fruit =" orange "


i = 1
while i <= 1000000:
    num1 = int( "1" + str( i ) )
    num2 = int( str( i ) + "1" )
    if num2 == 3 * num1 :
        print ( num2 ,"is three times ", num1 )
        break
    i += 1
else :
    print ( "No answer found " )
for i in range ( 4 ):
    for j in range ( i+1, 4 ):
        print ( " ({} ,{}) ". format ( i, j ) )