import json
from urllib.parse import parse_qs
import json
import pytz
from datetime import datetime, timezone
import dateutil.parser

def localize_tz(dt, timezone="UTC"):
    loc_tz = pytz.timezone(timezone)
    dt = loc_tz.localize(dt)
    return dt

def parse_date(date_str, str_format="%Y-%m-%d %H:%M", timezone="UTC", convert_to_utc=True):
    if str_format:
        try:
            loc_tz = pytz.timezone(timezone)
            dt = loc_tz.localize(datetime.strptime(date_str, str_format))
        except ValueError:
            dt = dateutil.parser.parse(date_str)
    else:
        dt = dateutil.parser.parse(date_str)

    if not dt.tzinfo:
        dt = pytz.timezone("UTC").localize(dt)

    if dt.tzname() != "UTC" and convert_to_utc:
        dt = dt.astimezone(pytz.UTC)
    return dt

def now_utc():
    now = datetime.now(timezone.utc)
    return now


def is_midnight(_time):
    if _time.hour >= 21 and _time.hour <= 23:
        return True
    elif _time.hour >= 0 and _time.hour <= 4:
        return True
    return False


def form_urlencoded_parse(body):  # pragma: no cover
    """
    Parse x-www-form-url encoded data
    """
    try:
        data = parse_qs(body, strict_parsing=True)
        for key in data:
            data[key] = data[key][0]
        return data
    except ValueError:
        pass


def convert_to_dict(o): # pragma: no cover
    if isinstance(o, str):
        return json.loads(o)
    return o


def datetime_to_ref(mydate):
    return mydate.strftime("%Y:%j:%H:%M")


# def key_val_cache(func):
#     async def func_wrapper(key):
#         val = redis.get(key)
#         if val:
#             return val.decode('ascii')
#         else:
#             val = await func(key)
#             redis.set(key, val, ex=60)
#             return val

#     return func_wrapper


# def blocking(method):
#     """
#     Wraps the method in an async method, and executes the function on `self.executor`
#     """

#     @wraps(method)
#     async def wrapper(self, *args, **kwargs):
#         def work():
#             return method(self, *args, **kwargs)
#         return await IOLoop.run_in_executor(None, work)

#     return wrapper
