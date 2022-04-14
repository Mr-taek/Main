tensorflow func: convert_to_tensor

Link: [Magic method for Python][magic link]

[magic link]: https://ziwon.github.io/post/python_magic_methods/

what is Magic method?: 객체지향 <u>파이썬의 모든 것<u>. 항상 두개의 밑줄(__)로 둘러싸여있습니다.

1. new   init    del
+ new: 객체의 인스턴스화에서 호출되는 첫 번째 메소드. 클래스를 취한 다음 init에 전달할 다른 인자를 취한다. 거의 사용되지 않으며 유용하지도 않다.
+ init: 클래스의 initializer. 기본 생성자가 호출된 것과 관계없이 전달됩니다. init은 파이썬 클래스 정의서 보편적으로 사용됨.
+ del: 소멸자, del은 불리한 환경(?) 때문에 거의 절대 사용되어서는 안되니 주의하면서 사용.