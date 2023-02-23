#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start
class RandomizedSet:

    def __init__(self):
        self.l = list()
        self.valToIdx = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.valToIdx:
            return False
        else:
            self.l.append(val)
            self.valToIdx[val] = len(self.l) - 1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.valToIdx:
            return False
        else:
            idx = self.valToIdx[val]
            lastIdx, lastVal = len(self.l) - 1, self.l[len(self.l) - 1]
            
            # self.valToIdx[lastVal] = idx
            # self.l[idx] = lastVal
            # self.valToIdx.pop(val)
            # self.l.pop()
            
            #使用上面的方法也更明了,如果用下面，注意相等时候的情况。
            if val == lastVal:
                self.l.pop()
                self.valToIdx.pop(val)
            else:
                self.valToIdx.pop(val)
                self.valToIdx.pop(lastVal)
                self.l[idx] = lastVal
                self.valToIdx[lastVal] = idx
                self.l.pop()
                
            return True

    def getRandom(self) -> int:
        return choice(self.l)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

