"""
가상 생성자! 팩토리 메서드
부모 클래스에서 객체들을 생성할 수 있는 인터페이스를 제공하지만, 
자식 클래스들이 생성될 객체들의 유형을 변경할 수 있도록 하는 생성 패턴

P : 왜 쓰냐?
문제 내가 물류 관리 앱을 개발하고 있는데, 앱의 첫 번째 버전은 트럭 운송만 처리할 수 있어서 대부분의 코드가 Truck 클래스에있어
얼마 이후 당신의 앱이 유명해졌으며, 매일 해상 물류 회사들로부터 해상 물류 기능을 추가해달라고해 원래는 지상만 있었는데!!
클래스간 많은 결합으로 인하면 새로운 클래스를 추가하는것은 어렵겠지?

Truck 클래스에 결합된 코드들을 ship 클래스에 추가시키려면 전체 코드 베이스를 변경해야한다는데...
만약에 또 ship이아니라면? 이러면 어떻게 해야해 변경할 게 반복되잖아.

S : 어떻게 해결해?
팩토리 메서드 패턴은 (new 연산자를 사용한) 객체 생성 직접 호출들을 특별한 "팩토리" 메서드에 대한 호출들로 대체하는건 어때?
그냥 new연산자를 바로 안하고 createTransport()같은것을 이용하네? 이걸로 뭐가 될까?
생성자 호출을 프로그램의 한 부분에서 다른 부분으로 옮겼을 뿐인데...
하지만 이렇게 한다면 자식 클래스에서 팩토리 메서드를 "!!오버라이딩!!" 할 수 있기 떄문에 그 메서드에 의해 생성되는 제품들의
클래스들을 변경할 수 있게 되는것이지 물론 interface 즉 상위 클래스에 있는 Trasper는 Truck과 ship의 +deliver()를 상속해주는 것에 동시에 truck과 ship 클래스는 인터페이스를 그대로 따라해야해

클라이언트 코드라고도 부르는 이 팩토리 메서드는 실제로 자식 클래스들에서 반환되는 여러 제품 간의 차이에 대해 알지 못해
그래서 인지 클라이언트 코드는 모든 제품을 추상 Trasport(운송쳬계)로 간주하고 클라이언트들은 모든 Transport 객체들이
deliver(배달)이라는 메서드를 가져야 한다는 사실만 알고 있을 뿐, 어떤 작동을 하는지는 클라이언트하게 중요하지 않지!

결국 그래서 공통되는 생성자를 만드는 클래스를 선언하고 그 공통된 객체를 선언하는 클래스들은 추상적이어야하네?
객체들이 죄다 구체화시켜야한다는 건가보네... 아무튼 추상화 된 녀석이 extends를 통해 override이구먼.

독립성이 크니 좋다!, 즉 내 코드와 함께 작동해야하는 uvm의 정확한 객체들의 의존관계를 모르는 경우가 있으니 독립하게 써서
확장을 시킨다. 내가 creator 자식 클래스를 생성한 후 해당 클래스 내부의 팩토리 메서드를 오버라이딩만 하면 된다!.
"""

"""
우선 모든 제품(create된놈) 인터페이스를 모두 따라야 함.

장점 1. 단일 책임 원칙, 즉 제품 생성 코드를 프로그램의 한위치로 이동하여 코드를 더 쉽게 유지보수가능
장점 2. 개방/폐쇄 원칙, 기존의 클라이언트 코드를 훼손하지 않고 새로운 유형 제품을 프로그램에 도입가능.
단점 1. 코드 복잡해짐, 그러나 크레이터 클래스들의 기존 계층구조에 패턴을 도입시키면 됨

