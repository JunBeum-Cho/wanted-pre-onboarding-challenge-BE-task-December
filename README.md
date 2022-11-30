## 사전 과제

- **(1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a64e8af5-bc20-4102-88c4-d9ee4b09cf43/Untitled.png)
    
    ### 동기 (Synchronous)
    
    클라이언트가 서버에 요청 시, 응답을 수신할 때 까지 다른 동작을 수행할 수 없음
    
    - **장점** ) 간단한 설계, 직관적
    - **단점** ) 응답을 수신할 때 까지 대기
    
    ### 비동기 (Asynchronous)
    
    클라이언트가 서버에 요청 시, 응답 수신 유무와 상관없이 다른 동작을 수행할 수 있음
    
    - **장점** ) 요청-응답과 상관없이 다른 동작 수행 가능
    - **단점** ) 복잡한 설계
    
    [동기와 비동기의 차이](https://velog.io/@slobber/%EB%8F%99%EA%B8%B0%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0%EC%9D%98-%EC%B0%A8%EC%9D%B4)
    

- **(2) 블로킹과 논블로킹의 차이점을 설명해주세요.**
    
    ### 블로킹 (Blocking)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ff609d67-42e4-4dd9-a9c4-54a572aac55b/Untitled.png)
    
    A 함수가 B 함수를 호출 시, B 함수에게 **제어권** 부여
    
    - 호출된 B 함수가 작업 완료 후, 다시 호출한 A 함수로 제어권 반환
    
    ### 논-블로킹 (Non-Blocking)
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bdaa19a8-cb4f-441c-b43c-1036d61e5fc0/Untitled.png)
    
    A 함수가 B 함수를 호출 시, A 함수가 제어권 소유
    
    - 호출된 B 함수의 작업 완료 유무 관계없이 A 함수는 계속해서 실행
    
    **제어권** : 함수의 코드를 실행할 권리이며, 제어권을 가진 함수는 자신의 코드를 끝까지 실행한 후 자신을 호출한 함수에게 제어권을 반환
    
    <aside>
    😃 **동기/비동기 vs 블로킹/논-블로킹**
    동기/비동기 :  프로세스의 수행 순서 보장에 대한 매커니즘
    블로킹/논-블로킹 : 프로세스의 작업 완료 여부에 대한 개념
    
    </aside>
    
    [동기/비동기, 블로킹/논블로킹의 차이점?](https://velog.io/@ken1204/%EB%8F%99%EA%B8%B0%EB%B9%84%EB%8F%99%EA%B8%B0-%EB%B8%94%EB%A1%9C%ED%82%B9%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90)
    

- **(3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.**
    
    ### **Java : Thread를 사용한 비동기**
    
    - Source Code
        
        ```java
        import java.util.concurrent.ExecutorService;
        import java.util.concurrent.Executors;
        
        public class ThreadExample {
        
        	  // 출력을 어떤 스레드에서 하고 있는지 확인
            private static void log(String content) {
                System.out.println(Thread.currentThread().getName() + "> " + content);
            }
        
            public static void main(String[] args) {
                ExecutorService executorService = Executors.newCachedThreadPool();
        
                // 작업1 (스레드)
                executorService.submit(() -> {
                    log("작업 1 시작");
                    try {
                        Thread.sleep(1500);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                    log("작업 1 종료");
                });
        
                // 작업2
                log("작업 2 시작");
                try {
                    Thread.sleep(500);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                log("작업 2 종료");
        
                executorService.shutdown();
            }
        }
        ```
        
    - 실행 결과
        
        ```
        main> 작업 2 시작
        pool-1-thread-1> 작업 1 시작
        main> 작업 2 종료
        pool-1-thread-1> 작업 1 종료
        ```
        
    
    ### Java에서의 비동기 처리
    
    **1) Future 객체 사용**
    
    다른 주체에게 작업을 맡긴 상태에서 본 주체 쪽에서 작업이 끝났는지 직접 확인
    
    - **구현 방법**
        - **Future 객체**
            - 다른 스레드의 작업 여부 확인 2가지 경우
                - `isDone()`이나 `isCancled()` 메소드로 블로킹 없이 작업을 완료했는지의 여부만 확인
                - `get()`으로 작업이 완료될 때 까지 블로킹된 상태로 대기
            - 소스 코드
                
                ```java
                import java.util.concurrent.ExecutionException;
                import java.util.concurrent.ExecutorService;
                import java.util.concurrent.Executors;
                import java.util.concurrent.Future;
                
                public class FutureExample {
                    public static void main(String[] args) {
                        ExecutorService executorService = Executors.newCachedThreadPool();
                
                        // 작업1 Callable이 리턴한 값을 future에 담는다.
                        Future<String> future = executorService.submit(() -> {
                            log("작업 1 시작");
                            Thread.sleep(1000);
                            log("작업 1 종료");
                            return "Alice";
                        });
                
                        log("작업 2 시작 (작업 1 종료 대기)");
                        String result = "";
                        try {
                            // 논블로킹으로 작업 1이 종료되었는지 확인한다.
                            log("작업 1 종료 여부: " + future.isDone());
                            // 블로킹 상태에서 작업 1이 끝날 때까지 대기한다.
                            result = future.get();
                            // 논블로킹으로 작업 1이 종료되었는지 확인한다.
                            log("작업 1 종료 여부: " + future.isDone());
                        } catch (InterruptedException | ExecutionException e) {
                            e.printStackTrace();
                        }
                        log("작업 1의 결과: " + result);
                        log("작업 2 종료");
                    }
                
                    private static void log(String content) {
                        System.out.println(Thread.currentThread().getName() + "> " + content);
                    }
                }
                ```
                
            - 실행 결과
                
                ```
                main> 작업 2 시작 (작업 1 종료 대기)
                pool-1-thread-1> 작업 1 시작
                main> 작업 1 종료 여부: false
                pool-1-thread-1> 작업 1 종료
                main> 작업 1 종료 여부: true
                main> 작업 1의 결과: Alice
                main> 작업 2 종료
                ```
                
        - **FutureTask**
            - Future의 구현체인 FutureTask로 구현
            - 소스 코드
                
                ```java
                // FutureTask를 생성한다. 비동기로 수행할 작업을 짜 넣는다.
                FutureTask<String> futureTask = new FutureTask<>(() -> {
                    System.out.println(Thread.currentThread().getName() + "> 작업 1 시작");
                    Thread.sleep(1000);
                    System.out.println(Thread.currentThread().getName() + "> 작업 1 종료");
                    return "Alice";
                });
                
                // FutureTask를 수행하는 스레드를 시작한다.
                executorService.submit(futureTask);
                
                // 작업 결과는 Future와 같은 방식으로 얻어온다.
                futureTask.get();
                ```
                
    
    **2) CompletableFuture**
    
    Future 객체는 다른 주체의 작업 결과를 얻어오려면 잠시 블로킹 상태에 도입하는 한계를 극복하기
    
    - 스레드를 생성한 뒤 그 안에서 작업 1을 `supplyAsync()`를 통해 호출하고, 작업 2를 작업 1이 끝난 직후에 블로킹 없이 시작할 수 있도록 `thenAccept()`를 통해 호출
    - `main` 스레드에서 작업 3을 불러 시작
    - 이전 작업의 결과를 `get()`을 통해 블로킹으로 가져올 필요 없이, `then...()` 함수를 통해 논블로킹을 유지하며 바로 사용
    - 소스 코드
        
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
        
    - 실행 결과
        
        ```
        main> 작업 3 시작
        ForkJoinPool.commonPool-worker-1> 작업 1 시작
        ForkJoinPool.commonPool-worker-1> 작업 1 종료
        ForkJoinPool.commonPool-worker-1> 작업 1의 결과: Alice
        ForkJoinPool.commonPool-worker-1> 작업 2 시작
        main> 작업 3 종료
        ForkJoinPool.commonPool-worker-1> 작업 2 종료
        ```
        
    
    **2) Callback 구현**
    
    다른 주체에게 맡긴 작업이 끝나면 다른 주체 쪽에서 본 주체가 전해 준 Callback 함수를 실행
    
    - **구현 방법**
        - **CompletionHandler**
            - 비동기 I/O 작업의 결과를 처리하기 위한 목적으로 만들어졌으며, Callback 객체를 만드는데 사용
            - `completed()` 메소드를 Override해서 Callback을 구현
            - `failed()` 메소드를 오버라이드해 작업 실패 경우의 처리를 구현
            - try-catch나 if문을 이용해 작업이 성공했는지 판단 후 Callback 객체의 `completed()`를 호출하고, 실패 시 `failed()`를 호출하는 방식
            - 아래 소스 코드를 보면 `pool-1-thread-1` 쪽에서 Callback을 호출해 계속해서 `main` 스레드와 별개로 비동기적으로 실행
            - 소스 코드
                
                ```java
                import java.nio.channels.CompletionHandler;
                import java.util.concurrent.ExecutorService;
                import java.util.concurrent.Executors;
                
                public class CallbackExample1 {
                
                    private static ExecutorService executorService;
                    // CompletionHandler를 구현한다.
                    private static final CompletionHandler<String, Void> completionHandler = new CompletionHandler<>() {
                        // 작업 1이 성공적으로 종료된 경우 불리는 콜백 (작업 2)
                        @Override
                        public void completed(String result, Void attachment) {
                            log("작업 2 시작 (작업 1의 결과: " + result + ")");
                            try {
                                Thread.sleep(1000);
                            } catch (InterruptedException e) {
                                e.printStackTrace();
                            }
                            log("작업 2 종료");
                        }
                
                        // 작업 1이 실패했을 경우 불리는 콜백
                        @Override
                        public void failed(Throwable exc, Void attachment) {
                            log("작업 1 실패: " + exc.toString());
                        }
                    };
                
                    public static void main(String[] args) {
                
                        executorService = Executors.newCachedThreadPool();
                
                        // 작업 1
                        executorService.submit(() -> {
                            log("작업 1 시작");
                            try {
                                Thread.sleep(1000);
                            } catch (InterruptedException e) {
                                e.printStackTrace();
                            }
                            log("작업 1 종료");
                
                            String result = "Alice";
                            if (result.equals("Alice")) { // 작업 성공
                                completionHandler.completed(result, null);
                            } else { // 작업 실패
                                completionHandler.failed(new IllegalStateException(), null);
                            }
                        });
                
                        // 별개로 돌아가는 작업 3
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
                
            - 실행 결과
                
                ```
                main> 작업 3 시작
                pool-1-thread-1> 작업 1 시작
                pool-1-thread-1> 작업 1 종료
                pool-1-thread-1> 작업 2 시작 (작업 1의 결과: Alice)
                main> 작업 3 종료
                pool-1-thread-1> 작업 2 종료
                ```
                
        - **함수형 인터페이스**
            - [Runnable](https://docs.oracle.com/javase/10/docs/api/java/lang/Runnable.html)
                
                인자와 리턴 값이 모두 없음
                
            - [Supplier<R>](https://docs.oracle.com/javase/10/docs/api/java/util/function/Supplier.html), [Callable<R>](https://docs.oracle.com/javase/10/docs/api/java/util/concurrent/Callable.html)
                
                인자는 없고, R 타입의 객체를 리턴
                
            - [Consumer<T>](https://docs.oracle.com/javase/10/docs/api/java/util/function/Consumer.html)
                
                T 타입의 인자를 받고, 아무것도 리턴 X
                
            - [Function<T, R>](https://docs.oracle.com/javase/10/docs/api/java/util/function/Function.html)
                
                T 타입의 인자를 받고, R 타입의 객체를 리턴
                
                `@FunctionalInterface`를 통해 [커스텀 함수형 인터페이스](https://docs.oracle.com/javase/8/docs/api/java/lang/FunctionalInterface.html)를 만들 수 있음
                
            - `execute()`의 인자로 `execute()`의 작업이 모두 끝난 뒤 실행 될 Callback을 작성
            - `execute()`의 작업 하나를 마치고 나서 실행될 다른 작업을 작성
            - 소스 코드
                
                ```java
                import java.util.concurrent.ExecutorService;
                import java.util.concurrent.Executors;
                import java.util.function.Consumer;
                
                public class CallbackExample2 {
                
                    private static ExecutorService executorService;
                
                    public static void main(String[] args) {
                
                        executorService = Executors.newCachedThreadPool();
                
                        // execute 함수의 인자로 callback의 구현체를 넣는다.
                        execute(parameter -> {
                            log("작업 2 시작 (작업 1의 결과: " + parameter + ")");
                            try {
                                Thread.sleep(1000);
                            } catch (InterruptedException e) {
                                e.printStackTrace();
                            }
                            log("작업 2 종료");
                        });
                
                        // 별개로 돌아가는 작업 3
                        log("작업 3 시작");
                        try {
                            Thread.sleep(1500);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                        log("작업 3 종료");
                    }
                
                    public static void execute(Consumer<String> callback) {
                        executorService.submit(() -> {
                            log("작업 1 시작");
                            try {
                                Thread.sleep(1000);
                            } catch (InterruptedException e) {
                                e.printStackTrace();
                            }
                            String result = "Alice";
                            log("작업 1 종료");
                
                            // 작업을 마친 후 인자로 받아온 callback의 구현체를 비동기로 실행한다.
                            callback.accept(result);
                        });
                    }
                
                    private static void log(String content) {
                        System.out.println(Thread.currentThread().getName() + "> " + content);
                    }
                }
                ```
                
            - 실행 결과
                
                ```
                main> 작업 3 시작
                pool-1-thread-1> 작업 1 시작
                pool-1-thread-1> 작업 1 종료
                pool-1-thread-1> 작업 2 시작 (작업 1의 결과: Alice)
                main> 작업 3 종료
                pool-1-thread-1> 작업 2 종료
                ```
                
    - **구현 시 유의 사항**
        - 다른 스레드와 공유하는 변수 등에 접근할 경우 Race Condition이 발생할 수 있으므로 반드시 `synchronized` 블록 등의 기법을 통해 자원을 동기화하여 사용
    
    [Java에서의 비동기 프로그래밍](https://velog.io/@pllap/Java%EC%97%90%EC%84%9C%EC%9D%98-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D)
    

- **4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.**
    
    ### **메시지 큐(Message Queueing)**
    
    - 프로세스 또는 프로그램 인스턴스가 데이터를 서로 교환할 때 사용하는 통신 방법
    - **메시지 지향 미들웨어(Meesage Oriented Middleware: MOM)**를 구현한 시스템
        - **MOM** : 비동기 메시지를 사용하는 응용 프로그램 간의 데이터 송수신
    - 대용량 데이터를 처리하기 위한 배치 작업이나, 채팅 서비스, 비동기 데이터를 처리할 때 사용
        - ‘트래픽 부하(사용자 요청 급증) → 응답 시간 증가 → 대기 시간 지연 → 서비스 부하’ 를 막기 위해 분산되어 있는 데이터 처리를 한 곳에 집중하며 ‘메세지 브로커’를 두어 필요한 프로그램에 작업을 분산
        
    
    ### 메시지 큐 사용 시 이점
    
    - **비동기 (Asynchronous)**
        
        Queue에 넣기 때문에 나중에 처리할 수 있습니다.
        
    - **비동조 (Decoupling)**
        
        Appliction과 분리할 수 있습니다. (각 서비스의 연결을 느슨하게 합니다)
        
    - **탄력성 (Resilience)**
        
        일부가 실패 시 전체에 영향을 받지 않습니다.
        
    - **과잉 (Redundancy)**
        
        실패할 경우 재실행 가능합니다.
        
    - **보증 (Guarantees)**
        
        작업이 처리된걸 확인할 수 있습니다.
        
    - **확장성 (Scalable)**
        
        다수의 프로세스들이 큐에 메시지를 보낼 수 있습니다.
        
    
    ### ****메시지 큐를 사용 예시****
    
    **1) 이메일 전송**
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/500efb49-d487-49c1-8552-da0bfcb601fc/Untitled.png)
    
    - 어느 정도의 응답 지연이 허용되며, 어플리케이션의 핵심 기능이 아닌 경우인 이메일 전송의 경우 이점
        - 비밀번호 재설정을 위해 이메일을 발급하는 서비스, 회원 가입을 위해 이메일을 발급하는 서비스 등은 메시지(이메일)를 큐에 삽입
        - 이메일 전송 전용 서비스는 이메일이 어느 서비스로부터 생산 되었는지와는 관계없이, 메시지 큐의 메시지를 하나씩 소비하고, 그저 이메일이 전송되어야 할 곳으로 이메일을 전송
        - 이와 같은 접근 방식은 메시지 큐에 들어오는 메시지 수가 너무 많아지는 경우 이메일 전송 전용 서비스 인스턴스를 더 둠으로써 확장할 수 있으므로 확장성이 뛰어남
    
    **2) 블로그 포스팅**
    
    - 블로그 서비스의 응답 시간을 저해하지 않으면서 사용자들에게 유연성을 제공하는 방법
    - 사용자가 업로드한 모든 이미지를 게시 과정에서 즉각 처리하는 것이 아닌, 사후처리하며 최적화하는 방법
    - 사용자 경험에 약간의 영향을 미칠 수는 있지만, 최적화는 응용 프로그램에서 가장 중요한 것은 아니며 작업을 즉시 수행할 필요도 없다. 메시지 큐는 이러한 상황에서도 사용
        - 사용자가 고용량의 이미지가 포함된 블로그 포스팅을 한다.
        - 이미지는 저장소에 전송된다.
        - 업로드된 이미지에 대한 정보가 포함된 메시지를 이미지 최적화 서비스의 메시지 큐에 담는다.
        - 이미지 최적화 서비스는 저장소에서 이미지를 가져와 최적화하고, 2번에서 저장해놨던 이미지를 대체한다.
    
    [메시지 큐 Message Queue](https://heeonii.tistory.com/17)
    
    [메시지 큐에 대해 알아보자!](https://tecoble.techcourse.co.kr/post/2021-09-19-message-queue/)
    

- **(5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)**
    
    [https://github.com/Hyundai-IT-E-Team4/where_is_my_room](https://github.com/Hyundai-IT-E-Team4/where_is_my_room)
    
    [https://github.com/Hanseunghoon/freelec-springboot2-webservice](https://github.com/Hanseunghoon/freelec-springboot2-webservice)
    

- **(6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.**
    - 실무에서 사용하는 클라우드 컴퓨팅 인프라 구조에 대한 지식 학습
    - AWS 개념 및 사용법 기본기 학습
