# 문자열 내 p와 y의 개수

Level: 1
URL: https://programmers.co.kr/learn/courses/30/lessons/12916
개발일: 27/08/2021
문제 유형: 기초
사용 언어: Python
체감: ★☆☆☆☆

### 문제 설명

---

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

---

### 제한 조건

- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

---

### 예시

- 입출력 예

    [제목 없음](%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%8B%E1%85%A7%E1%86%AF%20%E1%84%82%E1%85%A2%20p%E1%84%8B%E1%85%AA%20y%E1%84%8B%E1%85%B4%20%E1%84%80%E1%85%A2%E1%84%89%E1%85%AE%205c3d5841f7064accace3abf7fb7b8303/%E1%84%8C%E1%85%A6%E1%84%86%E1%85%A9%E1%86%A8%20%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%82%E1%85%B3%E1%86%AB%20%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%87%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%89%E1%85%B3%20774bf7ce47d2426582b2cb9134f105cb.csv)

- 입출력 예 설명

    입출력 예 #1'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

    입출력 예 #2'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

    ※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.

---

### 해결 방법

---

- `count()` 함수가 결정적

---

### 코드

---

```python
def isSame(s):
    s = s.lower()
    p_c = s.count('p')
    y_c = s.count('y')
    return True if p_c == y_c else False

def solution(s):
    return isSame(s)
```

---