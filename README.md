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

## Develop Web Page (~24. 10. 14)
유저가 사용할 수 있도록 웹 페이지를 개발하였다.

## Update Web Page (~24. 10. 19)
페이지 크기에 따라 동적으로 웹페이지를 구성할 수 있도록 코드를 수정하였다.
또한 해당 코드를 실행하기 쉽도록 requirements.txt를 추가해 필요 라이브러리를 쉽게 받을 수 있도록 하였다.

<br/>

# 사용법

## 가상환경 세팅 (생략 가능)
### 가상환경 생성
아래 명령어를 통해 Python 가상환경을 생성한다
```aiignore
python3 -m venv {가상환경이름}
```

### 가상환경 실행
아래 명령어를 통해 Python 가상환경을 실행한다.
#### MAC
```aiignore
source {가상환경이름}\bin\activate
```
#### Windows
```
source {가상환경이름}\Scripts\activate
```

## 필요 라이브러리 설치
모든 필요 라이브러리는 requirements.txt 파일에 정의되어 있으며 위 라이브러리를 아래 명령어를 통해 한번에 설치할 수 있다.
```aiignore
pip3 install -r requirements.txt
```

## 데이터베이스 생성
MySQL을 설치하여 "graduate" 스키마를 생성하고 아래 SQL 코드를 통해 테이블을 생성한다
```mysql
create table summary
(
    summaryId  int auto_increment
        primary key,
    videoCode  varchar(255) not null,
    summary    text         null,
    is_created tinyint(1)   not null
);
```

## 서버 실행
라이브러리 설치 및 데이터베이스 세팅이 완료 되었다면 아래 명령어를 통해 서버를 실행한다.
```aiignore
python3 main.py
```

"127.0.0.1" 로 웹 브라우저에서 접속하면 서비스 이용이 가능하다  
