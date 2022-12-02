## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
<pre>
    - 동기 : 모든 작업이 순차적으로 수행되는 것. A, B의 순서로 작업이 수행될 경우, B 작업은 A 작업이 완료될 때까지 기다려야 함.
    - 비동기 : 모든 작업이 순차적으로 수행되지 않음. A, B의 순서로 작업이 수행될 경우, B 작업은 A 작업의 완료여부를 신경쓰지 않음.

동기/비동기는 프로세스의 순서 보장에 대한 매커니즘, 함수의 작업 완료 여부와 함수 실행/리턴의 순차적인 흐름을 따르는지의 여부를 봄
</pre>
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
<pre>
    - 블로킹 : 작업을 시작하다가 다른 주체의 작업이 시작되면 다른작업이 끝날 때까지 기다렸다가 작업을 시작하는 것
    - 논블로킹 : 다른 주체의 작업에 관련없이 자신의 작업을 하는 것

블로킹/논블로킹은 전체적인 작업의 흐름을 막는지/안막는지 여부
</pre>  

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
<pre>
- CompletableFuture 인터페이스 사용

CompletableFuture<String> cf = CompletableFuture.supplyAsync(() -> "Hello");
cf.get(); // Hello
</pre>


- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
<pre>
- 몇 천명의 사람들이 한번에 주문을 할 경우, 트랜잭션의 순서와 동시에 처리되는 개수의 수를 제어할 수 있음.
- 기존 메시징 시스템에서는 메시지의 수가 많을수록 시스템의 성능이 크게 감소하였으나 메시지 큐는 메시지를 파일 시스템에 저장하기 때문에 메시지의 수가 많아도 성능이 크게 감소하지 않음.
</pre>


- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
<pre>
https://github.com/hodu-56/crud
</pre>

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
