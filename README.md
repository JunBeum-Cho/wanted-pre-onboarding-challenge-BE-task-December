## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.   
  * 동기는 요청에 대해 시간이 얼마나 걸리던지 결과를 반환해줄때까지 기다린다. 하지만 비동기는 요청에 대한 결과를 기다리지 않고 다음 작업을 수행할 수 있다.
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.   
  * 간단하게 제어권이 호출된 본인에게 있는가로 갈린다.
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.   
  * 주로 Java를 사용하며 함수형 프로그래밍 또는 Thread를 생성하여 비동기 프로그래밍을 수행한다.
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.   
  * 이미지 처리, 빅데이터와 같은 대용량 데이터 처리와 같은 작업에서 MQ를 사용하면 서버가 처리할 양을 MQ에 가져와서 처리할 수 있다. 즉, 서버의 부담을 줄여줄 수 있다
  * 서버 간 데이터를 주고 받거나 작업을 요청할 때 서버가 failover라면 통신이 불가능하다. MQ를 사용하면 이 문제를 해결할 수 있다. 
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)    
  * [chois-english-back](https://github.com/bodyMist/chois-english-back)
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
  * Nosql DB의 설계방법과 CI/CD에 대해 배우고 싶습니다
