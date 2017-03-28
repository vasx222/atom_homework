import datetime

class Task:
    def __init__(self, title, estimate, state = "in_progress"):
        self.title = title
        self.state = state
        self.estimate = estimate

    def _remaining_getter(self):
        if self.state == "in_progress":
            return self.estimate - datetime.date.today()
        else:
            return 0
    remaining = property(_remaining_getter)

    def _is_failed_getter(self):
        return self.state == "in_progress" and self.estimate < datetime.date.today()
    is_failed = property(_is_failed_getter)
    
    def ready(self):
        self.state = "ready"

class Roadmap:
    def __init__(self, tasks = []):
        self.tasks = tasks

    def _today_getter(self):
        ls = []
        for task in self.tasks:
            if task.estimate == datetime.date.today():
                ls.append(task)
        return ls
    today = property(_today_getter)

    def filter(self, state = ""):
        ls = []
        for task in self.tasks:
            if task.state == state:
                ls.append(task)
        return ls

        
t = Task("my_title", datetime.date(2017, 4, 25))
r = Roadmap([t])
