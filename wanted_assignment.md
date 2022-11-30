# 사전과제

## 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

- 동기 프로그래밍: 동기 프로그래밍은 작업의 시작과 끝이 서로 연관있다. a 가 끝나면 b 가 시작되고 b가 끝나면 c가 시작된다. blocking 과 잘 어울린다. 직관적이지만 결과가 주어질 때까지 대기해야 한다.

```jsx
a:|---->|
b:	|---->|
c:	      |---->|
```

- 비동기 프로그래밍: 각 작업은 서로 연관성이 없다. a 가 끝나지 않아도 b,c,d 의 작업이 시작된다. 웹에서 하나의 요청이 끝나지 않았음에도 불구하고 다음 요청을 받아서 처리하는 예가 있다. non-blocking 과 자연스럽게 연결된다. 자원을 효율적으로 사용할 수 있지만 복잡하다.

```jsx
a:|---->|
b: |---->|
c:  |---->|
d:   |---->|
```

## 블로킹과 논블로킹의 차이점을 설명해주세요.

- 블로킹은 실행주체가 제어권을 넘긴다. 제어권을 이어받은 다른 실행주체의 작업이 끝날 때 까지 제어권을 넘겨준 실행주체는 작업을 멈춘다. 함수가 다른 함수를 호출 했을 때 제어권을 넘기므로 제어권을 넘겨받은 함수의 작업이 완료된 후 제어권을 돌려받은 함수가 나머지 작업을 이어나간다.
- 논블로킹은 실행주체가 제어권을 계속 가지고 있다. 제어권을 이어 받지 못한 다른 실행주체의 작업과 별도로 실행주체는 작업을 계속 이어나간다. 함수가 다른 함수를 호출 했을 때 호출 한 함수는 다른 작업을 계속 이어나간다. 호출 된 함수는 제어권 없이 별도로 작업을 한다.

## 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

- nodeJs 를 주로 사용함
- 비동기 프로그래밍을 사용하는 방법은 크게 3가지가 있다.
  - callback: callback 방식은 가장 기초적인 방법으로 하나의 작업이 끝나면 다음 작업을 callback 하여 작업을 이어나간다. 아래의 예에서 3초가 지나면 callback 을 실행한다.
  ```jsx
  setTimeout(callback, 3000);
  ```
  - promise: callback 은 이른바 ‘callback 지옥’ 처럼 가독성이 매우 나빠질 여지가 있다. 그래서 promise 를 사용한다. es6 에서 추가되었다. Promise 객체를 선언하고 resolve 는 에러 없이 성공 했을 때 callback 을 불러오고, reject 는 실패 했을 때 callback 이다. resolve 는 then() 으로 실행한다. reject 는 catch() 로 실행한다.
  ```jsx
  const fn = () =>
    new Promise((resolve, reject) => {
      resolve("성공");
    });

  fn().then((value) => console.log(value));

  const fn2 = () =>
    new Promise((resolve, reject) => {
      reject("실패");
    });

  fn2()
    .then()
    .catch((value) => console.log(value));
  ```
  - async / await: es7 에서 추가됐다. promise 역시 then 이 연달아 붙는 ‘promise 지옥’ 을 연출할 여지가 높다. 가독성이 좋지 않기 때문에 ‘syntatic sugar’ 인 async 를 사용할 수 있다. 아래의 예와 같이 함수에 async 를 붙이면 자동으로 promise 가 된다. 마찬가지로 then 과 catch, finally 를 사용할 수 있다. await 는 이름 그대로 어떤 작업이 끝날 때 까지 기다리라는 명령어다. 아래의 예에서 awiat 를 붙이지 않는다면 6초 후에 ‘성공1 성공2’ 가 인쇄되지 않고 바로 인쇄된다. await 를 붙이면 6초후 인쇄된다.
  ```jsx
  const fn = async () => {
    return "성공";
  };
  fn().then((value) => console.log(value));

  const fn2 = async () => {
    throw "실패";
  };
  fn2().catch((value) => console.log(value));

  /* --------------------------------------------- */

  const delay = (ms) => {
    return new Promise((resolve) => setTimeout(resolve, ms));
  };

  const fn1 = async () => {
    await delay(3000);
    return "성공1";
  };

  const fn2 = async () => {
    await delay(3000);
    return "성공2";
  };

  const fn = async () => {
    const a = await fn1();
    const b = await fn2();
    console.log(a, b);
  };

  fn();

  /* 위의 사례에서 3초 후 둘다 인쇄하는 방법 */
  const fn = () => {
    return Promise.all([fn1(), fn2()]).then((value) => value.join("+"));
  };

  fn().then((value) => {
    console.log(value);
  });
  ```

## 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

- 메세지 큐는 생산자와 소비자가 즉각 연결될 필요가 없는 상황에서 사용 가능하다.
- 어느 정도의 응답 지연이 허용되는 상황이 있다. 예를 들어서 이메일로 아이디나 패스워드를 찾는 경우가 있다. 메시지는 잠시 생산자에 의해 큐에 머물렀다가 이메일 전송 어플리케이션(소비자)이 큐에서 전송 서비스가 필요한 작업을 골라낸다. 고른 작업은 이메일로 전송된다.
- 언제 작업이 처리될지 확신 할 수 없기 때문에 핵심 기능보다 부가적인 기능을 수행하는데 메시지 큐를 사용한다. 예를 들어서 큐에 각각의 파일을 업로드하고 각 파일을 코드 검사 어플리케이션(소비자)이 하나씩 꺼내어 바이러스 검출을 할 수 있을 것이다.

## 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)

- https://github.com/sockwon/pre_on_boarding-4th-YOLO-Crocket

## 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

- AWS 를 사용할 일이 거의 없다보니 어떻게 활용해야 할지 감이 잘 잡하지 않습니다. 구체적인 사례와 함께 AWS 활용 방안을 배울 수 있다면 좋겠습니다
