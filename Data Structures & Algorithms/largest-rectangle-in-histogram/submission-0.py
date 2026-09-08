class Solution:
    # first thoughts: naive approach: brute force all possible combinations
    # whats being repeated? finding min of [l, r]
    # prefix, suffix? can we do that?
    # not necessarily, b/c knowing the prefix/ suffix does not exactly tell you the min
    # of the element in the interval
    # whats another approach that you can think of?
    # well, the thing is that as we iterate, we'll have two rectangles
    # one being the current possible rectangle, which would be min * length so far
    # the other being thesecondlargest potential rectangle that we can use?
    # well now my mind is going to pointers. why?
    # well im thinking, we can have our right pointer go forward once each time
    # our left pointer points at the largest value possible.
    # once we hit a new largest value >= left value, we bring left pointer forward until we 
    # reach right pointer. issue: how do we know what the min is as we go forward?
    # well, wouldnt we have found that at 
    # by the hint, i know we have to apply a stack, but im not sure how. 
    # the only idea i have is
    # popping the list if we find an elem>= than the cur
    # which kind of makes sense? butim not sure how it works
    # ok well lets think of what happens when we find an elem larger than our left pointer.
    # okay well first, we know that since by assumption, left is max,
    # then as we shrink,there's no way for us to get a larger possiblerectangle
    # so that means we can use our right pointer to keep track ofthe min  (as it iterates up)
    # and when we find a new max,we set our min to that max, decreaes as r goes forward.
    # so  not really sure what the point of the stack is so much.

    # ISSUE: what if we had 7 1 6 6 6? if we iterated with those rules, then
    # we would nevre select the 6 6 6 
    # so cannot really do a greedy approach. 
    # what if instead, we popped if elem[i-1] < elem[i]? but this doesnt work,
    # b/c if we had 2 3 2, then we would miss the 2nd half of 2s. 
    # what if we only add elements if they are <= then cur top? and we store the index of the current
    # that might work better. 
    # okay yeah, b/c for 232, we wouldnt add 3, but we would add the 2, and we could calculate width with the is.
    # but for 71666, we still wouldn't touch 666 correctly. 
    # okay but whats the point of the stack? like what would we store?
    # and at this point, i think thats the important question. 
    # and i think that the stack would help by 

    # now im thinking that as we iterate over all possib

    # okay, from hint, we know that we're going to start by looking at each
    # block, and using that as our min, and we'll extend left and right.
    # doing this for all would be n^2, so yeah
    # well, what operations are we repeating?
    # equality checking. if we instead could calculate the bounds, that would be useful.
    # but how do we calculate the bounds?
    # prefix, suffix min/max?
    # wait, now im thinking, if we want to extend l, r,
    # and since for most leetcode, it doesnt make sense to look into left
    # we always look right b/c we\ve already claculated, but not left
    # so im thinking that as we iterate forward, we use our current pointer as min,
    # and for all prev values, we calcuate max. 
    # well firstly, we want the bound lookup to be O(1).
    # so that means that if we are using a queue, then the top element
    # has to be the correct bound for that element. 
    # but this can't necessarily be possible, b/c how would we know in advance what the best bound is?
    # and what would the point of the stack be?
    # well we also know that the recommended time comp is O(n). so 
    # that means as we pop/add elems, we can only do it once for each index.
    
    # okay after comig back to this problem after sleeping i have an idea
    # we will add in bars as we iterate through them.
    # how do you know when to pop, calculate a new rectangle?
    # okay i now realize i have no clue how to solve this problem.

    # my idea was that assuming i have somehow identified that its time to calculate a rectangle,
    # my stack would contain (height, index)
    # and i could assume that all the elems in my stack are >= my cur height until i reach one that isnt
    # but once i hit a rectangle that was less than my cur height, i would stop.
    # the issue is that if i have 123456, i could have 6, 10, 12, 10
    # so the process of adding to this stack would be like:
    # i add (1, 0), 
    # i add (2,1). since (1,0), i know that my max at this point is 
    # 2 * 1 (width * height)
    # i add (3,2).
    # i know my cur height at this point would be 2 for 2
    # i add (4,3). 
    # but i would preemptively stop at (3,2), so i would be 2 for 3.
    # okay so clearly this technique doesn't work, and we need to try popping further. 
    # okay but how?
    # lets think of the simplest case
    # 1, 2
    # 2, 2, 
    # 2, 1
    # in 1, 2 i would add on 1, calculate 1x1, add on 2, go back to 1, 
    # can we perhaps update stack values?
    # 1234
    # add on (1,0)
    # add on (2, 1)
    # add on (3,2), change 
    # add on (4, 3)
    # i just want an array that can store 


    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        m = 0
        for i, height in enumerate(heights):
            prev = i
            while len(s) > 0:
                if (s[-1][0] >= height):
                    m = max(m, s[-1][0]*(i-s[-1][1]))
                    prev = min(prev, s[-1][1])
                    s.pop(-1)
                else:
                    break
            s.append((height, prev))
        while (len(s) > 0):
            print(s[-1])
            m = max(m, s[-1][0]*(len(heights)-s[-1][1]))
            print(s[-1][0]*(len(heights)-s[-1][1]))
            s.pop(-1)
        return m