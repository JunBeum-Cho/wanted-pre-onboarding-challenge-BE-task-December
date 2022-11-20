## 성승영 (tmddud73@gamil.com)

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
  동기:요청을하면 결과값이 나와야하는것, 결과값이 나올때까지 기다린다.
  비동기:요청과 응답이 동시에 일어나지 않는다는 뜻으로 결과가 나올때까지 기다리지않는다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
  블로킹:요청을 하면서 제어권도 같이 넘겨줌, 그후 작업이 끝날때까지 기다리다가 작업이 끝나면 제어권을 돌려받는다.
  논블로킹:요청을 하지만 제어권은 자신에게 있기때문에 작업을 요청해놓고 자기는 할것함, 일찍끝나는것먼저 결과값을 받음,

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  JavaScript(Node.Js):
  논블로킹 I/O :오래걸리는 함수를 백그라운드로 보내서 다음 코드가 먼저 실행되게 하고, 나중에 오래 걸리는 함수를 실행
  논 블로킹 방식 하에서 일부 코드는 백그라운드에서 병렬로 실행됨
  일부 코드 : I/O 작업(파일 시스템 접근, 네트워크 요청), 압축,암호화 등
  나머지 코드는 블로킹방식으로 실행됨
  I/O 작업이 많을 때 노드 활용성이 극대화

  비동기 작업을할때 promise나 async await 방법으로 동기처럼 이용할 수 있음,

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.

 이메일 전송:
  어떤 웹 사이트의 비밀번호를 잊어버려서 이메일을 통해 임시 비밀번호를 받거나, 새로운 회원가입을 위한 인증 코드를 받아본 경험이 있을 것이다. 우리는 이러한 상황들에서 이메일이 즉각적으로 수신되기를 기대하지는 않는다. 아무리 성격이 급한 사람이라도 몇 분 안에 오겠거니 생각할 것이다. 어느 정도의 응답 지연이 허용되며, 어플리케이션의 핵심 기능은 아닌 경우이므로 메시지 큐는 이런 경우 도움이 될 수 있다.

 블로그 포스팅:
 모든 블로그 사용자가 웹에 최적화되어 있거나, 용량이 작은 이미지만 업로드하진 않을 것이다. 블로그 사용자가 게시글에 업로드한 이미지의 용량이 매우 큰 경우를 생각해보자. 블로그 서비스의 응답 시간을 저해하지 않으면서 사용자들에게 유연성을 제공하는 방법으로, 사용자가 업로드한 모든 이미지를 게시 과정에서 즉각 처리하는 것이 아닌, 사후처리하며 최적화하는 방법이 있다. 사용자 경험에 약간의 영향을 미칠 수는 있지만, 최적화는 응용 프로그램에서 가장 중요한 것은 아니며 작업을 즉시 수행할 필요도 없다. 메시지 큐는 이러한 상황에서도 사용될 수 있다.


- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)

  https://github.com/networkbanjang/NODE_React_SNS 의 BACK폴더.

  express를 이용한 프로젝트이며 프론트단은 Next입니다.
  인프런에있는 NodeBird강좌를 기본 베이스로잡고 추가적으로 웹소켓,외부API(KAKAO LOGIN)활용,프로필사진 바꾸기 등등의 기능을 구현했습니다.
  데이터베이스 CRUD는 Sequelize ORM을 사용하였습니다.

  https://github.com/networkbanjang/SpringBoot-KCAR.git

  일단 Java와 Oracle 쿼리(My batis)를 이용한 프로젝트도 있긴합니다.
  하지만 이건 국비교육시절때 팀프로젝트로 만든거여서 기술적인 질은 그다지 좋진못하고
  JAVA를 써본적있다. MVC패턴을 사용해서 프로젝트를 만든적이있다. 데이터베이스를 설계해본적이 있다. 
  정도입니다.

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

  요즘엔 백엔드 지망생도 인프라에대한 지식은 필수라고생각합니다.
  제가 아직 인프라에대한 지식은 빈약한데 이번기회로 인프라에대한것도 습득해서 좋은 백엔드개발자가 되고 싶습니다.