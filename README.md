## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  - 동기와 비동기는 특정 작업을 수행할 때 해당 작업의 완료 여부를 신경쓰는지에 따라 구분된다.
  - 동기: A함수가 B함수를 호출하여 작업을 수행할 때, A함수가 B함수가 종료될 때까지 기다리다가 그 결과값을 받고나서 다음 작업을 수행하는 경우
  - 비동기: B함수의 종료까지 기다리지 않고 A함수가 다음 작업을 수행한다. 이때 B함수의 작업 결과는 콜백함수로 반환된다.
 
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
  - 블로킹, 논블로킹은 작업을 수행할 때 제어권이 누구한테 있는지에 따라 구분된다. 호출되는 함수가 바로 리턴하느냐 마느냐가 관심사이다.
  - 블로킹: 특정 작업을 수행할 때 작업이 완료될 때까지 제어권을 반환하지 않는다. 작업의 수행이 완료될 때까지 계속 대기하다가 작업이 완료되면 제어권을 받아서 다른 작업을 수행한다.
  - 논블로킹: 해당 작업을 바로 완료할 수 없는 경우에 제어권을 먼저 반환하여 해당 작업을 호출한 쪽에서 다른 작업을 수행할 수 있는 기회를 준다.
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  - Asynchronous Programming in Java
    1. Thread
      - new thread 를 생성하여 비동기적으로 작업을 수행할 수 있다. Java 8에서 람다 표현식이 출시되면서 더우 깔끔하고 가독성이 높아졌다.
      ```
      int number = 20;
      Thread newThread = new Thread(() -> {
        System.out.println("Factorial of " + number + " is: " + factorial(number));
      });
      newThread.start();
      ```
    2. FutureTask
    - Java 5 부터 Future interface 가 `FutureTask` 를 사용하여 비동기 작업을 수행하는 방법을 제공한다. `ExecutorService` 의 submit 메서드를 사용하여 작업을 비동기적으로 수행하고 FutureTask 의 인스턴스를 반활할 수 있다.
    ```
    ExecutorService threadpool = Executors.newCachedThreadPool();
    Future<Long> futureTask = threadpool.submit(() -> factorial(number));

    while (!futureTask.isDone()) {
        System.out.println("FutureTask is not finished yet..."); 
    } 
    long result = futureTask.get(); 

    threadpool.shutdown();
    ```
    3. CompletableFuture
    - Java 8은 Future와 CompletionStage가 결합된 CompletableFuture를 도입했다. 비동기 프로그래밍을 위해 supplyAsync, runAsync 및 thenApplyAsync 와 같은 다양한 메서드를 제공한다.
    ```
    CompletableFuture<Long> completableFuture = CompletableFuture.supplyAsync(() -> factorial(number));
    while (!completableFuture.isDone()) {
        System.out.println("CompletableFuture is not finished yet...");
    }
    long result = completableFuture.get();
    ```
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
  - 애플리케이션 / 시스템 간의 통신
    - 서버 간에 데이터를 주고 받거나 어떤 작업을 요청할 때는 항상 시스템 장애를 염두에 두어야 한다. 서버가 갑자기 죽거나 서버 점검 등으로 다운타임이 발생하는 동안에는 요청을 보낼 수 가 없다. 요청하는 서버에서 failover 처리를 해놓고 연계 시스템이 다시 살아났을 때 요청을 보내는 방도 있지만 MQ를 이용하면 더욱 간편하게 처리할 수 있다. producer는 consumer에 직접 요청하는 것이 아닌 MQ에 전달한다. 그럼 consumer는 MQ로부터 요청 데이터를 수신해서 처리한다. 만약 consumer가 요청을 받을 수 없는 상황이라면 해당 요청은 consumer가 받을 때까지 MQ에 머무르게 된다.
  - 서버 부하가 많은 작업
    - 이미지 처리, 비디오 인코딩, 대용량 데이터 처리와 같은 작업은 메모리와 CPU를 많이 사용한다. 이러한 작업은 동시에 처리할 수 있는 양이 상당히 한정적이어서 필요하다고 무작정 요청을 처리할 수는 없다. 이 때 처리해야 할 작업을 MQ에 넣어두고 서버는 자신이 동시에 처리할 수 있는 양에 따라 하나의 작업이 끝나면 다음에 처리할 작업을 MQ에서 가져와 처리하면 된다.
    
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
  - https://github.com/sojournre/seb39_main_054
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
