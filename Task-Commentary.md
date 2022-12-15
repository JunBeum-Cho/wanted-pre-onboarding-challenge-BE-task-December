## 목차
- [1번 문제](#1번-문제)
- [2번 문제](#2번-문제)
- [3번 문제](#3번-문제)
- [4번 문제](#4번-문제)
- [5번 문제](#5번-문제)

<br/>

## 1번 문제
### Q. 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
> **'결과 값을 기다린다'**: A 함수에서 B 함수를 호출했을 때, A 함수가 B 함수의 결과 값을 기다리는지 여부를 의미

- 동기: Synchronous, A 함수에서 B 함수를 호출했을 때, B 함수의 리턴 값을 계속 확인하면서 함수를 실행하는 것
- 비동기: Asynchronous, A 함수에서 B 함수를 호출했을 때, 콜백 함수를 함께 전달해 B 함수가 실행이 완료되었을 때 콜백 함수를 실행하는 것(B 함수의 실행 완료 여부는 확인하지 않음)

## 2번 문제
### Q. 블로킹과 논블로킹의 차이점을 설명해주세요.
> **'제어권'**: 자신의 코드를 실행할 권리, 제어권을 가진 함수는 자신의 코드를 끝까지 실행해 자신을 호출한 함수에게 리턴

- 블로킹: Blocking, A 함수가 B 함수를 호출했을 때, 제어권을 A 함수에서 B 함수로 넘겨줌
- 논블로킹: Non-blocking, A 함수가 B 함수를 호출했을 때, 제어권은 A 함수가 가지고 있음

## 3번 문제
### Q. 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
▶ Python
> **'코루틴'**: Coroutine, 특정 시점에 자신의 실행과 관련된 상태를 어딘가에 저장한 뒤 실행을 중단하고, 나중에 그 상태를 복원해 실행을 재개할 수 있는 서브 루틴  
> **'서브 루틴'**: Subroutine, 일반적으로 실행되는 함수

- 3.5 버전 이후, `asyncio`라는 비동기 표준 라이브러리의 `async`, `await`라는 키워드를 사용해 비동기 프로그래밍을 구현할 수 있다.
    - `async`: 함수 선언부에 함께 선언해 코루틴 함수 정의
    - `await`: 코루틴 함수 내에서 실행할 코루틴 함수와 함께 선언해 코루틴 함수를 중첩해 실행

```
import asyncio

async def do_async():
    pass

async def main_async():
    await do_async()

# 3.6 버전 이하 비동기 루프 실행
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async())
    loop.close()

# 3.7 버전 이상 비동기 루프 실행
if __name__ == '__main__':
    asyncio.run(main_async())
```

## 4번 문제
### Q. 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
> **'메세지 큐'**: 보관된 메세지를 사용자가 꺼낼때까지 안전히 보관된다는 특성을 보장하는 비동기 통신 매체

- 서비스 또는 서버 간 결합이 느슨해져서, 규모의 확장성이 보장되야하는 안정적 애플리케이션을 구성할 수 있다는 점이 장점이며, 알림 푸쉬 발송, 이메일 방송 등에 사용되어 시간이 오래 걸릴 수 있는 프로세스를 비동기적으로 처리한다.

## 5번 문제
### Q. 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)
@https://github.com/Jjenny-K/crowdfunding

<br/>

**★ 3번, 4번 문항 조금 더 상세히 알아보는 시간 가지기 ★**

<br/>

> **References**
>
> @https://velog.io/@nittre/%EB%B8%94%EB%A1%9C%ED%82%B9-Vs.-%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9-%EB%8F%99%EA%B8%B0-Vs.-%EB%B9%84%EB%8F%99%EA%B8%B0  
> @https://inpa.tistory.com/entry/%F0%9F%91%A9%E2%80%8D%F0%9F%92%BB-%EB%8F%99%EA%B8%B0%EB%B9%84%EB%8F%99%EA%B8%B0-%EB%B8%94%EB%A1%9C%ED%82%B9%EB%85%BC%EB%B8%94%EB%A1%9C%ED%82%B9-%EA%B0%9C%EB%85%90-%EC%A0%95%EB%A6%AC
>
>@https://blex.me/@baealex/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D  
>@https://it-eldorado.tistory.com/159
>
>@https://12bme.tistory.com/176