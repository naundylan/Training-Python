"""
S(n) = (n*(u1+un)) / 2 tổng dãy só cấp số cộng
un = u1 + (n-1)*d 
"""

n, u1, d = map(int, input().split())

un = u1 + (n-1)*d

print((n*(u1+un))//2)