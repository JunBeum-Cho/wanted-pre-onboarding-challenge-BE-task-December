## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  - 동기: 데이터의 요청과 결과가 한 자리에서 동시에 일어나는 것을 말합니다. 가령 A노드와 B노드의 트랜잭션을 맞출 때 동기적으로 처리합니다. 은행 전산은 동기적으로 처리해야만 합니다. 
  - 비동기: 데이터의 요청과 결과가 따로따로 일어나는 것을 말합니다. 결과가 주어지는데 시간이 걸리더라도 그 시간 동안 다른 작업을 할 수 있으므로 자원을 효율적으로 사용할 수 있습니다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
  - 블로킹: A와 B함수가 있다고 할 때, 블로킹은 A함수가 B함수를 호출하면서 A함수가 제어권을 B함수에 넘겨주는 것입니다. 제어권이 없으므로 A함수는 B함수가 끝나서 제어권을 넘겨줄 때까지 기다려야 합니다. 스택 구조를 생각하면 쉽습니다. 
  - 논블로킹: A와 B함수가 있다고 할 때, 논블로킹은 A함수가 B함수를 호출해도 제어권은 그대로 가지고 있습니다. A함수는 계속 제어권을 가지고 있기 때문에 B함수를 호출한 이후에도 자신의 코드를 계속 실행합니다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  Java에서 비동기 프로그래밍을 할 때는 크게 Future 객체를 사용하는 방식과 Callback을 구현하는 방식이 있습니다. 
  - Future 객체 사용: B에게 작업을 맡긴 상태에서 A 쪽에서 작업이 끝났는지 직접 확인하는 방법입니다. 이렇게 확인하는 방법으로는 두 가지가 있습니다. 하나는 isDone()이나 isCanceled() 메소드로 블로킹 없이 작업을 완료했는지의 여부만 확인하는 방법이고, 다른 하나는 get()으로 작업이 완료될 때까지 블로킹된 상태로 대기하는 방법입니다. 오래 걸리는 작업을 다른 주체에게 맡겨 두고 get()을 호출하기 전까지 이 쪽에서 할 일을 하다가, 작업을 마치면 get()을 호출해 작업의 결과를 받아오는 식으로 사용합니다. get() 메소드를 통해 Future 객체에 담긴(담길) 작업 결과를 얻을 수 있습니다.
  - Callback 구현: B에게 맡긴 작업이 끝나면 B 쪽에서 A가 전해 준 콜백 함수를 실행하는 방법입니다. 인터페이스를 만들어 처리합니다. 

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
  - 메세지 큐를 사용하는 것은 비동기적이며 확장성이 있기 때문입니다. 예컨대 모든 서비스는 서버가 잠시 구동되지 않을 때를 고려해야 합니다. 이때 요청은 서버의 응답을 받지 못하고 없어질 수 있는데, 메세지 큐가 있다면 여기에 쌓인 요청이 나중에 실행될 것입니다. 고용량 이미지나 비디오를 업로드하여 블로그 포스팅을 하는 경우에도 메세지 큐가 사용됩니다. 사용자에게 블로그가 포스팅되었다고 알리는 동시에 애플리케이션은 고용량 자료를 최적화해야 합니다. 최적화 서비스의 메시지 큐에 담아서 처리한다면 메모리 부하를 분산할 수 있고, 추후 확장을 할 때도 용이합니다. 

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
  - https://github.com/bytenari/roobits 
    코드스테이츠 백엔드 부트캠프 과정을 수료하며 팀원들과 함께 만든 프로젝트입니다. 제가 맡은 부분은 Room 단이며 CRUD기능이 모두 포함되어 있습니다. 
  - https://github.com/bytenari/focusmediakorea_task
    얼마 전 취업을 위해 과제전형에서 작성한 코드입니다. C, R, D만 있습니다. 

