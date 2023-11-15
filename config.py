from decouple import config


class Config:  # Класс набор конфигурационных данных (датакласс)
    TOKEN_BOT = config("TOKEN_BOT", cast=str)  # Функция, которая достает данные из файла .env; cast=str, чтобы вернуть нужный нам тип данных
