fp = open('some_data.txt', 'w') #open defaults to read. 'w' enables write mode.

fp.write("Hello world") #writes to file. Can only write strings to file. To write anything else, must turn them into strings.
fp.write("More words that go to my file.") #Puts everything together into file without line breaks or spaces. Can put in f-strings!

#Running this multiple times replaces the file instead of repeating the lines over and over.



fp.close()

fp = open('some_data.txt', 'a') #Append mode. Goes to the end of the file. Can work with new file. May be best practices to save work.
fp.write("\nThis stuff was appended to the file.")

#There is no fp.append. Use fp.write, but just make sure it's in append mode.