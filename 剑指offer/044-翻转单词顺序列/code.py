class Solution:
    def ReverseSentence(self, s):
        # write code here
        stack = [n for n in s.split(' ')]
        stack.reverse()
        return ' '.join(stack)

print(Solution().ReverseSentence("I am a student."))