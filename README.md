## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

1) 동기 프로그래밍 : 데이터 처리가 순차적으로 진행되어 이전 데이터의 처리가 완료되었을 때 다음으로 진행이 된다.
설계가 간단하고 직관적이다.

2) 비동기 프로그래밍 : 데이터 처리가 순차적인 것 아니라 여러 데이터의 처리가 동시에 진행될 수 있다. 
자원을 효율적으로 사용할 수 있다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

1) 블로킹 : 요청 함수가 요청한 작업이 끝날 때 까지 다른 작업을 하지 않고 기다린다.
함수에는 제어권이라는 작업들을 진행할 수 있는 권한 같은 것이 있는데 이 제어권을 다른 함수를 호출할 때 아예 넘겨주고 끝나야 돌려 받기 때문에 그러하다.
여기서 요청 받은 함수는 실행이 끝나면 제어권과 함께 리턴 값을 돌려준다.

2) 논블로킹 : 다른 함수를 호출할 때 제어권을 넘겨주긴하나 바로 돌려받아 요청한 작업이 수행되는 동안 다른 작업이 진행되는 방식이다.

동기, 비동기, 블로킹, 논블로킹의 조합을 통해 4가지 방식으로 로직을 구현할 수 있다.


- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
현재 제 업무에서는 자바스크립트를 다룰 때 제일 많이 씁니다.

제 블로그에도 정리를 해두었습니다.

https://velog.io/@mongu_93/자바스크립트-비동기-처리

자바 스크립트에서 비동기 처리는 우선 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 특성이며 

특정 코드의 연산 즉 데이터가 준비가 완료된 시점에서 원하는 동작을 수행하기 위해서 

Callback, Promise, Async & Await를 사용해서 로직을 제어한다.

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
- 
메시지 큐를 알기위해서는 MOM이라는 걸 알아야 하는데 MOM은 간단히 말해 비동기 메시지 프로그램 간에 데이터 송수신을 의미한다.

메시지 큐는 이러한 MOM을 구현한 서비스로 프로세스 간에 데이터 교환을 할 때 사용되는 통신 방법이다.

어플리케이션이나 시스템 사이에서의 통신에서 시스템 장애를 방지하기 위해 사용할 수 있고 

또 서버에서 대용량 데이터 처리가 필요할 때 서버가 처리할 수 있는 양을 분산시켜 처리가 가능하다.

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

JPA를 배워보고 쇼핑몰 운영 회사에 지원을 해보고 싶어서 최근에 연습해보고 있는 프로젝트입니다.

아직 미완성이고 해둔게 거의 없지만 빠르게 완성 시키도록 하겠습니다.

https://github.com/zpka14/ShopMallProject

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

현재 재직중인 회사에서 AWS를 쓰는데 확실히 알고있으면 도움이 될 것 같습니다.
저의 사전 과제가 부족하지만 참여를 꼭 하고 싶습니다.
