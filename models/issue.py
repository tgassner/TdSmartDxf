from dataclasses import dataclass


@dataclass
class Issue:
    severity: str   # "INFO" | "WARNING" | "ERROR"
    message: str