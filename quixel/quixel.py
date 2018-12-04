import wikipedia
import wordcloud.wordcloud

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
        sub_topics = wikipedia.search(content)
        sub_topic_summary = []
        for topic in sub_topics:
            sub_topic_summary.append(wikipedia.summary(topic))
        print(sub_topic_summary)


q = Quixel()
q.analyze("facebook")
