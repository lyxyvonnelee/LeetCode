class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, max_fruit = 0, 0
        basket = defaultdict(int)
        for end in range(len(fruits)):
            basket[fruits[end]] += 1
            while len(basket) > 2:
                basket[fruits[start]] -= 1
                if basket[fruits[start]] == 0:
                    del(basket[fruits[start]])
                start += 1
            max_fruit = max(max_fruit, end-start+1)
        return max_fruit


