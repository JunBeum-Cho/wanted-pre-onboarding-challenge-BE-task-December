# 원티드 온보딩 - 사전과제

### 1. 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

**[동기]**

동기 처리방식은 요청된 순서에 따라 작업을 순차적으로 진행하는 방식입니다. 예를들어 작업 A,B,C가 순서대로 요청될 경우, 작업은 A → B → C 순서로 처리됩니다.

[**비동기]**

비동기 처리방식은 작업이 요청된 순서와 관계없이 작업을 병렬적으로 처리하는 방식입니다. 예를들어 작업 A, B, C가 있고 처리에는 각 20초 10초 30초가 소요된다고 가정해봅니다. 이 경우, 요청 순서와 관계없이 먼저 처리가 완료된 작업인 B → A → C 순으로 결과가 반환됩니다.

**[차이점]**

1. 동기방식은 요청된 순서에 따라 작업을 처리하므로 직관적입니다. 비동기 방식에 비해 설계가 쉽다는 장점이 있습니다.

2. 비동기방식은 동기방식에 비해 자원을 효율적으로 사용할 수 있습니다. 
    작업 A, B, C가 순서대로 요청되었고, 각 처리에는 20초 10초 30초가 소요된다고 가정해봅니다. 동기방식으로 이 작업들을 처리하면 모든 작업이 처리 완료되는데 60초가 소요됩니다. B, C 작업은 각 20초 30초의 대기가 발생합니다. 
    반면, 비동기 방식은 A, B, C 시작(0초) → B반환(10초) → A(20초) → C(30초)와같은 순서로 작업이 처리되므로 자원을 효율적으로 사용할 수 있습니다.

### 2. 블로킹과 논블로킹의 차이점을 설명해주세요.

메서드 A와 B가 있고, A가 B를 호출했을때의 상황을 가정해 설명을 진행하겠습니다.

**[블로킹]**

블로킹은 A함수가 B 함수를 호출하면, A는 제어권을 B에게 넘겨줍니다.

이 경우, A는 B 함수에게 제어권을 넘겨주었으므로, A는 잠시 실행을 멈추고, B는 실행을 시작합니다.

**[논블로킹]**

논블로킹은 A함수가 B 함수를 호출했을 때, A와  B 모두 제어권을 가지고 있는 상황을 의미합니다.

이 경우, A와 B 둘 다 제어권을 가지고 있으므로 A함수는 B 함수를 호출한 이후에도 실행을 유지합니다. 즉, A와 B함수는 동시에 실행되게 됩니다.

### 3. 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

저는 C#을 사용하는데 익숙한 편입니다. 이 문항에서는 C#의 비동기 프로그래밍 방법에 대해 소개합니다.

설명을 위해 A는 아침식사를 준비하고 있는 상황을 가정해 보겠습니다. A는 아침식사에 간단하게 구운 식빵과 커피를 먹을 예정이며, 현재 아침식사를 준비하고 있습니다. 

위의 상황을 C# 코드로 나타내면 다음과 같습니다.

```csharp
public class Toster 
{
	public Bread BakeBread(Bread bread)
  {
		// 빵 굽기.
		// 7분 걸림.
  }
}

public class CoffeMachine
{
	public Coffe MakeCoffe(CoffeBean coffeBean)
	{
		// 커피 내리기
		// 10분 걸림
	}
}

Public class Life 
{
	private Toaster _toaster = new Toaster();
	private CoffeMachine _coffeMachine = new CoffeMachine();

	private void PrepareBreakfastWithBakedBreadAndCoffe ()
  {
		var bread = new Bread();
		var coffeBean = new CoffeBean();

		// 빵 굽기
		var bakedBread = _toaster
					.BakeBread(bread);

		// 커피 내리기
		var coffe = _coffe
					.MakeCoffe(coffeBean);
  }
}
```

위 코드는 메서드 내부의 코드를 동기적으로 실행합니다. 즉, 빵을 7분동안 구운 뒤, 커피를 10분동안 내리는 순서로 작업이 진행됩니다. 

