from stats import number_of_chars
from stats import get_num_words
import sys

def main():
	#filepath = "/home/Aceb/Desktop/bookbot/bookbot/books/frankenstein.txt"
	if len(sys.argv) == 2:
		x = get_num_words(sys.argv[1])

		print("========== BOOKBOT ==========")
		print("Analyzing book found at books/frankenstein.txt...")
		print("------------ Word Count ------------")
		print(f"Found {x} total words")
		print("--------- Character Count --------")
		number_of_chars(sys.argv[1])
		print("========== END ============")
	else:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
main()
