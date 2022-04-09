from datetime import time, datetime


# Making all timestamps dates at 1970-01-01 to use mongo DateTime
def timestamp_to_date(timestamp):
    if isinstance(timestamp, time):
        return datetime.fromisoformat('1970-01-01' + " " + str(timestamp))
    return None


def json_default(value):
    if isinstance(value, datetime):
        return str(value)
    else:
        return value.__dict__
