# writing to a file :
# To write to a file you need to create file 
stream = open('output.txt', 'wt')
print('\n Can I write to this file : ' + str(stream.writable()))

stream.write('H') # write a single string ...
stream.writelines(['ello',' ', 'Susan']) # write multiple strings 
stream.write('\n') # write a new line 

# You can pass for writelines a list of strings 
names = ['Alen', 'Chris', 'Sausan']
# Here is how to write to a file using a list, and then you can use a neat feature so you can separate them using whatever you want using join
stream.writelines(','.join(names))
stream.writelines('\n'.join(names))

stream.close() # flush stream and close 