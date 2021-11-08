# Reading files 
stream = open('./demo.txt', 'rt') # the default mode is read and txt file 
print('\n Is this file readable : ' + str(stream.readable()))
print('\n Read one charachter (the first one) : ' + stream.read(1))
print('\n Read to end of this line : ' + stream.readline())
print('\n Read all lines to end of this file : ' + str(stream.readlines()))

