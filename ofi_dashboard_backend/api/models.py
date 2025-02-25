from django.db import models
from .constants import ACTIVITY_CHOICES

class Case(models.Model):
    """
    Represents a case in the system.

    Attributes:
        id (AutoField): The primary key for the case.
    """
    id = models.AutoField(primary_key=True)

    def __str__(self):
        """
        Returns a string representation of the case.
        """
        return f"Case {self.id}"

class Activity(models.Model):
    """
    Represents an activity related to a case.

    Attributes:
        case (ForeignKey): The case to which the activity is related.
        timestamp (DateTimeField): The timestamp of the activity.
        name (CharField): The name of the activity, chosen from predefined choices.
    """
    case = models.ForeignKey(Case, related_name='activities', on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    name = models.CharField(max_length=25, choices=ACTIVITY_CHOICES)

    def __str__(self):
        """
        Returns a string representation of the activity.
        """
        return f"{self.case.id} - {self.name} at {self.timestamp}"