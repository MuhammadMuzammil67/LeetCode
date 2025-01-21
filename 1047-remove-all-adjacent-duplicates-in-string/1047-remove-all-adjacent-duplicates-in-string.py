class Solution:
    def removeDuplicates(self, s: str) -> str:
        myStack = []
        for i in s:
            if len(myStack) != 0 and myStack[-1] == i:
                myStack.pop()
            else:
                myStack.append(i)
        return "".join(myStack)