class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:  # The first jump must be 1 unit
            return False
        
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        
        for stone in stones:
            for step in dp[stone]:
                for next_step in (step - 1, step, step + 1):
                    if next_step > 0 and stone + next_step in dp:
                        dp[stone + next_step].add(next_step)
        
        return bool(dp[stones[-1]])