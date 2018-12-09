from __future__ import absolute_import

import os
import nltk
import inspect
import wikipedia
import numpy as np
from PIL import Image
from wordcloud import WordCloud
from nltk.corpus import stopwords

CONCEPT_TAGS = ['NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'JJR', 'JJS', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
PATH_TO_SAVE_IMG = os.path.dirname(os.path.abspath((inspect.stack()[1])[1]))
CURRDIR = os.path.dirname(__file__)


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
        for topic in sub_concept[:10]:  # selecting only 1st 10 results
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
        text = ' '.join(f"{word}" for word in text)
        mask = np.array(Image.open(os.path.join(CURRDIR, "cloud.png")))
        wc = WordCloud(background_color="white",
                       max_words=200,
                       mask=mask)
        wc.generate(text)
        wc.to_file(PATH_TO_SAVE_IMG, "wordle.png")
