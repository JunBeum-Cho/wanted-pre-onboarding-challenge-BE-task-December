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


# 과제 제출
## (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

둘의 차이점의 키-포인트는 _**순서**_ 입니다.
```text
함수 A() {
  B();
  C();
}

함수 B() { /* 실행... */ }
함수 C() { /* 실행... */ }
```

> A 함수 실행하면?

### 🚶‍♀️🚶‍♂️ 동기 (Synchronous)
A는 B가 작업이 완료되었는지 확인하고 요청이 완료되면 C를 실행하게 됩니다.
<br>
B → C 순서대로 실행이 되고, 실행 순서를 보장하게 됩니다.

고길동이 둘리와 도우너에게 일을 맡긴다고 생각해봅시다.
- **[🗡️ 고길동]** : 둘리, 자료좀 정리해줄래?
- **[🪄 둘리]** : Yes, sir!
- (둘리 자료 정리 중...)
- **[🗡️ 고길동]** : (둘리 작업을 기다리며...) 둘리, 아직 멀었니??
- **[🪄 둘리]** : 지금 끝났습니다!
- **[🗡️ 고길동]** : Okay! 다음 도우너, 이거 검토 부탁해!
- **[🎻 도우너]** : 넵!
- (반복...)

고길동은 둘리의 작업을 신경쓰며 기다리다가 작업이 완료 되면 도우너에게 일을 맡기게 됩니다.
<br>
둘리의 일이 끝날때까지 기다리고 신경쓴다는 점에서 어떻게 보면 비효율적일 수 있습니다.
<br>
하지만 자료가 준비되지 않았는데, 검토를 할 수는 없겠죠? 🤔
<br>
이와 같이 순차적으로 진행을 해야될 때 사용하게 됩니다.

### 🕺🤸‍♂ ️비동기 (Asynchronous)
A가 B를 호출 할때 콜백 함수를 함께 전달해서, B가 완료되면 콜백 함수를 실행합니다.
<br>
이는 즉 각 B, C가 각각 수행과 종료를 스스로 처리하는 것을 말합니다.
<br>
A는 B, C의 작업 완료 여부는 전혀 신경을 쓰지 않기 때문에 B, C 중에 무엇이 먼저 끝나는지 알 수 없습니다.
<br>
즉 실행 순서를 보장하지 않습니다.

고길동이 둘리와 도우너에게 일을 맡긴다고 생각해봅시다.
- **[🗡️ 고길동]** : 둘리, 발표 자료 A안 준비 해줘.
- **[🪄 둘리]** : Yes, sir!
- (둘리 자료 정리중...)
- **[🗡️ 고길동]** : (기다리지 않고 바로) 도우너, B안 부탁할게!
- **[🎻 도우너]** : 넵!
- (도우너 자료 정리중...)
- **[🗡️ 고길동]** : (회의장으로 발걸음을 옮기며...) 나는 회의 참석하러 갈게! 파이팅!

`동기(Synchronous)`와는 다르게 둘리의 작업을 기다리지 않고 도우너에게 일을 맡기고 본인도 본인 업무를 하러 갑니다.
<br>
이렇게 각자가 동시에 업무를 처리하기 때문에 매우 효율적으로 업무 처리를 할 수 있습니다.
<br>
이와 같이 순차적으로 진행할 필요가 없다면 효율적으로 비동기적 방식을 많이 사용합니다.

⚠️ 주의할 점은 순서를 보장하지 않기 때문에, 둘리와 도우너 중에 누가 업무를 먼저 끝낼지는 알 수가 없습니다.
<br>
그래서 만약에 둘리가 먼저 일을 끝내야 한다면 비동기적 방식보다는 동기적 방식을 사용하는것이 좋습니다.

## (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
둘의 차이점의 키-포인트는 _**제어권**_ 입니다.
```text
함수 A() {
  B();
  // 다음 작업!
}

함수 B() {
  // 열심히 실행!
}
```

> A 함수 내에서 B 함수 실행 시?

### ⛔️ 블로킹 (Blocking)
A는 B에게 제어권을 넘겨주고, 함수 실행을 잠시 멈춥니다(Block!).
<br>
B는 함수를 실행하고 A에게 제어권을 넘겨줍니다.
<br>
A는 제어권을 넘겨받고 나서 다음 작업을 이어갑니다.

`Javascript`에서 `alert()` 함수로 설명해보겠습니다.
```javascript
alert('Hi!');
console.log('Bye!');
```
위의 작업의 결과는 보이는 바와 같이 아래와 같습니다.
```shell
# 메시지 알림으로 Hi! 팝업
Bye!
```
메시지 팝업으로 `Hi!`를 보여준 후에 `Bye!`가 콘솔로 출력됩니다.
<br>
이는 `alert` 함수로 제어권이 넘어가서 실행을 완료되기 전까지 Block 됩니다.
<br>
메시지 창을 닫고 나서야 제어권이 다시 돌아와 다음 작업을 실행하게 되는 것이죠.

