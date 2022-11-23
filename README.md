## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

    ### 동기
    - 요청과 결과가 동시에 일어난다는 약속
    - 요청을 하면 시간이 얼마나 걸리던지 요청한 곳에서 결과가 주어져야 한다.
    - 장점 : 설계가 간단하고 직관적임
    - 단점 : 결과가 주어질 때까지 아무것도 못하고 대기해야 함

        ![image](https://user-images.githubusercontent.com/37575974/203498511-fa4d2175-3ec4-402a-9c20-3df69f871795.png)

    ### 비동기
    - 요청과 결과가 동시에 일어나지 않을 거라는 약속
    - 하나의 요청에 대한 응답을 즉시 처리하지 않고, 대기 시간동안 다른 요청에 대해 처리 가능하다.
    - 장점 : 대기하는 시간 없이 다른 작업을 할 수 있으므로 자원을 효율적으로 사용할 수 있음
    - 단점 : 동기보다 설계가 복잡함

        ![image](https://user-images.githubusercontent.com/37575974/203498717-37a70fa0-198b-4152-841f-eaf1c898f9c8.png)

<br>

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
    ```
    동기와 비동기와 개념을 햇갈릴 수 있지만, 
    동기와 비동기는 작업을 수행하는 주체가 2개 이상이어야 하지만, 
    블로킹과 논블로킹은 작업의 대상이 2개 이상이어야 한다.
    ```

    ### 블로킹
    - A 함수가 B 함수를 호출하면 제어권을 A가 호출한 B 함수에게 넘겨준다.
    - 제어권을 넘겨받은 B는 함수를 실행한다. A는 아무것도 안함
    - B 함수는 실행이 끝나면 A에게 제어권을 돌려준다. 

    ### 논블로킹
    - A 함수가 B 함수를 호출해도 제어권은 자신이 가지고 있는다.
    - A 함수가 제어권을 계속 가지고 있어 B를 호출한 이후에도 자기 할거 한다.

<br>

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
    ### Future 인터페이스
    - Java5 에 Furture가 추가되어 비동기 작업에 대한 결과값을 반환 받을 수 있게 했다.
    - 하지만, 블로킹 코드를 통해서만 이후 결과를 처리할 수 있고, 여러 작업을 조합할 수 없는 한계가 있다.

    ### CompletableFuture
    - Java8 에서 Furter를 기반으로 외부에서 작업을 완료시킬 수 있게 `CompletableFuture` 가 등장
    - `runAsync`는 반환값이 없고, future가 별도의 스레드에서 실행됨.
    - `supplyAsync`는 반환값이 있고, future가 별도의 스레드에서 실행됨.

    ```java
    void runAsync() throws ExecutionException, InterruptedException {
        CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
            System.out.println("future 스레드: " + Thread.currentThread().getName());
        });

        future.get();
        System.out.println("main 스레드: " + Thread.currentThread().getName());
    }

    void supplyAsync() throws ExecutionException, InterruptedException {

        CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
            return "future 스레드: " + Thread.currentThread().getName();
        });

        System.out.println(future.get());
        System.out.println("main 스레드: " + Thread.currentThread().getName());
    }
    ```

<br>

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

    ### 1. 이메일 전송
        - 비밀번호를 잊어버려 이메일을 통해 임시 비밀번호를 받을 때 사이트에서 인증번호를 사용자 메일로 보내준다.
        이 때 사용자는 이메일이 즉각적으로 수신되는 것을 기대하지 않고 그냥 기다린다.
        어느 정도의 응답 지연이 허용되는 핵심 기능이 아닌 경우에는 메시지 큐를 사용하면 유용하다

        - 큐에 비밀번호 재설정을 위해 발급하는 서비스 메시지를 넣는다.
        - 메일 전송 서비스는 이메일이 어느 서비스로부터 생산되었는지 관계 없이, 메시지 큐의 메시지를 하나씩 소비하고 이메일을 전송한다.
        - 메시지 큐에 메시지 수가 많이 들어온다면, 메일 전송 서비스 인스턴스를 추가로 둬 확장할 수 있다.

    ### 2. 블로그 포스팅
        - 블로그 사용자가 이미지를 올리는 경우 큰 용량을 올릴 때는 업로드한 이미지를 즉시 처리하지 않는다. 
        사후처리하며 최적화할 수 있다.
        
        - 사용자가 용량이 큰 이미지를 포스팅한다.
        - 이미지는 저장소에 전송된다.
        - 업로드된 이미지에 대한 정보가 포함된 메시지를 큐에 담는다.
        - 저장소에서 이미지를 가져와 최적화한다. 

<br>

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

    - github repo : https://github.com/MBTI-Channel/server

    - mbti 기반의 커뮤니티 사이트의 백엔드 서버를 담당했습니다.
      배포는 도커로 감싸서 aws ec2에 배포하였습니다.


<br>

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

    - 인프라 구조에 깊이있는 공부를 한적이 없어서 이번 기회에 제대로 된 인프라 구조에 대한 지식을 습득하고 싶습니다.