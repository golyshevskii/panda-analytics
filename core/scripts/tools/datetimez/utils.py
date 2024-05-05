from datetime import datetime, timedelta, timezone
from typing import Union


def to_utc(dt: Union[str, datetime], utc_offset: int = 0) -> datetime:
    """
    Converts datetime to a specific UTC datetime

    Params:
        dt: datetime to convert
        utc_offset: UTC offset in hours
    """
    if isinstance(dt, str):
        dt = datetime.fromisoformat(dt)
    return dt.astimezone(timezone(timedelta(hours=utc_offset)))
