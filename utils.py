

from datetime import datetime

def now_ts():
    return
datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def make_log(message,note=None):
    result=f"{now_ts()} - {message}"
    if note:
        result+=f"(Note:{note})"
    return result
