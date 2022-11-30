## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

#### (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

> 기준 : `결과를 돌려주었을 때 순서와 결과에 관심이 있는지 아닌지`

- 동기(Synchronous : 동시에 일어나는)
  - 동시에 일어난다는 뜻으로, 요청과 그 결과가 동시에 일어난다는 약속입니다.
  - 바로 요청을 하면 시간이 얼마가 걸리든지 요청한 자리에서 결과가 주어져야 합니다.
  - A노드와 B노드 사이의 작업 처리 단위(transaction)를 동시에 맞추겠다는 의미입니다.
  
- 비동기(Asynchronous : 동시에 일어나지 않는)
  - 동시에 일어나지 않는다는 뜻으로, 요청과 결과가 동시에 일어나지 않을 것이라는 약속입니다.
  - 요청한 그 자리에서 결과가 바로 주어지지 않습니다.
  - 노드 사이의 작업 처리 단위를 동시에 맞추지 않아도 됩니다.

|  | 장점 | 단점 |
| --- | --- | --- |
| 동기 | 의뢰한 처리가 끝났는지 여부를 쉽게 확인할 수 있어서 구조가 간단하고 구현 난이도도 낮다 | 의뢰한 처리가 끝나기까지 기다려야 하기 때문에 대기 시간을 활용할 수 없다 |
| 비동기 | 의뢰한 처리가 진행되고 있는 동안 시간을 효율적으로 사용해서 병렬 처리를 할 수 있다 | 의뢰한 처리가 끝났는지 확인하지 않으면 모르기 때문에 불필요한 확인 처리가 늘어난다. 구조가 복잡해서 구현 난이도가 높다 |

---

#### (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

> 기준 : `다른 주체가 작업할 때 자신의 제어권이 있는지 없는지`

- 블로킹(Blocking)
  - A 함수가 B 함수를 호출하면, 제어권을 B에게 넘겨줍니다.
  - 제어권을 넘겨받은 B는 함수를 실행합니다. 이때, A는 B에게 제어권을 넘겨주었기 때문에 함수 실행을 멈춥니다.
  - B 함수의 실행이 끝나면 A 함수에게 제어권을 돌려줍니다.
  - 즉, 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 끝날 때까지 기다렸다가 자신의 작업을 시작하는 것을 블로킹이라고 합니다.

- 논블로킹(Non-Blocking)
  - A 함수가 B 함수를 호출해도 제어권은 그대로 A 함수가 가지고 있습니다.
  - A 함수는 제어권을 계속 가지고 있기 때문에 B 함수를 호출한 뒤에도 자신의 코드를 계속 실행합니다.
  - 즉, 다른 주체의 작업에 관련없이 자신의 작업을 하는 것을 논블로킹이라고 합니다.

---

#### (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

`Asynchronous Programming in Java`

**Thread**
  - 모든 작업을 비동기적으로 수행하기 위해 새 스레드를 만들 수 있습니다.
  - 다음은 숫자의 계승을 계산하고 출력하는 스레드입니다.

```java
int number = 20;
Thread newThread = new Thread(() -> {
    System.out.println("Factorial of " + number + " is: " + factorial(number));
});
newThread.start();
```

**FutureTask**
  - Java 5부터 Future 인터페이스는 FutureTask를 사용하여 비동기 작업을 수행하는 방법을 제공합니다.
  - ExecutorService의 submit 메서드를 사용하여 작업을 비동기적으로 수행하고 FutureTask의 인스턴스를 반환할 수 있습니다.
  - Future 인터페이스에서 제공하는 isDone 메서드를 통해 작업이 완료되었는지 확인할 수 있습니다. 
  - 완료되면 get 메소드를 사용하여 결과를 검색할 수 있습니다.

```java
ExecutorService threadpool = Executors.newCachedThreadPool();
Future<Long> futureTask = threadpool.submit(() -> factorial(number));

while (!futureTask.isDone()) {
    System.out.println("FutureTask is not finished yet..."); 
} 
long result = futureTask.get(); 

threadpool.shutdown();
```

**CompletableFuture**
  - CompletableFuture는 Future와 CompletionStage를 구현한 클래스로, Java 8부터 도입되었습니다.
  - 비동기 프로그래밍을 위해 supplyAsync, runAsync 및 thenApplyAsync와 같은 다양한 메서드를 제공합니다.
  - Future이지만 직접 스레드를 생성하지 않고 async로 작업을 처리할 수 있고, 여러 CompletableFuture를 병렬로 처리하거나, 병합하여 처리할 수 있습니다.
  - ExecutorService를 명시적으로 사용할 필요가 없으며, CompletableFuture는 작업을 비동기적으로 처리하기 위해 내부적으로 ForkJoinPool을 사용합니다.

```java
CompletableFuture<Long> completableFuture = CompletableFuture.supplyAsync(() -> factorial(number));
while (!completableFuture.isDone()) {
    System.out.println("CompletableFuture is not finished yet...");
}
long result = completableFuture.get();
```

---

#### (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

1. 장애 복원력
- 시스템 일부에 장애가 발생하더라도 시스템 전체로 확대되지 않게 합니다. 메세지가 큐에 추가되어 있기 때문에 어떤 모듈에서 장애가 발생하였더라도 해당 모듈 복구 후 작업을 마저 수행할 수 있습니다. 즉, 메시지 큐를 사용하면 애플리케이션 간 상호 운용성을 향상시켜서 시스템 전체 안정성을 향상시킬 수 있습니다.

2. 낮은 결합도와 확장성
- 생산자 서비스와 소비자 서비스가 독립적으로 행동하게 됨으로써 서비스 간 결합도가 낮아집니다.
- 예를 들어, 이미지 보정 애플리케이션을 만든다고 가정해 보겠습니다. 샤프닝, 블러링 등의 보정 작업은 시간이 많이 걸리기 때문에 비동기적으로 처리하는 것이 유리합니다. 따라서 서버는 보정 작업이 필요한 이미지를 메시지 큐에 발행하고, 실제 보정 작업을 수행하는 프로세스들은 작업을 메시지 큐에서 꺼내서 비동기적으로 처리합니다. 이렇게 하면 웹 서버와 보정 작업 프로세스를 각각 독립적으로 확장할 수 있습니다.

---
#### (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
- https://github.com/Inno-8080/sorisam-backend-server

#### (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

AWS EC2, S3 등을 사용해 본 경험이 있지만 깊이 있게 학습하고 고민해 봤다고 자신할 수 없습니다. 이번 기회에 백엔드 개발자로서 필수적으로 알아야 하는 AWS 인프라에 대해 제대로 학습하고, 현업에서 주니어 개발자에게 요구하는 역량을 쌓고 싶습니다.
