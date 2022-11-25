## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

---

### (1) ‘Synchronous’와 ‘ASynchronous’의 차이

1. 동기(Synchronous)는 작업은 한 번에 하나씩 수행되며 하나가 완료될 때만 다음 작업이 차단(Blocking) 해제됩니다. 즉, 다음 작업으로 이동하려면 작업이 완료될 때까지 기다려야 합니다.

순서에 맞춰 진행되는 장점이 있지만,  여러 가지 요청을 동시에 처리할 수 없다.

2. 비동기(Asynchronous)는 이전 작업이 완료되기 전에 다른 작업으로 이동할 수 있습니다. 이러한 방식으로 비동기 프로그래밍을 사용하면 여러 요청을 동시에 처리할 수 있으므로 훨씬 짧은 시간에 더 많은 작업을 완료할 수 있습니다.

여러 개의 요청을 동시에 처리할 수 있는 장점이 있지만 동기 방식보다 속도가 떨어질 수도 있다.

‘Blocking, Non-Blocking’과 ‘Sync, Async’은 굉장히 유사점을 가지고 있어서 이를 정리하자면, 다음 표와 같다.

![image](https://user-images.githubusercontent.com/88137420/203763737-69f69741-0221-415d-b421-8201e27c0afb.png)

<참고>

[Asynchronous vs. Synchronous Programming: When to Use What (Using Low-Code as Example)](https://www.outsystems.com/blog/posts/asynchronous-vs-synchronous-programming/#asynchronous-vs-synchronous-difference)

[Asynchronous vs synchronous execution. What is the difference?](https://stackoverflow.com/questions/748175/asynchronous-vs-synchronous-execution-what-is-the-difference)

[sync와 async, blocking과 non-blocking 차이점은?](https://www.slipp.net/questions/367)

[동기와 비동기의 개념과 차이](https://dev-coco.tistory.com/46)

[Sync async-blocking-nonblocking-io](https://www.slideshare.net/unitimes/sync-asyncblockingnonblockingio)

---

### (2) ‘Blocking’과 ‘Non-Blocking’의 차이점

Blocking, Non-Blocking은 `호출된 함수`가 `호출한 함수`에게 제어권을 건네주는 유무의 차이라고 볼 수 있다.

- Blocking : 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 `끝날 때까지 기다렸다가` 작업을 시작하는 것
- Non-Blocking : 다른 주체의 작업에 `관련 없이` 자신의 작업을 하는 것

- **Blocking I/O 예시**
    - Blocking I/O model
    
![image](https://user-images.githubusercontent.com/88137420/203744562-8770d9f2-6c26-438a-819c-67c7d0946a07.png)
    
    - 실제 I/O를 수행하는것은 커널레벨에서만 가능하기에 유저 프로세스(또는 쓰레드)는 커널에게 I/O를 요청해야한다. I/O에서 블로킹 형태의 작업은 유저 프로세스가 커널에게 I/O를 요청하는 함수를 호출하고, 커널이 작업을 완료되면 함수가 작업 결과를 반환한다.
    - 함수를 호출하고 반환할 때까지 전체 시간동안 application은 차단(Blocking)됩니다.
    - 여러 클라이언트가 접속하는 서버인 경우, I/O 작업을 호출한 작업은 중지되어도 다른 클라이언트가 실행하는 작업은 중지되면 안 되기 때문에 클라이언트 별로 스레드를 생성하게 되어 클라이언트의 수가 매우 많아지는 단점을 가지고 있다.
    
- **Non-blocking I/O 예시**
    - Blocking I/O model
    
![image](https://user-images.githubusercontent.com/88137420/203744588-e1eb59c6-5024-49a4-bdf3-dd96b79cd9cf.png)
    
    - application은 함수의 결과가 준비 되었는지 확인하기 위해 지속적으로 커널을 폴링(명령의 수신 여부를 체크)합니다.
    - 함수를 호출하는 처음 세 번에는 반환할 데이터가 없으므로 커널은 대신 EWOULDBLOCK 오류를 즉시 반환합니다. 함수를 네 번째로 호출하면 결과가 성공적으로 반환됩니다.
    - 이것은 system call을 폴링하는 단점을 가지고 있습니다.

<참고>

[[10분 테코톡] 🐰 멍토의 Blocking vs Non-Blocking, Sync vs Async](https://youtu.be/oEIoqGd-Sns)

[[10분 테코톡] 🎧 우의 Block vs Non-Block & Sync vs Async](https://www.youtube.com/watch?v=IdpkfygWIMk)

[Blocking I/O와 Non-blocking I/O](https://www.youtube.com/watch?v=XNGfl3sfErc)

[[Network] Blocking/Non-blocking & Synchronous/Asynchronous](https://github.com/gyoogle/tech-interview-for-developer/blob/master/Computer%20Science/Network/%5BNetwork%5D%20Blocking%2CNon-blocking%20%26%20Synchronous%2CAsynchronous.md)

[I/O Models](http://www.masterraghu.com/subjects/np/introduction/unix_network_programming_v1.3/ch06lev1sec2.html)

[Blocking / Non-Blocking](https://ozt88.tistory.com/20)

[Blocking I/O and non-blocking I/O](https://medium.com/coderscorner/tale-of-client-server-and-socket-a6ef54a74763)

--- 
### (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

```java
import java.util.concurrent.*;

public class FutureExample {
    public static void main(String[] args) {

        new Thread(() -> {
            try {
                CompletableFuture
                        .supplyAsync(FutureExample::work1)
                        .thenAccept(FutureExample::work2)
                        .get();
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }).start();

        work3();
    }

    private static String work1() {
        log("작업 1 시작");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        log("작업 1 종료");
        return "Alice";
    }

    private static void work2(String result) {
        log("작업 1의 결과: " + result);
        log("작업 2 시작");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        log("작업 2 종료");
    }

    private static void work3() {
        log("작업 3 시작");
        try {
            Thread.sleep(1500);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        log("작업 3 종료");
    }

    private static void log(String content) {
        System.out.println(Thread.currentThread().getName() + "> " + content);
    }
}
```
