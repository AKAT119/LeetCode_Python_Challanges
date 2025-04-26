
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() #to remove the spaces in leading and tailing of the string 
        words = s.split()
        words.reverse()
        sentence = ' '.join(words)

        return sentence







sol = Solution()
s = "the sky is blue"
print(sol.reverseWords(s))  # Output: "blue is sky the"

