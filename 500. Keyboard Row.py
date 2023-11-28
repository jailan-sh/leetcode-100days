class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
        row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
        result = []
        
        for word in words:
            new = word.lower()
            if new[0] in row1:
                for i in range(len(new)):
                    if new[i] not in row1:
                        break
                else:
                    result.append(word)
            elif new[0] in row2:
                for i in range(len(new)):
                    if new[i] not in row2:
                        break
                else:
                    result.append(word)
            elif new[0] in row3:
                for i in range(len(new)):
                    if new[i] not in row3:
                        break
                else:
                    result.append(word)
        return result
