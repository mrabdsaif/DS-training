# How do you read and write to a specific file :
# We have a few different ways to do that using a file stream :
# To open a file, you create a stream object 
# we determine the file name and the mode, most of time we leave the buffer_size ti the default

stream = open(file_name, mode, buffer_size)

# Modes :
# r - Read (default)
# w - truncate and write  # W will overwrite the existing contents in the file 
# a - append if file exists  # we use a (append) to add more lines without overwriting what is already there
# x - write, fail if file exists # x allows you to write to the file, but this should be a new file that I am creating, and if the file exist i want to get an error back
# + - Updating (read/write) # updating the file 
# t - Text (default)
# b - Binary  # for binary fiiles like images 

## The most common scenario is to read from a file
# Reading a file :

# stream = open('demo.txt') # by default it is txt file and the mode assuming that I need to read the file 
print(stream.readable()) # Can we read ?
print(stream.readable(1)) # Read the first charachter 
print(stream.readline()) # read a line 
stream.close() # Close the stream  

# How to write to a file ?
# here we specify the mode 'w' for writing and t cause I am writing a text to the file (the default mode is 'r' reading)
stream = open('output.txt', 'wt') # write txt 
stream.write('H') # using the write() method to one or more charachters # write a single string 
stream.writelines(['ello', 'World']) # write multiple strings
stream.write('\n') # write new line 

names = ['Ali', 'Hani'] # You can creat a list of strings and pass it to the writelines 
stream.writelines(names) # write to the file the name list 

stream.close() # close the stream and flush the data

## Managing the stream :
# You do not actually write to the file, you write to a file stream and then that stream goes to the file 

stream = open('output.txt', 'wt')
stream.write('demo!') # I am writing this to the file stream 
# You can use the seek command to reposition where you are in the stream, so moving the cursor around for where things are being written 
stream.seek(0) # put the cursor right back at the beginning of the stream 
stream.write('cool') # So here if we do another write it is gonna overwrite cool instead of demo (so the demo word got overwritten by cool)
# Flush command, flushes the data of the stream to the file 
stream.flush() # write the data to file 
stream.close() # flush and close the stream 



