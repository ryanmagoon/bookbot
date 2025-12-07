from stats import get_num_words

def sort_on(dict):
  return dict['count']

def main():
  file_path = "books/frankenstein.txt"
  with open(file_path) as f:
    char_counts = {}
    char_count_list = []
    file_contents = f.read().lower()
    num_words = get_num_words(file_contents)
    chars = "".join(file_contents)

    for char in chars:
      if char.isalpha():
        if char in char_counts:
          char_counts[char] += 1
        else:
          char_counts[char] = 1

    for char, count in char_counts.items():
      char_count_list.append({"char": char, "count": count})
    
    char_count_list.sort(key=sort_on, reverse=True)

    print(f"--- Begin report of {file_path} ---")
    print(f"Found {num_words} total words\n")
    for entry in char_count_list:
      print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()