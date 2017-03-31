from classes import Task
import datetime

import yaml
from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def get_dataset(filename):
    try:
        with open(filename, 'rt', encoding='utf-8') as input:
            try:
                package = load(input, Loader=Loader)
                dataset = package.get('dataset')
                if not isinstance(dataset, list):
                    raise ValueError('wrong format')
                yield from dataset
            except yaml.YAMLError:
                raise yaml.YAMLError
    except OSError:
        raise OSError


dataset = list(get_dataset("dataset.yml"))

class WSGIApplication:
    default_headers = [
        ('Content-Type', 'text/html'),
        ('Server', 'WSGIExample/1.0'),
    ]

    def __init__(self, environment, start_response):
        self.environment = environment
        self.start_response = start_response

    def __iter__(self):
        msg = ''
        self.start_response('200 OK', self.default_headers)

        date = datetime.date.today()
        for data in dataset:
            task = Task(data[0], data[2], data[1])
            if (task.remaining < datetime.timedelta(3)) and task.state == 'in_progress':
                msg += task.title + '<br>'

        yield msg.encode('utf-8')


from wsgiref.simple_server import make_server

http_server = make_server('127.0.0.1', 12345, WSGIApplication)
while True:
    http_server.handle_request()
