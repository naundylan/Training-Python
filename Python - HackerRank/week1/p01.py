# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

n = int(input())

if n%2!=0:
    print("Weird")
else:
    if n in range(2, 5+1):
        print("Not Weird")
    elif n in range(6, 20+1):
        print("Weird")
    else:
        print("Not Weird")