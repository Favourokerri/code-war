#write me a function stringy that takes a size and returns a string of alternating 1s and 0s.
#the string should start with a 1.
#a string with size 6 should return :'101010'.
#with size 4 should return : '1010'.
#with size 12 should return : '101010101010'.

def stringy(size):
    new_str = ''
    while size != 0:
        if new_str == '':
            new_str += '1'
        elif new_str[-1] == '1':
            new_str += '0'
        else:
            new_str += '1'
        size = size -1
    return new_str

s = stringy(65)
print(s)