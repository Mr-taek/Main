### tf의 keras는 본래 native keras로서 존재했다. 그러나 이제부터는 tf의 keras로 사용되고 있다.

### tensorflow의 keras api는 모두 과거 keras에서부터 온 것이다. model, Sequential()등은 keras로부터 온 것이다.

# keras - model
" model은 각 층(layer)(입력층, 은닉층, 출력층)을 포함하고 있는 인공 신경망 자체를 나타낸다. " -> model=Sequential() ""모델 생성""
" model의 기본 단위는 층이며, 이러한 층을 레고처럼 순차적으로 쌓기만 하면 일반 신경망(ANN) CNN RNN 또는 이들을 ㄹ조합한 다양한 모델을 구축할 수 있다. "
-> model.add() ""층 추가""
-> model.add() ""층 추가""
-> model.add() ""층 추가""

" 모델이 만들어지면 손실 함수 같이 최소가 될 때까지 input값을 바꿔가며 weight 와 bias값을 찾는 학습이 진행된다."
-> model.compile(...) ""손실함수 지정 + 옵티마이저 지정""
-> model.fit(...) ""학습을 진행""