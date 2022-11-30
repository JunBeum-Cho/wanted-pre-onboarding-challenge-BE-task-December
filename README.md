## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

💡 **동기(synchronous)**

어떠한 작업이 순차적으로 실행되는 개념이며, 요청을 하면 결과가 반환되는 것을 기다려야 한다.
사용자가 데이터를 서버에게 요청한다면 그 서버가 데이터 요청에 따른 응답을 사용자에게 다시 리턴하기 전까지 사용자는 다른 활동을 할 수 없으며 기다려야만 한다.

💡 **비동기(Asynchronous)**

어떠한 작업이 동시에 일어날 수 있는 개념이며, 요청과 결과 반환이 동시에 일어나지 않는다.
서버에게 데이터를 요청한 후 요청에 따른 응답을 계속 기다리지 않아도되며 다른 외부 활동을 수행해도되고 서버에게 다른 요청사항을 보내도 상관없다.

**💡 동기와 비동기 프로그래밍의 장단점**

**동기방식**은 설계는 매우 직관적이지만, 결과 반환까지 대기해야 하기에 비효율적이라는 단점이 있다.
**비동기방식**은 설계는 병렬적으로 작업을 진행하기 때문에 자원을 효율적으로 사용할 수 있다는 장점이 있지만, 설계가 복잡한 단점이 있다.

---
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

**❓ 동기/비동기와 블럭/논블럭**

블록/논블록은 기술적으로 명확히 구분이 된다.
블록/논블록과 다르게 기술적으로 구분되지 않으며, 추상적인 구분 즉, 행위에 대한 이야기는 위에 설명한 동기/비동기 개념이다.

**💡 블럭(Block)**

A라는 함수를 실행했을 때, A라는 함수가 모든 행위를 끝마칠 때까지 기다렸다가 다른 함수가 실행되면 이것은 블로킹되었다고 한다.
즉, 호출된 함수가 자신이 할 일을 모두 마칠 때까지 제어권을 계속 가지고서 호출한 함수에게 바로 return 하지 않으면 블럭이다.

**💡 논블럭(Non-Block)**

만약 A라는 함수를 호출했는데, A라는 함수의 로직이 끝나기도 전에 B라는 함수가 실행된다면 이것은 논블록킹 되었다고 한다.
즉, 호출된 함수가 자신이 할 일을 마치지 않았더라도 바로 제어권을 바로 return하여 호출한 함수가 다른 일을 진행할 수 있도록 하면 논블럭이다**.**

---
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

💡 javascript

자주 사용하는 비동기 처리 방식은 제이쿼리의 ajax가 있다. 제이쿼리로 실제 웹 서비스를 개발할 때 ajax 통신을 빼놓을 수가 없습니다. 보통 화면에 표시할 이미지나 데이터를 서버에서 불러와 표시해야 하는데 이때 ajax 통신으로 해당 데이터를 서버로부터 가져올 수 있다.

```javascript
function getData() {
	let testData;
	$.get('https://domain.com/products/1', function(response) {
		testData = response;
	});
	return testData;
}

console.log(getData()); // undefined
```

또 다른 비동기 처리 사례는 setTimeout()이다. setTimeout()은 Web API의 한 종류다. 코드를 바로 실행하지 않고 지정한 시간만큼 기다렸다가 로직을 실행한다.

```javascript
console.log('Hello');

setTimeout(function() {
	console.log('Bye');
}, 3000);

console.log('Hello Again');

// ‘Hello’ 출력
// ‘Hello Again’ 출력
// 3초 있다가 ‘Bye’ 출력
```

setTimeout() 역시 비동기 방식으로 실행되기 때문에 3초를 기다렸다가 다음 코드를 수행하는 것이 아니라 일단 setTimeout()을 실행하고 나서 바로 다음 코드인 console.log('Hello Again');으로 넘어간다. 따라서, ‘Hello’, ‘Hello Again’를 먼저 출력하고 3초가 지나면 ‘Bye’가 출력된다.

💡 java

자바에서는 스레드를 사용하여 비동기 프로그래밍을 한다. 자바에서 스레드를 생성하는 방법은 두 가지가 있다.

☝️ Runnable 인터페이스를 구현하는 방법

✌️ Thread 클래스를 상속받는 방법

두 방법 모두 스레드를 통해 작업하고 싶은 내용을 run() 메소드에 작성하면 된다.

---
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

❓ 메시지 큐란

메시지 큐(Message Queue)는 프로세스 또는 프로그램 간에 데이터를 교환할 때 사용하는 통신 방법 중에 하나로, 메시지 지향 미들웨어(Message Oriented Middleware:MOM)를 구현한 시스템을 의미한다.

💡 사용 예시 2가지

☝️ **이메일 전송**

어떤 웹 사이트의 비밀번호를 잊어버려서 이메일을 통해 임시 비밀번호를 받거나, 새로운 회원가입을 위한 인증 코드를 전송하기 위해 사용한다. 사용자는 이러한 상황들에서 이메일이 즉각적으로 수신되기를 기대하지는 않는다. 어느 정도의 응답 지연이 허용되며, 어플리케이션의 핵심 기능은 아닌 경우이므로 메시지 큐는 이런 경우 사용한다.

**✌️ 블로그 포스팅**

모든 블로그 사용자가 웹에 최적화되어 있거나, 용량이 작은 이미지만 업로드하진 않을 것이다. 블로그 사용자가 게시글에 업로드한 이미지의 용량이 매우 큰 경우를 생각해보자. 블로그 서비스의 응답 시간을 저해하지 않으면서 사용자들에게 유연성을 제공하는 방법으로, 사용자가 업로드한 모든 이미지를 게시 과정에서 즉각 처리하는 것이 아닌, 사후처리하며 최적화하는 방법이 있다. 사용자 경험에 약간의 영향을 미칠 수는 있지만, 최적화는 응용 프로그램에서 가장 중요한 것은 아니며 작업을 즉시 수행할 필요도 없다. 메시지 큐는 이러한 상황에서도 사용될 수 있다.

---
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)

[https://github.com/skskdmsdl/pictureDiary](https://github.com/skskdmsdl/pictureDiary)

---
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
