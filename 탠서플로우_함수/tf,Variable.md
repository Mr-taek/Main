tensorflow func : Variable
    [link keyword][https://www.tensorflow.org/api_docs/python/tf/Variable?hl=ko]
===================================

1. The Variable() constructor requires an  **initial value for the variable** ,which can be a Tensor of any type and shape 선언시 꼭! 초기값 필요, TENSOR의 데이터타입, 차원수는 상관없다. ex)v= tf.Variable(Value)
2. Variable 함수는 특히 한번 선언되면 내부 값을 변경할 수가 있다. **v.assign(Value)**

3. Just like any Tensor, variables created with Variable() can be used as inputs to operations. Variable()로 선언된 변수는 일반 Tensor처럼 연산자의 입력으로 사용될 수 있다! ex)

# Variable(Argument)
1. initial_value: validate_shape인자가 False(default: True)가 아니라면 반드시 초기값은 *차원* 이 확실히 정해진 값이 들어와야 한다. 
2. trainable: default는 True, True상태시 경사하강법을 위한 func인 GradienTape()의 함수가 Variable()을 자동으로 watch상태로 만든다.
3. validate_shape: 만약 True면 초기값의 차원이 반드시 정해져야하며 False는 그 반대다.
4. etc .... 이후 추가

# Methods