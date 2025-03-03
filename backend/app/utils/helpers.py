# backend/app/utils/helpers.py
def format_datetime(dt):
    """
    Format a datetime object into a human-readable string.
    """
    return dt.strftime("%Y-%m-%d %H:%M:%S")
