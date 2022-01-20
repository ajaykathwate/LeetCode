from math import ceil
class Solution:
	def minEatingSpeed(self, piles: List[int], h: int) -> int:
		low, high = 1, max(piles)

		while low<high:
			hours = 0 
			k = low + (high-low) // 2
			for i in piles:
				hours += ceil(i/k) # even if she finishes, she waits until the hour is over to eat another pile so roundup 

			if hours <= h: # koko eats too fast, slow down
				high = k

			if hours > h: # koko eats too slow, speed up
				low = k + 1 

		return low