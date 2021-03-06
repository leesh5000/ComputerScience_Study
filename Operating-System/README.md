- [Introduction](#introduction)
  - [1. 운영체제](#1-운영체제)
  - [2. 운영체제의 목적](#2-운영체제의-목적)
  - [3. 운영체제의 분류](#3-운영체제의-분류)
  - [4. Multiprocessor](#4-multiprocessor)
  - [5. 커널](#5-커널)
  - [6. 운영체제의 예](#6-운영체제의-예)
  - [7. 운영체제의 역할](#7-운영체제의-역할)
- [컴퓨터시스템 구조](#컴퓨터시스템-구조)
  - [1. CPU](#1-cpu)
  - [2. 운영체제](#2-운영체제)
  - [3. Mode bit](#3-mode-bit)
  - [1. Timer](#1-timer)
  - [2. I/O Controller](#2-io-controller)
  - [3. Memory Controller](#3-memory-controller)
  - [4. DMA controller](#4-dma-controller)
  - [5. System call](#5-system-call)
  - [6. I/O 작업](#6-io-작업)
  - [7. Interrupt](#7-interrupt)
  - [8. a/synchronous I/O](#8-asynchronous-io)
  - [10. 컴퓨터의 작동방식](#10-컴퓨터의-작동방식)
  - [14. 메모리 계층 구조](#14-메모리-계층-구조)
  - [15. 프로그램이 실행되는 과정](#15-프로그램이-실행되는-과정)
  - [16. 커널의 가상메모리](#16-커널의-가상메모리)
- [Process](#process)
  - [1. 프로세스](#1-프로세스)
  - [2. 프로세스의 상태](#2-프로세스의-상태)
  - [3. PCB](#3-pcb)
  - [4. 문맥교환](#4-문맥교환)
  - [5. 프로세스를 스케쥴하기위한 큐](#5-프로세스를-스케쥴하기위한-큐)
  - [6. 컴퓨터 내부의 스케줄러](#6-컴퓨터-내부의-스케줄러)
  - [7. 프로세스](#7-프로세스)

## Introduction

### 1. 운영체제
- 컴퓨터시스템의 자원을 효율적으로 관리하기 위한 컴퓨터 소프트웨어
- 응용프로그램과 하드웨어의 사이에 존재
- 사용자와 컴퓨터 하드웨어를 연결
- 시스템이 부팅되면 메모리에 상주

### 2. 운영체제의 목적
- 컴퓨터시스템의 자원을 효율적으로 관리
- 컴퓨터시스템을 편리하게 사용

### 3. 운영체제의 분류
- 동시작업여부
  - 단일 작업(single tasking)
    - 한번에 하나의 작업만 처리
    - 예) MS-DOS 
  - 다중 작업(multi tasking)
    - 동시에 여러개의 작업 처리
    - 예) UNIX, MS Widows
- 사용자의 수
  - 단일 사용자
    - 예) MS-DOS, MS Windows
  - 다중 사용자
    - 예) UNIX, NT Server
- 처리방식
  - 일괄처리(batch processing)
    - 작업요청을 일정량 모아서 한꺼번에 처리 -> 응답시간이 김
    - 현대에는 거의 안쓰임
  - 시분할방식(time sharing)
    - 컴퓨터 처리능력을 일정한 시간 단위로 분할하여 사용
    - 짧은 응답시간가짐
    - 일반적인 PC 운영체제
  - 실시간(realtime OS)
    - 정해진 시간 안에 반드시 종료가 보장되는 시스템을 위한 OS
    - 예) 원자로/공장 제어, 미사일 제어

### 4. Multiprocessor
- CPU가 여러개
- 여기서 공부할 것은 하나의 CPU가 있는 범용 운영체제

### 5. 커널
- 운영체제 중에서 메모리에 상주하는 핵심부분
- 프로세스, 기억장치, 파일, 입출력 등을 관리

### 6. 운영체제의 예
- UNIX
  - 트리 구조의 파일시스템
  - 대부분 C언어로 작성(C언어는 UNIX프로그램을 만들기위해 개발된 것)
  - 높은 이식성
  - 소스코드 공개
  - 다양한 버전이 존재
    - 예) System V, FreeBSD, Linux
- MS Windows
  - plug and play
  - GUI
  - 선점형 멀티태스킹

### 7. 운영체제의 역할
- CPU 스케줄링
- 메모리 관리
- 파일 관리
- I/O 관리
- 프로세스 관리
- 그 외 하드웨어보호, 네트워킹 등등

<br><br><br>

## 컴퓨터시스템 구조

### 1. CPU
- 매 클럭 주기마다 PC(program counter)가 가리키는 메모리에 접근하여 명령어를 가져옴
- 가져온 명령어를 Decode
- 오퍼랜드를 인출
- 지정된 연산을 수행하고 결과를 저장

### 2. 운영체제
- CPU 통제를 담당
- 현대의 운영체제는 인터럽트에 의해 구동
- 운영체제는 평소에는 CPU 소유권을 갖지 않고, 인터럽트가 발생할때만 운영체제가 CPU 사용
- 인터럽트가 발생하면 인터럽트 백터에 있는 주소를 통해 ISR로 인터럽트를 처리한 후, 다시 사용자 프로그램에 CPU 소유권을 넘겨준다.
- 운영체제가 사용자 프로그램에게 CPU 소유권을 넘기기 전에 mode bit을 1로 바꾸고, Timer를 설정한 후 넘겨준다.

### 3. Mode bit
- 1은 사용자모드: 사용자 프로그램 수행
- 0은 커널모드: OS 코드 수행
- Interrupt 발생 시 mode bit이 0으로 바뀌고 CPU 소유권이 운영체제로 넘어감
- 운영체제가 사용자 프로그램에게 CPU 소유권을 넘기기 전에 mode bit을 1로 바꿈

### 1. Timer
- 정해진 시간이 흐른 뒤 운영체제에게 제어권이 넘어가도록 인터럽트를 발생
- CPU를 특정 프로그램이 독정하는 것을 방지
- Time sharing을 구현하기 위해 사용
- 운영체제가 사용자 프로그램에 CPU를 넘겨줄때 mode bit을 1로 하고 Timer를 설정한 후 넘겨준다.
- 사용자 프로그램에 운영체제가 할당한 Timer 시간이 끝나면, timer가 다시 CPU에 인터럽트를 걸어 사용자 프로그램으로 부터 CPU 제어권을 운영체제가 갖게한다.
- 결국 운영체제는 타이머 인터럽트의 도움을 받아서 여러 프로그램을 번갈아가면서 실행할 수 있다.

### 2. I/O Controller
- I/O장치를 관리하는 일종의 작은 CPU
- CPU가 I/O장치에 직접 접근하지 않고 이 Device controller를 통해 접근
- 제어정보를 위해 control register, status register를 가짐
- local buffer(data register)를 가짐

### 3. Memory Controller
- CPU가 메모리를 접근할 때 메모리 컨트롤러를 통해서 접근

### 4. DMA controller
- 직접 메모리에 접근할 수 있는 컨트롤러
- I/O장치가 메모리에 접근하기위해 CPU에 인터럽트를 거는데, 너무 자주 걸기때문에 CPU가 제 할 일을 못하는 경우가 발생
- 이것을 방지하기 위해 I/O 장치의 로컬버퍼 안에 작업이 다 완료되면 DMA가 직접 버퍼내용을 메모리에 복사한 후 CPU에 알려줌
- 이때, 동시에 접근하는 것을 방지하기 위해 memory controller에서 통제

### 5. System call
- 사용자 프로그램이 운영체제의 커널 함수를 호출하는 것

### 6. I/O 작업
- I/O 작업은 사용자 프로그램에서 직접 할 수 없고, 운영체제 커널을 통해서만 작업 가능
- 사용자 프로그램이 I/O 작업이 필요하면 CPU 인터럽트 라인을 통해 인터럽트 발생
- 사용자 프로그램이 운영체제에 요청하는 것을 시스템 콜이라고 함
- 먼저, 사용자 프로그램이 I/O 요청을 위해 운영체제에 인터럽트 발생 (소프트웨어 인터럽트 - system call)
- 운영체제에서 해당 요청을 검사 후, I/O 컨트롤러에 해당 작업을 지시한 후 CPU 소유권을 다른 곳에 넘김
- I/O 장치에서 시킨 일이 다 끝나면 I/O controller에서 CPU에 하드웨어 인터럽트를 발생
- 다른 곳에서 일을 하던 CPU는 인터럽트가 발생한 곳으로 이동 후 해당 작업 수행

### 7. Interrupt
- 인터럽트가 발생하면, PC의 현재주소를 저장한 후 CPU 제어를 ISR(인터럽트 서비스 루틴)에 넘김
- 인터럽트 벡터는 ISR의 주소를 가지고 있음
- ISR은 각각의 인터럽트마다 수행해야할 매뉴얼로 운영체제 안에 커널함수로 정의되어있음
- 하드웨어 인터럽트를 Intrrupt, 소프트웨어 인터럽트를 Trap

### 8. a/synchronous I/O
- synchronous I/O
  - I/O 요청 후 I/O 작업이 다 완료될때까지 기다림
- asynchronous I/O
  - I/O 요청 후 I/O 작업이 끝나기를 기다리지 않고 바로 CPU 제어를 얻어와서 다른작업을 함

### 10. 컴퓨터의 작동방식
- CPU는 매번 PC에 해당하는 메모리 주소에 있는 명령어를 실행함
- 메모리에는 사용자 프로그램, 운영체제 커널 등이 존재한다.
- CPU는 mode bit이라는 것이 있는데, 이것이 0이면 CPU의 ISA(기계어집합)를 전부 실행할 수 있고, 1이면 한정된 기계어(Instruction)들만 실행할 수 있음
- 운영체제가 CPU 제어권을 가지고 있을때는 mode bit이 0이라서 모든 instruction을 실행 할 수 있음
  - 예를들어, 다른 사용자 프로그램의 메모리에 접근하는 것 등의 mode bit이 0일때만 할 수 있는 instruction들이 있음
  - 또, I/O 장치에 접근하는 모든 instruction들은 mode이 0일때, 즉, 운영체제만 실행할 수 있도록 막혀있다.
  - mode bit이 1일때는 사용자프로그램이 CPU를 갖고 있을때로 한정된 명령어들만 실행가능함 (예를들어, 운영체제 커널의 메모리에 접근한다거나, I/O장치에 접근하는것 등은 mode bit이 0일때만 가능하므로 사용자프로그램이 CPU를 갖고있을때는 불가능)
- 만약, CPU가 사용자프로그램이 있는 메모리 주소에서 Instruction들을 실행하다가 I/O작업을 해야할 상황이 생기면, 현재 mode bit이 1이므로 (사용자프로그램에서 CPU를 가지고있으므로) I/O 작업을 못한다.
- 따라서, I/O 작업을 할 수 있는 (mode bit이 0인) 운영체제가 있는 메모리로 CPU를 이동시켜야하는데 운영체제가 있는 메모리로 CPU를 이동시키는 것은 mode bit이 1일때는 못하므로 사용자프로그램에서 의도적으로 CPU에 있는 Interrupt line을 필요한 작업에 알맞은 번호로 세팅을 한다. (예를들어, 키보드 입력이 필요하면 키보드 입력 인터럽트 3번으로 세팅)
- 그러면, CPU는 인터럽트 라인이 세팅되었으므로 하던 일을 멈추고 인터럽트 라인의 세팅된 번호에 해당하는 매뉴얼이 있는 운영체제가 상주하는 메모리 주소로 이동해야한다.
- 운영체제가 있는 메모리로 간 CPU는 이제 인터럽트 라인에 세팅된 번호에 해당하는 매뉴얼을 수행해야하는데, 이 번호에 해당하는 매뉴얼이 있는곳을 나타내는 것이 인터럽트 벡터이다. 또한, 이 인터럽트에 해당하는 매뉴얼들이 인터럽트 서비스 루틴(ISR)이다. ISR은 운영체제 안에 존재하며, 인터럽트마다 수행해야할 커널 함수들이 정의되어있다.
  - 운영체제로 간 CPU는 인터럽트 벡터에 있는 해당 인터럽트 번호에 해당하는 메모리 주소로 이동해야한다. (운영체제의 커널함수가 있는 주소) 해당 인터럽트에 해당하는 메모리 주소에는 ISR이 있는데, 이 ISR이 해당 인터럽트에 알맞은 처리 작업 명령어들이 있다. CPU는 이제 이 명령어들을 수행한다.
  - 위에서 받은 인터럽트가 키보드 입력을 받는 인터럽트이므로, ISR에는 키보드 입력을 요구하는 작업들이 있다. 이 작업을 실행하여 키보드 입력을 요구한다.
    - 이때, 키보드와 같은 I/O 장치들에 직접 접근하지는 않고, device controller를 통해 접근한다. 각 I/O 장치들 마다 자신들을 통제하는 cpu들이 있는데 이것을 device controller라고한다. 이 device controller에는 제어정보를 위한 control register, 상태정보를 위한 status register, 현재 값을 저장하기 위한 local buffer들이 있다.
    - I/O 작업은 동기식 입출력, 비동기식 입출력 두 가지가 있다. 동기식 입출력은 사용자 프로그램에서 I/O 작업을 요청 후 해당 입출력 작업이 완료될때까지 기다리는 것이다. 하지만, 전부 다 기다리는 것은 너무 낭비가 크기 때문에 주로 기다리지 않고, 다른 사용자 프로그램에게 CPU 제어를 주는 방법을 사용한다. 비동기식 입출력은 해당 입출력 작업을 기다리지 않고, 요청만 해놓고 곧바로 해당 프로그램의 다음 명령을 실행하는 것이다.
    - I/O 작업은 Cpu에 비해 수백만배 속도가 더 느리다. 그래서 CPU가 이 I/O 작업을 계속 기다리는 것은 낭비이므로, 운영체제는 cpu 제어권을 다른 프로그램에게 넘겨 CPU가 계속 일을 할 수 있도록 한다. (운영체제가 cpu 제어를 넘긴다는것은 즉, CPU가 실행하고있는 ISR에 분기 명령어가 있다는 뜻)
    - I/O 요청 후, I/O 작업이 다 끝나지 않아서 CPU가 다른 일을 하고 있다고 생각해보자. 이때, I/O 장치에서 운영체제에서(ISR 해당하는 작업) 요청한 작업이 다 끝나면, I/O 장치(device controller)는 CPU에게 인터럽트 라인을 세팅하여 I/O 작업이 모두 끝났음을 알려준다. 이러한, 하드웨어에서 요청하는 인터럽트를 Interrupt라고 한다.
      - 하지만, 이때 너무 많은 I/O 장치들이 CPU에 인터럽트를 건다면, 사용자 프로그램에서 작업하던 CPU가 하던 일을 멈추고 다시 OS로 가서 인터럽트를 처리하는 등 상당한 오버헤드가 발생한다. (예를들어, I/O 장치에서 입력이 생기면 메모리에 가서 입력값을 복사해줘야하는데 메모리에 접근할 수 있는 것은 CPU 뿐 이므로 인터럽트를 발생시켜줘야한다.)
      - 즉, 이런 작은 일 하나하나 마다 CPU에 인터럽트를 걸면 CPU에 발생하는 오버헤드가 너무 커지기 때문에 DMA controller라는 장치가 있다.
        - 이 DMA는 direct memory access로 원래 cpu만 직접 접근할 수 있는 메모리에 DMA도 CPU의 중재없이 메모리에 접근할 수 있다. 즉, I/O 장치는 I/O 작업을 요청받으면, 자신이 가지고 있는 버퍼에 요청한 내용을 추가하고, DMA는 이 버퍼의 내용을 메모리에 추가한다. 여기서 버퍼의 내용은 block단위이다. 그 후, 요청한 만큼 데이터가 추가되면, DMA가 CPU에 인터럽트를 한 번만 걸어서 알려준다. 이렇게 함으로서 CPU가 인터럽트 되는 빈도를 줄여 오버헤드를 감소시킬 수 있다.
      - 본래 CPU만 메모리에 접근할 수 있다. 하지만, I/O 장치가 CPU에 인터럽트를 걸
    - 그러면, CPU는 또 다시 운영체제로 가서 (CPU는 운영체제 아니면 사용자프로그램 둘 중 하나의 일을한다. 이 처럼 현대의 운영체제는 인터럽트가 발생할때만 CPU를 소유한다.) 아까 분기한 ISR 명령어로 돌아간뒤, 남아있는 ISR 작업을 완료한다. (여기서는 키보드의 입력 인터럽트였으므로, 입력받은 값을 메모리로 복사해 온다)
    - ISR 작업을 다 완료하면, 이제 운영체제는 CPU를 다른 사용자프로그램에 넘겨준다. 이때, 그냥 넘겨주지는 않고 mode bit를 1로, Timer를 일정시간으로 설정한 뒤 넘겨준다.(넘겨준다라고 했는데, 실제로는 CPU가 ISR 명령어를 모두 완료하면, ISR 명령어의 끝에 mode bit, timer 설정 명령어를 실행하고 아까 진행 중이던 사용자 프로그램 메모리 주소로 JUMP하는 명령어를 실행한다.)
  - timer란, 
- 이것처럼 사용자 프로그램과 같은 소프트웨어가 직접 인터럽트를 발생시킨 것을 Trap(소프트웨어 인터럽트)이라고 하며, Trap에는 두 종류가 있는데, 위에처럼 사용자 프로그램이 직접 운영체제의 커널함수를 호출하는 것을 System call이라고하며, 프로그램 오류에 의해서 호출되는 인터럽트는 Exception이라고 한다.
- CPU가 운영체제가 있는 메모리에서 ISR 작업을 완료하면, 이제 운영체제 소프트웨어가 CPU의 소유권을 다른 사용자 프로그램이 있는 메모리 주소에 넘겨준다.(기계어의 JUMP등의 명령어)
- 이때, 운영체제는 그냥 넘겨주지 않고, mode bit을 1로 바꾸고, timer에 일정시간을 설정한 후에 CPU의 제어권을 다른 사용자 프로그램으로 넘긴다.
- 여기서 timer란, 컴퓨터 내에 존재하는 하드웨어로 CPU를 특정 프로그램이 독점하는 것을 방지하는 장치이다. 운영체제가 작업이 다 끝나면 타이머에 시간을 설정한 후 사용자 프로그램에 CPU를 넘겨준다. 타이머에 할당된 시간이 끝나면, 타이머에서 CPU의 Interrupt line을 통해 인터럽트를 발생시키킨다. 그럼 CPU는 다시 운영체제로 가서 운영체제가 지시하는 작업을 수행한다. 이떄 운영체제는 또 타이머에 시간을 설정한 후 다른 사용자 프로그램에 CPU를 넘겨준다. 이런 방식으로 운영체제는 CPU가 매우 짧은 시간동안 여러 프로그램들을 작업할 수 있도록 한다. 이런 방식을 Time sharing이라고 한다.

### 14. 메모리 계층 구조
- Register -> Cache -> Main memory -> Magnetic Disk -> ...
- 오른쪽으로 갈수록 가격과 속도가 낮다. 
- Register, Cache는 SRAM으로 만든다. SRAM은 트랜지스터 6개로 구현되며, 속도가 빠르고 전력이 공급되는 한 정보를 유지한다.
- Main memory는 DRAM으로 만들어져있다. DRAM은 트랜지스터 1개로 구성되며, 정보 유지를 위해 따로 리프래쉬를 해줘야한다.
- SRAM이 DRAM 보다 더 비싸고, 크고, 빠르다.
- 레지스터는 CPU 코어 내부에 있고, 캐시는 코어 외부 CPU 내부에 있다.
- 레지스터에는 IR, MBR, MAR 등 여러종류가 있다. 이 레지스터에는 Instruction, 오퍼랜드 등이 Load-Store 방식으로 저장된다.
- 캐시는 램에서 자주 사용되는 데이터를 지역성의 원리에 따라 재사용을 목적으로하는 저장공간으로, CPU와 RAM의 거리 차이를 좁히기 위해 둔 장치이다.

### 15. 프로그램이 실행되는 과정
- 대부분의 프로그램은 하드디스크에 파일형태로 담겨있다.
- 프로그램의 실행파일을 실행하면, 프로그램의 Address space가 형성되는데 이것은 메모리 주소 공간이다. 즉, 0번지부터 시작되는 프로그램 만의 독자적인 주소 공간이 생성된다.
- 이 독자적인 주소공간은 code, data, stack 영역으로 구성된다. code는 프로그램의 기계어 코드, data는 전역변수와 같은 프로그램에 사용되는 되는 자료구조, stack은 함수 구조의 지역변수, 매개변수와 같은 변수들이 저장된다.
- 이러한 독자적인 주소공간을 가상메모리라고 한다.
- 가상메모리가 완료되면, 이제 이것을 물리적인 메모리에 적재시킨 후 프로그램을 실행한다. 이때, 메모리에는 커널 영역이 있는데 이것은 운영체제의 프로그램이 적재된 것으로 컴퓨터가 부팅 후 종료될때까지 메모리에 항상 상주한다.
- 일반 사용자 프로그램들은 실행되면, 가상메모리를 생성한 후 물리적인 메모리에 적재하는데, 이때 가상메모리의 모든 부분을 메모리에 담는 것은 아니고 프로그램의 실행에 당장 필요한 것만 메모리에 적재시킨 후, 그렇지 않은 부분은 하드디스크의 Swap area에 내려놓게 된다.
  - 가상메모리의 주소를 물리적인 메모리의 주소로 적재시킬때, 변환 작업이 필요한데, 이것을 `Address translation`이라고 하며, 운영체제가 하는 것은 아니고 주소변환을 담당하는 하드웨어 장치에서 이것을 담당한다.
  - Swap area는 메모리 용량의 한계로 메모리 연장 공간으로 사용되는 것이다. 즉, 프로그램이 종료되면 사라지는 램과 마찬가지로 Swap area도 사라진다.
- 즉, 가상메모리는 프로그램이 실행되면 생성되는 각 프로그램마다 갖는 독자적인 주소 공간이며, 실제 물리적으로 존재하는 것은 아니다.
- 프로그램의 실행파일을 실행하면, 프로그램 구동에 꼭 필요한 부분만 물리적인 메모리에 적재되어 프로세스가 된다.

### 16. 커널의 가상메모리
- code: 하드웨어 자원을 관리하는 코드, (하드웨어)인터럽트 처리 코드, 시스템콜 처리 코드, ...
- data: 운영체제가 관리를 위해 사용하는 여러 자료구조, 프로세스 관리를 위해 자용하는 자료구조(PCB)
- stack: 운영체제도 함수 구조로 코드가 짜여져있기 때문에 함수를 호출하거나 반환할때 사용

<br><br><br>

## Process

### 1. 프로세스
- Process is a program in execution
- 프로세스의 문맥은 프로그램이 처음에 실행된 후 언젠가는 종료가 되는데 문맥이란것은 중간 어느시점을 딱 봤을때, 이 프로그램이 현재 시점이 어떤상태인지, 정확하게 나타내기 위해서 사용되는 개념이 문맥이다. 즉, 프록세스의 문맥이란것은 특정시점을 봤을떄 이 프로세스가 어디까지 수행을 했고 또 
- 프로세스는 실행이 되면 , 이 프로세스만의 독자적인 주소공간이 형성되는데, 이 프로세스가 CPU를 잡게되면 프로그램 카운터라는 래지스터가 이 프로세스의 코드 어느 부분을 가리키게되고 그러면 매순간 이 프로세스의 공간에서 기계어를 하나씩 불러들인후 데이터 레지스터에 집어넣고 산술논리연산장치에서 연산을 한다. 그 다음에 그 결과를 레지스터에 저장하거나 혹은 바깥의 메모리에 다시 저장을 한다. 이런식으로 계속 짆애을하다가 과연 이 프로세스는 어디까지 와있는가를 규명하는 것이 바로 프로세스의 문맥이다.
- 그래서 현재시점의 프로세스 문맥을 나타내기 위해서는 이 PC가 프로세스의 코드영역의 어느부분까지 실행했는가를 알아야하고 그 다음에 이 프로세스의 메모리에 어떤내용을 담고있는가 (예를들어 프로세스가 실행되면서 함수같은거를 실행했으면 스택영역에 데이터들이 쌓여있을것이다, 또한 데이터영역의 변수 데이터들) 또는 프로그램이 실행되면서 현재 래지스터에 어떤값이 있으며 어떤 명령어 까지 실행했는가 이런 모든 요소를 알아야지만 프로세스의 현재 상태를 알 수 있는데,  이 프로세스의 현재상태를 나타내는데 필요한 모든 요소를 프로세스의 문맥이라고 한다. 즉, 프로세스의 현재 시점의 정확한 상태를 규명하기 위해서 필요한 요소들을 문맥이라고 부른다.
- 문맥은 크게 3가지로 설명을 할 수 있다. 먼저 첫번쨰는 시피유와 관련된 하드웨어 문맥이다. 프로세스라는것은 시피유를 잡고 매순간마다 명령어를 실행하는데 즉 현재시점의 이 프로세스가 명령어를 어디까지 실행했는가를 알기위해서는 현재 레지스터와 pc가 어디를 가리키는지 이런 것들이 필요하다. 즉 이런것을 하드웨어문맥이라고 한다. 주로 레지스터와 PC를 맗나다.
- 두번쨰는 메모리와 관련된 프로세스의 주소공간인데, 즉 현재시점의 이 프로세스의 코드,데이터,스택영역에 어떤내용이 들어있는가 이걸 알아야 프로세스의 현재상태를  정확하게 나타낼수잇다.
- 세번째는 운영체제의 역할 중에 하나가 현재 컴퓨터에 실행되고있는 프로세스를 관리하는역할이다. 그래서 프로세스가 하나 시작될때마다 운영체제는 이 프로세스를 관리하기 위해서 자신의 데이터영역에 PCB라는 프로세스 관리 자료구조를 만드는데, 즉, 프로세스가 하나씩 실행될때마다 운영체제는 이 pcb라는 것을 하나씩 두고있으면서 이 pcb한테 각종 하드웨어 자원, 즉, cpu, 메모리등을 얼마나 줘야할지 혹은 이 프로세스가ㅏ 나쁜짓을 하지는 않는지 이런것을 관리하는 역할을 한다. 즉, 프로세스의 현재상태를 알려면 하드웨어와 프로세스의 주소도 알아야하지만, 운영체제가 이 프로세스를 어떻게 생각하는ㄴ지도 알아야한다. 이것들은 운영체제의 pcb, 커널스택를보면 알수잇다. 이 커널스택은 무엇이냐면, 각 프로세스가 만약 자신 프로세스안에서 함수호출이 이루어지면 자신의 스택영역에서 함수를 호출한다음에 리턴, 또는관련된 정보들을 쌓아두고 이것들을 사용한다. 만약에, 프로세스가 실행도디ㅏ가 i/o작업같은 프로세스에서 할 수 없는일을 하려면 운영체제에 요청을해야한다(시스템콜) 이 시스템콜을 하게되면, 현재 진행중이던 프로세스를 가리키던 프로그램 카운터가 운영체제 커널 주소공간에 커널함수가 있는 곳을 가리키게 되고 cpu는 이 커널함수르 실행하게된다. 이 커널도 코드,데이터,스택영역이 있는데, 커널함수호출이 이루어지면 커널스택에다가 관련되 정보들을 쌓아둔다. 근데 이 커널은 다른 프로세스(프로그램)과는 좀 다른데 왜냐면 커널은 여러 사용자 프로그램(프로세스)들이 공유할 수 있는 코드이다. 즉 어떤 프로세스간에 운영ㅇ체제한테 요청을 해야하기때문에 이 커널함수는 모든 프로세스가 공유할수잇어야한다. 이제 커널입장에서는 요청이 들어왔을떄 이게 누구 프로세스의 요청인지 알아야하니까 스택에다가 어떤 프로세스가 커널함수를 호출했는지 정보를 담아야한다. 즉, 운영체제의 커널은 스택에 프로세스마다 별도로 담고있다. 
- 즉 이러한 일련의 정보들을 가지고 있으면 현재 프로세스가 어떤 상태를 가지고 있는지 정확하게 규명할 수 있다. 그렇다면 왜 이렇게 프로세스의 현재 상태를 규명해야할까? 만약, 프로세스가 혼자실행된다면 우리는 프로세스의 문맥상태를 알 필요가 없다. 하지만 현재의 컴퓨터는 시분할 시스템, 멀티태스킹, 즉 프로세스들이 번갈아 가면서 실행하기때문에 하나의 프로세스가 cpu를 잡고있다가 , 운영체제에 다시 cpu를 주고, 운영체제는 다시 다른 프로세스한테 cpu를 주고 이런 방식으로 하기떄문에 현재 만약 이 프로세스가 cpu에 레지스터값을 넣고 어떤 값을 실행하고있었다고 할떄 즉 이 정보들을 (프로세스의문맥) 어딘가에 기록해둬야한다. 기록하지않으면  다음에 다시 이 프로세스가 cpu를 잡았을때 다 까먹게 되므로 항상 프로세스의 문맥을 파악하고있어야한다. (정확히 프로세스가 어디까지 실행했는지를 알아야한다)
  
### 2. 프로세스의 상태
- 프로세스는 이런방식으로 상태를 바꿔가면서 실행하는데, 컴퓨터 안에 cpu는 하나뿐이다. (싱글코어인 cpu라고가정하자) 즉, cpu가 하나밖에 없기떄문에 cpu를 잡고있는 프로세스는 매 순간 하나이다. 즉 지금 cpu를 잡고 명령어를 실행하고이는 프로세스의 상태를 바로 running이라고 부른다. 또한 cpu를 기다리고 있는 프로세스가 있는데 이 프로세스는 ready상태이다. 근데 이 ready는 당장 이 프로그램이 cpu에서 실행이 되려면 당장 필요한 부분은 적어도 물리적인 메모리에 올라와있어서 cpu를 잡았을때 바로실행할수 있는 상태가 바로 ready이다. (cpu가 i/o접근은 못하니까 i/o작업 데이터들은 물리적인 메모리에 다 올려놓은 상태) 대부분은 이 rady상태의 프로그램들이 cpu를 잡고 놨다 하면서 시분할 시스템을 구현한다., 다음은 cpu를 지금 줘봤자 명령어를 실행할수없는 상태인데, 예를들어 시간이 오래걸리는 I/O작업을 한다ㄴ든지 디스크에서 뭘 읽어와서 반드시 이 읽어온 값이 있어야 다음 명령어를 실행할수잇는 프로세스가 있다고한다면 이 프로세스의 상태는 Blocked(wait,sleep)상태이다. 또한, 우리는 어떤 프로그램의 메모리 전체(주소공간 전체)를 물리적인 메모리 (램)에 올려놓고 실행하지 않는다. 메모리 공간을 여럿이 동시에 써야하기때문에 절약해야한다. 그래서 만약에, 프로그램의 어떤 부분을 실행을해야하는데 이 부분이 아직 메모리에 올라와있지 않고 디스크에 있다면 이 프로세스한테도 당장 시피유를 줘봤자 실행할수 없으므로 이런 프로세스의 상태를 블락드 상태라고한다.
- 즉 프로세스는 크게 이 3가지 상태, 시피유를 잡고있거나 기다리거나 오래걸리는 작업을 하고있거나. 경우에따라서는 new라고 프로세스가 생성중인 상태와 terminated로 프로세스가 종료중인 상태인데, 프로세스가 종료되면 원래 프로세스가 아니라서 상태가 없는데 프로세스는 종료되기전에 약간의 정리하는 작업이 있다. 이 terminated는 프로세스의 수행이 끝났지만, 약간 정리할게 남아있는 상태를 말한다.
- 즉, 프로세스의 상태도는 처음에는 new(프로세스가 생성중인상태이고) 다 생성되면 ready(즉, cpu만 얻으면 바로 실행가능한 상태 이때는 최소한의 메모리는 가지고있다) 이제 ready가 cpu를 얻게되면 running상태가 되고 여기서 이 프로세스가 cpu를 내놓는 경우가 2가지가 있는데, 하나는 자진해서 cpu를 내놓는 경우인데 이것은 i/o같은 오래걸리는 작업인 경우 이 프로세스는 cpu를 자진으로 내려놓고 blocked상태로 된다. 또다른 경우는 이 프로세스가 cpu를 계속 쓰고싶지만 timer가 할당한 시간이 다 끝나서 timer 인터럽트가 들어온 경우를 말한다. 이경우 cpu를 내려놓고 ready상태로 들어간다.
- 이런식으로 프로세스는 계속일을 하다가 언젠가 본인의 명령어를 전부 다 하면 프로세스가 종료가 되는 것이다.
- 이런 상태는 사실 큐들로 구현되는데, cpu는 매우 빠르고 여럿이 공유하는 자원이기 때문에 하나의 프로세스만 cpu에서 명령어를 수행하다가 timer 인터럽트가 들어오면 cpu를 뻇기고 큐의 맨뒤에가서 줄을서고 그다음 프로세스가 다시 cpu를 얻고 그러다가 만약, 프로세스가 디스크에서 뭔가를 얻어와야한다면 이 프로세스는 running 상태에서 blocked로 바뀐뒤 ready queue에 들어가지않고 disk I/O queue에 줄을선다. 그러면 디스크는 이 요청이 들어온것들을 disk컨트롤러의 통제아래에 순서대로 처리를 하고 만약, 아까 들어온 프로세스 작업이 끝나면 이제 디스크 컨트롤러가 다시 시피유에 인터럽트를 걸고 시피유는 물론 지금 프로세스를 실행하고있었지만 인터럽트가 발생했기떄문에 하던 작업을 멈추고 이 cpu제어는 운영체제 커널이 갖는다. 그럼 이 운영체제 커널은 아까 io를 요청한 프로세스의 입출력작업이 끝나서 인터럽트로 운영체제로 온 것이므로 이 운영체제 커널은 이 프로세스의 입출력작업이 요구한것 예를들어 디스크를 읽는것이면 이 읽은 것을 이제 시피유에 넘겨주다(램에 넣다)거나 혹은 이 프로세스의 상태를 이제 입출력작업이 끝났으니까 다시 ready바꾸고 이제 다시 큐의 맨앞 프로세스한테 cpu를 준다. 
- 주의할점은 이게 꼭 하드웨어 서비스를 기다려야해서 블락대기줄에 서는경우도있지만, 자원중에는 소프트웨어 자원이 있는데 예를들면 공유데이터와 같은건데 이 공유데이터는 여러 프로세스가 동시에 접근하면, 즉 하나의 프로세스가 이 공유데이터에 접근하는 도중에 타이머 시간이 다되서 다른 프로세스가 cpu를 얻게되고 이때 이 프로세스도 공유데이터를 접근하게 되면 이 공유데이터의 일관성이 깨지게 된다. 그래서 어떤 프로세스가 이 공유데이터에 접근하고있으면 다른 프로세스의 접근을 막아줘야한다. 그렇기 때문에 이 공유데이터에 접근하는 대기줄도 있고, 이 대기줄에 있을때돞 프로세스는 블락드 상태가도니느것이다. 즉, 오래기다리는 작업 필요하면 v프로세스는 blocked 상태가 되고 이것이 디스크떄문인지 혹은 키보드 혹은 공유데이터떄문인지에 따라 각각에 해당하는 큐에 들어가고 이것이 완료되면 다시 레디 큐로 와서 시피유를 얻게되는 것이다.
- 사실은 여기서 각각의 대기줄은 사실 커널 주소공간의 데이터영역에 자료구조로 queue를 만들어놓고 운영체제가 각 프로세스의 상태를 바꿔가면서 cpu를 주고 안주고를 결정하는것이다.

### 3. PCB
- 그래서 운영체제 커널이 이런식으로 각 프로세스마다 지금 이 프로세스오 ㅏ관련된 정보, 즉 프로세스들을 관리하기위해서 운영체제가 자신의 데이터영역에 두고있는것이 PCB이다. 이 pcb는 프로세스 하나당 하나씩 있는것이다. 이 pCB는 4가지 정도로 구성되어있다. 먼저 첫번쨰는 운영체제가 관리상 사용하는 정보이다. 이거는 뭐냐면 현재 프로세스의 상태 즉 이 프로세스가 래디냐 블락드냐 러닝이냐 이런것들이고 그 다음은 프로세스 아이디인데 이것은 프로세스의 식별자이고, 그다음은 스케줄링 정보와 우선순위이다. 스케줄링 정보와 우선순위는 뭐냐면 뒤에 나올 시피유 스케줄링에 의해 프로세스들을 (사실 위에서 모든 프로세스들이 round robin방식으로 하는것처럼 묘사했지만 사실 뒤에서 배울거지만 사실 정확한 cpu 스케줄링은 큐 안에서 가장 우선순위가 높은 아이한테 cpu를 넘겨준다.) 그래서 이런 스케줄링 정보와 우선순위도 OS가 관리상사용하는 정보에 들어간다.
그다음 두번쨰는 이 프로세스의 문맥을 표시하기 위한 정보들인데, 이거는 cpu가 프로세스를 실행할떄 레지스터 안에 어떤값들을 넣고 실행하고있었는지에 관한 정보이다. 그래서 이 정보들을 프로세스를 줄때 시피유에게 함깨 줘야한다
그다음은 메모리 관련 정보인데 이것들은 프로세스의 code, data, stack이 메모리 어디에 이있었는가에 관한 정보, 그다음은 파일관련인데 이것들은 이 프로세스가 열고있었던 파일이나 그런것과 관련된 정보들이다.
이런 것들이 프로세스의 pbc를 구성하고있는것이고 운영체제가 이것을 관리한다.

### 4. 문맥교환
- 시피유는 굉장히 빠른 자원이기떄문에 어떤 프로세스가 cpu를 계속적으로 쓰는것이 아니고 짧은 시간간격으로 cpu를 얻어다가 뻇겼다가 이런 과정을 반복한다. 이떄 cpu를 뺏겻다가 다시 얻으면 뺏기던 시점의 문맥을 기억해놨다가 다시 cpu를 얻었을떄 뺏겻던 시점에서부터 이어서 시작할수있게 하는 이런 매커니즘이 필요하다. 문맥교환이라는 것은 시피유가 사용자 프로세스로부터 다른 사용자 프로세스로 넘어가는 과정을 문맥교환이라고 한다. 
- 그러면 문맥교환시에 어떤 작업들이 필요할까? 어떤 프로세스 a가 cpu에서 실행중이면 pc가 프로세스의 어딘가를 가리키고 있고 시피유 레지스터의 어떤 값들을 넣어서 실행하고잇고 메모리의 위치정보 맵이 있고 이런방식으로 cpu안에서 실행되고있었을 것이다. 그런데 만약 타이머 인터럽트라든가 어쨋든 이 프로세스가 cpu를 뺴앗기게 될경우 그러면 그냥 이 레지스터값과 메모리 값들을 지워버리면 되는것이아니고 cpu가 다시 이 프로세스를 작업하려 왔을떄 정확하게 이 시점부터 작업하게 즉, 이 문맥부터 실행을 재게하기 위해서 레지스터,메모리, pc에 저장된 값들을 운영체제 커널 가상공간의 데이터영역 안에있는 pcb에 저장을 해논다. 그래서 프로세스가 시피유를 빼앗기면 위에있는 정보를 운영체제가 저장해놓고 만약, 이번에 시피유를 얻은 프로세스 또한 어딘가 과거에 저장해둔 문맥이 이을것이다. 그래서 운영체제가 시피유를 넘겨줄떄 이 프로세스의 문맥을 pcb에서 찾아서 cpu의 하드웨어에 복원을 시켜놓는다. 이런식으로 cpu를뺏고 넘겨주고 하는것이다.
- 문맥교환에서 햇갈리기 쉬운 개념이 있는데, 우리가 시스템콜또는 인터럽트가 있고 이런 여러가지 상황이 생긴다. 시스템콜은 프로세스가 본인이 필요해서 운영체제한테 ㅇ청을 하는것이고 인터럽트는 컨트롤러같은 장치가 시피유한테 정보를 전달할 목적으로 인터럽트를 거는것이다. 시스템콜이 됫든 인터럽트가 됫든 이런게 발생하면 시피유 제어권이 사용자 프로세스로 부터 운영체제 커널한테 넘어가게되는데 이런식으로 사용자프로세스로부터 cpu가 운영체제에 넘어가는것 이걸 문맥교환이라고 하는것은아니다! 문맥교환은 사용자 프로세스로부터 다른 사용자프로세스로 넘어가는 것을 말한다.시스템 콜이나 인터럽트는 사용자 프로그램으로 부터 운영체제한테 시피유가 넘어가는 것이고 이걸 문맥교환이라 하지는안흔다 그렇지만, 이런 시스템콜이나 인터럽트가 발생한 이후에 운영체제가 시피유를 다른 프로세스한테 넘겨주는 경우가 있는데 이렇게 되면 문맥교환이 맞다. 하지만, 시스템콜이나 인터럽트가 발생했는데 운영체제가 이것들을 처리를하고 그다음 다시 발생하기 이전의 프로세스에게 cpu를 주면 이것은 문맥교환이 아니다!
- 인터럽트는 외부에서 발생하는 것이고 시스템콜은 프로세스가 본인이 필요해서 요청하는것이다.
- 예를들어 사용자 프로그램이 유저모드에서 작업을 하다가 외부에서 인터럽트가 오거나 혹은 본인이 시스템콜을 발생시켜 cpu가 운영체제로 갔다. 이떄 cpu의 모드빗은 커널모드가 되고 운영체제는 인터럽트가 들어오면 인터럽트 서비스 루틴을 실행하고 시스템콜이 들어오면 관련된 커널 함수를 실행한다. 이런 해결작업들이 끝난다음에 보통은 cpu를 이 원래 프로세스에 넘겨주게된다. 그러면 여기서는 문맥교환이 발생한게 아니고 그냥 유저모드에서 프로세스를실행하다가 커널모드로 왔다가 다시 유저모드로 간것이다. 반면에 두번째는 유저모드에서 프로세스가 실행되다가 인터럽트 중에서도 타임인터럽트가 들어왔다거나 아니면 입출력 작업을 위한 시스템콜을 발생했다면 커널모드로 가서 cpu가 운영체제로 가고 운영체제는 이제 커널 가상공간안에 데이터영역 안에 가서 각 pcb들을 확인한다음 당장 실행가능한 레디 상태의 프로세스에게 이 cpu를 주는데 이떄는 문맥교환이맞다
- 1번의 경우에도 비록 문맥교환은 일어나지 않았지만, 시피유가 사용자 프로세스의 가상공간안의 어느 코드 부분을 실행하다가 인터럽트가 발생하여 커널의 코드를 실행한것이다 그후 다시 원래작업하던 사용자 프로세스로 넘어가기때문에 cpu문맥 즉, 레지스터 pc 등의 데이터들을 세이브 해놓고 커널의 코드를 실행해야하기떄문에 약간의 문맥은 백업이 되어야한다. 그렇지만 프로세스 자체가 바뀌는 문맥교환에 비해서는 훨씬 오버헤드가 적다. 예를들어 캐시메모리 라는 게 있는데 만약 문맥교환이 일어나게되면 이 캐시메모리를 전부 지워야한다. ( 그전 프로세스가 사용하더 ㄴ캐시내용) 하지만, 문맥교환이 아니고 그냥 유저모드->커널->유저 인 경우는 캐시메모리를 초기화 할 필요가 없다는 것이다. 이런것을 cache memory flush라고 하는데 이것이 상당한 오버헤드를 발생시킨다는것이다.

### 5. 프로세스를 스케쥴하기위한 큐
- 프로세스를 스케쥴하기위한 큐는 여러가지가 종류가 있다. job q, ready q, device q등이이는데, 레디큐는 현재 메모리 내에있고, 준비가 다되어 시피유만 오면 실행될수잇는 프로세스들의 집합이고 디바이스큐는 입출력 장치들의 처리를 기다리는 프로세스들의 집합이다. 먼저 job q는 현재 시스템에 있는 모든 프로세스의 집합이다. 즉 job q에는 레디큐나 디바이스큐 안에 있는 프로세스가 잡큐에도 포함이 되어있는것이다. 하지만 , 레디큐에 있으면 디바이스쿠에 없고 디ㅏ바이스큐에이으면 레디큐에 없다
- 큐에 줄새우는것은 사실 프로세스를 줄세우는것이 아니고, 운영체제가 이 ㅡㅍ로세스의 문맥이 담긴 pcb들을 줄세우는것이다. pcb에는 포인터가 있어가지고 이 pcb들을 줄줄이 연결시킬 수 잇다.

### 6. 컴퓨터 내부의 스케줄러
- 스케줄러는 순서를 정해주는 것이다. 스케줄러는 각각의 자원별로 이번에 무슨일을하고 다음에 무슨일을하고 이 일 할 시간을 얼마큼씩 잡고 이런일을 결정해주는것이 스케줄러이다. 이 부분에서는 디스크 스케줄러는 안나온다. 디스크는 i/O장치로 치니까
- 먼저, 단기스케줄러(cpu scheduler, short-term sch~)를 먼저 보면, 이 단기스케줄러가 시피유스케줄러다. 굉장히 짧은 시간단위로 스케줄이 이어지기 때문에 시피유 스케줄러라고 말하낟. 보통 스케줄 시간 단위가 ms단위이다. 이 시피유 스케줄러는 다음번에 어던 프로세스한테 cpu를 줄지 결정하는 스케줄러이다.
- 이 단기 스케줄러와 반대되는 개념이 장기스케줄러(job scheduler)인데 이것은 메모리를 어떤 프로세스한테 줄지를 결정하는 것으로 잡 스케줄러 라고도 한다. 정확히 말하자면 처음 프로세스가 시작이 되어 new상태에서 ready상태로 넘어올떄, 즉 처음프러세스가 시작되고 나서 메모리를 얻지 못하면 아무일도 하지못하기 때문에 메모리에 올라가는걸 허락해줘야 이 프로세스가 ready상태가 된다. 이런 식으로 장기 스케줄러가 이것을 결정해주낟. 즉 new상태에있는 프로세스들중 어떤 프로세스에게 메모리를 줄지, 결정한다. 다시말하자면 시작 프로세스 중 어떤 것들을 ready queue로 보낼지를 결정한다. 즉 메모리를 주는것과 관련된 문제를 다룬다. 어떤 프로그램들이 실행되면 바로 메모리를 얻어가지고 실행이 될거라고 생각하늕데 사실 이게 맞다. 여기서 말한 장기스케줄러는 프로그램을 실해응ㄹ 시켜놔도 이 장기스케줄러가 자기 마음에 드는 프로세스한테만 메모리를 주주어 실행가능하게 만들어주는개념으로 설명한것이다. 즉 degree of multiprogramming을 제어한다. 이 멀티프로그래밍은 메모리에 여러 프로그램들이 동시에 올라가는것을 말한는데 degree of multi~이것은 메모리에 올라가있는 프로그램(프로세스)들의 수를 제어하는 것이 이 장기스케줄러의 역할이다. 즉, 실행 시작된느 프로그램들 중 10개가 만약 실행이 시작되고있다면, 10개한테 다 메모리를 주면 DOM이 10이되는것이고 이 10개중 하나한테만 주면 DOM이 1이 되는것이다. ( 즉메모리에 올라가있는 프로세스가 하나) 메모리에 올라가있는 프로세스의 수를 조정해야할 필요가 있다. 메모리에 프로그램이 너무 많은 프로그램이 동시에 올라가도 컴퓨터의 전체성능이 안좋아진다 또한 너무 적게 올라가도 성능이 안좋아진다 에를들어 메모리에 프로그램이 하나밖에 엇으면 이 프로그램이 cpu를 스다가 입출력하러가면 cpu는 이제 작업할 다른 프로세스가 없으니까 놀게된다. 그렇지만 메모리에 프로그램이 10개가 올라가있으면 하나의 프로그램이 입출력을 하러가도 또 다른 프로그램한테 시피유를 넘겨줄수가잇다. 그러면 이제 시피유가 놀지않고 일을할수이어 도 좋다. 반면에 너무 많은 프로그램을 메모리에 올려놓으면 그래도 성능이 안좋은데, 왜냐하면 cpu를 잡고 프로그램을 실행하려고 봣더니 당장 필요한 부분 마저도 메모리에 업세 된다 왜냐면 각 프로그램들이 ㅇ메모리를 너무 많이 가지고있기 때문이다. 그래서 또 io를 하러가야한다. 즉 DOM을 제어하는 것은 굉장히 중요한 문제이고 장기 스케줄러가 이 dom을 결정한다. 대부분 우리가 사용하는 시분할 시스템에서는 장기 스케줄러가 없다. 즉, 지금 우리가 스는 시분할시스템에서는 프로그램이 실행이 되면 일단 전부 메모리에 들어가서 readyㅛ상태가 된다. 그렇다면 지금 우리가 쓰는 시스템이 dom을 어떻게 조절할까
- 끄걸 바로 중기스케줄러 midium-term-scheduler 또는 swapper가 이 dom을 조절한다. 장기스케줄러는 프로그램이 시작될떄 메모리를 줄지말지를 결정ㅎ는데 지금 시스템은 프로그램이 시작되면 무조건 메모리를 준다. 하지만. 이런식으로 하다보니까 메모리에 너무 많은 프로그램이 올라가 있ㅇ면 문제가 되기때문에 이걸 조정해주기위해 중기스케줄러가있다. 중기스케줄러는 메모이리에 너무 많은 프로그램이 올라가있으면 일부 프로그램을 골라가지고 메모리에서 통째로 쫒아낸다. 이런 방식을 통해서 dom을 조정한다. 즉 원래 장기 스케줄러의 개념이 나왔을때는 처음부터 메모리에 올라가는 프로그램을 조정햇는데 지금은 중기스케줄러로 일단 메모리에 올리고 너무 많다싶으면 몇개를 쫒아내늗ㄴ것이다
- 그래서 이 중기스케줄러가 있기때문에 현대의 운영체제에서는 앞에서 말한 프로세스의 상태 세가지에 중기스케줄러때문에 추가된 상태가 하나있느데 그것이 바로 Suspended 상태이다. 앞ㅇ서말한 cpu를 잡고잇는상태, 대기중인상태, 블락디드 상태인데 이 세가지로는 중기스케줄러에의해 메모리를 빼앗긴 상태를 나타낼수없다. 메모리를 통째로 빼앗기면 cpu를 얻어도 아무일도 못하는데 이것은 러닝도 아니고 레디도 아니고 블락디드도 아니다 . 서스펜디드 또는 스탑드 상태는 외부에서 프로세스를 정지시켜놓은상태이다. 그래서 이 상태는 메모리에서 이 프로세스가 모두 쫒겨나서 디스크로 swap out이 된 상태를 말한다.
- 이 blocked 와 suspended를 구분하는 것은 blocked는 자신이 요청한 일을하면서 오래 기다리는 상태이고 , 서스펜디드는 외부에서 정지시켜놓은 상태이다. 그래서 블락디드는 자신이 요청한 ㅇ비출력 작업 같은게 끝나면 다시 레디상태로 돌아갈수 잇는것이고 서스펜디드는 외부에서 정지를 해놨기 떄문에 (메모리도 모두뺴앗고) 외부에서 다시 재게를 시켜줘야지만 다시 active상태로 넘어갈수잇다. 서스펜디드의 예는 중기스케줄러에 의해 메모리에 쫒겨난 경우와 사용자가 일부로 프로그램을 일시정지시킨 것도 있다. 예를 들어 리눅스에서의 ctrl+Z, 이떄도 이 프로세스는 메모리를 통재로 잃어버린다. 사람이 정지시키면 사람이 다시 재개시켜야 다시 이 프로세스 액티브 한 상태로 된다.
- 러닝상태는 프로세스가 cpu를 가지고있으면서 본인의 코드를 실행중인 유저모드의 러닝과 본인이 어떤일을 할수업어서 운ㅇ여체제에 요청하는 즉 시스템콜을 해서 운영체제의 코드가 실행중인 상태가 있는데, 이 상태를 우리는 이 프로세스가 cpu를 잃고 운영체제가 cpu를 얻어서  운영체제 커널이 runnig하고 있다 이렇게 표현하지않는다.즉, 운영체제 본인의 상태는 없고, 왜냐면 상태는 운영체제가 프로세스를 관리하기위해 만든것이기때문이다. 위와 같은 상황은 프로세스가 커널모드에서 러닝 상태이다 라고 한다. 또한 사용잪 프로그램이 실행되다가 인터럽ㅌ가 발생하면 cpu가 운영체제 커널로 가서 인터럾트 서비스 루틴이 실행되는데 이 경우에 이 인터럽트는 이 프로세스 때문에 실행되는것이 아니고 물론 외부에의해서 인터럽트가 들어와쎄곘지만 일반적으로 이러한 상황도 이 프로세스가 커널(모니터)모드에서 러닝하고있다고 부른다.  
- 서스펜디드도 블락드 상태에서 서스펜디드가 되었ㅇ느냐 혹은 레디상태에서 되었느냐에 따라서 서스펜디드 블락드 , 서스펜디드 레디라고한다. 이 둘다 서스펜디드 상태이므로 서스펜디드상태는 외부에서 중지시켯으므로 프로세스가 얼어붙어서 inactive(정지)상태라고한다. 즉 서스펜디드는 외부에 의해 프로세스가 아예 메모리에 쫒겨나 정지된상태를 말한다. 서스펜디드 상태가 외부에 의해 다시 재게가 되면 active상태가 된다(서스펜디드는 다시 외부에서 재게를 시켜줘야함)


### 7. 프로세스
- 일단 동기식입출력과 비동기식입출력의 차이 : 동기식 입출력은 어떤 프로세스가 입출력 요청을 하면, 근데 입출력요청은 입출력은 운영체제에서 할수잇기때문에, 사용자 프로세스는 운영체제에 입출력 요청을 하고, 입출력은 좀 오래걸리기때문에, 수행이 