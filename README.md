## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  동기 - 요청과 그 결과가 동시에 일어난다는 뜻으로 요청을 하면 요청한 자리에서 결과가 주어진다.
  비동기 – 서버에게 데이터를 요청한 후 요청에 따른 응답을 계속 기다리지 않아도 된다. 다른 활동을 수행하거나 다른 요청사항을 보내도 된다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
  블로킹 - 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 자신의 작업을 멈추고 다시 자신의 작업을 시작한다.
  논블로킹 – 다른 주체의 작업을 관련없이 자신의 작업을 하는 것을 의미한다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  자바는 Future라는 클래스로 비동기 처리를 해왔는데 Future에는 블로킹 코드(get)를 통해서만 이후의 결과를 처리할 수 있다는 한계점이 존재해 그것을 해결해줄 CompletableFuture(jdk 1.8)이 등장했다.
Future 예제
ExecutorService는 Single Thread를 생성합니다.
 submit()으로 Callable을 전달하면, 인자로 전달된 Callable을 수행
future.get()는 Future 객체에 어떤 값이 설정될 때까지 기다립니다. 
submit()에 전달된 Callable이 어떤 값을 리턴하면 그 값을 Future에 설정합니다

  ExecutorService executor
          = Executors.newSingleThreadExecutor();

  Future<Integer> future = executor.submit(() -> {
      System.out.println(LocalTime.now() + " Starting runnable");
      Integer sum = 1 + 1;
      Thread.sleep(3000);
      return sum;
  });

CompletableFuture - runAsync,supplyAsync
runAsync와 supplyAsync는 기본적으로 자바7에 추가된 ForkJoinPool의 commonPool()을 사용해 작업을 실행할 쓰레드를 쓰레드 풀로부터 얻어 실행시킨다. 만약 원하는 쓰레드 풀을 사용하려면, ExecutorService를 파라미터로 넘겨주면 된다.

runAsync 예제
  
      void runAsync() throws ExecutionException, InterruptedException {
      CompletableFuture<Void> future = CompletableFuture.runAsync(() -> {
          System.out.println("Thread: " + Thread.currentThread().getName());
      });

      future.get();
      System.out.println("Thread: " + Thread.currentThread().getName());
      }

SupplyAsync 예제

     void supplyAsync() throws ExecutionException, InterruptedException {

      CompletableFuture<String> future = CompletableFuture.supplyAsync(() -> {
          return "Thread: " + Thread.currentThread().getName();
      });

      System.out.println(future.get());
      System.out.println("Thread: " + Thread.currentThread().getName());
      }

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
  메시지는 메시지 큐에 남아 있어 소비자 서비스가 다시 시작될 때마다 추가 설정이나 작업을 수행하지 않고도 메시지 처리를 시작할 수 있다
  기존 동기화 방식에 비해 메시지 큐는 생산된 메시지의 저장, 전송에 대해 동기화 처리를 진행하지 않고, 큐에 넣어 두기 때문에 나중에 처리할 수 있다.

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
  https://github.com/jeeyoun-kang/Movie-Website-SpringBoot
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
  EC2,RDS를 포함한 AWS에서 제공하는 다양한 서비스를 알아보고 싶고 이번 현업에서 쓰이는 서비스를 개발해보고 싶습니다.
