class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        cur_sum = 0
        
        for op in ops:
            if op == "+":
                right = stack.pop()
                left = stack[-1]
                stack.append(right) # returns right value
                
                cur_sum += left + right
                stack.append(left + right)
            
            elif op == "C":
                cur_sum -= stack.pop()
            elif op == "D":
                cur_sum += stack[-1] * 2 
                stack.append(stack[-1]*2)
            else:
                stack.append(int(op))
                cur_sum += stack[-1]
        return cur_sum