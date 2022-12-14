## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
```
spring scheduled annotation -> 싱글 스레드로 작동, 스케줄 큐가 쌓이면 스케줄이 지연됨
spring scheduled annotation + Async anotation -> 싱글 스레드(scheduled annotation) + 추가 스레드(Async annotation)로
지연의 원인의 되는 스케줄을 추가 스레드에서 실행 할 수 있음.
```
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
```
블로킹 : API의 Request body와 Response body
논블로킹 : spring netty, 서버를 열어두면 상시 데이터를 수신받음 (socket)
```
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
```java
@Schleduled(cron = "0 0 1 * * *") //약 3시간 걸리는 배치
@Async
public void 정말_느린_코드() { someService.realSlow(); }
```

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
```
서버 혼자 여러 서비스(kibana, dw, socket 등)에 보내기 버겁다

특정 고객사에게만 이벤트를 발송(알림톡)을 보내기 위해
```

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
```
https://github.com/GHGHGHKO/goose-auth-api-server
```

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
```
prod 환경의 aws 기반의 아키텍처에 대해
```

