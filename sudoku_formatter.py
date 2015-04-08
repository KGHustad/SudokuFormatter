instructions = """INSTRUCTIONS:
Copy a sudoku puzzle from http://www.menneske.no/sudoku/ to a text file, 
and provide this file as the first command line argument and the file for 
output as the second command line argument

Remember that box height and width must be added manually (before/after 
formatting)"""

import sys
#step #1: fjerne enkle mellomrom bak alle tall
#step #2: bytte ut tall > 9 med bokstaver
#step #3: erstatte doble mellomrom med .
#step #4: erstatte enkle mellomrom med .
#step #5: fjerne tabulering

if len(sys.argv) == 2:
    if sys.argv[1] == 'help':
        print instructions
        sys.exit(1)

#parse command line arguments
try:
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
except IndexError:
    print "ERROR: Insufficient number of command line arguments."
    print "Correct usage:"
    print "python %s <input_file> <output_file>\n" % sys.argv[0]
    print "For help:"
    print "python %s help" % sys.argv[0]
    sys.exit(1)

#read from file
try:
    infile = open(in_filename, 'r')
    data = infile.read()
    infile.close()
except IOError:
    print "ERROR: Unable to read from %s" % in_filename
    sys.exit(1)


#step 1
data = data.replace('1 ', '1')
data = data.replace('2 ', '2')
data = data.replace('3 ', '3')
data = data.replace('4 ', '4')
data = data.replace('5 ', '5')
data = data.replace('6 ', '6')
data = data.replace('7 ', '7')
data = data.replace('8 ', '8')
data = data.replace('9 ', '9')
data = data.replace('0 ', '0')

#step 2
dic = { '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F', 
        '16':'G', '17':'H', '18':'I', '19':'J', '20':'K', '21':'L', 
        '22':'M', '23':'N', '24':'O', '25':'P', '26':'Q', '27':'R', '28':'S', 
        '29':'T', '30':'U', '31':'V', '32':'W', '33':'X', '34':'Y', '35':'Z'}

numbers = range(10,36)
for number in numbers:   
    data = data.replace(str(number), dic[str(number)])

#step 3
data = data.replace('  ', '.')

#step 4
data = data.replace(' ', '.')

#step 5
data = data.replace('\t', '')

#write to file
try:
    outfile = open(out_filename, 'w')
    outfile.write(data)
    outfile.close()
    print "The sudoku puzzle was successfully formatted. "
except IOError:
    print "ERROR: Unable to write to %s" % out_filename
    sys.exit(1)
