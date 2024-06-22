

def isStrobogrammatic( num: str):

  rotated = {"0":"0", "1":"1", "6":"9" , "9":"6", "8":"8" }

  r = len(num)-1
  l = 0

  while (l<=r):
      if num[r] not in rotated:
          return False
      if rotated[num[r]] != num[l]:
          return False
      r -= 1
      l += 1
  return True

print(isStrobogrammatic("69"))

