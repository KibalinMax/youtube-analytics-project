import json
import os
from googleapiclient.discovery import build
import isodate

api_key: str = os.getenv('YT_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

def printj(dict_to_print: dict) -> None:
    """Выводит словарь в json-подобном удобном формате с отступами"""
    print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.channel_info = self.get_channel_info()
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.channel_desc = self.channel_info['items'][0]['snippet']['description']
        self.url = "https://www.youtube.com/channel/" + self.channel_info['items'][0]['snippet']['customUrl']
        self.subscribes = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API."""
        return youtube

    def get_channel_info(self):
        """Возвращает информацию о канале"""
        channel_id = self.__channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        return channel

    def to_json(self, filename):
        """Метод, сохраняющий в файл значения атрибутов экземпляра `Channel`"""
        channel_item = {
            "id канала": self.channel_id,
            "Название канала": self.title,
            "Описание канала": self.channel_desc,
            "Ссылка на канал": self.url,
            "Число подписчиков": self.subscribes,
            "Количество видео": self.video_count,
            "Количество просмотров": self.view_count
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(channel_item, file, indent=2, ensure_ascii=False)

    @property
    def channel_id(self):
        return self.__channel_id
