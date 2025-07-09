from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

    @classmethod
    def choices(cls):
        return [
            (cls.PENDING, "Pending"),
            (cls.IN_PROGRESS, "In Progress"),
            (cls.COMPLETED, "Completed"),
        ]

class TaskPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

    @classmethod
    def choices(cls):
        return [
            (cls.LOW, "Low"),
            (cls.MEDIUM, "Medium"),
            (cls.HIGH, "High"),
        ]
