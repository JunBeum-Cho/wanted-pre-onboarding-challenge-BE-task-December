## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요. 
```
- 동기 프로그래밍 : 프로그램이 동작하는 과정을 쪼개 단위시간을 만든다. 이 단위시간을 동안 어떠한 과정이 동작하고 결과가 나오게 한다.
- 비동기 프로그래밍 : 하나의 과정이 동작하고 결과가 나오기만 하면 된다.
- 차이점 : 단위 시간이라는 개념이 존재하지 않기 때문에 어떠한 작업의 시간이 짧다면 동기 프로그래밍보다 훨씬 효율적이게 동작된다. 
  더 길 경우에도 비동기 프로그래밍이 더욱 효율적이다. 
  예를 들어 단위시간 기준으로 2.3단위시간의 동작이 있을 때 동기 프로그래밍에서는 3단위시간을 사용하며 0.7단위시간의 잉여시간이 발생한다. 
  하지만 비동기 프로그래밍에서는 2.3단위시간의 작업이 끝나면 바로 다음 작업이 들어올 수 있다.
```
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
```
- 블로킹 : 두 함수가 X, Y가 존재할 때, X가 Y를 호출할 때 제어권을 넘긴다. 
  제어권이 없는 X는 동작을 멈추고 제어권을 받은 Y가 동작한다. 
  이후 Y가 완료되면 X가 다시 제어권을 받고, 이 제어권을 받아 X를 재실행한다. 
- 논블로킹 : 두 함수 X, Y가 존재할 때, X가 Y를 호출해도 제어권을 X가 가지고 있는다. 
  제어권이 X에 있기 때문에 Y가 실행되는 동안에도 X가 진행될 수 있다. 
  X를 http에서는 서버가 될 수 있고, OS에서 쓰레드가 될 수 있다 .
- 차이점 : 시간의 차이가 존재한다. X라는 서버가 블로킹일 경우, Y가 호출되어 완료될 때 까지 아무 동작도 할 수 없게 된다. 
  이로 인해 서버의 입장에서는 잉여시간이 발생한다. 
  비동기의 경우 X가 Y를 호출하고 나서도 X는 다른 일을 할 수 있다. 
```
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
```
- 자바의 비동기 프로그래밍 : Thread를 사용합니다. 
  ThreadPool을 이용해 여러 쓰레드 풀에 명령을 내려 서로 다른 동작을 하게 할 수 있다. 
  명시적으로 다른 쓰레드를 통해 명령을 전송하므로, 동작의 완료여부, 결과 확인을 위해 Callback을 이용하기도 한다. 
  Callback을 통해 멀티 쓰레드에서 메인 서버에 동작이 완료됨을 알려줄 수 있다. 
  반대의 방식으로 메인이 계속해서 쓰레드에 완료여부를 확인하는 방법으로는 Future을 사용하기도 한다. 
  하지만 이런 Future의 방식은 사용할 시 메인 서버가 쓰레드의 응답을 받을 때 까지 동작을 할 수 없는 블로킹 상태가 된다. 
  보통은 CallBack을 사용하지만, Future의 방식을 사용하기 위해 CompletableFuture을 사용하기도 한다. 
```
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
```
- 메세지 큐는 일반적으로 핵심작업보다는 어플리케이션의 부가적인 기능에 사용하는게 적합한 기능이다. 
  꼭 사용할 정보라고 보장되진 않더라도, 언젠가 생산자에게서 가져가 소비자가 가져가 사용해 처리될 것이라고 믿는것이 전제된다. 
  가져가 바로 사용되어 처리되기 때문에 비동기적이다.
  예시 1) 작업에 응답이 필요하지 않은 경우 : 
  비밀번호를 잃어버려서 이메일을 통해 임시 비밀번호를 받거나, 
  새로운 환경에 로그인 되었다고 메일이 올 때 처럼 특정 메일을 확인하고 응답이 필요하지 않을 때, 
  메세지 큐를 통해 늦게라도 송신되며 응답이 필요하지 않는 경우에 사용할 수 있다. 
  예시 2) 동시에 많은 요청이 들어오는 경우 : 
  이 때 클라이언트는 서버의 응답을 기다리다가 타임아웃 되면 연결이 종료된다. 
  이를 메세지 큐를 이용해 job scheduler처럼 활용 할 수 있다. 
```
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
```
  https://github.com/JangAJang/ShoppingMall
  간단한 쇼핑몰 프로젝트를 계속해서 리펙토링하고 있는 레포지토리입니다. 
  https://github.com/JangAJang/Do-the-meeting-now
  지하철 노선도에서 중간 만남 지점을 구하려고 만들었던 서버 레포지토리입니다. 
```
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
```
  저는 배포에 대해서 아직 공부해본 적이 없습니다. 
  AWS와 도커, 쿠버네티스등 다양한 정보에 대해서 찾아보고 이에 대해 읽어보긴 했지만 찬찬히 뜯어보고 공부하고 사용해보질 않았습니다. 
  간단한 정보를 넘어서 이들의 특성이나 사용시의 특이점등에 대해서 알아보고 싶습니다. 
```
