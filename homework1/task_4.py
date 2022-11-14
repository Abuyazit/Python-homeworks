def l_substr(x):
    longest_seq = ""
    cur_seq = x[0]
    for i in range(len(x)-1):
        if x[i] == x[i+1]:
            cur_seq += x[i]
        else:
            cur_seq = x[i]
        if len(cur_seq) > len(longest_seq):
            longest_seq = cur_seq
    return longest_seq
print(l_substr("a"))
assert(l_substr("a")) == 'a'
assert(l_substr("aa")) == 'aa'
assert(l_substr("abb")) == 'bb'
assert(l_substr("hellloo worldd")) == 'lll'
assert(l_substr("aaabbbbbaabbccaaaaaaaaa")) == 'aaaaaaaaa'
assert(l_substr("4512451111111111111111111111111111111111111111111122222222222223333")) == '11111111111111111111111111111111111111111111'

    

    