### ⛩️ 논블로킹 (Non-blocking)
A에서 B를 호출하지만 B가 바로 제어권을 반납하여 A가 제어권을 가지게 됩니다.
<br>
A는 B를 호출하고도 계속해서 다음 작업을 실행합니다.

똑같이 `Javascript`로 예시를 들어보겠습니다.
<br>
비동기 함수로 사용되는 `setTimeout()`로 설명해볼게요.
```javascript
setTimeout(() => 
  console.log('Hi!'), 0); // 2번째 매개변수: 대기 시간을 0으로 설정!
console.log('Bye!');
```
위의 작업을 실행하게 되면 어떻게 될까요?
<br>
정답은 아래와 같습니다.
```shell
Bye!
Hi!
```
제어권을 바로 반납 받아 (`Hi!`를 기다리는 것이 아닌) `Bye!`를 실행하게 되기 때문입니다.
<br>
이렇게 제어권을 바로 반납 받아 다른 일을 할 수 있도록 하는것을 논블로킹이라고 합니다.

## (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

Java 8 부터 지원하고 있는 `CompletableFuture` 인터페이스를 사용하고 있습니다.

### ✨ 장점
- 명시적 Thread Pool 선언이 필요 없습니다.
- 함수형 프로그래밍 방식을 지원합니다.
    - 간결한 코드, 높은 가독성을 제공합니다.
    - 각 병렬 Task 들의 손쉬운 결합, 예외처리를 지원합니다.

### 🪄 간단 사용방법
1. 반환값 여부에 따른 함수 사용
    - `static CompletableFuture<Void> runAsync(Runnable runnable)`
      <br> : 반환 값이 필요 없는 경우
    - `static <U> CompletableFuture<U> supplyAsync(Supplier<U> supplier)`
      <br> : 반환 값이 필요한 경우
2. 비동기 작업 완료 콜백
    - `CompletableFuture<Void> thenAccept(Consumer<? super T> action)`
      <br> : 비동기 작업이 완료 됐을 때, 완료 결과를 소비(Consume) 처리함. 작업의 끗!
    - `<U> CompletableFuture<U> thenApply(Function<? super T, ? extends U> fn)`
      <br> : 비동기 작업이 완료 됐을 때, 결과 T를 새로운 값 U로 변환하는 함수를 실행
    - `CompletableFuture<T> exceptionally(Function<Throwable, ? extends T> fn)`
      <br> : 비동기 작업에서 예외가 발생했을 때, 예외를 Throwable 받고, 결과 T를 생성

이를 조합해서 간단하게 사용해본다면? 아래와 사용할 수 있습니다. 🧐
```java
CompletableFuture.supplyAsync(() -> {
    // 어마어마한 작업
    return "작업 후 반환!";
}).thenApply(s -> {
    log.info("다음 작업으로 토스 가능! {}", s);
    return s + " > 토스";
}).thenAccept(s -> {
    log.info("작업이 완료되었습니다. 끗! {}", s);
}).exceptionally(e -> {
    log.error("예외가 발생했습니다. {} ", e);
    return null;
});
```

### 🎓 사용 예시
회원 가입을 할 때, 사옹자가 프로필 사진을 선택적으로 함께 등록(To. Aws S3)하는 기능을 추가할 때 사용했습니다.
<br>
코드를 예시로 설명 드리겠습니다.
```java
public void join(회원정보, Optional<이미지_파일>) {
  회원정보_등록(회원정보);
  
  1_이미지가_존재한다면(이미지_파일 ->
    CompletableFuture.supplyAsync(() ->
      2_서버에_이미지_업로드(이미지_파일)
    ).thenAccept(opt ->
      opt.ifPresent(이미지_URL ->
        // 이미지가 정상적으로 업로드가 완료된 경우
        3_회원_프로필_이미지_업데이트(회원정보, 이미지_URL);
      )
    )
  );
}
```
1. 회원가입 때, 이미지 파일을 `Optional`로 받습니다.
2. 이미지가 존재한다면 (이미지 DTO 클래스가 있다면 변환하고) 비동기로 이미지 업로드를 진행합니다.
    - 먼저 서버에 업로드를 하고,
    - 성공적으로 업로드가 되었다면, 등록된 회원 정보에 프로필 정보를 업데이트 합니다.

이렇게 사용하는 이유는 만약에 동기적으로 진행하여 AWS 외부에 이미지를 업로드 한다면,
<br>
AWS 서버에 지연이 되는 등 문제가 발생했을 때, 사용자는 이미지 업로드가 될때까지 회원가입을 기다려야 합니다.
<br>
이를 비동기 함수를 사용함으로써 사용자가 외부적 요인에 의해 기다리는 일이 없도록 서비스를 원할하게 사용할 수 있도록 하였습니다.

## (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

