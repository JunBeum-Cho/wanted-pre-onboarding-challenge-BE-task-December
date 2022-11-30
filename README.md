## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  
## 1-2) 사전 과제 
- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요
  - 동기 : 동기는 요청과 그 결과가 동시에 일어난다는 개념입니다. 쉽게 말하면 동기는 서버에 request(요청)를 보내고 response(응답)를 받을 때 까지 다음 동작을 하지 않고 순차적으로 일을 진행하는 것을 말합니다. 
  - 비동기 : 비동기는 요청과 그 결과가 동시에 일어나지 않는다는 개념입니다. 서버에 request(요청)를 보낸 후 response(응답)와는 상관 없이 다른 동작을 수행해도 되어 자원을 효율적으로 사용할 수 있습니다.
  
- (2) 블로킹과 논블로킹의 차이점을 설명해주세요
  - 블로킹 : 블로킹은 작업을 진행하다가 다른 주체의 작업이 시작되면 제어권을 다른 주체에게 제어권을 넘기고 멈춰 있다가 다른 주체가 끝난 이후 제어권을 돌려 받아서 진행하는 방식입니다.
           
  - 논블로킹 : 논블로킹은 작업을 진행하다가 다른 주체의 작업이 시작되어도 제어권은 그대로 가지고 있고, 다른 주체가 작업을 진행해도 자신의 작업도 계속해서 진행합니다.
  
- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
  - 저는 주로 Node.js 를 사용합니다 Node가 다른 서비스들에 비해 속도가 빠른 이유는 비동기성 프로그래밍 구조때문입니다.
  - Node.js 는 실행할 코드를 이벤트 루프로 가져와 실행하다가, 비동기작업이 발생하면 이를 스레드풀에 넘기고, 프로그램을 계속해서 진행합니다.
````javascript
async function waitFunction(time) {
    console.log(2)  // (3) 호출스택 -> console -2-
    const rst = await new Promise(function (resolve, reject) {
        console.log(3) 호출스택 -> console -3-
        setTimeout(() => { resolve(5) }, time)  // promise 가 resolve 될 때 까지 대기 후 -> queue에 갔다가 마지막에 console -5-
    })
    console.log(rst)
}

(async () => {
    console.log(1)  // (1) 호출스택 -> console -1-
    waitFunction(1000) // (2) 호출스택 -> but 대기
    console.log(4)  // (4) 호출스택 -> console -4-
})();

// result
// 1
// 2
// 3
// 4  
// 5

// 위와 같은 결과가 나오는 이유는 callstack(호출스택) 함수들을 실행하다가, callstack(호출스택)이 비어지게 되면 루프를 통해서 queue에서 비동기 작업에 대한 결과물을 callstack(호출스택)에 이동 // 시키고 이를 실행하기 때문입니다.

// Async / await
// callback함수를 전달받아 비동기 처리를 하는 promise 를 조금 더 편하게 사용
const userSignUp = async(req,res,next) => {
    try {
        const result = await sequelize.transaction(async (t) => {
            const { email, password, name, profileName } = req.body;
            const createUser = await User.create({  // (1) 유저의 정보를 DB에 저장
                email,
                password,
                name
            }, { transaction: t });
            const createProfileWithUserId = await Profile.create({  // (2) 저장된 유저의 정보를 사용하여 Profile을 생성 해 주었습니다.
                user_id: createUser.id,
                profileName
            }, { transaction: t });
            logger.info('info 회원가입 Test');
            return createUser;
        })
    } catch (err) {
        next(err);
    }
}

````

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
    - (1) 이메일 전송
      - 회원가입을 위해 이메일을 발급하는 서비스에서 이메일을 큐에 넣을 수 있습니다. 이메일 전송 전용 서비스는 이메일 만을 전송(어떠한 서비스에서 이메일 생산되었는지 상관없음)하게 되는데, 
      메시지 큐에 메시지 수가 너무 많아지는 경우 인스턴스를 한개 더 두면서 작업을 분산시킬 수 있습니다(확장성)
      
    - (2) 블로그 포스팅
      - 블로그에 사용자가 이미지를 업로드한 이미지를 바로 처리하지 않고 메시지 큐를 이용하여 사후처리를 하며 최적화 하는 경우
      
- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
  - https://github.com/top-hoon/Soomgo

- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
  - 실제로 현업에서 쓰이는 형태의 인프라 구조를 배우고 싶습니다..!
  - 아직 써보지 못한 aws 의 다양한 서비스들을 사용해 보고 싶습니다.

