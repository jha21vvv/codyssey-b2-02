# Troubleshooting Log

> **과제 요구사항**: Git 트러블슈팅 실습 4종 시나리오를 팀 전체가 모두 수행하고 문서로 남긴다.  
> - 팀원별 최소 기준: 각 팀원은 최소 1개 시나리오의 해결 기록 작성에 참여해야 한다 (이름/역할 명시).

---

## 시나리오 1: `git commit --amend` (최근 커밋 메시지 수정)

### 참여자
- 작성 및 실습: **강동하**

### 상황
- 로컬에서 기능 개발 후 커밋을 작성했으나, 커밋 메시지에 오타(`Ad` -> `Add`)가 발생하고 변경 파일 1개가 누락되었음을 원격 push 직전에 발견함.
- 불필요하게 `fix typo` 같은 무의미한 커밋을 히스토리에 남기지 않고 직전 커밋을 깔끔하게 바로잡아야 하는 상황.

### 시도한 명령/절차
```bash
# 1. 오타가 있는 커밋 생성
git commit -m "feat: Ad string utility functions"

# 2. 누락된 파일 스테이징 및 커밋 메시지 수정
git add src/utils/string_utils.py
git commit --amend -m "feat: Add string utility functions with unit tests"

# 3. 변경 결과 확인
git log -1 --stat
```

### 결과
- 직전 커밋 해시가 갱신되면서 메시지 오타가 수정되고 누락되었던 파일이 단일 커밋으로 깔끔하게 통합됨.
- 주의할 점: 이미 원격 저장소(`origin`)에 push된 커밋에 대해 `amend`를 수행하면 강제 푸시(`--force`)가 필요해 다른 팀원의 로컬 저장소와 충돌을 일으키므로, 반드시 **원격 푸시 전 로컬 커밋에만 사용**해야 함.

### 왜 이 방법을 선택했는가 (Why)
- 새로운 커밋을 추가하는 대신 직전 커밋 객체를 대체하여 Git 히스토리를 군더더기 없이 깨끗하게(Clean Git Graph) 유지할 수 있는 가장 표준적이고 안전한 방법이기 때문임.

---

## 시나리오 2: `git reset --soft HEAD~1` (로컬 커밋 취소 + 변경사항 유지)

### 참여자
- 작성 및 실습: **안재현**

### 상황
- 기능 개발 후 커밋을 완료했으나, 아직 테스트가 덜 끝난 미완성 코드와 임시 디버그 로그 파일이 커밋에 포함되어 버렸음을 인지함.
- 작업했던 파일 내용은 1바이트도 날리지 않고 그대로 유지한 채, 커밋 단위만 취소하여 다시 검토하고 싶은 상황.

### 시도한 명령/절차
```bash
# 1. 취소할 커밋 상태 확인
git log -1 --oneline

# 2. soft reset 실행 (작업물 스테이징 유지)
git reset --soft HEAD~1

# 3. 스테이징 상태 및 파일 보존 확인
git status
# Changes to be committed: (파일들이 녹색으로 스테이징 유지됨)
```

### 결과
- 직전 커밋은 히스토리에서 말끔히 제거되었으나, 작성했던 코드 변경사항은 Staged(인덱스) 상태 그대로 안전하게 보존됨. 디버그 코드를 제거한 뒤 완벽한 상태로 재커밋 완료.
- 주의할 점: `git reset --hard`를 사용하면 작업 트리의 모든 수정사항이 완전히 삭제되어 복구하기 어려우므로, 작업 내용을 보존할 때는 반드시 `--soft` 또는 `--mixed`를 사용해야 함.

### 왜 이 방법을 선택했는가 (Why)
- `reset --hard`의 작업 유실 위험을 원천 차단하고, 커밋만 '언커밋(Uncommit)'하여 파일 변경사항을 손쉽게 재조정할 수 있는 가장 안전한 복구 수단이기 때문임.

---

## 시나리오 3: `git revert` (원격에 push된 커밋 취소)

### 참여자
- 작성 및 실습: **안재현, 김진우**

### 상황
- `main` 브랜치에 머지되어 이미 원격 저장소(`origin/main`)에 push 완료된 특정 기능 커밋에서 뒤늦게 심각한 런타임 오류가 발견됨.
- 이미 다른 팀원들이 이 커밋을 pull 받아 작업 중이므로, 공유 브랜치의 히스토리를 되돌리는 `reset`을 사용할 수 없는 상황.

### 시도한 명령/절차
```bash
# 1. 되돌리고자 하는 원격 커밋 해시 확인
git log --oneline -n 3
# a1b2c3d (origin/main) feat: Introduce experimental date parser

# 2. 안전한 역커밋(revert) 생성
git revert a1b2c3d --no-edit

# 3. 새로운 취소 커밋 확인 및 원격 푸시
git log -1 --oneline
# e4f5g6h Revert "feat: Introduce experimental date parser"
git push origin main
```

### 결과
- 문제의 커밋이 변경했던 내용이 정반대로 상쇄되는 새로운 "Revert 커밋"이 추가됨. 기존 히스토리를 파괴하지 않으면서 안전하게 프로덕션 버그를 원상 복구함.
- 주의할 점: 충돌이 발생할 경우 충돌을 수동 해결하고 `git revert --continue`를 수행해야 함.

### 왜 이 방법을 선택했는가 (Why)
- 공유 저장소(`main`)에서 `reset` 후 `push --force`를 하면 다른 모든 팀원의 히스토리가 꼬여 협업이 마비됨. `revert`는 과거의 기록을 투명하게 남기면서 안전하게 롤백할 수 있는 실무 표준 롤백 기법이기 때문임.

---

## 시나리오 4: `git stash` / `git stash pop` (작업 보관 후 전환)

### 참여자
- 작성 및 실습: **김진우**

### 상황
- `src/utils/date_utils.py` 기능을 개발하던 중, 긴급하게 `main` 브랜치에 올라온 다른 팀원의 PR 머지 결과를 확인하고 테스트해야 하는 요청이 들어옴.
- 아직 작성 중이던 코드가 미완성이라 커밋할 수 없으며, 그렇다고 변경사항을 버릴 수도 없는 상황.

### 시도한 명령/절차
```bash
# 1. 미완성 작업물을 임시 저장소(Stash Stack)에 저장
git stash save "WIP: date utils format enhancement"

# 2. 작업 트리가 깨끗해진 상태 확인 후 브랜치 전환
git status  # "working tree clean"
git checkout main
# (긴급 확인 및 테스트 수행)

# 3. 원래 작업 브랜치로 복귀
git checkout feature/kim-date-utils

# 4. 보관해 둔 작업물 복원 및 스택에서 제거
git stash pop
git status  # 보관했던 파일들이 온전히 복원됨 확인
```

### 결과
- 미완성 코드를 더미 커밋으로 남기지 않고도 작업 트리를 깨끗하게 비워 안전하게 브랜치를 오갈 수 있었으며, 복귀 후 `git stash pop`으로 작업을 끊김 없이 재개함.
- 주의할 점: 추적되지 않은 새 파일(Untracked file)은 `git stash -u` 옵션을 주어야 함께 보관됨.

### 왜 이 방법을 선택했는가 (Why)
- Git 히스토리에 의미 없는 "temp", "wip" 커밋을 남기는 것을 원천 방지하고, 컨텍스트 스위칭을 가장 빠르고 깔끔하게 수행할 수 있는 전문 도구이기 때문임.