아침식사는 빵을 먹을때쯤이면 이미 10분이 지나 식어있을지도 모릅니다. 하지만 실제 세계는 위 코드처럼 작업이 진행되지 않습니다. A는 빵 굽기와 커피 만들기를 동시에 시작할 것입니다. 
위 코드는 메서드 내부의 코드를 동기적으로 실행합니다. 즉, 빵을 7분동안 구운 뒤, 커피를 10분동안 내리는 순서로 작업이 진행됩니다. 빵을 먹을때쯤이면 이미 10분이 지나 식었을수도 있습니다. 

하지만 실제 세계는 위 코드처럼 작업이 진행되지 않습니다. A는 빵 굽기와 커피 만들기를 동시에 시작할 것입니다. 그렇다면 실제 세계에서 A의 아침식사 준비과정을 표현해 보겠습니다. 
작업 비동기적으로 실행되게 변경한 코드는 아래와 같습니다.

```csharp
public class Toster 
{
	public Task<BakedBread> BakeBread(Bread bread)
  {
		// 빵 굽기.
		// 7분 걸림.
  }
}

public class CoffeMachine
{
	public Task<Coffe> MakeCoffe(CoffeBean coffeBean)
	{
		// 커피 내리기
		// 10분 걸림
	}
}

Public class Life 
{
	private Toaster _toaster = new Toaster();
	private CoffeMachine _coffeMachine = new CoffeMachine();

	private async void PrepareBreakfastWithBakedBreadAndCoffe ()
  {
		var bread = new Bread();
		var coffeBean = new CoffeBean();

		// 빵 굽기 작업
		Task<BakedBread> bakingBreadTask = _toaster
					.BakeBread(bread);

		//커피 내리기 작업
		Task<Coffe> makingCoffeTask = _coffeMachine
					.MakeCoffe(coffeBean);
	

		// 구운 빵 가져오기.
		BakedBread bakedBread = await bakingTaks;

		// 커피 받기.
		Coffe coffe = await makingCoffeTask;
  }
}
```

C#은 각 비동기 작업을 Task<TResult> 객체로 추상화 합니다. 작업 결과를 비동기적으로 받고자 할 때는 awiat 키워드를 사용합니다. await를 사용하기 위해서는 메서드를 선언할 때, async Task<TResult> method()의 형태로 작성해야 합니다. 이때 asnyc는 컴파일러에게 이 메서드는 1개 이상의 await를 가지고 있음을 알리는 역할을 합니다.

컴파일러는 await 키워드를 만나면, 쓰레드가 정지되지 않고 다른 작업을 실행할 수 있도록 적절한 코드를 추가합니다. awiat는 해당 Task가 끝날때까지 기다린 후 값이 반환되면 다음 코드를 실행합니다.

```csharp
// 빵 굽기 작업
Task<BakedBread> bakingBreadTask = _toaster
			.BakeBread(bread);

//커피 내리기 작업
Task<Coffe> makingCoffeTask = _coffeMachine
			.MakeCoffe(coffeBean);
```

이 코드들은 빵 굽기 작업과 커피 내리기 작업을 동시에 시작한 것으로 볼 수 있습니다. 실제로 코드를 실행하면 대기시간 없이 이어지는 다음 코드를 바로 실행합니다.

```csharp
// 구운 빵 가져오기. 완료에 7분 소요
BakedBread bakedBread = await bakingTaks;

// 커피 받기. 완료에 10분 소요
Coffe coffe = await makingCoffeTask;
```

_toast.BakeBread()와 _coffeMachine.MakeCoffe()는 동시에 작업을 시작했습니다. 이제 A는 커피와 빵을 열심히 준비하고 있을 것입니다. A가 아침식사를 시작한 시점으로 7분 뒤 bakeBread에 bakingTask의 결과(BakedBread)가 반환될 것입니다. 마찬가지로 coffe에 makingCoffeTask의 결과 Coffe가 반한될 것입니다.

### 4. 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요

