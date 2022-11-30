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

## 1. 동기와 비동기

동기는 작업을 처리함에 있어 시간이 얼마나 걸리던 결과를 기다리게 됩니다.
만약 한 작업이 다른 작업을 호출하는 경우 호출된 작업의 완료 여부를 신경쓰게 됩니다.
이 때 주기적으로 완료 여부를 물어보거나, 기다립니다.
우리는 보통 위에서 아래로 순차적으로 진행될 것으로 생각하며 코드를 짜게 되는 데 동기가 이해하기 쉽기 때문입니다.

비동기는 동기와 다르게 작업의 완료 여부를 신경쓰지 않습니다.
작업의 결과를 기다리지 않기 때문에 다른 작업을 수행할 수 있습니다.
비동기 작업은 작업이 완료되면 그대로 종료하거나 콜백 함수를 실행합니다.

## 2. 블로킹과 논블로킹

블로킹과 논블로킹은 전체적인 작업 흐름의 제어권을 가진 주체가 누구냐로 구분할 수 있습니다.

블로킹은 말 그대로 막힌, 제한되는 상태를 의미합니다.
메서드 A가 메서드 B를 호출한 순간 제어권이 메서드 B에 넘어가게 되고, 메서드 A는 제어권이 없으므로 메서드 B가 완료될 때까지 멈춰있게 됩니다.

논블로킹은 블로킹과 반대로 호출된 메서드에게 제어권을 넘겨주지 않습니다.
메서드 A가 메서드 B를 호출해도 제어권은 넘어가지 않기 때문에 메서드 A는 계속해서 작업을 수행할 수 있습니다.

## 3. 내가 사용하는 비동기 프로그래밍

저는 회사에서 프론트엔드 업무로 리액트를 사용하고 있습니다.
자바스크립트는 강력한 비동기 프로그래밍을 지원하며 쉽게 사용할 수 있습니다.

자바스크립트의 비동기는 Promise 객체로 쉽게 작업할 수 있습니다.
async/await 키워드는 Promise를 마치 동기처럼 작성할 수 있게 하는 키워드로 많이 사용됩니다.

```javascript
const getData = async () => {
    const response = await fetch(URL);

    if (response.status == 200) {
        return response.json();
    }

    throw new Error(response.status);
}
```

자바에서는 CompletableFuture 클래스로 비동기 프로그래밍을 구현할 수 있습니다.
함수형 프로그래밍 방식을 지원하여 코드가 간결하고 쉽게 예외처리를 할 수 있습니다.

```java
long start = System.currentTimeMillis();
List<CompletableFuture<Integer>> futures = new ArrayList<>();
futures.add(supplyAsync(this::메소드_완료_1초_필요));
futures.add(supplyAsync(this::메소드_완료_2초_필요));

CompletableFuture<List<Integer>> results = allOf(futures.toArray(new CompletableFuture[0]))
        .thenApply(v ->
                futures.stream().map(CompletableFuture::join).collect(toList())
        )
        .exceptionally(throwable -> {
            log.error("Unexpected error occurred: {}", throwable.getMessage());
            return emptyList();
        });

int result = results.join().stream().mapToInt(v -> v).sum();

long elapsed = System.currentTimeMillis() - start;
log.info("[전체시간={}s] 결과는 a + b = {}", MILLISECONDS.toSeconds(elapsed), result);
```

## 4. 메시지 큐를 사용하는 이유

메시지 큐는 프로세스 또는 프로그램 간에 데이터를 교환하는 방법 중 하나입니다.
메시지는 Producer 컴포넌트가 생성하여 메시지 큐에 담으면 Consumer 컴포넌트가 메시지를 확인하고 특정 작업을 수행하게 됩니다.

클라이언트와 서버를 연결하여 요청을 메시지 큐에 저장하여 서버가 되는대로 작업을 수행할 수 있도록 도울 수 있어 웹 애플리케이션 성능의 향상을 기대할 수 있습니다.
확장성이 좋아 스케일 아웃에도 장점이 있으며, 서버 하나가 내려가더라도 요청은 메시지 큐에 저장되어 있기 때문에 서비스 복구에도 용이합니다.

## 5. github repo

[https://github.com/chicken4zo/project](https://github.com/chicken4zo/project)
[https://github.com/PartyMoZip/projectPM](https://github.com/PartyMoZip/projectPM)