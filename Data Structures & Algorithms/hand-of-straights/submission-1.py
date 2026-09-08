class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        hand.sort()
        print(hand)
        for num in hand:
            if count[num] > 0:
                for i in range(num, num+groupSize):
                    if count[i] <= 0:
                        return False
                    count[i] -= 1
        return True