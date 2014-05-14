"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""
from itertools import permutations

def logic_puzzle():
    
    days = Mon,Tue,Wed,Thu,Fri = [1,2,3,4,5]
    orderings = list(permutations(days))
    
    orde = ((Hamming,Knuth,Minsky,Simon,Wilkes) 
           for Hamming,Knuth,Minsky,Simon,Wilkes in orderings
           for programmer,writer,designer,manager,np in orderings
           for iphone,droid,laptop,tablet,ni in orderings
           #1. The person who arrived on Wednesday bought the laptop.
           if laptop is Wed #1
           #2. The programmer is not Wilkes.
           #3. Of the programmer and the person who bought the droid,
           #      one is Wilkes and the other is Hamming. 
           if programmer is Hamming and droid is Wilkes #2 & 3
           #4. The writer is not Minsky.
           if writer is not Minsky #4
           #5. Neither Knuth nor the person who bought the tablet is the manager.
           if manager is not tablet and manager is not Knuth #5
           #6. Knuth arrived the day after Simon.
           if Knuth is Simon+1
           if Thu is not designer
           if Fri is not tablet
           if designer is not droid
           if Knuth is manager+1
           if (laptop is Mon or laptop is writer ) and (Wilkes is Mon or Wilkes is writer ) and laptop is not Wilkes
           if Tue is tablet or Tue is iphone
 
           )
    config = next(orde)

    names = ['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']
    
    srt = sorted(zip(names,config),key = lambda x:x[1])
    
    return [s[0] for s in srt]

print logic_puzzle() 

                            

      

