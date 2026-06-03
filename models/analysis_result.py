from dataclasses import dataclass, field
from models.issue import Issue

@dataclass
class AnalysisResult:

    total_entities: int = 0

    entity_counts: dict[str, int] = field(default_factory=dict)

    layers: set[str] = field(default_factory=set)

    text_count: int = 0
    dimension_count: int = 0

    closed_polylines: int = 0
    open_polylines: int = 0

    zero_length_lines: int = 0

    duplicate_lines: int = 0

    issues: list[Issue] = field(default_factory=list)