# import posix
from random import random
from turtle import *

# the materials
# https://brilliant.org/practice/exploding-genomes/?p=7
# there is some confusion as the lenght of the link is 50 nm but th length of the single nucleobase is 0.34 nm
# so there is a question if the nucleobase is only 0.34 and the totla link is 50. So is the rest 49.66 is the link itself? Or I've messed up and don't understand the concept behind 

lengthOfDoubleStrandedDNA = 50 # The persistence length of double-stranded DNA is about 50 nm
startingPostion = position()

def draw_dna_strand (prinitOneStrand):
    forward(lengthOfDoubleStrandedDNA)
    if prinitOneStrand == 1:
        penup()
        right (90)
        forward(5)
        right (90)
        pendown()
        forward(lengthOfDoubleStrandedDNA)
    l_angel  = random()*360
    right(l_angel)
    # print(position()[0]) 
    # print(position()[1])
    return position()

for i in range(5):
    endingPostion = draw_dna_strand(0)
    
print (startingPostion)
print (endingPostion)

done()