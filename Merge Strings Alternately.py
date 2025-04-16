class Solution(object):
    def mergeAlternately(self, word1, word2):
    
        p_w1 = 0
        p_w2 = 0
        result = []
        len_w1 = len(word1)
        len_w2 = len(word2)
        while p_w1 < len_w1 and p_w2 < len_w2:
            result.append(word1[p_w1])
            result.append(word2[p_w2])
            p_w1+=1 
            p_w2+=1
        result.append(word1[p_w1:])
        result.append(word2[p_w2:])
        return "".join(result)




