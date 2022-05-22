# re표현식.
1. 문자열 바꾸기 sub
    - re표현식.sub(Replace_str,str,count=number) : str에 re객체에서 정해진 정규표현식 규칙에 해당하는 값을 Replace_str로 대체하는데, 총 횟수는 count 숫자만큼 대체한다.
        ```
        c="Laventa is always saying hola senorita but Laventa is chinese"
        r=re.compile("Laventa")
        p=r.sub("nihoa",c,count=1)
        print(p)
        ->
        nihoa is always saying hola senorita but Laventa is chinese
        ```
    + subn : sub와 같은 기능/parameter이지만 반환을 튜플로 돌려준다 (변경된문자열,바꾸기가 발생한 횟수) 의 형태이다.

2. .findall() : 표현식과 같은 모든 값을 리턴.
3. .match()
4. .search()
# re객체 오직 match,search 에만 있음
1. .group() : 표현식에 맞는 값들의 이름을 출력.