class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canBeShipped(self, capacity):
            daysT = 1
            cap = 0
            print("capacity=",capacity)

            for i in weights:
                if i+ cap > capacity:
                    cap =0
                    daysT += 1
                else:
                    cap += i

            return daysT <= days

        l,r = max(weights), sum(weights)
        print(l, r)

        while l<= r:
            m = l + (r-l)//2
            print(m)
            if canBeShipped(m):
                r = m-1
            else:
                l = m+1

        return l

