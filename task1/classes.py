import datetime

class Task:
    def __init__(self, title, estimate, state = 'in_progress'):
        if type(title) != type(''):
            raise TypeError('Incorrect type of title: ' + type(title))
        if type(estimate) != type(datetime.date.today()):
            raise TypeError('Incorrect type of estimate: ' + type(estimate))
        if type(state) != type(''):
            raise TypeError('Incorrect type of state: ' + type(state))
        if (state != 'in_progress') and (state != 'ready'):
            raise ValueError('Incorrect state')

        self.title = title
        self.estimate = estimate
        self.state = state

    remaining = property()

    @remaining.getter
    def remaining(self):
        delta = self.estimate - datetime.date.today()
        return datetime.timedelta(delta.days)

    is_failed = property()

    @is_failed.getter
    def is_failed(self):
        return (self.state == 'in_progress') and (self.estimate < datetime.date.today())

    def ready(self):
        self.state = 'ready'

    def __repr__(self):
        return "Task:\ntitle = %s\nstate = %s\nestimate = %s\n" % \
               (self.title, self.state, self.estimate)

class Roadmap:
    def __init__(self, tasks = []):
        self.tasks = tasks

    today = property()
    @today.getter
    def today(self):
        return [task for task in self.tasks
                if task.estimate == datetime.date.today()]

    def filter(self, state=""):
        return [task for task in self.tasks
                if task.state == state]
