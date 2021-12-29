import mysql.connector


class UseDatabase():
    def __init__(self, config_params: dict) -> None:
        self.configuration = config_params

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()  # self because it's also needed in the __exit__

        return self.cursor

    def __exit__(self, *args, **kwargs) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
