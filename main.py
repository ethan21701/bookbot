import sys
from stats import count_words , character_count , sort

def get_book_text(book_path):
    with open(sys.argv[1],'r') as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(count_words(text))
        print("------- Character Count -------")
        for item in sort(character_count(text)):
            print((f"{item['char']}: {item['num']}"))
        print("============= END ===============")

  


    

    





main()


