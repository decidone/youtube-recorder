# youtube-recorder

## Table of Contents
- [Description](#description)
- [Development Environment](#development-environment)
- [Usage](#usage)

## Description
- 특정 채널의 유튜브 라이브 스트리밍을 감지하여 자동녹화 해주는 프로그램
- 사용 전 외부 프로그램 설치 및 약간의 코드 수정 필요
```sh
youtube-recorder.py
  - self.channel_id -> 유튜브 채널ID
  - self.file_path  -> 파일 저장경로
```

## Development Environment
- Python - 3.10.0
- Streamlink - 3.0.1

## Usage
- Python, Streamlink 설치
- 필요한 모듈 설치(requests, BeautifulSoup ...)
- self.channel_id, self.file_path 지정
- 실행 시 설정한 유튜브 채널에서 라이브 스트리밍을 하는지 정해진 시간(기본 10초, 변경 가능) 간격으로 체크하며, 방송이 켜지면 자동으로 녹화 시작
