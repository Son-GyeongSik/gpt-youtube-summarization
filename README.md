# Coming Soon (Nov. 2024)

## gpt-youtube-summarization
develop gpt youtube summarize logic for 2024 skku graduate evaluation   

<br/>

# Research Note

## Naive Version (24.08.22.)
기본적인 스크립트 불러오기와 요약본 생성 로직을 개발하였다.

스크립트 불러오기는 YouTube_Transcript_API 라이브러리를 사용하여 불러오며 불러오는 자막 우선순위는 직접 생성여부와 언어에 따라 차등적으로 부여되어 불러온다.

한 번의 요청 내에 모든 스크립트를 담지 못하는 경우가 있다. (Script Size > Model Context Size) 따라서 이를 분할하는 로직을 적용하였는데

현 버전에서는 Naive하게 글자수로 분할한다. 추후 개발에서 이를 잘 분할할 수 있는 여러 방안을 탐구하여 적용할 예정이다.


## Recursive Version (24. 08. 25)
LangChain의 RecursiveCharacterTextSplitter 메소드를 활용한 텍스트 분할 로직을 추가하였다.


## spaCy Version (24. 08. 28)
spaCy Tokenizer를 기반으로 텍스트를 분할하는 로직을 추가하였다.

## Compressive Summarization (24. 09. 02)
단계적으로 압축하는 로직을 개발하였다.

