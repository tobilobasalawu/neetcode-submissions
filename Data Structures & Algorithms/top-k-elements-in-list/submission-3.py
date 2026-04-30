class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = 0
        answer = []

        for i in nums:
            if i in hashmap:
                hashmap[i] = hashmap[i] + 1
            else:
                hashmap[i] = 1

        while count < k:
            maxi= max(hashmap, key=hashmap.get)
            answer.append(maxi)
            count += 1
            hashmap.pop(maxi)

        return answer