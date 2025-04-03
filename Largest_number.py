def find_largest(lst):
  if not lst:
      return None  
  largest = lst[0]
  for number in lst:
      if number > largest:
          largest = number
  return largest

numbers = [1,6,4,8,9,4,3]
print(find_largest(numbers))
