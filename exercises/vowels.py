def count_vowels(strings: str) -> int:
  vowels = "aeiou"
  count = 0

  for char in strings:
    if char in vowels:
      count+=1
  return count
word = input("Insert the word you want to count vowels: ")
print(f"The word {word} has {count_vowels(word)} vowels in total.")