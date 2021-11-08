# when you write to a stream file you need to remember that you are not actually writing to the file 
# you can actually move up and down around the file stream as you are writing to it.
# using seek command it helps to repeostion where are you ariting in the file stream.

# create a file and open a file manage to write text :

stream = open('./manage.txt', 'wt')

# write the word demo! to the file :
stream.write('demo!')

# Move back to the beginning of the file :
stream.seek(0)

# write again to the file stream where you are at the position Zero 
# This will overwrite the cool word instead of demo 
stream.write('cool')

# Flush the stream file contents to the file buffer  (Flush it takes the contents of the file stream to the actual file)
stream.flush()

# flush the stream file and close :
stream.close()


