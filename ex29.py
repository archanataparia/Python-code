people = int(raw_input ("enter number of people: "))
cats = int(raw_input ("enter number of cats: "))
dogs = int(raw_input ("enter number of dogs:"))

if people < cats :
    print "cats are everywhere"
if people < dogs :
    print "the world is drooled on"
if people > cats :
    print "cats are limited"
if people > dogs :
    print "dogs are limited"
    
dogs += 5
#print dogs

if people <= dogs :
    print "people are less than dogs"
    
if people >= dogs :
    print "people are more than dogs"
    
if people == dogs :
    print "people are dogs"