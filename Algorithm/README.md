- [동적계획법과 분할정복](#동적계획법과-분할정복)
  - [1. 동적계획법](#1-동적계획법)
  - [2. 분할정복](#2-분할정복)
  - [3. 공통점과 차이점](#3-공통점과-차이점)

## 동적계획법과 분할정복

### 1. 동적계획법
- Dynamic Programming
- 작은 문제를 먼저 해결한 후, 이 문제의 해를 활용해서 보다 큰 문제를 해결
- 상향식 접근법
- Memoization: 다시 계산하지 않기 위해 이전의 값을 저장해둠
- 예) 피보나치 수열

### 2. 분할정복
- Divide and Conquer
- 문제를 중복되지 않는 최소단위로 나누어 해결한 후, 다시 병합하여 답을 얻는 알고리즘
- 하향식 접근법
- 예) 병합정렬, 퀵정렬

### 3. 공통점과 차이점
- 공통점
  - 문제를 쪼개서 해결
- 차이점
  - 동적계획법
    - 부분문제는 중복되어 상위 문제 해결 시 재활용
    - Memoization 사용
  - 분할정복
    - 부분문제는 서로 중복 불가
    - 중복되지 않기 때문에 굳이 Memoization 사용 안함

