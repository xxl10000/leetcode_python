#
# @lc app=leetcode.cn id=391 lang=python3
#
# [391] 完美矩形
#

# @lc code=start
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        X1, Y1, X2, Y2 = rectangles[0]
        sSum = 0
        s = set()
        for x1, y1, x2, y2 in (rectangles):
            sSum += (x2 - x1 ) * (y2 - y1)
            X1 = min(X1, x1)
            Y1 = min(Y1, y1)
            X2 = max(X2, x2)
            Y2 = max(Y2, y2)
            vertex =( (x1, y1), (x2, y1),(x2, y2),(x1, y2))
            for v in vertex:
                s.add(v) if v not in s else s.remove(v)
        # print(sSum)
        # print((X2 - X1) * (Y2 - Y1))  
        # print(s)
        if sSum != (X2 - X1) * (Y2 - Y1): return False
        if len(s) != 4: return False
        if (X1, Y1) not in s or (X2, Y1) not in s or (X1, Y2) not in s or (X2, Y2) not in s:
            return False
        return True
        
            
# @lc code=end

