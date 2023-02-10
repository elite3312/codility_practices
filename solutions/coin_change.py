

from cmath import inf


def solution(denominations:list,amount:int):
  ''' Let dp[i, j] be the minimum number of coins needed to pay the amount j if we
  use the set containing the i smallest denominations.
  '''
  dp=[[0]*(amount+1) for i in range(len(denominations)+1)]
  for i in range(amount+1 ):#any amount greater than 0 is unreachable for empty denom set
    dp[0][i]=inf
  for i in range(len(dp)):#we need 0 coins for the amount 0
    dp[i][0]=0
  for i in range(1,len(denominations)+1):
    for j in range(0,denominations[i-1]):
      dp[i][j]=dp[i-1][j]
    vis_dp(dp)
    
    for j in range(denominations[i-1],amount+1):
      dp[i][j]=min(dp[i][j-denominations[i-1]]+1,dp[i-1][j])

  return dp
def vis_dp(dp):
  for i in range(0,len(d)+1):
      print(dp[i])
  
if __name__ == "__main__":
    d=[1,3,4]
    amount=6
    dp=solution(d,amount)
    vis_dp(dp)