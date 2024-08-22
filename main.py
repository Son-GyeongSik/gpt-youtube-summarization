from script import *
from summary import *


async def root():
    print("Please Input Youtube Code : ")
    url = input()
    script = Script()
    get_script(script, url)
    print("script = " + script.text)
    summary, summary_list = await generate_summary(script.raw_script, '')
    print(summary)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(root())