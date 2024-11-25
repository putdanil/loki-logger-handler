import json


class _LokiRequestEncoder(json.JSONEncoder):
    def default(self, obj):
        print("Data being serialized:", obj)  # Отладка
        if isinstance(obj, Streams):
            return {"streams": [stream.__dict__ for stream in obj.streams]}
        elif isinstance(obj, set):  # Добавлено: обработка множеств
            obj= list(obj)
        if isinstance(obj, list):
            # Рекурсивно сериализуем каждый элемент списка
            obj = [self.default(item) if isinstance(item, (Streams, Stream)) else item for item in obj]
        return json.JSONEncoder.default(self, obj)


class Streams:
    def __init__(self, streams=None):
        if streams is None:
            streams = []
        self.streams = streams

    def addStream(self, stream):
        self.streams.append(stream)

    def addStreams(self, streams):
        self.streams = streams

    def serialize(self):
        return json.dumps(self, cls=_LokiRequestEncoder)
