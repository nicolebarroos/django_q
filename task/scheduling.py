from django.utils.timezone import now

from task.models import TaskMessage


def run_task():
    message = f"task execulted on {now().strftime('%Y-%m-%d %H:%M:%S')}"
    TaskMessage.objects.create(message=message)
