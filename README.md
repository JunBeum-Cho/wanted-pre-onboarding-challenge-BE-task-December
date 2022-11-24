
## (1) 동기와 비동기 프로그래밍에 대한 차이점을 설명해주세요.

    동기 프로그래밍은 여러 작업들을 순차적으로 실행하도록 개발하는 것입니다.
    비동기 프로그래밍은 여러 작업들을 독립적으로 실행하도록 개발하는 것입니다.

##  (2) 블로킹과 논블로킹의 차이점을 설명해주세요.

    Blocking 개념
    작업을 요청한 프로세스/스레드가 해당 요청이 완료될 때까지 대기 상태에 있는 것을 의미합니다.
    
    NonBlocking 개념
    작업을 요청한 프로세스/스레드를 블락시키지 않고 요청에 대한 현재 상태를 즉시 리턴시킵니다. 그래서 스레드가 다른 작업을 수행할 수 있습니다. 
    그래서 요청한 작업에 대해서 완료를 확인해야 할 필요성이 있습니다.

##  (3) 본인이 주로 사용하는 언어에서 비동기 프로그래밍을 사용하는 방법을 설명해주세요.

    async
    python에서 함수 앞에 async를 등록 할 경우 해당 함수는 비동기 함수로 만들 수 있습니다.
    asyncio는 이벤트 루프와 코루틴을 기반으로 동작하며 데이터를 요청하고 응답을 기다리는 I/O bound한 작업에서 효율적입니다.
    코루틴 기반이므로 멀티 스레드와 비교하여 문맥교환에 따른 비용이 다소 적게 들어갑니다.
    
    이벤트 루프
    이벤트 루프는 작업들을 반복문 돌면서 하나씩 실행을 시킵니다. 이때, 실행한 작업이 데이터를 요청하고 응답을 기다린다면 
    다른 작업에게 event loop에 대한 권한을 넘깁니다. 
    권한을 받은 event loop는 다음 작업을 실행하고 응답을 받은 순서대로 대기하던 작업부터 다시 권한을 가져와 작업을 마무리합니다.
    
        
    비동기 함수로 만든 후 해당 함수를 실행시키기 위해선 asyncio.run() 안에 비동기 함수를 넣어주어야 합니다.
    
    print_numbers는 0.25초 간격으로 숫자를 출력하는 함수
    print_alphabet은 0.25초 간격으로 알파벳을 출력하는 함수입니다.

    이 때 각각의 함수에서 프린트 되는 숫자와 알파벳을 합쳐 두개의 함수가 서로 병렬적으로 실행되게 표현해보겠습니다.
    
    동기적으로 코드를 작성했을 경우 1번부터 26까지의 숫자를 출력하고 나서 알파벳을 출력하겠지만, 
    비동기적으로 코드를 작성함으로써 두 함수가 병렬적으로 실행되는 것을 확인할 수 있습니다.

## code
    import asyncio

    async def print_numbers():
        for i in range(1, 27):
            print(i, '->', end=' ')
            await asyncio.sleep(0.25)

    async def print_alphabet():
        for i in range(26):
            print(chr(ord('a')+i))
            await asyncio.sleep(0.25)

    async def main():    
        task1 = asyncio.create_task(print_numbers())
        asyncio.create_task(print_alphabet())

        await task1
    
    asyncio.run(main())


    import logging
    import socket
    import select


    logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

    def create_blocking(host, ip):
        logging.info('Blocking - creating socket')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        logging.info('Blocking - connecting')
        s.connect((host, ip))

        logging.info('Blocking - connected')
        logging.info('Blocking - sending')

        s.send(b'Hello\r\n')

        logging.info('Blocking - waiting')
        data = s.recv(1024)

        logging.info(f'Blocking - data = {len(data)}')
        logging.info('Blocking - closing')
        s.close()


    def create_nonblocking(host, port):
        logging.info('Non Blocking - creating socket')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        logging.info('Non Blocking - connecting')
        result = s.connect_ex((host, port)) #Blocking

        if result != 0:
            logging.info('Non Blocking - failed to connect')
            return

        logging.info('Non Blocking - connected')
        s.setblocking(False)

        input = [s]
        output = [s]

        while input:
            logging.info('Non Blocking - waiting')
            redable, writable, exceptional = select.select(input, output, input, 0.5)

            for s in writable:
                logging.info('Non Blocking - sending')
                data = s.send(b'hello\r\n')
                logging.info(f'Non Blocking - sent: {data}')
                output.remove(s)

            for s in redable:
                logging.info('Non Blocking - reading')
                data = s.recv(1024)
                logging.info(f'Non Blocking - data: {len(data)}')
                logging.info('Non Blocking - closing')
                s.close()
                input.remove(s)
                break

            for s in exceptional:
                logging.info('Non Blocking - error')
                input.remove(s)
                output.remove(s)
                break


    # create_blocking('voidrealms.com', 80)
    create_nonblocking('voidrealms.com', 80)


##  (4) 메세지 큐를 쓰는 이유에 대하여 2가지 예시를 서술해주세요.
        메세지 큐를 쓰는 목적은 서버가 사용자에게 빠르고 안정적으로 정보를 전달하기 위해 사용한다. 아래는 메세지 큐를 사용함으로써 갖는 장점이다. 
        
        메세지 큐는 생성된 메세지의 저장, 전송에 대해 동기화 처리를 진행하지 않고 큐에 넣어둠으로써 나중에 처리할 수 있다.
        소비자 서비스가 다운되더라도 어플리케이션이 중단되지 않고 메세지 큐에 소비되지 않은 메세지가 남아 있음으로써 소비자가 다시 시작될 때 메세지를 처리할 수 있다.

        예시)
        앱에 요청을 했을 때 어느정도 지연이 허용되는 경우 메세지 큐를 사용한다. 여러가지 상황에서 사용자가 인증번호 발급을 위해 하나의 api를 호출할 때 
        중간에 메세지 큐를 둠으로써 1)비밀번호를 잊어버렸을 때의 상황, 2)본인 확인을 위한 상황 등의 여러가지 상황에서 요청에 대응 할 수 있다.

 
##   (5) 본인이 작성한 서버 코드가 있는 github repo 주소를 제출해주세요. (CRUD 기능을 모두 포함하여야 하며, 서버에 대한 설명을 README에 작성해주시면 더욱 좋습니다.) 
        깃허브 링크
        https://github.com/woodstock1993/DRF
 
##   (6) 해당 수업을 통해 꼭 배우고 싶은 주제 또는 지식이 있다면 자유롭게 서술해주세요.
         대용량 처리를 하는 방법에 대해서 배우고 싶습니다.