![image](https://user-images.githubusercontent.com/93169519/204757299-a5354b39-7ab3-4d27-8a83-c80e3e52f34a.png)
[[이미지 : AWS Message Queue 참고]](https://aws.amazon.com/ko/message-queue/)

메시지 큐는 그림과 같이 Producer(생산자)가 메시지(요청)를 메시지 큐에 추가하고,
<br>
해당 메시지를 Consumer(소비자)가 메시지를 가져와 이를 수행하게 됩니다.
<br>
(각 메시지는 하나의 소비자에 의해 순차적으로 수행하게 됩니다.)

### 메시지 큐의 장점
- 비동기(Asynchronous) : 데이터를 바로 전송이 아닌 큐에 넣고 후에 전송 가능
- 낮은 결합도(Decoupling) : 앱과 분리 가능하여 확장성 용이
- 탄력성(Resilience) : 일부가 실패해도 전체에 영향을 주지 않는다.
- 과잉(Redundancy) : 실패할 경우 재실행 가능
- 보장성(Guarantees) : 작업이 처리된 것을 확인 가능
- 확장성(Scalable) : N : 1 : M 구조로 다수의 프로세스들이 큐에 메시지 전송 가능

---
> 👉 이제 **MQ(Message Queue)** 사용 이점에 대해 두 가지 예시를 들어 설명 드리겠습니다.

### 1. 모니터링, 로그와 같이 많은 양의 데이터를 다루는데 있어 매우 적합합니다.
요즘 기업들은 데이터 분석과 활용 측면에 있어서 많은 관심을 가지고 이를 적극적으로 활용하고 있습니다.
<br>
하지만 이러한 대용량 데이터를 전송하다보면 서버에 부하가 심해, 서버가 죽어버리거나 메시지 손실이 있을 수가 있는데요.
<br>
이러한 측면에서 MQ를 매우 유용하게 활용할 수 있습니다.

로그를 처리하는 서비스(Consumer)를 분리하여 독립적으로 구성할 수 있고,
<br>
전달되는 메시지는 큐에 저장이 되고 순차적으로 받기 때문에 로그 처리 서비스는 자신의 처리량에 맞게 메시지를 가져와서 처리할 수 있습니다.
<br>
그리고 독립적인 확장(ex: 로그 처리 서비스 인스턴스 확장)을 통해 대용량 트래픽도 처리할 수도 있습니다.

메시지 손실의 경우에도 백업이 따로 존재하기 때문에 재전송 처리를 통해 손실을 방지할 수 있습니다.
<br>
이와 같이 대용량 트래픽에 있어서 MQ를 활용하면 원할하게 대응할 수가 있습니다.

### 2. 비동기적 처리에 용이합니다.
예를 들면 먼저 이메일 전송 기능이 있습니다.
<br>
요즈음 구글이나 네이버로 바로 회원가입/로그인을 활용하기 때문에, 기본적으로 이메일 인증이나 비밀번호 재설정 등 많이 활용되는 데요.
<br>
이러한 이메일 전송은 각 외부의 구글이나 네이버 서버의 상황에 따라 달라질 수 있기 때문에, 즉각적으로 이메일 전송이 될것이라고 기대하기 힘듭니다.
<br>
그래서 비동기 방식에 적합하고, 어느 정도의 응답지연이 허용됩니다.
<br>
이 경우에 MQ가 큰 도움이 될 수 있습니다.

MQ를 중심으로 **기존 서버**와 **이메일 전송 서비스**를 독립적으로 구성할 수 있으며 각자 확장도 가능합니다.
<br>
각자 독립적이기 때문에 이메일 전송 서비스는 그저 메시지 큐에서 순차적으로 받아서 이메일을 전송하기만 하면 됩니다.
<br>
그리고 혹여나 사용자가 급증해서 트래픽에 부하가 오는 경우에는 이메일 전송 서비스에서의 인스턴스 확장을 통해서 부하를 줄일 수도 있습니다.

그 외에도 사진 보정 기능과 같이 시간이 오래 걸리는 경우에도 메시지 큐를 사용하면 순차적으로 작업이 가능하고, 필요에 따라 해당 서버만 확장이 가능하기 때문에 매우 유용합니다.

## (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
- https://github.com/prgrms-web-devcourse/Team_04_SFam_BE
  <br>
    - 설명 : 동네 사람과 함께 운동하는 매칭 앱
    - 기간 : 2022.07.24 ~ 2022.08.15
    - 참여 인원 : 백엔드(5) / 프론트(4)
    - 백엔드 기술 스택 : Spring Boot 2.7.0, Java 17, JPA, MySQL, AWS 등

## (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
요즘 많은 회사들에서 메시지큐에 대한 지식이나 경험을 많이 요구하고 있다보니,
<br>
먼저 메시지 큐를 활용하는데 있어서 실제 회사에 있는 다양한 사례들을 알아보고 어떤식으로 잘 사용하고 대처할 수 있는지를 배우고 싶습니다.
<br>
그리고 상황에 맞게 인프라를 선택한다는 부분도 비용적인 측면과 효율성 면에서 회사에서 정말 중요한 부분이라고 생각이 되어서, 이 부분도 꼭 배워보고 싶네요.