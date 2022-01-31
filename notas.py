import datetime

class Note:
    def __init__(self, title: str = '', message: str = '', type: str = 0) -> None:
        self.title = title
        self.message = message
        self.date = str(datetime.datetime.today())
        self.type = type

    def get_note(self):
        data_note = {
            "title": self.title,
            "message": self.message,
            "type": self.type,
            "date": self.date
        }

        return data_note
