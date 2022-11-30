## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

(1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

**동기(synchronous : 동시에 일어나는)**
 - 동기는 말 그대로 동시에 일어난다는 뜻입니다. 요청과 그 결과가 동시에 일어난다는 약속. 바로 요청을 하면 시간이 얼마가 걸리던지 요청한 자리에서 결과가 주어져야 한다.
  - 요청과 결과가 한 자리에서 동시에 일어남
  - A노드와 B노드 사이의 작업 처리 단위(transaction)를 동시에 맞춤
 
**비동기(Asynchronous : 동시에 일어나지 않는)**
- 비동기는 동시에 일어나지 않는다를 의미합니다. 요청과 결과가 동시에 일어나지 않을거라는 약속
- 요청한 그 자리에서 결과가 주어지지 않음
- 노드 사이의 작업 처리 단위를 동시에 맞추지 않아도 됨

![](https://velog.velcdn.com/images/celeste/post/2f64490e-c735-45b8-820a-b6a4ec83b2d3/image.png)

**동기식 처리 모델의 예시**
- Ex) 버거가 먹고 싶어서 맥도날드에 가기로 결정합니다. 카운터에서 버거를 주문하면 버거가 준비되는 동안 기다리라는 안내를 받습니다. 이 동기식 상황에서는 햄버거가 제공될 때까지 카운터에 갇혀 있습니다.

**동기식 처리 모델의 장점과 단점**
- 장점 : 설계가 매우 간단하고 직관적입니다.
- 단점 : 요청에 따른 결과가 반환되기 전까지 아무것도 못하고 대기해야합니다.

**비동기식 처리 모델의 예시**
- 버거가 먹고 싶어서 롯데리아에 가기로 결정했습니다. 카운터에 가서 햄버거를 주문합니다. 롯데리아는 햄버거가 준비되면 알려주는 부저를 제공합니다. 이 비동기 상황에서는 기다리는 동안 더 많은 자유를 누릴 수 있습니다.

**비동기식 처리 모델의 장점과 단점**
- 장점 : 요청에 따른 결과가 반환되는 시간 동안 다른 작업을 수행할 수 있습니다.
- 단점 : 동기식보다 설계가 복잡하고 논증적입니다.

 
출처:
https://docs.aws.amazon.com/ko_kr/lambda/latest/dg/invocation-async.html?tag=mochaglobal20-20
https://www.koyeb.com/blog/introduction-to-synchronous-and-asynchronous-processing

---
(2) 블로킹과 논블로킹의 차이점을 설명해주세요.

블로킹과 논블로킹은 A 함수가 B 함수를 호출했을 때, 제어권을 어떻게 처리하느냐에 따라 달라진다.
- 제어권 : 제어권은 자신(함수)의 코드를 실행할 권리 같은 것이다. 제어권을 가진 함수는 자신의 코드를 끝까지 실행한 후, 자신을 호출한 함수에게 돌려준다.
- 결과값을 기다린다는 것 : A 함수에서 B 함수를 호출했을 때, A 함수가 B 함수의 결과값을 기다리느냐의 여부를 의미한다.

**블로킹**
- 블로킹은 A 함수가 B 함수를 호출하면, 제어권을 A가 호출한 B 함수에 넘겨준다.
![](https://velog.velcdn.com/images/celeste/post/5d947573-4fb7-4d6c-9ee2-dba113c5005b/image.png)
1. A함수가 B함수를 호출하면 B에게 제어권을 넘긴다.
2. 제어권을 넘겨받은 B는 열심히 함수를 실행한다. A는 B에게 제어권을 넘겨주었기 때문에 함수 실행을 잠시 멈춘다.
3. B함수는 실행이 끝나면 자신을 호출한 A에게 제어권을 돌려준다.

**논블로킹**
- 논블로킹은 A함수가 B함수를 호출해도 제어권은 그대로 자신이 가지고 있는다.
![](https://velog.velcdn.com/images/celeste/post/9e4e611e-76de-4946-8e74-7c0ee052fb97/image.png)
1. A함수가 B함수를 호출하면, B 함수는 실행되지만, 제어권은 A 함수가 그대로 가지고 있는다.
2. A함수는 계속 제어권을 가지고 있기 때문에 B함수를 호출한 이후에도 자신의 코드를 계속 실행한다.

요약하자면,

동기/비동기 = 요청받은 함수가 작업을 완료했는지를 체크해서 순차적 흐름의 차이

동기 : 요청자가 요청받은 함수의 작업이 완료되었는지 계속 확인 (여러 함수들이 시간을 맞춰 실행됨)
비동기 : 요청자는 요청후 신경X, 요청받은 함수가 작업을 마치면 알려줌 (함수들의 작업 시작/종료 시간이 맞지 않을수도)

출처:
https://luminousmen.com/post/asynchronous-programming-blocking-and-non-blocking
https://velog.io/@nittre/%EB%B8%94%EB%A1%9C%ED%82%B9-Vs.-%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9-%EB%8F%99%EA%B8%B0-Vs.-%EB%B9%84%EB%8F%99%EA%B8%B0
https://www.youtube.com/watch?v=oEIoqGd-Sns

---

(3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

파이썬은 원래 동기 방식으로 동작하도록 설계된 언어지만, Python 3.4 버전부터 asyncio 라이브러리가 표준으로 채택되고 Python 3.5 버전부터 async/await 키워드가 추가되면서, Python에서도 비동기 프로그래밍을 더욱더 쉽게 할 수 있게 되었다.

동기식으로 웹페이지를 다운받는것을 시뮬레이션 한 아래의 코드를 비동기식으로 변환시켜보면서 어떻게 파이썬에서 비동기 프로그래밍이 사용되는지 볼 수 있다.

```py
import time

def download_page(url) :
​​​​time.sleep(1) # 페이지를 다운로드
​​​​#html 분석
​​​​print("complete download:", url)
​​​​
def main() :
​​​​download_page("url_1")
​​​​download_page("url_2")
​​​​download_page("url_3")
​​​​download_page("url_4")
​​​​download_page("url_5")

print(f"stated at {time.strftime('%X')}")
main()
print(f"finish at {time.strftime('%X')}")
# 하나의 페이지를 다운로드 하는데 1초가 걸린다고 하면 다른 작업을 제외하고도 최소한 5초가 걸리게 된다.
```

**1. asyncio 임포트**
비동기 함수를 만들기 위해서는 비동기 관련 기능을 담고 있는 asyncio 모듈을 임포트(import) 해야 한다.

```python
import asyncio
```

**2. def 대신 async def**
비동기 함수는 def 대신 'async def' 키워드를 사용한다. async def문을 이용해 구현된 함수를 파이썬에선 코루틴이라고 부른다. 

```python
import asyncio

# def download_page(url) :
async def download_page(url) :  # async def 키워드로 대체
​​​​time.sleep(1) 
​​​​#html 분석
​​​​print("complete download:", url)
​​​​
# def main()     
async def main() :              # async def 키워드로 대체
​​​​download_page("url_1")
​​​​download_page("url_2")
​​​​download_page("url_3")
​​​​download_page("url_4")
​​​​download_page("url_5")
```

**3. asyncio.sleep()**
`time.sleep()`은 1초가 지나기 전까진 리턴하지 않고 멈춰 있는 동기 함수다. 이것을 `asyncio.sleep()` 함수로 대체 하겠다. `asyncio.sleep()`은 비동기 함수로써 시작하자 마자 바로 리턴하지만, 백그라운드로 1초간 대기 후 시간이 만료 되면 만료를 통보한다.

```python
import asyncio

async def download_page(url) :
​​​​# time.sleep(1) 
​​​​asyncio.sleep(1)           # 비동기 함수로 대체
​​​​#html 분석
​​​​print("complete download:", url)
​​​​
async def main() :
​​​​download_page("url_1")
​​​​download_page("url_2")
​​​​download_page("url_3")
​​​​download_page("url_4")
​​​​download_page("url_5")
```

**4. await**
비동기 함수가 바로 리턴 해버리면서 완료 되지 않은 결과에 접근하는 것을 방지하기 위해 아래 처럼 비동기 함수(asyncio.sleep) 호출 앞에 await 키워드를 사용한다.
await = 다음으로 바로 진행하지 않고 완료 통보가 올 때 까지 진행한다. 이벤트 루프에 일거리가 있다면 해당 작업들을 처리하면서 기다린다.

※ 아래 처럼 함수(또는 객체가) await 표현식에서 사용 될 수 있을 때, 이를 어웨이터블 객체라고 말한다.
```py
import asyncio

async def download_page(url) : 
​​​​# asyncio.sleep(1)
​​​​await asyncio.sleep(1)     # await 키워드 사용
​​​​#html 분석
​​​​print("complete download:", url)
​​​​
async def main() :
​​​​await download_page("url_1")
​​​​await download_page("url_2")
​​​​await download_page("url_3")
​​​​await download_page("url_4")
​​​​await download_page("url_5")
```

**5. asyncio.run()**

코루틴을 실행하기 위해선 일반 함수의 호출과는 달리 asyncio.run() 함수를 통해서만 호출이 가능하다.

**6. asyncio.gather()**

asyncio 모듈에서는 여러 비동기 함수를 한번에 등록 할 수 있는 gather() 함수를 제공한다.

```py
import time
import asyncio

async def download_page(url) :
​​​​await asyncio.sleep(1) # 페이지를 다운로드
​​​​#html 분석
​​​​print("complete download:", url)
​​​​
async def main() :
​​​​await asyncio.gather(
​​​​​​​​download_page("url_1"),
​​​​​​​​download_page("url_2"),
​​​​​​​​download_page("url_3"),
​​​​​​​​download_page("url_4"),
​​​​​​​​download_page("url_5")
​​​​)    

print(f"stated at {time.strftime('%X')}")
asyncio.run(main())
print(f"finish at {time.strftime('%X')}")

# OUTPUT :
# stated at 20:50:32
# complete download: url_1
# complete download: url_3
# complete download: url_5
# complete download: url_2
# complete download: url_4
# finish at 20:50:33 <-------- 1초 걸림
```

`main()` 에서 시작된 첫번째 `download_page("url_1")` 함수는 실행과 동시에 - 내부의 `asyncio.sleep()`이 즉시 - 리턴하고, 이벤트 루프에 있는 다른 비동기 함수를 실행한다. 이런 식으로 모든 `download_url()` 함수들을 호출하고, 모든 비동기 함수가 완료 되면 `asyncio.run()` 함수는 그 결과를 모아 한번에 리턴하고 프로그램은 종료 된다.

출처:
https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D
https://dojang.io/mod/page/view.php?id=2469
https://kukuta.tistory.com/345

---

(4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

**메시지 큐**는 서버리스 및 마이크로 서비스 아키텍처에 사용되는 비동기식 서비스 대 서비스 통신 형태이다. 메시지는 처리되고 삭제되기 전까지 대기열(=Queue)에 저장된다. 각 메시지는 하나의 소비자가 한 번만 처리한다. 메시지 대기열은 규모가 큰 처리 작업을 결합 해제하고, 버퍼링 또는 배치 작업을 수행하고, 급변하는 워크로드를 원활하게 지원하는 데 사용될 수 있다.

메세지 큐를 사용하기 적합한 경우는 다음과 같다.
1. 어플리케이션, 시스템 간 통신에 사용
- 서버 간 데이터를 주고 받거나 작업을 요청할 때 , 항상 시스템 장애를 생각해야 한다. 서버가 갑자기 죽어버리거나, 서버 점검 등 다운타임이 발생하는 동안에는 요청을 받을 수 없다. 서버에서 failover 처리를 해놓고 시스템이 정상적으로 돌아왔을 때 요청을 보내는 방법이 있지만, MQ를 사용하면 간편하게 처리가 가능하다.
2. 서버 부하가 많은 작업에 사용
- 이미지 처리, 비디오 인코딩 등 대용량 데이터 처리와 같은 작업은 메모리, CPU를 많이 사용한다. 동시에 처리할 수 있는 양이 한정적이여서 무작정 요청을 보내 처리를 할 수 없다. 이 때, MQ를 사용하면 서버가 처리할 수 있는 양을 MQ에서 가져와 처리하면 된다.

![](https://velog.velcdn.com/images/celeste/post/85b8dd72-9156-4776-abf6-79b95d3cbc86/image.png)


출처:
https://aws.amazon.com/ko/message-queue/
https://heeonii.tistory.com/17
https://velog.io/@kimjaejung96/%EB%A9%94%EC%84%B8%EC%A7%80-%ED%81%90Message-Queue%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80

---

(5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

  - 와인 추천 및 리뷰 사이트 구현 (https://github.com/sc680/Hangover-backend)
    - 상품 리뷰 CRUD
    - 회원가입, 로그인 API - JWT 인증 포함
    - 상품 필터 - 가격,주종,잘어울리는 음식, 원산지, 평점, 정렬 등 다양한 필터링에 관한 정보를 받아, 조건에 부합하는 상품을 정렬조건에 맞게 정렬하여 반환
    - 상품 검색 - 검색어를 포함하고 있는 카테고리 혹은 상품을 반환. 검색어가 카테고리나 상품명에 포함되지 않을 경우 추천검색어 반환
    

  - 맛집 추천 및 예약 사이트 구현 (https://github.com/sc680/WeEats-backend)
    - 음식점 리뷰 CRUD, 마이페이지 및 user API 구현
    - 보다 간편한 로그인을 위해 OAuth 2.0 프로토콜을 이용해 카카오 소셜 로그인을 구현하였으며 인증에는 JWT 토큰을 사용해 특정 사용자와 관리자 권한을 분리하였습니다. 
    - AWS EC2,RDS를 활용해 backend api 서버 배포하였습니다.
  

---
(6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

  - AWS라고 하면 막연한 두려움만 가지고 있었고, 이론으로 배워도 실전으로 사용하기 어렵다는 생각을 가지고 있었습니다. AWS API Gateway, Lambda, EC2 같은 꼭 알아야 하지만 습득하기 쉽지 않은 기술에 대해 자세히 알고 자신감을 갖고 싶습니다.
