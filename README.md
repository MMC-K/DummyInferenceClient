
## 사용 전 라이브러리 설치
```bash
pip install -r requirements.txt
```

## 사용 방법
1. 터미널 창에서 Client 폴더로 작업 디렉터리를 변경 후 python client.py 입력
```bash
e.g. python client.py
```

2. play code를 입력하는 문구가 출력된다면 start 혹은 continue 선택하여 서버로부터 데이터를 받아오기
```bash
# start: 처음부터 다시 받아오기
# continue: 마지막 종료 지점부터 이어서 받아오기
e.g. play code: [start | continue]: start
```

3. 서버로부터 데이터를 받아오는 시간을 조절하는 방법
   - client.py 파일의 INTERVAL을 수정 (초 단위, 소수점 가능)
```bash
e.g. INTERVAL = 3.2
```

## 출력 데이터 예시
```bash
{
    "affective_state": "중립",
    "channel": "front",
    "device_id": "device01",
    "expressions": [
        {
            "nonverbal": {
                "additional": "",
                "function": "",
                "gaze": ""
            },
            "paraverbal": "",
            "verbal": "퇴근하고"
        },
        {
            "nonverbal": {
                "additional": "",
                "function": "",
                "gaze": ""
            },
            "paraverbal": "",
            "verbal": "계속"
        },
        {
            "nonverbal": {
                "additional": "",
                "function": "",
                "gaze": ""
            },
            "paraverbal": "",
            "verbal": "마라톤을"
        },
        {
            "nonverbal": {
                "additional": "",
                "function": "",
                "gaze": ""
            },
            "paraverbal": "",
            "verbal": "하고"
        },
        {
            "nonverbal": {
                "additional": "",
                "function": "호응적",
                "gaze": ""
            },
            "paraverbal": "",
            "verbal": "있구요"
        }
    ],
    "strategy": "주관적정보 구체화",
    "user_id": 1,
    "utterance": " 퇴근하고 계속 마라톤을 하고 있구요"
}
```
