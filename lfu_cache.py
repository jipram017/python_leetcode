# Leetcode 460 - LFU Cache
# Level: HARD
# O(1) for get and set, O(N) space

from collections import defaultdict, OrderedDict

class MyDict(OrderedDict):
    def __missing__(self, key):
        val = self[key] = MyDict()
        return val
    
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.values = defaultdict(int)
        self.counts = defaultdict(int)
        self.frequencies = MyDict()
        self.minimum = 0

    def get(self, key: int) -> int:
        if key in self.values:
            count = self.counts[key]
            self.counts[key] = count + 1
            del self.frequencies[count][key]
            if len(self.frequencies[count]) == 0 and count == self.minimum:
                self.minimum += 1
                del self.frequencies[count]
            
            self.frequencies[count + 1][key] = self.values[key]
            return self.values[key]
        
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.values:
            self.values[key] = value
            self.get(key)
            return
        
        if len(self.values) >= self.capacity:
            evit = list(self.frequencies[minimum].items())[0][0]
            del self.frequencies[self.minimum][evit]
            del self.counts[evit]
            del self.values[evit]
        
        self.counts[key] = 1
        self.values[key] = value
        self.frequencies[1][key] = value
        self.minimum = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Driver code
if __name__ == '__main__':
    LFUCache lfu = new LFUCache(2);
    lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
    lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
    lfu.get(1);      // return 1
                     // cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                     // cache=[3,1], cnt(3)=1, cnt(1)=2
    lfu.get(2);      // return -1 (not found)
    lfu.get(3);      // return 3
                     // cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                     // cache=[4,3], cnt(4)=1, cnt(3)=2
    lfu.get(1);      // return -1 (not found)
    lfu.get(3);      // return 3
                     // cache=[3,4], cnt(4)=1, cnt(3)=3
    lfu.get(4);      // return 4
                     // cache=[3,4], cnt(4)=2, cnt(3)=3