import collections


def find_all_substring(s,word):
    def find_correct_index(start):
        check_freq_word=collections.Counter()
        for i in range(start,start+unit_size*len(word),unit_size):
            part=s[i:i+unit_size]
            it = word_to_freq[part]
            if it == 0:
                return False
            check_freq_word[part]+=1
            if check_freq_word[part]>word_to_freq[part]:
                return False
        return True


    word_to_freq=collections.Counter(word)
    unit_size=len(word[0])
    return[i for i in range(len(s)-unit_size*len(word)+1) if find_correct_index(i)]


print(find_all_substring("abefcdefgh",["ef","cd"]))