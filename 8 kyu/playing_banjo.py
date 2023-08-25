#Create a function which answers the question "Are you playing banjo?".
#If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo" 
    else:
        return name + " does not play banjo"