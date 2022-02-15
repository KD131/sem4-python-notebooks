import string

class TextContainer:

    def __init__(self, text):
        """"Text container with methods for counting stuff, and removing punctuation."""
        self.text = text

    def count_words(self):
        words = [word for word in self.text.split(" ") if word] # removes empty cells.
        print(f"Text contains {len(words)} words.")
        return len(words)
    
    def count_chars(self):
        print(f"Text contains {len(self.text)} characters.")
        return len(self.text)
    
    def count_ascii(self):
        # letters = [char for char in self.text if char in string.ascii_letters]
        # print(f"Text contains {len(letters)} ASCII letters.")
        # return len(letters)
        ascii_count = sum(c in string.ascii_letters for c in self.text)
        # better. could be used for other methods as well.
        print(f"Text contains {ascii_count} ASCII letters.")
        return ascii_count

    def remove_punctuation(self):
        # self.text = "".join([char for char in self.text if char not in string.punctuation])
        # for c in self.text:
        #     if c in string.punctuation:
        #         self.text = self.text.replace(c, "")
        for c in string.punctuation:
            self.text = self.text.replace(c, "")
        # 3 different ways of removing punctuation.
        print("Punctuation removed.")
        return self.text

if __name__ == "__main__":
    tc = TextContainer("  This is   a test.  ")
    print("Original text:", tc.text)
    print(tc.count_words())
    print(tc.count_chars())
    print(tc.count_ascii())
    print(tc.remove_punctuation())
