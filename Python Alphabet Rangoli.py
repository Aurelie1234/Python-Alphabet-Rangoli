 for i in (*range(size), *range(size - 2, -1, -1)):
# run from 0 to size then back down to zero
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
# create a string of letters from the last to a (such as e-d-c)
        print((s+s[::-1][1:]).center(size*4-3, '-'))
#print the line with a form such as  '----e-d-c-d-e----'
