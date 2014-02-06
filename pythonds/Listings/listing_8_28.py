def simpleMatcher(pattern, text):
    starti = 0      #tracks the start of each attempt
    i = 0           #index into text
    j = 0           #index into pattern
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i = i+1
            j = j+1
        else:
            starti = starti + 1    #shift to right
            i = starti
            j = 0

        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True

    if match:
        return i-j
    else:
        return -1
