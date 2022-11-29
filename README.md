## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
    동기 - 요청과 결과에 동시에 일어나는 방식이다. 해당 요청에 대한 결과를 바로 주어져야 하기에 순서에 맞춰 진행되기에는 좋지만
    오랜 시간이 걸리는 로직이 먼저 실행 중이면 후 순위 요청들이 대기를 해야 한다.
    비동기 - 요청에 대한 결과가 동시에 일어나니 않는 것으로 요청이 들어와도 후순위로 결과가 주어 질 수 있다.
    덕분에 여러 개의 요청을 동시에 처리 할 수 있는 장점이 있지만 상대적으로 동기 요청보다는 속도가 떨어 질 수 있다. 

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
    Block, 전체적인 작업 흐름을 막는지에 따라 정해진다.
    블로킹 - 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 자신의 작업을 멈추고 해당 작업을 기다렸다가 자신의 작업을 시작한다.
    논블로킹 - 블로킹과 다르게, 다른 주체의 작업에 관련 없이 자신의 작업을 하는 것을 의미한다.
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
   자바 - Future, CompletableFuture, CallBack 등을 사용하는 방법이 있다.
     
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
   - 비동기 요청이 가능하다.
   - 서버 부하가 많은 작업의 경우 원하는 만큼만 메세지 소비를 할 수 있다.
    
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
   개인 사이드 프로젝트
   https://github.com/JHyunJung/yummy
    
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
   - AWS API Gateway, Lambda, EC2 만큼은 꼭 완벽히 이해 하고 배워서 끝내고 싶습니다.
