from langchain_text_splitters import RecursiveCharacterTextSplitter, SpacyTextSplitter
import textwrap
from gpt import *


async def generate_summary(script: str, mode: int):

    chunks = []

    if mode == 1:
        chunks = naive_divide(script)
    elif mode == 2:
        chunks = recursive_divide(script)
    elif mode == 3:
        chunks = spacy_divide(script)

    summary_prompt = constants['prompt']['final_summary']['kr']

    tasks = [request_gpt(summary_prompt + "\n script : " + chunk,
                         constants['prompt']['final_summary']['system_message']) for idx, chunk in enumerate(chunks)]

    summaries = await asyncio.gather(*tasks)

    final_summary = ''
    for idx, summary in enumerate(summaries):
        final_summary += summary + '\n \n '

    final_summary = reformat_summary(final_summary)

    return final_summary

async def generate_compress_summary(script: str, mode: int):

    max_cycle = int(len(script) / constants['chunk_size']['large']) + 1
    summary_prompt = constants['prompt']['summary']['kr']
    final_summary_prompt = constants['prompt']['final_summary']['en']
    summary = ''

    for cycle in range(max_cycle):

        chunks = []

        if mode == 1:
            chunks = naive_divide(script)
        elif mode == 2:
            chunks = recursive_divide(script)
        elif mode == 3:
            chunks = spacy_divide(script)

        if len(chunks) == 1:
            summary = await request_gpt(script + final_summary_prompt,
                                            constants['prompt']['final_summary']['system_message'])
            break

        tasks = [request_gpt(summary_prompt + "\n script : " + chunk,
                                 constants['prompt']['summary']['system_message']) for idx, chunk in enumerate(chunks)]

        chunk_summaries = await asyncio.gather(*tasks)
        summary = ' '.join(chunk_summaries)

        script = summary

    return summary


def naive_divide(script: str):

    chunks = textwrap.wrap(script, 3000)

    return chunks


def recursive_divide(scripts: str):

    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 3000, chunk_overlap = 50, length_function = len, is_separator_regex = False)
    chunks = text_splitter.split_text(scripts)
    print(chunks)

    return chunks

def spacy_divide(scripts: str):

    text_splitter = SpacyTextSplitter(chunk_size = 3000, chunk_overlap = 50)
    chunks = text_splitter.split_text(scripts)
    print(chunks)

    return chunks

def reformat_summary(summary: str):
    summary.replace("\#", "#")
    return summary

def preprocess_script(script: str):
    script.replace("[음악]", "")
    script.replace("[박수]", "")
    script.replace("[환호]", "")

    return script