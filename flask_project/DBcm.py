import mysql.connector


class UseDatabase():
    def __init__(self, config_params: dict) -> None:
        self.configuration = config_params

    def __enter__(self):
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = conn.cursor #self because it's also needed in the __exit__

        return cursor
