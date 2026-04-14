class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for i in range(len(nums)+1)]
        res = []

        countMap = {}

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        for c, i in countMap.items():
            freqs[i].append(c)

        for i in range(len(freqs) -1, 0, -1):
            for num in freqs[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
