## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
      *동기 : 다른 함수를 호출한 뒤, 리턴값을 기다리는 것(계속해서 작업이 끝났는지 확인)
             순차적인 흐름에 따라 작업을 동시에 수행하거나 동시에 끝내거나 끝나는 동시에 시작하거나 한다.
      *비동기 : 다른 함수를 호출할 때 콜백함수도 전달하고, 리턴값을 기다리지 않는 것
            시작과 종료 시간이 일치하지 않으며 끝나는 동시에 시작하지도 않는다
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
      *블로킹 : 다른 함수를 호출할 때 제어권을 넘겨줘서 실행이 잠시 멈췄다 제어권이 돌아오면 실행한다.
      *논블로킹 : 다른 함수를 호출해도 제어권은 그대로 가지고 있어서 별개로 계속 실행한다. 
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
      Java에서는 Future 객체를 사용하는 방식과 Callback을 구현하는 방식이 있다.
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
      *비동기 처리 
      *탄력성(일부 실패에도 전체에 영향을 받지 않음)
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 현재 없음
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
