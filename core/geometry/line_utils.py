def is_zero_length_line(entity) -> bool:

    if entity.dxftype() != "LINE":
        return False

    return entity.dxf.start == entity.dxf.end

def normalize_point(point):

    return (
        round(point.x, 4),
        round(point.y, 4)
    )

def normalize_line(start, end):

    p1 = normalize_point(start)
    p2 = normalize_point(end)

    return tuple(sorted([p1, p2]))