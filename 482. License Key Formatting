class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k > len(s):
            return s.replace("-","").upper()
        items = []
        s = s.replace("-",'').upper()
        part =  len(s) % k
        if part != 0:
            items.append(s[:part])
        i = part
        while i < len(s):
            items.append(s[i:i+k])
            i += k

        return "-".join(items)
