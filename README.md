## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
> 동기(Synchronous) : 함수 A가 함수 B를 호출한 뒤, 함수 B의 리턴값을 계속 확인하면서 신경쓰는 프로그래밍
<br> 비동기(Asynchronous) : 함수 A가 함수 B를 호출할 때 콜백 함수를 함께 전달해서, 함수 B의 작업이 완료되면 함께 보낸 콜백 함수를 실행한다. 함수 A는 함수 B를 호출한 후로 함수 B의 작업 완료 여부에는 신경쓰지 않는 프로그래밍이다.
<br> 두가지의 가장 큰 차이점은 호출되는 함수의 작업완료 여부를 신경쓰는지 아닌지 여부이다. 

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
> 블로킹(blocking) : 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 끝날 때까지 기다렸다가 자신의 작업을 시작하는 것
<br> 논블로킹(non-blocking) : 다른 주체의 작업에 관련없이 자신의 작업을 하는 것
<br> 블로킹과 논블로킹은 처리되어야 하는 작업이 전체적인 작업 흐름을 막는 지에 대한 관점이다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
> callee 메서드 쪽에서, @Async 를 붙여서 비동기로 동작하게 하는 방법과, Caller가 호출방식을 직접 비동기로 호출하는 방법. 

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
> 대용량 데이터를 처리하기 위한 배치 작업, 채팅 

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
> https://github.com/bbring2/restdocs-test 
(업데이트 하겠습니다!)

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
> 메시징 큐에 대해서 제대로 배워보고 싶습니다. 
