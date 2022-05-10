from string import punctuation

import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import STOPWORDS, ImageColorGenerator, WordCloud


def clean_text(text):
    # nltk.download('punkt')
    # nltk.download('stopwords')
    # nltk.download('wordnet')
    # nltk.download('averaged_perceptron_tagger') # for POS_tag
    # nltk.download('maxent_ne_chunker') # for NER
    # nltk.download('words') # for NER
    # nltk.download('omw-1.4')

    words = word_tokenize(text)
    words = list(map(str.lower, words))
    stop_words = set(stopwords.words('danish'))
    words = [w for w in words if w not in stop_words and w not in punctuation]
    return ' '.join(words)

def do_wordcloud(text):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    with open('text.txt', 'r') as f:
        text = f.readlines()
        text = ''.join(text)

    do_wordcloud(text)
    text = clean_text(text)
    do_wordcloud(text)
