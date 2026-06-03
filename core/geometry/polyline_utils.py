def is_closed_polyline(entity) -> bool:

    if entity.dxftype() == "LWPOLYLINE":
        return entity.closed

    if entity.dxftype() == "POLYLINE":
        return entity.is_closed

    return False