from sys import argv
script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    #seek() operation moves pointer to some other part of the file so you can read or write at that place
    f.seek(0)
    #seek(0) means your reference point is the beginning of the file
    #seek(1)means your reference point is the current file position
    #seek(2)means your reference point is the end of the file
    
def print_a_line(line_count, f):
#reading a line from the fi le and moving the read head to right after the\n that ends that file with readline().
    print line_count, f.readline(),#adding comma after print overwrite \n by readline()
    
current_file = open (input_file)

print "first lets print the whole file:\n"
print_all (current_file)

print "now lets rewind kind of a tape:\n"
rewind(current_file)

print "lets print 3 lines:\n"

current_line = 1
print_a_line (current_line, current_file)

current_line = current_line + 1
print_a_line (current_line, current_file)

current_line += 1 #shorthand notation is += here 
print_a_line (current_line, current_file)
