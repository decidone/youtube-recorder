# youtube-recorder

## Table of Contents
- [Description](#description)
- [Development Environment](#development-environment)
- [Usage](#usage)

## Description
- 유튜브 라이브 스트리밍을 자동녹화 해주는 프로그램
- 사용 전 외부 프로그램 설치 및 약간의 코드 수정 필요

## Development Environment
- Python - 3.10.0
- Streamlink - 3.0.1

## Usage
- Python, Streamlink 설치
- 필요한 모듈 설치(requests, BeautifulSoup ...)
- self.channel_id를 녹화를 원하는 유튜브 채널ID로 변경
- self.file_path를 원하는 파일 저장경로로 변경
- 실행 시 설정한 유튜브 채널에서 라이브 스트리밍을 하는지 정해진 시간(기본 10초, 변경 가능) 간격으로 체크하며, 방송이 켜지면 자동으로 녹화 시작
