import nltk
import numpy as np
import wikipedia
from os import path
from wordcloud import WordCloud
from nltk.corpus import stopwords

CONCEPT_TAGS = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
CURRDIR = path.dirname(__file__)


class Quixel:
    """
    Quixel is light weight open source project for text content analysis semantically.
    """

    def analyze(self, content):
        """
        Run analysis on given text content.
        :param content: your text content on which you want analysis.
        :return: None.
        """
        words = self.remove_stop_words(content)
        words = self.select_relevant_pos_words(words)
        concepts = [self.get_wiki_content(word) for word in words]
        self.create_wordcloud(concepts)

    def remove_stop_words(self, content):
        """
        Removes stop words from text.
        :param content: your text content
        :return: list of filtered words
        """
        stop_words = set(stopwords.words('english'))
        words = nltk.word_tokenize(content)
        words = [word.lower() for word in words if word.isalpha()]
        return [w for w in words if not w in stop_words]

    def select_relevant_pos_words(self, words):
        """
        Does part of speech tagging and select relevant words.
        :param words: list of words after stop words removed
        :return: list of expected concepts in text
        """
        tagged_words = nltk.pos_tag(words)
        return [word for word, tag in tagged_words if tag in CONCEPT_TAGS]

    def get_wiki_content(self, concept):
        """
        Generate content on concept with the help of wikipedia.
        :param concept: expected concept
        :return: list of content from wikipedia regarding each concept
        """
        concepts = []
        sub_concept = wikipedia.search(concept)
        for topic in sub_concept:
            try:
                concepts.append(wikipedia.summary(topic))
            except:
                print(f"Too broad concept {topic}, skipping...")
        return concepts

    def create_wordcloud(self, text):
        """
        Generate word cloud or wordle.
        :param text: list of content regarding each concept
        :return: None
        """
        mask = np.array(Image.open(path.join(CURRDIR, "cloud.png")))
        wc = WordCloud(background_color="white",
                       max_words=200,
                       mask=mask)
        wc.generate(text)
        wc.to_file(path.join(CURRDIR, "wordle.png"))



q = Quixel()
q.analyze("This is a sample sentence, showing off the stop words filtration.")
