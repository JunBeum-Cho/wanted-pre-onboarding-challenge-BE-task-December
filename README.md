## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*



## 1-2) 사전 과제

#### 1. 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

* 동기(Synchronous)
    * 동기는 동시에 일어난다는 뜻으로, 동기 프로그래밍은 요청과 결과가 동시에 일어나고, A노드와 B노드의 작업 처리 단위를 동시에 맞추게 된다.
* 비동기(Asynchronous)
    * 비동기는 동시에 일어나지 않는다는 뜻으로, 비동기 프로그래밍은 요청한 그 자리에서 결과가 주어지지 않고, 노드 사이의 작업 처리 단위를 동시에 맞추지 않아도 된다.

#### 2. 블로킹과 논블로킹의 차이점을 설명해주세요.

* 블로킹(Blocking)
    * 자신의 작업을 진행하다가 다른 주체의 작업이 시작되면 자신의 작업을 멈추고 해당 작업을 기다렸다가 다시 자신의 작업을 시작한다.
* 논 블로킹(Non-Blocking)
    * 다른 주체의 작업에 관련 없이 자신의 작업을 하는 것을 의미한다.

#### 3. 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

* 자바 스크립트와 달리 파이썬은 기본적으로 동기 방식으로 동작하도록 설계된 언어다. 그렇기에 파이썬에서 비동기식 프로그래밍을 하기 위해서는 한번 주면 기다리기만 하는 함수를 발전시켜 멀티태스킹이 가능한 함수로 만들어야한다. 이를 코루틴(Coroutine)이라고 하는데, 파이썬에서는 Coroutine을 내장 라이브러리인 asyncio를 통해 구현 할 수 있다.
```python
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from articles.models import Team

connected_user = []
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        username = self.scope["user"].nickname
        if username in connected_user:
            pass
        else:
            print(connected_user)
            connected_user.append(username)
            print(connected_user)
            message = username + "님이 입장하셨습니다"
            await self.channel_layer.group_send(
                self.room_group_name, 
                {
                    "type": "chat_message", 
                    "message": message,
                    "username": "admin",
                    "connected_user": connected_user,
                }
            )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        username = self.scope["user"].nickname
        if username not in connected_user:
            pass
        else:
            connected_user.remove(username)
            message = username + "님이 퇴장하셨습니다"
            await self.channel_layer.group_send(
                self.room_group_name, 
                {
                    "type": "chat_message", 
                    "message": message,
                    "username": "admin",
                    "connected_user": connected_user,
                }
            )


    # Receive message from WebSocket
    async def receive(self, text_data):
        username = self.scope["user"].nickname
        userPk = self.scope["user"].pk
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        message = username + ":" +  message + ":" + str(userPk)
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message,
                "username": username,
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        # connected_user = event["connected_user"]
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "username": username, "connected_user": connected_user,}))
```
- 위는 제가 이번 프로젝트에서 비동기적 채팅을 구현한 코드입니다. `async`을 통해 코루틴을 정의하고, `await`을 사용해 정의한 코루틴을 호출합니다.

#### 4. 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

* 이중화 
  *  메시지 큐의 가장 명백한 장점 중 하나이다. 보통 애플리케이션은 충돌, 시간 초과, 코드 오류 등의 기타 문제가 있다. 이는 특히 매달 수백만 또는 수십억 건의 트랜잭션을 처리하는 애플리케이션에서 적용된다.
    큐는 메시지를 읽는 프로세스를 통해 트랜잭션이 완료되었으며 제거해도 안전하다는 것을 확인함으로써 이중화를 돕는다. 만약 어떤 것이 실패한다면, 메시지는 어딘가에 저장되어 있고 손실되지 않을 것이다. 나중에 재처리할 수 있다.
* 비동기 메시징
  * 대기열은 애플리케이션에 무언가 수행이 필요하지만 지금 수행 할 필요가 없거나 결과에 신경을 쓰지 않는 시나리오에서 유용 할 수 있습니다. 웹 서비스를 호출하고 완료 될 때까지 기다리는 대신 큐에 메시지를 쓰고 나중에 동일한 비즈니스 로직이 발생하도록 할 수 있습니다. 대기열은 비동기 프로그래밍 패턴 을 구현하는 훌륭한 방법 입니다.

#### 5. 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 

* [YAMMYCHU](https://github.com/Pangpyo/Yammychu)

#### (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

* 5번에서 제출한 프로젝트를 하면서, 장고에서 웹소켓을 사용한 채팅기능을 구현했었습니다. 하지만 배포단계에서 aws에 대한 지식 부족으로 결국 채팅기능은 배포단계에서 폐기되었었습니다. 이번 기회를 통해 백엔드 개발자로서 aws에 대한 기본 지식들을 배우고, 채팅기능이 왜 배포단계에서 실행되지 않았는지 배우고 싶습니다.