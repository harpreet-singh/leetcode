class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lmax = []
        rmax = []
        lm = 0
        rm =0
        for i,val in enumerate(height):
            lmax.append(lm)
            rmax.append(rm)
            
            if lm < val:
                lm = val
            if rm < height[-i-1]:
                rm = height[-i-1]
        print(lmax)
        rmax = rmax[::-1]
        print(rmax)
        res = 0
        for i,val in enumerate(height):
            res+=max(0, min(lmax[i], rmax[i]) - val)
            
        return res
            
