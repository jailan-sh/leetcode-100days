class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        mydic = {}
        mylist = []
        for i in nums:
            if i not in mydic:
                mydic[i] = 1
            else:
                mydic[i] += 1
    #  mydic[i] = mydic.get(i, 0) + 1
        sorted_dic = sorted(mydic.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            mylist.append(sorted_dic[i][0])
        return mylist
       
            