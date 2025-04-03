# ssafy 서울 7반 알고리즘 스터디 2팀
### 바로가기
- [📢 RULES](#📢-rules)
- [ℹ️ 코드 업로드 방식](#ℹ️-코드-업로드-방식)
- [📁 폴더 구조 ](#📁-폴더-구조)
- [ℹ️ Commit Convention](#ℹ️-commit-convention)
- [ℹ️ PR 방법](#ℹ️-pr-방법)
- [ℹ️ 이슈 작성 방법](#ℹ️-이슈-작성-방법)


## 📢 RULES
- 평일 하루 1문제, 주말 하루 3문제 이상 풀기. 
- 풀지 못한 문제라도 코드리뷰를 위해 올려주세요. ( 내 힘으로 풀고싶다면 사전에 양해 구해주세요. )
- 본인 조 OR 다른 조라도 PR 확인 후 코드리뷰 작성하기.
- 중간에 막히는 부분이 있어 질문하고 싶으면 이슈 적극 활용하기

## ℹ️ 코드 업로드 방식
1. 메인 레포지토리를 FORK 한다.
2. 폴더 구조와 커밋 컨벤션에 맞춰 업로드 한다.
3. 메인 레포지토리로 PULL REQUEST를 올린다. ( 하단의 PR 방법 참고 )
4. 코드리뷰 2개 이상 달릴시 메인 레포지토리에 머지 됨.

## 📁 폴더 구조 
아래 양식에 따라 디렉토리 생성 생성해주세요!
- `본인이름 / 문제 사이트 / 문제 번호`
- `BOJ`: 백준
- `SWEA`: SWEA
- `PGM`: 프로그래머스
- `※ input 파일은 들어가지 않습니다. ※`

### 예시
```
📦seunghoon
 ┣ 📂BOJ
 ┃ ┣ 📂1125
 ┃ ┃ ┗ 📜sol.py
 ┃ ┗ 📂1592
 ┃ ┃ ┗ 📜sol.py
 ┗ 📂SWEA
```

## ℹ️ Commit Conventionℹ
### title
- `[Commit Type] : message `
- `Commit Type`
    - 문제 해결 완료: `[Solve]`
    - 문제 미해결: `[Fail]`
    - 코드 수정: `[Fix]`
    - 코드 최적화: `[Refactor]`
    - 문서 작업: `[Docs]`

- `예시`
    - [Solve] :문제이름 문제 해결
    - [Fail] : 문제이름 문제 시간초과로 실패
    - [Fix] :문제이름 문제 오타 수정
    - [Refactor] : 문제이름 문제 코드 함수화
    - [Docs] : README.md 추가 내용 추가

### body
- 구조
```
'''
[문제 사이트트] - 문제 이름

문제풀이 세부 내용
'''
```
- `문제 사이트`
    - [BOJ]
    - [SWEA]
    - ...
### 최종 메세지 예시  
- 문제 해결시
```
[Solve] : 문제이름 문제 해결

[BOJ] 1234:
    - 문제 유형 : BFS
    - 문제 난이도 : 백준 골드 3
    - 시간복잡도 : 23ms
    - 공간복잡도 : 1000mb
```

- 문제 해결 실패시
```
[Fail] : 문제이름 문제 런타임 에러로 해결 실패

[BOJ] 1234:
    - 문제 유형 : BFS
    - 문제 난이도 : 백준 골드 3
    - 재귀 깊이 런타임 에러로로 인해 실패
```

- 풀이 수정시
```
[Fix] : 문제이름 문제 오타 수정

[BOJ] 1234:
    - printt(a) => print(a) 오타 수정정

```

- 코드 리팩토링시
```
[Refactor] : 문제이름 문제 

[BOJ] 1234:
    - 함수 단일 책임 원칙에 따른 더하기, 찾기 로직 분리

---
```


## ℹ️ PR 방법
### 1. 메인 레포지토리에서 FORK 버튼 클릭
![alt text](/README_ASSETS/image.png)

### 2. 레포지토리 경로 설정 후 Create Fork 클릭
![alt text](/README_ASSETS/image-1.png)

### 3. 문제 커밋 진행 후, 상단의 Pull Requests 클릭 후 new pull request 버튼 클릭
![alt text](/README_ASSETS/image-2.png)

### 4. 경로 확인(중요) 후 create pull request 버튼 클릭
![alt text](/README_ASSETS/image-3.png)

### 5. 내용 작성후 create pull request 버튼 클릭
- 제목 : [문제 사이트] - 문제 번호 + 메세지
- 내용 : 문제 링크, 풀이 코드, 풀이 방법 설명
- 예시
> ```
> # [BOJ] 1054
> [문제 이름](문제 url)
>
> ## 문제 코드
> '''python
> print('test')
> '''
> 
> ## 풀이 방식
> - 프린트함
> ```
![alt text](/README_ASSETS/image-4.png)

## ℹ️ 이슈 작성 방법
### 1. 이슈 버튼 클릭
![alt text](/README_ASSETS/issue.png)

### 2. 이슈 작성
- 제목 : [문제 사이트] - 문제 번호 + 메세지
- 내용 : 자유 형식이되 코드를 같이 붙여 넣어주세요!
![alt text](/README_ASSETS/issue2.png)

### 3. assigness 설정
- 도와줄 스터디원들 + 자기 자신 assigness 설정해주세요.
- ![alt text](/README_ASSETS/issue3.png)

### 4. label 설정
- 자기가 작성한 리뷰에 맞는 라벨링을 진행해 주세요!
![alt text](/README_ASSETS/issue4.png)

### 이후 create 하면 완료!
