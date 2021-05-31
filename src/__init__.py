import asyncio
from functools import partial, wraps


def asyncify(Function):
    @wraps(Function)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop() 
        return await loop.run_in_executor(executor, partial(Function, *args, **kwargs))

    return run