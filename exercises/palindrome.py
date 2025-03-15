def is_palindrome(string: str) -> bool:
  string = string.lower()
  left = 0
  right = len(string) - 1

  while left < right:
    if string[left] != string[right]:
      return False
    left += 1
    right -= 1
  return True
input_word = input("Enter a word: ")
if is_palindrome(input_word):
  print(f"{input_word} is a palindrome.")
else:
  print(f"{input_word} is not a palindrome.")