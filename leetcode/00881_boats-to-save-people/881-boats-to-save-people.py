class Solution:
    # time O(NlogN), space O(1)
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        curr_people = 0
        curr_weight = 0
        l, r = 0, len(people) - 1

        while l <= r:
            if curr_weight + people[r] <= limit and curr_people < 2:
                curr_people += 1
                curr_weight += people[r]
                r -= 1
                continue
            elif curr_weight + people[l] <= limit and curr_people < 2:
                curr_people += 1
                curr_weight += people[l]
                l += 1
                continue

            curr_people = 0
            curr_weight = 0
            count += 1

        if curr_weight > 0:
            count += 1

        return count
