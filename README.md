## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
동기 방식의 경우 요청 순서대로 각각의 결과가 올때까지 프로그램이 기다리게 되며 비동기의 경우 요청에 대한 순서가 존재하지 않아 여러가지를 한번에 처리할 수 있습니다. 그렇지만 동기 방식의 경우 단위 테스트 및 프로그램 오류를 예측하기 쉬운 반면 비동기 방식은 그렇지 않습니다. 

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

블로킹 방식은 요청에 대한 처리를 결과가 올때까지 기다립니다. 논블로킹의 경우 요청을 하고 결과를 기다리지 않고 자신의 작업을 처리합니다. 동기/비동기와의 가장 큰 차이점으로는 전자는 순서에 포커스가 맞춰져 있고 후자는 요청에 맞춰줘 있는점입니다. 

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
 
JAVA의 경우 비동기 프로그래밍을 위해 Concurrent 패키지를 제공합니다. List나 Queue 같은 컬렉션을 동시성을 고려해 thread-safety한 자료구조로 만들어져 있습니다.
비동기 처리를 할때 다음과 같은 컬렉션을 사용하며 multi thread를 이용해 처리를 하고 싶을때 ThreadPoolExcecutor를 이용해 간단한 설정만으로 스레드 제어를 가능하게 합니다.

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

1. Logging 
애플리케이션에서 유저 정보와 같은 대용량 로그 정보를 받아와 저장할때 메세지 큐를 사용해 더 유연하게 처리할 수 있습니다. 클라이언트 요청은 요청대로 처리하고 로그 정보에 관한 것은 
큐에 넣어놓고 비동기로 처리할 수 있습니다. 이것을 동기 방식으로 처리한다면 클라이언트 요청 처리가 지연되고 서비스 장애로 이어지게 됩니다.

2. Evenet
다량의 요청 이벤트를 처리하는 경우 메시지 큐를 사용해 처리를 분산시키면 하나의 서버에서 처리하는것보다 빠르게 처리할 수 있습니다.
이벤트를 수신하고 처리하는 역할을 분담하여 MSA 형식으로 처리가 가능합니다.

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

https://github.com/kangyun9957/1-1-RESTAPI.git

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

대용량 처리를 하기 위한 애플리케이션 및 인프라 구조에 대해 배우고 직접 구현해보고 싶습니다.
