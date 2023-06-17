from pocketbase.client import Record 

class User(Record):

    username: str
    password: str

    def load(self, data: dict):
        super().load(data)
        self.username = data.get('username', '')
        self.password = data.get('password', '')

        return self