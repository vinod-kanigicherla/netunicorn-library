from netunicorn.library.tasks.tasks_utils import subprocess_run
from netunicorn.base import Task, Result


class TsharkCommand(Task):
    requirements = ["apt-get install -y tshark"]

    def __init__(self, command: list[str], *args, **kwargs):
        self.command = command
        super().__init__(*args, **kwargs)

    def run(self) -> Result:
        return subprocess_run(self.command)
