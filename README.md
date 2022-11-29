## 1-1) 사전과제 진행 가이드

- 아래 총 5 문제에 대한 해설을 작성한 뒤 Pull Request를 날려주세요.
- 문제 해설에 대한 정해진 양식은 없으며, 최대한 자세히 해설해주시면 좋습니다.
- 문제 유형은 해당 코스에서 다룰 주제들을 포함하고 있으니 완벽히 이해하시면 코스를 수강하는데 큰 도움이 될 것입니다.

**문의 사항은 사전 과제 Repository의 Issue로 등록해 주세요.*
  


## 1-2) 사전 과제

- (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.
    1. 동기 : 동시에 일어난다는 뜻으로, 요청을 하면 시간이 얼마나 걸리던지 요청한 자리에서 결과가 주어져야 한다.
    2. 비동기 : 동시에 일어나지 않는다는 것을 의미하며, 요청과 결과가 동시에 일어나지 않는다.

- (2) 블로킹과 논블로킹의 차이점을 설명해주세요.
    1. 블로킹 : 제어권을A가 호출한 B함수에 넘겨준다.
        1. A함수가 B함수를 호출하면 B에게 제어권을 넘겨, B는 함수를 실행하고, A는 함수 실행을 잠시 멈춘다.
        2. B함수는 실행이 끝나면 자신을 호출한 A에게 제어권을 돌려준다.
    2. 논블로킹 : A함수가 B함수를 호출해도 제어권은 그대로 자신이 가지고 있는다.
        1. A함수가 B함수를 호출하면, B함수는 실행되지만, 제어권은 A함수가 그대로 가지고 있는다.
        2. A함수는 계속 제어권을 가지고 있기 때문에 B함수를 호출한 이후에도 자신의 코드를 계속 실행한다.

- (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.
    ```java
    // (1)
    public List<String> findPrices(String product) {
        // 첫번째 스트림 처리
        List<CompletableFuture<String>> priceFutures = 
            shops.stream()
            .map(shop -> CompletableFuture.supplyAsync(
                () -> shop.getName() + " price is " +
                            shop.getPrice(product)))
            .collect(Collectors.toList());

        // 두번째 스트림 처리
        return priceFutures.stream()
                        .map(CompletableFuture::join) // 모든 비동기 동작이 끝나길 기다린다
                        .collect(toList());
    }
    ```
    - 첫번째 스트림의 경우 supplyAsync는 반환값이 있는 경우 비동기로 작업 실행을 콜하는것을의미한다.
    - 두번째 스트림의 경우 map을 이용하여 모든 비동기 동작이 끝나기를 기다린다.
    <br/>

    ```java
    public static void main(String[] args) {
	
	
		Thread t = new Thread(()->{
			method1();
		});
		Thread t2 = new Thread(()->{
			method2();
		});
		Thread t3 = new Thread(()->{
			method3();
		});
		
		
		t.start();
		t2.start();
		t3.start();
		
	}
	
	public static void method1() {
		System.out.println("method1");
	}
	public static void method2() {
		System.out.println("method2");
	}
	public static void method3() {
		System.out.println("method3");
	}
    ```
    - 자바의 대표적으로 Multi Thread의 동작이 비동기식으로 작동한다.
    <br/>

- (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
    - 메세지 큐는 프로세스 또는 프로그램 간에 데이터를 교환할때 사용하는 방법중 하나로, 메시지 지향 미들웨어를 구현한 시스템을 의미한다.
    - 예시1) 이메일 전송
        - 비밀번호를 잊어버려서 임시 비밀번호를 받거나, 새로운 회원가입을 위한 인증 코드
        - 비밀번호 재설정을 위해 이메일을 발급하는 서비스, 회원가입을 위해 이메일을 발급하는 서비스 등은 메시지(이메일)을 큐에 넣을 수 있다.
        - 이메일 전송 전용 서비스는 이메일이 어느 서비스로부터 생산되었는지와는 관계없이, 메시지 큐의 메시지를 하나씩 소비하고, 그저 이메일이 전송되어야 할곳으로 이메일을 전송
    - 예시2) 블로그 포스팅
        - 사용자가 용량이 큰 이미지가 포함한 블로그 포스팅을 하면, 이미지는 저장소에 전송된다.
        - 업로드된 이미지에 대한 정보가 포함된 메시지를 이미지 최적화 서비스의 메시지 큐에 담아, 이미지 최적화 서비스는 저장소에서 이미지를 가져와 최적화하고, 저장해놨던 이미지를 대체한다.
    <br/>

- (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
    https://github.com/soyounjeong/Us
    
    <br/>
- (6 - Optional) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
    실서비스에서는 aws는 어떻게 사용하고 이를 활용할수 있는 부분에대해 배우고 싶으며, aws와 관련된 Docker와  Kubernates에 대해 어떻게 사용하는지에 대해 알고 싶습니다.
