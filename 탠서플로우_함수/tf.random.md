tensorflow func: ramdom
__usage: tf.random.??~__

[link keyword][https://www.tensorflow.org/guide/random_numbers?hl=ko]

==========================
※seed는 일종에 tensorflow내부에 저장된 ...값일까? 도대체 정체가 뭐냐 넌.

* tf.random.Generator
    각 RNG(Random number generate?)호출 마다 다른 결과 생성하려면 사용. 또한 내부 값은 tf.Variable객체가 관리하기 때문에 tf를 사용하기에 매우 좋음.
    - Additional Method
        + **tf.random.Generator.from_seed(integerm, alg='(ex)philox페록스')**: seed로부터 생성기를 생성한다. seed>=0. 특정 알고리즘으로 난수 생성가능(페록스)
            - 할당된 변수 이름으로 호출하고 .normal(shape=[?])로 n 차원 tensor 난수를 생성한다.
        + **tf.random.Generator.reset()**: 

* tf.random.get_global_generator() *tensorflow Experimental func*
    ex)g2=~global_generator() -> print(g2.normal(shape=[2,3]))-> 항상 호출되면 [2,3] tensor만큼의 임의의 값을 새로 생성한다.(저장이 안된다.)
    - Non-Argument.

* tf.random.set_seed(integer)
    이 함수 뒤에 나오는 모든 random 값들을 일종에 저장시킨다. 즉 한번 정해진 random 값들이 저장된다고 보면 되며, 다시 프로그램을 돌렸을 때도 초기에 정해진
    random 값들이 그대로 사용된다.
    - Argument
        + integer: 사실상 아무 값이나 넣어도 된다. 물론 정수여야함. 다른 seed interger가 선언되면 서로 다른 random값들이 저장된다.

* tf.random.uniform(~) *주의: tf.random.uniform은 구버전이므로 사용을 권장하지 않습니다.*
    - Argument
        + shape: 정수 Tensor, 또는 파이썬 array.출력할 tensor의 shape을 결정.
        + minval: minvalue, default:0, 무작위 값의 최저의 값 범위.
        + maxval: 무작의 값의 최대의 값 범위.
        + dtype: 출력 값의 type. **float16** **float32** **float64** **int32** **int64**
        + seed: tf.random.set_seed 와 함께 사용됨. 여러 호출에 걸쳐 텐서 시퀀스를 재현할 수 있습니다. 호출: 초기선언과 재선언.
        + name: a name of operation(optional)
    
* tf.random.normal() 