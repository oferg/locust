from .core import WebLocust, Locust, TaskSet, task, mod_context
from .exception import InterruptTaskSet, ResponseError, RescheduleTaskImmediately
from .config import configure

__version__ = "0.8dr1"
