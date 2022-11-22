## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

1. 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

- 호출되는 함수의 작업 완료 여부를 신경쓰냐에 따라, 함수 실행/리턴 순차적인 흐름을 따르느냐, 안따르냐가 관심사
    1. 동기
        - A가 함수 B를 호출한 뒤, 함수 B의 작업 완료 여부를 계속 확인 하면서 신경쓰는 것
    2. 비동기
        - A가 함수 B를 호출한 뒤, 함수 B의 작업 완료 여부를 신경쓰지 않는 것

2. 블로킹과 논블로킹의 차이점을 설명해주세요.

- 처리되어야 하는 (하나의) 작업이, 전체적인 작업 '흐름'을 막느냐 안막느냐에 대한 관점
- 제어권이 누구한테 있느냐가 관심사
    1. 블로킹
        - A 함수가 B 함수를 호출하면, 제어권을 A가 호출한 B 함수에 넘겨준다.
    2. 논블로킹
        - A 함수가 B 함수를 호출해도 제어권은 그대로 자신이 가지고 있는다.

3. 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

- 자바 8에서 부터 지원하는 CompletableFuture 인터페이스를 사용하여 비동기 프로그래밍을 구현할 수 있다.

runAsync는 반환 값이 없으므로 Void 타입이며, 아래의 코드를 실행해보면 future가 별도의 쓰레드에서 실행됨을 확인할 수 있다.

```java
@Test
void runAsync()throws ExecutionException,InterruptedException{
		CompletableFuture<Void> future=CompletableFuture.runAsync(()->{
		System.out.println("Thread: "+Thread.currentThread().getName());
		});

		future.get();
		System.out.println("Thread: "+Thread.currentThread().getName());
		}
```

supplyAsync는 runAsync와 달리 반환값이 존재한다. 그래서 비동기 작업의 결과를 받아올 수 있다.

```java
@Test
void supplyAsync()throws ExecutionException,InterruptedException{

		CompletableFuture<String> future=CompletableFuture.supplyAsync(()->{
		return"Thread: "+Thread.currentThread().getName();
		});

		System.out.println(future.get());
		System.out.println("Thread: "+Thread.currentThread().getName());
		}
```

4. 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
    1. 데이터 손실 방지
        - consumer가 broker에 처리 완료에 대한 응답을 주지 않은 경우(메세지 처리 중 문제가 발생하는 경우) 브로커는 큐에 메세지를 다시 넣어 처리할 수 있게 할 수 있음
    2. 부하 분산에 용이하다.
        - 한 큐에 여러 consumer가 존재할 수 있기 때문에 부하 분산이 가능하고, Scaling 대응에 적합하다.

5. 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)