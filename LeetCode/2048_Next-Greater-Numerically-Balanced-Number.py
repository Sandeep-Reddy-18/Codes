class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBalance(number):
            number_str = str(number)
            counts = {}
            for i in number_str:
                if i in counts:
                    counts[i] += 1 
                else:
                    counts[i] = 1

            
            for i in counts:
                if int(i) != counts[i]:
                    return False

            return True

        n+=1
        while not isBalance(n):
            n+=1
        
        return n



