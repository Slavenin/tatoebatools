from datetime import datetime

class UserSentence:
    """Contains user-verified suggestion"""

    def __init__(
        self, username, sentence_id, check, date_added, date_last_modified
    ):
        # the id of the sentence
        self._usr = username
        self._sid = sentence_id
        self._check = check
        self._dtad = date_added
        self._dtlm = date_last_modified

    @property
    def username(self):
        """Get the name of the user who have this language skill"""
        return self._usr
    
    @property
    def sentence_id(self):
        """Get the id of the sentence of this transcription"""
        return int(self._sid)

    @property
    def check(self):
        """Get the name of the user who have this language skill"""
        return self._check

    @property
    def date_added(self):
        """Get the date of the addition of the sentence."""
        try:
            dt = datetime.strptime(self._dtad, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            dt = None
        finally:
            return dt

    @property
    def date_last_modified(self):
        """Get the date of the last modification of the sentence."""
        try:
            dt = datetime.strptime(self._dtlm, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            dt = None
        finally:
            return dt
