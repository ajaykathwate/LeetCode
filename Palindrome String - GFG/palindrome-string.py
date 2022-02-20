#User function Template for python3
class Solution:
	def isPalindrome(self, s):
		# code here
		n = len(s)
		low = 0
		high = n - 1
		while high > low:
		    if s[low] != s[high]:
		        return 0
		    low += 1
		    high -= 1
	    return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPalindrome(S)
		print(answer)

# } Driver Code Ends