[**비동기적인 처리 (Asynchronous Invokation)]**

비동기적인 처리는 요청에 대한 처리 결과값을 즉시 반환할 필요가 없을 때 적합합니다. 

예를들어 한 블로그 사이트가 있다고 가정해봅니다. 이 사이트는 게시글을 저장할 수 있습니다. 또한 2개의 부가기능을 가지고 있습니다. 게시글을 저장하면 사용자를 팔로우하는 다른 사용자에게 알람을 전송합니다. 다른 사용자에게 글을 추천해주기 위해 글의 내용을 분석하는 기능도 있습니다.

A 사용자는 글을 저장하려고 합니다. 이때, A 사용자의 관점에서 부가기능에 대한 처리 결과는 중요하지 않습니다. 만약 글을 저장했을 때 부가적인 기능을 처리하느라 저장완료 메시지가 10초 이후에 전달된다면 사용자는 불편함을 느낄 것입니다.

이러한 상황에서 큐를 사용해 비동기적인 처리를 수행하는 아키텍처를 구현할 수 있습니다. A가 저장 버튼을 누르면 글을 저장한 뒤, 부가 기능을 위해 필요한 데이터를 큐로 전송합니다. 이후 사용자에게 저장 완료라는 피드백을 전달합니다. 이 과정은 최대 1초 이내로 소요될 것이며, 사용자는 즉각적인 피드백을 받음과 동시에 타 서비스는 부가기능을 실행하기 위한 충분한 시간을 얻을 수 있습니다.

[분산 **처리 아키텍처 구현]**

<aside>
💡 [상황 가정]
  한 SNS 사이트가 있습니다. 이 사이트는 엄청난 규모때문에 초당 100만건의 게시글 저장 요청이 발생됩니다. 이 사이트는 모든 게시글의 내용을 분석해 관심사가 비슷한 다른 사용자에게 글을 추천하고자 합니다. 사이트의 개발자는 서비스 초기에, 한 개의 서버로 내용 분석을 처리했으나  사이트의 규모가 커지자 개발자는 여러개의 서버에서 이 작업을 나누어 처리하려고 합니다.

</aside>

위 상황은 초당  100건이 발생하는 게시글 분석 요청을 여러대의 서버가 나누어 처리해야하는 요구사항이 있습니다. 또한, 인프라의 비용 최적화를 위해 모든 게시글은 한번만 처리되어야 합니다.

위 요구사항에서 큐를 사용해 여러개의 컨슈머(처리worker)를 가진 분산 처리 아키텍처를 사용할 수 있습니다. 큐는 일시적으로 데이터를 보관하는 기능을 수행함과 동시에, 자원 경쟁 문제를 적절하게 제어하는 특징을 가집니다. 큐는 매 데이터 요청마다(consuming) 중복되지 않은 데이터의 반환을 보장합니다. 이러한 큐의 특성을 이용해 n개의 워커가 큐를 참조하도록 구성하여 분산 처리 아키텍처를 구현할 수 있습니다.

큐를 참조하는 워커들은 데이터 중복 처리를 걱정할 필요 없이, 데이터를 처리하는데 집중할 수 있습니다.

### 5.  본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.)

저는 간단한 게시판 서비스를 개발한 경험이 있습니다. 이 게시판 서비스는 게시글의 CRUD 기능, 첨부파일 추가, 삭제등의 기능을 가지고 있습니다.

github: https://github.com/eagle-25/freelec-springboot2-webservice

service link: [http://peter-home-automation.link/](http://peter-home-automation.link/)

### 6. 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.

저는 AWS 자격증을 취득하며 AWS fundamental service와 아키텍팅에 대한 기초적인 지식을 갖추었습니다. 하지만 실무에서 AWS를 사용할 기회가 없었던 부분이 커리어적 경험에 아쉬움이 남습니다. 이번 기회를 통해 AWS를 서비스에 적용하기 위해 고민해야 할 부분을 다른 개발자분들과 함께 경험해보고 싶습니다.
