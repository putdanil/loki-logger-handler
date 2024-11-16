import json


class _LokiRequestEncoder(json.JSONEncoder):
    def default(self, obj):
        print("Data being serialized:", obj)  # Отладка
        if isinstance(obj, Streams):
            return {
                "streams": [
                    {
                        key: list(value) if isinstance(value, set) else value
                        for key, value in stream.__dict__.items()
                    }
                    for stream in obj.streams
                ]
            }
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
