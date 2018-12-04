class Quixel:
    """
    Quixel is light weight open source project for text content analysis semantically.
    """
    def train_model(self, corpus=self.corpus):
        """
        Train your own model instead of using default.
        :param corpus: corpus is directory data set for learning of model.
        :return: path to trained model.
        """
        pass

    def predict(self, content, model=self.quixel_model):
        """
        Does prediction using model on given text content.
        :param content: your text content on which you want analysis.
        :param model: model either your own trained or default. default is set to quixel model.
        :return: matrix will be predictions.
        """
        pass

    def load_model(self, path):
        """
        Load model to quixel internal system.
        :param path: path to model.
        :return: loaded model.
        """
        pass
