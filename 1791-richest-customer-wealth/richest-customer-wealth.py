class Solution(object):
    def maximumWealth(self, accounts):
        max_wealth = 0
        
        for customer in accounts:
            current_wealth = 0
            
            
            for money in customer:
                current_wealth += money
                
            if current_wealth > max_wealth:
                max_wealth = current_wealth
                
        return max_wealth
