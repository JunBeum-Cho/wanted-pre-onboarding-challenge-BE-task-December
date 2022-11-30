## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
동기는 실행된 함수가 실행이 종료될때까지 기다리는 방식이고,
비동기는 실행된 함수가 실행이 종료될때까지 기다리면서 다른 함수가 실행될 수 있는 방식입니다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
블로킹은 동기함수가 실행됬을때 이 함수가 실행중 일때 다른 함수를 실행 할 수 없고 현재 실행되고 있는 함수가 끝날때까지 다른 함수의 실행을 막고있는 상태이고,
논블로킹은 비동기 함수처럼 함수가 실행중일때 다른 함수도 실행될 수 있는 상태입니다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
python의 경우 동기화 언어이기때문에  import asyncio 로 비동기화 함수를 사용하기위한 모듈을 가져와야 사용이 가능합니다. async def main(): 처럼 함수정의시 앞에 async를 붙여주고 호출시 asyncio.run(main()) 를 사용하는 방식처럼 asynio내의 함수들을 이용해서 사용해주어야합니다.

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
어플리케이션과 DB사이에서 서버의 이상이 생겼을때 데이터의 중복전송이 될 경우를 방지할 수 있습니다.
예를 들어 게시판에 글을 작성할때 이용자가 게시판에 글을 작성하고 완료를 눌렀을때, 서버와의 접촉상태가 원활하지 않을 시, 완성된 게시물의 전송과정에서 대기시간을 참지못해 이용자가 재전송을 요구하는 경우를 줄일 수 있음.
또한 비동기 방식이지만 빠른 전송속도를 요구하지 않는경우인, 회원가입시 이메일인증과 같은 경우에 사용하여 이메일이 기다리는 동안 유저들이 다른작업을 할 수 있게 로딩페이지에 묶어두지 않음.
 
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
https://github.com/JHyeok-Choi/testback

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
