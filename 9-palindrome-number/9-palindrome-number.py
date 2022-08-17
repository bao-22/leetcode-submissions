class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            res = list(map(int, str(x)))
            result = True
            for i in range(round(len(res)/2)):
                if res[i] != res[len(res)-1-i]:
                    result = False
                    break
            return result
        else:
            return False
        