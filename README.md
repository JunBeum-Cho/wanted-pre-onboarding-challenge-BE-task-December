## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  - 동기 방식은 요청을 보내고 결과를 받아야지만 다음 작업이 이루어진다.
  - 비동기 방식은 요청을 보내고 결과와 상관없이 다음방식이 동작하는 방식이다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
    - 블로킹과 논블로킹은 작업이 다른 작업 흐름을 막는 지에 대한 것이다.
    - 블로킹은 작업을 진행하다가 다른 작업이 시작되면 자신의 작업을 멈추고 > 다른 작업 진행 > 다른 작업이 끝나면 자신의 작업 진행.
    - 논블로킹은 다른 작업에 관계 없이 자신의 작업을 수행한다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  - 코틀린에서는 coroutine을 이용해서 비동기 프로그래밍을 할 수 있다. async 키워드를 이용하면 동시에 다른 블록을 수행할 수 있다. launch와 비슷하게 보이지만 수행 결과를 await키워드를 통해 받을 수 있다는 차이가 있다.
결과를 받아야 한다면 async 결과를 받을 필요 없으면 launch 결과를 받으려면 await 을 사용하기만 하면 알아서 처리된다. 

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
  - 요청한 작업에 줄을 세우기 위해 -> 차례가 중요한 경우 순서를 유지해준다.
  - pub sub 구조이기 때문에 요청을 보내고 대기하는 동안 다른 작업을 할 수 있어 시스템 자원 사용에 용이하다.

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
  - https://github.com/chanqun/SpringApiServer

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
    - 비동기 프로그래밍을 하면서 에러를 복구하는 방법에 대해 배우고 싶다.
