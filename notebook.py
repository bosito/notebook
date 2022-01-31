class Book:
    def __init__(self) -> None:
        self.list_notes = []
        self.List_type = []

    def create_note(self, note):
        list_notes = self.get_all_notes()
        note["id"] = (len(list_notes) + 1)
        self.List_type.append(note["type"])
        list_notes.append(note)
        return note

    def delete_note(self, index):
        notes = self.get_all_notes()

    def update_note(self, index):
        notes = self.get_all_notes()
        pass

    def find_note(self, index):
        notes = self.get_all_notes()
        pass

    def get_all_notes(self):
        return self.list_notes
