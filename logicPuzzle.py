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
import itertools

def logic_puzzle():
    days = Mon,Tue,Wed,Thu,Fri = [1,2,3,4,5]

    orderings = list(itertools.permutations(days))

    return next(( o  for o in orderings
              for Mon,Tue,Wed,Thu,Fri in orderings
              for Hamming,Knuth,Minsky,Simon,Wilkes in orderings
              for laptop,droid,tablet,iphone,_ in orderings
              for manager,programmer,designer,writer,_ in orderings
              if Wed is laptop              #1
              if programmer is not Wilkes   #2
              if (programmer in [Wilkes,Hamming] or droid in [Wilkes,Hamming]) and programmer is not droid #3
              if writer is not Minsky       #4
              if Knuth is not manager and tablet is not manager #5
              if Knuth == Simon+1 #6
              if Thu is not designer #7
              if Fri is not tablet #8
              if designer is not droid #9
              if Knuth == manager+1 #10
              if (Wilkes in [Mon,writer] or laptop in [Mon,writer]) and Wilkes is not laptop #11
              if iphone is Tue or tablet is Tue
                  
              ))

      
dd = [d for d in list(logic_puzzle())]
print dd