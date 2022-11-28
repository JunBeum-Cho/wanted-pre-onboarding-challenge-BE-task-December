## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

#### (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.   
동기와 비동기 프로그래밍은 프로세스의 실행 순서와 관련 있습니다.   

동기 프로그래밍은 작업을 수행하는 함수들을 동시에 처리합니다.   
즉, 두개 이상의 함수가 시작과 종료를 동시에 하거나 한 함수가 작업을 완료했을 때 다른 함수가 작업을 합니다.  

비동기 프로그래밍은 호출된 함수의 작업이 완료되지 않은 상태임에도 호출한 함수에 제어권을 넘기고 백그라운드로 작업을 합니다.   
이 때문에, CPU의 대기 상태를 최소화시켜 프로그램 효율을 향상시킬 수 있습니다.   

동기와 비동기를 코드로 구현하여 실행 시간을 비교하였습니다.

[ Synchronous ]
* Code
```python
import time

def print_sync(data: int) -> None:
    time.sleep(1)
    print("(func) print_sync -> " + str(data))
    
def main():
    print_sync(1)
    print_sync(2)
    print_sync(3)
    print_sync(4)
    print_sync(5)

if __name__ == '__main__':
    start = time.time()
    print("start time: " + str(start))
   
    main()   # 시작
    
    end = time.time()
    print("end time: " + str(end))
    print("elapsed time: " + str(end-start))
```
* Execution time
```cmd
start time: 1669634451.668655
(func) print_sync -> 1
(func) print_sync -> 2
(func) print_sync -> 3
(func) print_sync -> 4
(func) print_sync -> 5
end time: 1669634456.7038352
elapsed time: 5.035180330276489
```

[ Asynchronous ]
* Code
```python
import time
import asyncio


async def print_async(data: int) -> None:
    await asyncio.sleep(1)
    print("(func) print_sync -> " + str(data))
    
async def main():
    await asyncio.gather(
        print_async(1),
        print_async(2),
        print_async(3),
        print_async(4),
        print_async(5)
    )


if __name__ == '__main__':
    start = time.time()
    print("start time: " + str(start))
   
    asyncio.run(main())   # 시작
    
    end = time.time()
    print("end time: " + str(end))
    print("elapsed time: " + str(end-start))
```

* Execution time
```cmd
start time: 1669635072.3637366
(func) print_sync -> 1
(func) print_sync -> 3
(func) print_sync -> 5
(func) print_sync -> 2
(func) print_sync -> 4
end time: 1669635073.3815606
elapsed time: 1.0178239345550537
```


#### (2) 블로킹과 논블로킹의 차이점을 설명해주세요.     
블로킹과 논블로킹은 제어권과 결과 반환 시점에 따라 구별됩니다.   

블로킹은 호출된 함수에 제어권이 넘어가게 되며 작업이 완료된 시점에 호출한 함수에게 다시 제어권이 넘어옵니다.   
따라서, 작업이 완료된 후에 새로운 작업을 수행할 수 있습니다.   

![Blocking](https://user-images.githubusercontent.com/31979193/204277601-d3c1032f-dfaf-4ece-aa1c-db0f79f172ae.png)


논블로킹은 호출된 함수에 제어권을 넘기지 않고, 호출한 함수가 계속해서 제어권을 소유합니다.   
이 때문에, 작업 완료에 상관없이 새로운 작업을 수행할 수 있습니다.   

![Non-Blocking](https://user-images.githubusercontent.com/31979193/204277709-a848b233-c6e9-4709-99e1-a90e554bbeca.png)



#### (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.   
API 호출 권한을 체크할 때, 비동기 프로그래밍을 이용합니다.
```python
class AuthBackend(AuthenticationBackend):
    async def authenticate(self, conn: HTTPConnection) -> Tuple[bool, Optional[CurrentUser]]:
        current_user = CurrentUser()
        
        authorization: str = conn.headers.get("Authorization")
        if not authorization:
            return False, current_user

        try:
            scheme, credentials = authorization.split(" ")
            if scheme.lower() != "bearer":
                return False, current_user
            if not credentials:
                return False, current_user
        except ValueError:
            return False, current_user
        
        try:
            payload = jwt.decode(
                credentials,
                env.JWT_SECRET_KEY,
                algorithms=[env.JWT_ALGORITHM],
            )
            user_id = payload.get("user_id")
        except jwt.exceptions.PyJWTError:
            return False, current_user

        current_user.id = user_id
        return True, current_user
```
```python
@router.get(
    '/auth/test',
    response_model=Dict[str, str],
    dependencies=[Depends(PermissionDependency([IsAuthenticated]))]
)
def auth_test():
    return {'status': "success"}
```
```python
class BasePermission(ABC):
    exception = BaseException

    @abstractmethod
    async def has_permission(self, request: Request) -> bool:
        pass


class IsAuthenticated(BasePermission):
    exception = UnauthorizedException

    async def has_permission(self, request: Request) -> bool:
        if request.auth == False:
            return False

        key: str = request.headers.get('ConsumerKey')
        
        id = request.user.id
        check: str = await RedisBackend().get(key=id)

        if key == check:
            return True

        return False


class AllowAll(BasePermission):
    async def has_permission(self, request: Request) -> bool:
        return True


class PermissionDependency(SecurityBase):
    def __init__(self, permissions: List[Type[BasePermission]]):
        self.permissions = permissions
        self.model: APIKey = APIKey(**{"in": APIKeyIn.header}, name="Authorization")
        self.scheme_name = self.__class__.__name__

    async def __call__(self, request: Request):
        for permission in self.permissions:
            cls = permission()
            if not await cls.has_permission(request=request):
                raise cls.exception
```


#### (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
메세지 큐는 메세지 대기열 시스템으로 Publisher로부터 받은 Message를 Subscriber가 수신하고 처리할 수 있을 때까지 임시 버퍼(= Queue)를 사용하여 저장합니다. 이러한 유형의 통신을 비동기 통신이라고 합니다. 비동기 통신은 데이터를 손실시키지 않으며, 프로세스의 상태에 상관없이 정상적으로 작업을 수행합니다.

따라서, 메세지 큐을 사용하기 적합한 경우는 다음과 같습니다.
1. 서로 다른 애플리케이션 간의 통신 분리가 필요한 경우
2. 특정 데이터 저장소에 데이터를 빈번하게 전송하는 경우

![message queue](https://user-images.githubusercontent.com/31979193/204288981-14b36f29-51fa-47ee-9442-ad202c52333c.png)


#### (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
 `github repo` - [FastAPI_Basic](https://github.com/hahic/FastAPI_Basic)


#### (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
Kubernetes, CI/CD 관련된 수업을 듣고 싶습니다.
