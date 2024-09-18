from script import *
from summary import *


async def root():

    print("Please Input Youtube Code : ")
    url = input()

    print("Please Input Summary Mode (1: Normal, 2: Compress")
    summary_mode = int(input())

    print("Please Input Divide Mode (1: Naive, 2:RCTS, 3:SPACY) : ")
    mode = int(input())

    script = Script()
    get_script(script, url)

    print(script.text)

    if summary_mode == 1:
        summary = await generate_summary(script.text, mode)

    elif summary_mode == 2:
        summary = await generate_compress_summary(script.text, mode)

    print(summary)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(root())