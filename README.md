## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  - 프로세스 수행 순서 보장에 대한 매커니즘에 대한 개념
  - 데이터 처리 모델은 크게 동기식 처리 모델과 비동기식 처리모델로 나눌 수 있다.
  - 데이터 처리 모델이라 함은 클라이언트의 요청에 따라 서버에서 전송한 데이터 값을 어떻게 받느냐에 대한 방식을 의미한다.
  - 작업을 수행하는 주체가 두 개 이상을 전제한다.
  - 동기와 비동기 방식은 요청 후 데이터 값을 받기 전까지 다른 작업을 할 수 있는지에 대한 여부가 다르다.
    - 동기: 작업을 수행하는 두 개 이상의 주체가 서로 동시에 시작점과 종료점을 일치하도록 처리하는 것을 의미
        == 요청에 대한 서버 응답(데이터 전송)이 이루어질 때까지 다른 작업을 하지 못한 채 대기해야 함.
        == 요청과 결과가 한 자리에서 동시에 발생 (직렬적)
    - 비동기: 작업을 수행하는 두 개 이상의 주체가 다른 주체의 시작 및 종료시간과 별도로 각각의 작업 시작점과 종료점을 가지는 것을 의미
        == 요청에 대한 서버 응답이 그 자리에서 바로 이루어지지 않음. 그 사이에 다른 작업이 가능하다
        == 요청한 자리에서 결과가 주어지지 않음 (병렬적) 
  
  
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
  - 프로세스의 유휴 상태에 대한 개념
  - 블로킹과 논블로킹은 함수 호출 시 제어권에 대한 처리 방식이 다르다
  - 제어권이란 자신의 코드를 실행할 권리을 의미
  - 제어권을 가지는 함수는 자신의 코드를 끝까지 실행한 뒤 자신을 호출한 함수에게 자신의 값을 돌려준다
  - 블로킹과 논블로킹은 처리되어야 하는 하나의 작업이 전체적인 작업의 흐름을 막는지에 대한 여부가 다르다
    - 블로킹: 자신(A)의 작업을 수행하다가 다른 주체(B)의 작업이 시작되면 B가 끝날 때까지 A작업을 하지 않고 B가 완료가 된 후에야 자신의 작업(A)을 시작
    - 논블로킹: 다른 주체(B)의 작업여부와 상관없이 자기 자신(A)의 작업을 수행 (B를 호출하고서도 A함수는 중단없이 이어서 실행)
  
  
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  - Java: 비동기 처리를 위해 Thread 사용
  - Javascript: setTimeout()함수, Promise 객체, fetch 내장 라이브러리, jQuery + Ajax 활용.
  
  
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
  - 메세지 큐(Message Queue): 프로세스 또는 프로그램 간에 데이터를 교환할 때 사용하는 통신 방법
    == 일종의 메세지 임시 저장소(버퍼)
    - 클라이언트의 요청과 서버 응답 간의 차이가 있는 비동기 구조에서 사용이 용이하다
  - 이유 1) 부하 분산을 위해 유용하게 활용할 수 있음
  - 이유 2) 아직 처리되지 않은 데이터의 손실을 방지할 수 있음 


- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
  - 아직 개인 프로젝트를 해보지 않아 팀 프로젝트용만 있습니다.
  - 세미 프로젝트
    - https://github.com/Euiseon-Lee/KH3_Semi.git
    - 후기게시판 및 결제기능 구현 (API 미연동)
  - 파이널 프로젝트 
    - https://github.com/Euiseon-Lee/KH1_FINAL.git
    - 로그인, 계정찾기, 회원가입, 마이페이지 수정 및 탈퇴, 자동로그인 기능 구현


- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
  - 신입 개발자가 알아야하는 기본적인 인프라 구조에 대해 공부하고 싶습니다. 
  - 현업에서 활용하는 실제적인 지식을 기반으로 했으면 좋겠습니다.
