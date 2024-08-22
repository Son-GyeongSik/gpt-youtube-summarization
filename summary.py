import datetime

from config import constants
from gpt import *


async def generate_summary(scripts: dict, video_title: str):
    time_stamp, chunks = naive_divide(scripts)
    summary_prompt = constants['prompt']['final_summary']['kr']

    tasks = [request_gpt(summary_prompt + "\n script : " + chunk,
                         constants['prompt']['final_summary']['system_message']) for idx, chunk in enumerate(chunks)]

    summaries = await asyncio.gather(*tasks)

    final_summary = ''
    for idx, summary in enumerate(summaries):
        final_summary += summary + '\n \n '

    final_summary = reformat_summary(final_summary)
    return final_summary, summaries


def naive_divide(scripts: dict):

    chunk_text = ''
    time_stamp = 0

    time_stamps = []
    chunks = []
    for script in scripts:
        if len(chunk_text) > 3000:
            chunk_text.replace("[음악]", "")
            chunk_text.replace("[박수]", "")
            chunks.append(chunk_text)
            time_stamps.append(time_stamp)
            time_stamp = script['start']
            chunk_text = script['text'] + ' '
        else:
            chunk_text += script['text']

    if len(chunk_text) < 1000 and len(chunks) > 0:
        chunks[-1] += chunk_text
    else:
        time_stamps.append(time_stamp)
        chunks.append(chunk_text)

    return time_stamps, chunks


def reformat_summary(summary: str):
    summary.replace("\#", "#")
    return summary