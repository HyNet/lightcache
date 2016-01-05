# lightcache
A light weight cache

## what is lightcache

`lightcache` is a decorator that cache the return value of functions.
here is an example:

```python
import time
from lightchache import lightcache

@lightcache(timeout=4)
def cached_function(t=2)
    time.sleep(t)
    return random.randint(1, 100)

if __name__ == "__main__":
    val_pre = cached_function()
    val = cached_function()
    print(val == val_pre)
    time.sleep(6)
    val = cached_function()
    print(val != val_pre)
```

## TODO
- add support for redis
