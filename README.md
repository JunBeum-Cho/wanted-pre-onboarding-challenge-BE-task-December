## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
```
- 동기 : 요청과 결과가 동시에 일어나는 방식, 처음부터 끝까지 순차적으로 일을 처리하는 프로그램
- 비동기 : 요청과 결과가 동시에 일어나지 않는 방식, 테스크의 시간에 따라 시간이 걸리는 테스크를 넘기고 바로 다음 일을 처리하는 프로그램
```
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
```
- 블로킹 : 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 자신의 작업을 멈추고 해당 작업을 기다렸다가 다시 자신의 작업을 시작
- 논블로킹 : 다른 주체의 작업에 관련 없이 자신의 작업을 하는 것
```
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
```
python 자체적으로 비동기 프로그래밍을 사용하려면 asyncio를 표준 라이브러리로 사용하고, async, await를 문법으로 사용하면 된다.

def 키워드로 선언하는 모든 함수는 파이썬에서 기본적으로 동기 방식으로 동작한다.
def do_sync():
    pass

기존 def 키워드 앞에 async 키워드를 붙이면 이 함수는 비동기 처리되며, 이를 코루틴(coroutine)이라고 부른다.
async def do_async():
    pass

비동기 함수를 호출하면 coroutine 객체가 리턴된다.
do_async() # <coroutine object do_async at 0x1038de710>

따라서 비동기 함수는 일반적으로 async로 선언된 다른 비동기 함수 내에서 await 키워드를 붙여서 호출해야 한다.
async def main_async():
    await do_async()
```
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
```
1. 이메일을 보낼 때 큐에 담아서 비동기로 처리하고 유저는 이메일이 보내졌다는 메시지만 확인 후 다른 작업을 하게 할 수 있다.

2. 블로그 사용자가 이미지를 올리는 경우 큰 용량을 올릴 때는 업로드 한 이미지를 즉시 처리하지 않고 사후처리하며 최적화 할 수 있다.
```
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
- 술집 정보 및 후기 공유 커뮤니티를 제공하는 서비스
  - https://github.com/kimdakyeom/alcohol_trip

- 전국 야구장 내의 매점 정보와 밖의 맛집 정보, 커뮤니티를 제공하는 서비스
  - https://github.com/kimdakyeom/YammyChu

- 영화 리뷰 커뮤니티를 제공하는 서비스
  - https://github.com/kimdakyeom/pair_4
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
```
다양한 OS 개발 환경에서 프로그래밍을 진행하며 배포 환경에 대해 이해하고 응용해보고 싶다.
```