def sort_on(dict):
  return dict['count']

def main():
  file_path = "books/frankenstein.txt"
  with open(file_path) as f:
    char_counts = {}
    char_count_list = []
    file_contents = f.read().lower()
    words = file_contents.split()
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
    print(f"{len(words)} found in the document\n")
    for entry in char_count_list:
      print(f"The '{entry["char"]}' character was found {entry["count"]} times")
    print("--- End report ---")

main()