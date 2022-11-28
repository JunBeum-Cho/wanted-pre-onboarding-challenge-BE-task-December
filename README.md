## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

결과값

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

제어권

Function call corresponding to an I/O request will block the execution of the thread until the operation completes.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

Node.js/Javascript에서는 비동기 프로그래밍 사용하는 방법은 다음과 같다. 

1. Callback. 파일 읽기, 네드웨크 통신과 같은 작업들이 비동기 작업들이 완료되었을 때 작업이 완료되었음을 알릴 방법이 필요한데 callback은 비동기 호출 완료를 알리는 가장 기본적인 방법이다. 구체적으로 callback은 비동기 작업의 결과값을 갖고 runtime에서 호출하는 함수이다.
1. Promises
1. Async/Await

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.


- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

https://github.com/giwankim/WhatsAppPush

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
