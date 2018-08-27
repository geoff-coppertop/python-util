import sys
import asyncio as aio

class Prompt:
    '''
    Stolen from this stack overflow answer:
    https://stackoverflow.com/questions/35223896/listen-to-keypress-with-asyncio
    '''
    def __init__(self, loop=None):
        self.loop = loop or aio.get_event_loop()
        self.q = aio.Queue(loop=self.loop)
        self.loop.add_reader(sys.stdin, self.got_input)

    def got_input(self):
        aio.ensure_future(self.q.put(sys.stdin.readline()), loop=self.loop)

    async def __call__(self, msg, end='\n', flush=False):
        print(msg, end=end, flush=flush)

        return (await self.q.get()).rstrip('\n')
