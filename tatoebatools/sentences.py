from datetime import datetime


class Sentence:
    """A sentence from the Tatoeba corpus"""

    def __init__(
        self,
        sentence_id,
        lang,
        text
    ):
        self._id = sentence_id
        self._lg = lang
        self._txt = text

    @property
    def sentence_id(self):
        """Get the id of the sentence."""
        return int(self._id)

    @property
    def lang(self):
        """Get the language of the sentence."""
        return self._lg

    @property
    def text(self):
        """Get the text of the sentence."""
        return self._txt

