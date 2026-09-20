# Conflict Resolution Log

> **과제 요구사항**: 의도적으로 충돌 상황을 만들고 해결한 기록을 남긴다.  
> - 팀 전체 기준: 최소 2회 이상 충돌 해결 기록 (비자명 충돌 최소 1회 포함)  
> - 충돌 1: 같은 파일의 같은 hunk (인접 라인) 수정 충돌 (`data/food_data.json`)  
> - 충돌 2: 비자명 충돌 (파일 Rename vs 내용 Modify 충돌: `src/lottery.py` ➔ `src/tie_breaker.py`)

---

## 충돌 기록 #1: 동일 파일 인접 라인 충돌 (Adjacent Line Conflict)

### 참여자
- 작성자: 안재현
- 상대: 강동하

### 상황 (What happened)
- **대상 파일**: `data/food_data.json` (한국 음식 128선 데이터셋)
- **발생 브랜치**: `feature/ahn-tournament-engine` 와 `feature/kang-food-loader` 머지 과정
- **상황 설명**: 안재현은 `data/food_data.json` 10번 라인에 "순두부찌개" 데이터를 추가하였고, 강동하는 동일 라인에 "부대찌개" 데이터를 추가하여 머지 시 동일 hunk 인접 라인 충돌 발생.

### 충돌 내용 (Conflict markers)
```txt
<<<<<<< HEAD
    {"id": 3, "name": "순두부찌개", "category": "찌개/탕류", "desc": "부드러운 순두부와 얼큰한 해물 국물"},
=======
    {"id": 4, "name": "부대찌개", "category": "찌개/탕류", "desc": "햄과 소시지, 라면 사리가 가득한 푸짐함"},
>>>>>>> feature/kang-food-loader
```

### 해결 과정 (How)
- **선택한 해결 전략**: `Keep both` (양쪽 데이터 모두 유지)
  - 두 음식 모두 메뉴 월드컵에 유용한 항목이므로 두 음식을 모두 살려(Keep both) 배열에 순차 등록함.
- **수행 절차**:
  1. `data/food_data.json` 파일을 에디터로 열어 충돌 마커 확인
  2. 충돌 마커(`<<<<<<< HEAD`, `=======`, `>>>>>>>`)를 제거하고 두 음식을 순서대로 나열하여 id 번호 정리
  3. `git add data/food_data.json`
  4. `git commit -m "fix: Resolve merge conflict in food_data.json by keeping both dishes"`
  5. `git push origin feature/ahn-tournament-engine`

### 결과 (Outcome)
- 양쪽 브랜치의 음식 데이터가 유실 없이 병합되어 128선 DB가 정상 동작함.
- 관련 PR: [PR #7: feat: Add Sundubu-jjigae to food data](https://github.com/jha21vvv/codyssey-b2-02/pull/7)
- 충돌 해결 커밋: fafaa6d (fix: Resolve merge conflict in food_data.json by keeping both dishes)
- main 머지 커밋: a72615f (Merge pull request #7 from jha21vvv/feature/ahn-dish)

### 배운 점 (Learnings)
- Git은 라인 단위로 변경사항을 비교하므로 인접한 라인을 동시에 수정할 때 충돌 마커를 생성함을 확인함.
- 충돌 마커의 HEAD와 상대 브랜치 영역을 정확히 읽어 양쪽의 의도를 조화롭게 합치는 법을 배움.

---

## 충돌 기록 #2: 비자명 충돌 (Rename vs Modify Conflict)

### 참여자
- 작성자: 안재현
- 상대: 김진우

### 상황 (What happened)
- **대상 파일**: `src/lottery.py` ➔ `src/tie_breaker.py`
- **발생 브랜치**: `feature/ahn-game-integration` 와 `feature/kim-voting-system` 머지 과정
- **상황 설명**:
  - 안재현은 `src/lottery.py` 파일 내부의 동점 추첨 알고리즘을 개선하여 커밋함.
  - 김진우는 모듈의 명확성을 위해 `src/lottery.py`를 `src/tie_breaker.py`로 `git mv`(Rename)하여 커밋함.
  - 두 브랜치를 머지할 때 한쪽은 파일 이름이 변경되고 다른 쪽은 이전 이름의 파일 내용이 수정되어 Git 추적 충돌 발생!

### 충돌 내용 (Conflict markers / Git Warning)
```txt
CONFLICT (rename/modify): src/lottery.py renamed to src/tie_breaker.py in HEAD.
Version feature/ahn-game-integration of src/lottery.py left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```

### 해결 과정 (How)
- **선택한 해결 전략**: `3-Way Merge & Content Relocation` (리네임 수용 및 수정 내용 이식)
  - 김진우가 제안한 모듈 이름 변경(`tie_breaker.py`)을 최종 표준으로 채택하되, 안재현이 개선한 추첨 알고리즘 내용을 새 파일 `tie_breaker.py` 내부로 안전하게 통합.
- **수행 절차**:
  1. `git status`로 충돌 상태 확인
  2. 안재현의 최신 수정 로직을 `src/tie_breaker.py`에 이식
  3. 잔여 이전 파일 `src/lottery.py`를 `git rm`으로 정리
  4. `git add src/tie_breaker.py`
  5. `git commit -m "refactor: Resolve rename/modify conflict by migrating lottery to tie_breaker.py"`
  6. `git push origin feature/kim-voting-system`

### 결과 (Outcome)
- 비자명 충돌 상황에서 코드 유실 없이 파일명 변경과 로직 개선이 모두 반영된 단일 통합 모듈 완성.
- 관련 브랜치: eature/kim-rename-tiebreaker (Rename) & eature/ahn-modify-lottery (Modify)
- 충돌 해결 머지 커밋: 6a9cfd6 (fix: Resolve rename/modify conflict by migrating lottery to tie_breaker.py)

### 배운 점 (Learnings)
- 파일 이름 변경은 대규모 충돌을 유발할 수 있으므로 사전에 팀원들에게 리네이밍 계획을 공유하고, 변경 커밋과 리네임 커밋을 분리해야 함을 배움.
