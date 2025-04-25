class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s_list = list(s)  # Convert to list for mutability

        # Step 1: Collect indices and vowels
        indices = [i for i, char in enumerate(s) if char in vowels]
        vowels_char = [s[i] for i in indices]

        # Step 2: Reverse the vowels
        vowels_char.reverse()

        # Step 3: Put them back into the original string positions
        for i, char in zip(indices, vowels_char):
            s_list[i] = char
        return ''.join(s_list)

# Test
sol = Solution()
print(sol.reverseVowels("IceCreAm"))  # Output: "AceCreIm"
