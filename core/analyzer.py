import ezdxf

from models.analysis_result import AnalysisResult
from core.geometry.polyline_utils import is_closed_polyline
from core.geometry.line_utils import is_zero_length_line
from core.geometry.duplicate_detector import normalize_line
from models.issue import Issue

class DxfAnalyzer:

    def analyze(self, filename: str) -> AnalysisResult:

        doc = ezdxf.readfile(filename)
        msp = doc.modelspace()

        result = AnalysisResult()

        seen_segments = set()

        for entity in msp:

            result.total_entities += 1

            entity_type = entity.dxftype()

            result.entity_counts[entity_type] = (
                result.entity_counts.get(entity_type, 0) + 1
            )

            result.layers.add(entity.dxf.layer)

            match entity_type:

                case "TEXT" | "MTEXT":
                    result.text_count += 1

                case "DIMENSION":
                    result.dimension_count += 1

                case "LWPOLYLINE" | "POLYLINE":
                    if is_closed_polyline(entity):
                        result.closed_polylines += 1
                    else:
                        result.open_polylines += 1

                case "LINE":
                    if is_zero_length_line(entity):
                        result.zero_length_lines += 1
                    key = normalize_line(
                        entity.dxf.start,
                        entity.dxf.end
                    )

                    if key in seen_segments:
                        result.duplicate_lines += 1
                    else:
                        seen_segments.add(key)

        if result.open_polylines > 0:
            result.issues.append(
                Issue(
                    severity="WARNING",
                    message=f"{result.open_polylines} offene Konturen gefunden"
                )
            )

        if result.duplicate_lines > 0:
            result.issues.append(
                Issue(
                    severity="ERROR",
                    message=f"{result.duplicate_lines} doppelte Linien gefunden"
                )
            )

        if result.duplicate_lines > 0:
            result.issues.append(
                Issue(
                    severity="ERROR",
                    message=f"{result.duplicate_lines} doppelte Linien gefunden"
                )
            )

        if result.zero_length_lines > 0:
            result.issues.append(
                Issue(
                    severity="WARNING",
                    message=f"{result.zero_length_lines} Null-Linien gefunden"
                )
            )

        return result