## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  - 동기(Synchronous : 동시에 일어나는) : 동시에 일어난다.
  : 요청과 그 결과가 동시에 일어난다는 약속이다.
  -> 바로 요청을 하면 시간이 얼마나 걸리던지 요청한 자리에서 결과가 주어져야 한다.
  
    - 장점
    1) 순서에 맞춰 진행
    2) 설계가 매우 간단하고 직관적
    
    <br>
    
    - 단점
    1) 여러 가지 요청을 동시에 처리할 수 없다.
    2) 결과가 주어질 때까지 아무것도 못하고 대기해야 함
    
    <br>
    
    - 예시 <br>
    ![](https://velog.velcdn.com/images/jack_whiteblack/post/d127b631-5f81-4563-94a6-3a35a384a9f8/image.png) <br>
    1. A의 계좌는 10,000원을 뺄 생각을 하고 있다. <br> 
    2. A의 계좌가 B의 계좌에 10,000원을 송금한다. <br> 
    3. B의 계좌는 10,000원을 받았다는 걸 인지하고, A의 계좌에 10,000원을 받았다고 전송한다. <br> 
    4. A, B 계좌 각각 차감과 증가각 동시에 발생한다. <br> 
    -> 계좌이체 같은 작업은 동기 방식으로 처리
    <br>
    
  - 비동기(Asynchronous : 동시에 일어나지 않는) : 동시에 일어나지 않는다.
  : 요청과 결과가 동시에 일어나지 않을 거라는 약속이다.
  -> 하나의 요청에 따른 응답을 즉시 처리하지 않아도, 그 대기 시간동안 또 다른 요청에 대해 처리 가능한 방식이다.
  
    - 장점
    1) 여러 개의 요청을 동시에 처리
    2) 결과가 주어지는데 시간이 걸리더라도 그 시간 동안 작업을 할 수 있으므로 자원을 효율적으로 사용 가능
    
    <br>
    
    - 단점
    1) 동기 방식보다 속도가 느리다.
    2) 동기 방식보다 복잡하다.
    
    <br>
    
    - 예시 <br>
    ![](https://velog.velcdn.com/images/jack_whiteblack/post/e69d1bac-37d2-43d3-a9a5-36692342e8ea/image.png) <br>
    1. 학생은 시험 문제를 푼다. <br> 
    2. 시험 문제를 모두 푼 학생은 선생에게 전송한다. <br> 
    3. 선생은 학생의 시험지를 채점한다. <br> 
    4. 채점이 다 된 시험지를 학생에게 전송한다. <br> 
    5. 학생은 선생이 전송한 시험지를 받아 결과를 확인한다. <br> 
    -> 서로의 행위(목적)가 다르기 때문에 둘의 작업 처리 시간은 일치하지 않는다.

> 정리 <br>
> 동기 : 같은 행위(목적)가 동시에 이루어진다. <br>
> 비동기 : 행위(목적)가 다를 수도 있고, 동시에 이루어지지도 않는다.

<br>

---

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
> 제어권 : 자신(함수)의 코드를 실행할 권리 같은 것이다. 제어권을 가진 함수는 자신의 코드를 끝까지 실행 한 후, 자신을 호출한 함수에게 돌려준다.
>
> 결과 값을 기다린다는 것 : A 함수에서 B 함수를 호출했을 때, A 함수가 B 함수의 결과값을 기다리느냐의 여부를 의미한다.

  - 블로킹(Blocking) : 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 다른 작업이 끝날 때까지 기다렸다가 자신의 작업을 시작하는 것
  
  ✔ A함수가 B함수를 호출하면, 제어권을 A가 호출한 B 함수에 넘겨준다. <br>
  ![](https://velog.velcdn.com/images/jack_whiteblack/post/026e8efe-122c-4e15-827e-36b686099a00/image.png) <br>
  1. A함수가 B함수를 호출하면 B에게 제어권을 넘긴다. <br> 
  2. 제어권을 넘겨받은 B는 열심히 함수를 실행한다. A는 B에게 제어권을 넘겨주었기 때문에 함수 실행을 잠시 멈춘다. <br> 
  3. B함수는 실행이 끝나면 자신을 호출한 A에게 제어권을 돌려준다.
  
  <br>

  - 논블로킹(Non-Blocking) : 다른 주체의 작업에 관련없이 자신의 작업을 하는 것
  
  ✔ A함수가 B함수를 호출해도 제어권은 그대로 자신이 가지고 있는다. <br>
  ![](https://velog.velcdn.com/images/jack_whiteblack/post/948db41e-b21e-4a11-b534-e1f54b45049b/image.png) <br>
  1. A함수가 B함수를 호출하면, B함수는 실행되지만, 제어권은 A함수가 그대로 가지고 있는다. <br> 
  2. A함수는 계속 제어권을 가지고 있기 때문에 B함수를 호출한 이후에도 자신의 코드를 계속 실행한다.
  
<br>

---

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
JAVA

- execute
  - runnable 인터페이스 필요, result값 설정 가능
  - runnable - 객체를 리턴하지 않음, exception 발생시키지 않음
  - 객체를 리턴할 필요가 없을 때 사용한다.
  - shutdown() 걸어줘야 함.
```java
public class FutureEx {
    public static void main(String[] args) {
        ExecutorService es = Executors.newCachedThreadPool();
        es.execute(() -> {
            try {
                Thread.sleep(2000); //interrupt 발생시 exception 던질 수 있도록
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            log.info("Hello");
        });
        log.info("Exit");
    }
}
```

<br>

- submit
  - runnable, callable 인터페이스 사용 가능
  - runnable - 객체를 리턴하지 않음, exception 발생시키지 않음
  - callable - 값 리턴 가능, exception 발생시킬 수 있음
  - 객체 리턴이 필요하거나 exception 발생이 필요할 때 사용한다.
```java
public class FutureEx {
    public static void main(String[] args) {
        ExecutorService es = Executors.newCachedThreadPool();
        es.submit(() -> {
            Thread.sleep(2000); //interrupt 발생시 exception 던질 수 있도록
            log.info("Async");
            return "Hello";
        });
        log.info("Exit");
    }
}
```

<br>

> submit으로 리턴 받은 비동기 수행 결과값을 저장할 때 Future와 Callback을 사용한다.

- future
  - Future는 자바1.5에서 나왔다.
  - 비동기적 연산, 작업을 수행한 후 도출된 결과를 나타내는 것
  - 타 thread에서 return한 값을 메인Thread에서 받고 싶을 때 사용
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
```

<br>

- CallBack
  - Callback을 이용하여 비동기 실행 결과를 처리할 수 있는 코드
  - try/catch 작성이 빈번한 Future보다 더 우아한 코드라고 할 수 있다.
  - 더 나은 방법이 있지만, 기본기 중에서는 콜백 기법이 더 나음

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

<br>

---

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
1. 이메일 전송
: 비밀번호 재설정을 위해 이메일을 발급하는 서비스, 회원가입을 위해 이메일을 발급하는 서비스를 위해 메시지 큐를 사용한다.
2. 블로그 포스팅
: 고용량의 이미지가 포함된 블로그를 포스팅할 때 사용한다.

---

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) <br>
https://github.com/JONGHWI-PARK/team-project_HappyEver-Travel-Planner

---

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.