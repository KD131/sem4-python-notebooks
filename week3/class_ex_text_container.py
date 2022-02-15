class TextContainer:
    def __init__(self, text):
        """"Text container with methods for counting stuff, and removing punctuation."""
        self.text = text

    def count_words(self):
        words = [word for word in self.text.split(" ") if word] # removes empty cells.
        print(f"Text contains {len(words)} words.")
        return len(words)

if __name__ == "__main__":
    tc = TextContainer("This is a  test.")
    print(tc.count_words())
