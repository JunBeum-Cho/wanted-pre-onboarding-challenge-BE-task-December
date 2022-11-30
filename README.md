## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

\*_문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요._

## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

(1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

동기와 비동기는 처리해야 하는 작업들을 어떠한 흐름으로 처리할 것이냐 에 대한 관점에 따라 구분됩니다.
동기는 현재 작업의 응답과 다음 작업의 요청의 타이밍이 일치하지만, 비동기는 현재 작업의 응답과 다음 작업의 요청의 타이밍이 일치하지 않아도 됩니다.
동기 방식은 상위 프로세스가 하위 프로세스에게 작업을 지시할 때 작업의 종료 시점을 알고 있어야 하지만, 비동기 방식은 상위 프로세스가 하위 프로세스에게 작업을 지시한 후부터는 작업의 진행 상황에 대해 전혀 신경쓰지 않습니다.
동기 방식은 작업의 종료가 순차적으로 이루어지는 것을 보장하지만, 비동기 방식은 작업의 종료가 순차적으로 이루어지는 것을 보장하지 않습니다.

(2) 블로킹과 논블로킹의 차이점을 설명해주세요.

블로킹과 논블로킹은 처리되어야 하는 작업이 전체적인 작업 흐름을 막는 지의 여부에 따라 구분됩니다.
블로킹은 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 자신의 작업을 멈추고 해당 작업을 기다렸다가 다시 자신의 작업을 시작합니다.
논블로킹은 다른 주체의 작업과 상관없이 자신의 작업을 합니다.

(3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

JavaScript 에서는 비동기 프로그래밍을 사용하기 위해 콜백(Callback) 함수, Promise, async/await 패턴이 존재합니다.

콜백 함수

콜백 함수는 다른 함수의 인자로 함수를 넘겨 비동기 처리를 합니다.

```
// 해당 코드는 [자바스크립트 Deep Dive, 이웅모 (2020)]의 프로미스(p842)에서 가져왔습니다.
const POSTS_URL = 'https://jsonplaceholder.typicode.com/posts';

const getPosts = (url, whenSuccess, whenFail) => {
  const xhr = new XMLHttpRequest();
  xhr.open('GET', url);
  xhr.send();

  xhr.onload = () => {
    if (xhr.status === 200) {
      whenSuccess(JSON.parse(xhr.response));
    } else {
      whenFail(xhr.status, xhr.statusText);
    }
  };
};

const handlePosts = (response) => {
  // ...
};

const errorHandling = (status, statusText) => {
  // ...
};

const posts = getPosts(POSTS_URL, handlePosts, errorHandling);
```

비동기 함수인 xhr.onload() 는 외부에서 그 값을 바로 참조하지 못하여, 무조건 콜백 함수 내에서 그 처리를 해야 합니다. 콜백의 후속 처리를 모두 그 콜백 함수 내에서 처리해야 하기 때문에, 위처럼 다시 콜백함수를 넘기는 수 밖에 없게 되었습니다.

콜백의 후속 처리를 위해 넘기는 콜백함수 내에 또 예외 처리를 해야 한다면 그에 따른 또 다른 콜백함수를 넘겨야 할 것입니다. 이런 상황은 콜백 헬(callback hell)로 이어질 수 있습니다.

Promise
Promise 의 등장으로 비동기 함수의 후속 처리가 콜백함수에 비해 다루기 훨씬 쉬워졌습니다.

```
// 해당 코드는 [자바스크립트 Deep Dive, 이웅모 (2020)]의 프로미스(p842)에서 가져왔습니다.
const POSTS_URL = 'https://jsonplaceholder.typicode.com/posts';

const getPostsWithPromise = (url) => {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();

    xhr.open('GET', url);
    xhr.send();

    xhr.onload = () => {
      if (xhr.status === 200) {
        resolve(JSON.parse(xhr.response));
      } else {
        reject(xhr.status, xhr.statusText);
      }
    };
  });
};

const posts = getPostsWithPromise(POSTS_URL);

posts
  .then((res) => console.log(res))
  .catch((err) => console.error(err))
  .finally(() => console.log('끝'));
```

Promise로 생성된 posts는 각각 then, catch, finally로 후속 처리가 가능합니다.

Promise는 비동기 함수 처리를 쉽게 할 수 있다는 것 외에도, 여러 비동기 처리를 병렬 처리할 때 사용하는 `Promise.all()`, 여러 비동기 처리를 다룰 때 가장 먼저 fulfilled된 처리 결과를 반환하는 `Promise.race()` 등 일반 콜백 함수로 다루는 것보다 보다 더 다양한 작업이 가능합니다.

async/await

Promise는 여전히 콜백 함수를 사용하기 때문에, 콜백 헬의 문제를 해결할 수 없었습니다. ES8에서 보다 간단하고 가독성 좋게 비동기 처리를 동기 처리처럼 구현하는 async/await가 도입되었습니다.

async/await는 Promise를 기반으로 동작하며, then/catch/finally와 같은 후속 처리 메서드 없이 마치 동기 처리처럼 사용할 수 있습니다.

```
const getPostWithAsync = async (url) => {
  try {
    const response = await fetch(url);
    return await response.json(); // 혹은 다른 형태로 데이터 전처리 가능
  } catch (err) {
    console.err(err);
  } finally {
    console.log('끝');
  }
};

const posts = getPostWithAsync(POSTS_URL);
console.log('posts: ', posts);

posts.then(console.log);
```

(4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
메시지 큐는 대용량 데이터를 처리하거나 데이터 처리의 복잡성을 줄이고, 의존성 최소화를 위해 사용합니다.

예시 1) 회원가입 시 사용자 인증 이메일 발송

회원가입 시 사용자 인증 메일을 발급받는 상황이 있습니다. 이때 이메일 기능을 메시지 큐에 등록해 처리할 수 있습니다.
이와 같은 방법은 메시지 큐에 들어오는 메시지가 많아지는 경우 이메일 발송 전용 인스턴스를 둠으로써 확장해 사용할 수 있습니다.

예시 2) 게시글 등록 알람 기능

게시글을 등록하면 나를 팔로우하고 있는 사용자들에게 알림을 보내주는 기능이 있습니다. 게시글을 등록하면 데이터베이스에 게시글 정보를 저장하고 다시 데이터베이스에서 팔로워들의 정보를 가져와 알림을 보내는 일련의 과정이 필요합니다.

이 과정에서 오는 대기 시간을 줄이기 위해 팔로워들에게 알림을 보내는 기능을 메시지 큐에 등록해 처리함으로써 단계를 줄일 수 있습니다.

(5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요.
https://github.com/devRonPark/3_backend_ron_cafe_curation

(6) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

AWS 환경에서의 전반적인 인프라 구성에 대해 학습하고 싶습니다.
