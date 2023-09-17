```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

def process_natural_language(user_requirements):
    """
    Function to process natural language in user requirements.
    """
    stop_words = set(stopwords.words('english'))

    # Tokenize the user requirements
    tokenized = sent_tokenize(user_requirements)

    for i in tokenized:
        # Word tokenizers is used to find the words and punctuation in a string
        wordsList = nltk.word_tokenize(i)

        # Removing stop words from wordList
        wordsList = [w for w in wordsList if not w in stop_words]

        # Using a Tagger which is part-of-speech tagger or POS-tagger
        tagged = nltk.pos_tag(wordsList)

    return tagged
```