## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.   
  `동기(Synchronous)`는 호출하는 함수 A가 호출되는 함수 B의 작업 완료 후 리턴을 기다리거나, 바로 리턴 받더라도 미완료 상태이라면 
  작업 완료 여부를 스스로 계속 확인하며 신경쓰는 것이다. 다시 말해서 함수 A가 함수 B를 호출한 뒤, 함수 B의 리턴값을 계속 확인하면서 신경쓰는 것이다.     
  `비동기(Asynchronous)`는 함수 A가 함수 B를 호출할 때 콜백 함수를 함께 전달해서 함수 B의 작업이 완료되면 함께 보낸 콜백 함수를 실행한다.
  함수 A는 함수 B를 호출한 후로 함수 B의 작업 완료 여부에는 신경쓰지 않는다.
  
  출처 : https://inpa.tistory.com/entry/%F0%9F%91%A9%E2%80%8D%F0%9F%92%BB-%EB%8F%99%EA%B8%B0%EB%B9%84%EB%8F%99%EA%B8%B0-  %EB%B8%94%EB%A1%9C%ED%82%B9%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.       
  `블로킹`은 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 끝날 때까지 기다렸다가 자신의 작업을 시작하는 것이다.      
  `논블로킹`은 다른 주체의 작업에 관련없이 자신의 작업을 하는 것이다.    
  처리되어야 하는 (하나의) 작업이, 전체적인 작업 '흐름'을 막느냐 안막느냐에 대한 관점으로 `제어권`이 누구한테 있느냐가 관심사이다. 
  
  출처 : https://inpa.tistory.com/entry/%F0%9F%91%A9%E2%80%8D%F0%9F%92%BB-%EB%8F%99%EA%B8%B0%EB%B9%84%EB%8F%99%EA%B8%B0-%EB%B8%94%EB%A1%9C%ED%82%B9%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC
  
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.    
  주로 사용하고 있는 언어는 `Java`이다. Java 비동기 기술 중 `Future`와 `FutureTask`, `Callback` 사용하는 방법을 설명해보겠다.    
  - Future   
  1. 비동기적 연산, 작업을 수행한 후 도출된 결과를 나타내는 것이다.
  2. 타 thread에서 return한 값을 메인Thread에서 받고 싶을 때 사용한다.
  ```java
  public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();
        Future<String> f = es.submit(() -> {
            Thread.sleep(2000); //interrupt 발생시 exception 던질 수 있도록
            log.info("Async");
            return "Hello";
        });
        System.out.println(f.isDone()); //즉시 리턴(작업이 완료되었는지)
        Thread.sleep(2100);
        log.info("Exit");
        System.out.println(f.isDone());
        System.out.println(f.get());
    }
  }
  //log 결과
  //false
  //[pool-1-thread-1] INFO com.example.demo.FutureEx - Async
  //[main] INFO com.example.demo.FutureEx - Exit
  //true
  //Hello
  ```
  왜 log결과 Exit가 맨 끝에 있을까?    
  System.out.println(f.get())에서 get()메서드는 결과값을 받을 때까지 대기하는 Blocking 메서드이기 때문이다.     
  그럼, 굳이 ThreadPool만들어서 이렇게 구현할까? 이것 나름으로 Observer패턴 등을 활용할 때 유용하게 사용된다고 한다.
  - FutureTask
  1. Future 자체를 Object로 만들어준다.     
  
  FutureTask를 이용한 코드
  ```java
  public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();
        FutureTask<String> f = new FutureTask<>(()->{
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        });
        es.execute(f);

        System.out.println(f.isDone()); //즉시 리턴(작업이 완료되었는지)
        Thread.sleep(2100);
        log.info("Exit");
        System.out.println(f.isDone());
        System.out.println(f.get());
    }
  }
  ```
  FutureTask에 익명클래스로 done()메서드를 추가한 코드
  ```java
  public class FutureEx {
    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();
        FutureTask<String> f = new FutureTask<>(()->{
            Thread.sleep(2000);
            log.info("Async");
            return "Hello";
        }) { //비동기 작업이 모두 완료되면 호출되는 hook같은 것.
            @Override
            protected void done() {
                try {
                    System.out.println(get());
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }
            }
        };
        es.execute(f);
        es.shutdown(); //이 메서드를 쓰더라도 하던 작업이 중단되지는 않음
    }
  }
  ```
  - Callback
  ```java
  public class FutureEx {
    interface SuccessCallback {
        void onSuccess(String result);
    }
    interface  ExceptionalCallback{
        void onError(Throwable t);
    }
    public static class CallbackFutureTask extends FutureTask<String> {
        SuccessCallback sc;
        ExceptionalCallback ec;
        public CallbackFutureTask(Callable<String> callable, SuccessCallback sc, ExceptionalCallback ec) {
            super(callable);
            this.sc = Objects.requireNonNull(sc); //Tip. Null이 들어오면 안될 때 사용하는 메서드
            this.ec = Objects.requireNonNull(ec);
        }

        @Override
        protected void done() {
            try {
                sc.onSuccess(get());
            } catch (InterruptedException e) {
               Thread.currentThread().interrupt();
            } catch (ExecutionException e) {
                ec.onError(e.getCause());
            }
        }
    }

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        ExecutorService es = Executors.newCachedThreadPool();

        CallbackFutureTask f = new CallbackFutureTask(() -> {
            Thread.sleep(2000);
            if(1==1) throw new RuntimeException("Async ERROR!!!");
            log.info("Async");
            return "Hello";
        },
            s -> System.out.println(s),
            e-> System.out.println("Error: "+e.getMessage()));

        es.execute(f);
        es.shutdown(); //이 메서드를 쓰더라도 하던 작업이 중단되지는 않음
    }
  }
  ```
  
  출처 : https://heekim0719.tistory.com/384
  
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.


- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
