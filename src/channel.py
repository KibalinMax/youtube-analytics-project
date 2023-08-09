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

    def __init__(self, channel_id: str, title: str, description: str, url: str, subscriber_count: int, video_count: int, view_count: int) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.title = title
        self.description = description
        self.url = url
        self.subscriber_count = subscriber_count
        self.video_count = video_count
        self.view_count = view_count

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_id = self.channel_id
        channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        printj(channel)

    def get_service(self):
        return youtube

    def to_json(self):
        json.dump(self.channel_id, self.title, self.description, self.url, self.subscriber_count, self.video_count, self.view_count)
