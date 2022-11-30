## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
	- 동기와 비동기는 프로세스의 수행 순서 보장에 대한 작동방식.
	- 동기 :  호출하는 함수 A가 호출되는 함수 B의 리턴을 기다리거나, 바로 리턴 받더라도 미완료 상태라면 작업 완료 여부를 계속 확인하며 기다리는 것.
	- 비동기 : A가 B를 호출할 때 콜백 함수를 함께 전달해서, 함수 B의 작업이 완료되면 함께 보낸 콜백 함수를 실행한다. 즉, 함수 A는 함수 B를 호출한 뒤 B의 작업 완료 여부는 신경쓰지 않는다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
	- 블로킹과 논블로킹은 프로세스의 유휴 상태에 대한 개념. 제어권이 누구한테 있는지가 중요한 관심사
	- 블로킹 : A함수가 B함수를 호출하면 제어권을 A가 B에게 넘겨준다. 제어권을 넘긴 후 A는 함수실행을 잠시 멈춘뒤 B가 실행종료되면 제어권을 다시 넘겨받는다.
	- 논블로킹 : A함수가 B함수를 호출해도 제어권은 그대로 자신이 가지고 있는다. B함수를 호출한 이후에도 자신의 코드를 계속 실행한다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
	- 주로 사용하는 언어 : JAVA
	- 자바에서는 Thread 클래스를 사용하여 비동기프로그래밍을 하며, 크게 Future 객체를 사용하는 방식과 Callback을 구현하는 방식이 있다. Future는 다른 주체에게 작업을 맡긴 상태에서 본 주체 쪽에서 작업이 끝났는지 직접 확인하는 방법이고, Callback은 다른 주체에게 맡긴 작업이 끝나면 다른 주체 쪽에서 본 주체가 전해준 콜백함수를 실행하는 방법이다.
  
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
	- 이벤트들 간의 순서를 보장할 수 있다. 여러 서비스에서 동시에 많은 이벤트가 발생하는 상황에서 이벤트 간 일련의 순서를 지키고 싶을 때 메시지 큐를 사용하면 순서를 보장할 수 있다.
	- 이벤트를 보내고 받고 그 결과 처리를 기다리지 않을 수 있다. 즉, 이벤트 처리를 비동기로 진행할 수 있고 이를 통해 서비스 간 결합도를 낮출 수 있다. 이벤트를 발생시키는 쪽은 어느 서비스에 이벤트를 보내줄지 신경쓰지 않고 메시지 큐에만 넣으면 되고 이벤트를 받는 쪽은 메시지큐에 원하는 이벤트가 들어왔을 때만 이벤트를 받아서 처리하면 된다. 
  
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
	- https://github.com/ewqsaz123/triple_homework_project

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
	- AWS Lambda 에 대해 항상 공부하고 싶었는데 이번 기회에 제대로 배우고 싶습니니다.
