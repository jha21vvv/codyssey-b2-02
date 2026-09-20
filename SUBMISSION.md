# Submission Index - codyssey-b2-02

> **과제 미션**: 코디세이 b2-02 (3인 Git 실전 협업 시뮬레이션)
> **프로젝트**: 한국 음식 128선 식사 추천 이상형 월드컵 (Python 게임 모듈)
> **작성일**: 2026년 9월 20일 (일)
> **작성자**: 김진우

---

## 1. Team Information

- **팀명**: Codyssey B2 Team 2
- **저장소 URL**: [https://github.com/jha21vvv/codyssey-b2-02](https://github.com/jha21vvv/codyssey-b2-02)
- **팀원 구성 및 역할**

| 팀원 | GitHub | 역할 |
|:---|:---|:---|
| 안재현 | [@jha21vvv](https://github.com/jha21vvv) | Lead. 토너먼트 엔진, 게임 통합 실행기, 충돌 해결 주도 |
| 강동하 | [@Deviskido](https://github.com/Deviskido) | 음식 128선 DB·로더, 협업 가이드 보강, amend 실습 |
| 김진우 | [@wlsdn66597](https://github.com/wlsdn66597) | 다인원 투표기·동점 추첨기, 제출 인덱스, stash 실습, QA |

> ⚠️ **번호 안내**: GitHub는 Issue와 PR이 번호를 공유합니다. 기획 문서에 적힌 "PR #1~#6"은 계획상 순번이며, 아래 링크가 **실제 발행 번호**입니다.

---

## 2. Member Contributions

### 안재현 (@jha21vvv)

**생성 및 머지한 PR**
- [PR #2: feat: Implement tournament bracket engine (Closes #1)](https://github.com/jha21vvv/codyssey-b2-02/pull/2)
- [PR #7: Feature/ahn dish](https://github.com/jha21vvv/codyssey-b2-02/pull/7)
- [PR #12: feat: Integrate game runner and add simulation tests (Closes #4)](https://github.com/jha21vvv/codyssey-b2-02/pull/12)

**작성한 코드 리뷰**
- [강동하 PR #6 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/6) — `src/food_loader.py` 예외 처리 및 `random.sample` 비복원 추출 검토
- [김진우 PR #4 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/4) — `src/voting.py` 턴 순서 강제 및 동점 연계 로직 검토

**리뷰 피드백 반영**
- PR #2에서 강동하의 엣지 케이스 지적을 반영하여 커밋 `b3ae7de` (`refactor: Add edge case test coverage based on review feedback`) 작성

**연결 Issue**
- [Issue #1: [FEAT] 토너먼트 대진 브래킷 상태머신 엔진 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/1)

> 📌 PR #12 본문의 `Closes #4`는 기획 문서상의 계획 번호를 그대로 적은 것으로, 실제 #4는 이슈가 아닌 김진우의 PR입니다. 게임 통합 작업에 대응하는 Issue는 발행되지 않았습니다.

---

### 강동하 (@Deviskido)

**생성 및 머지한 PR**
- [PR #6: feat: 한국 음식 128선 로더 및 무작위 토너먼트 샘플러 구현 (Closes #5)](https://github.com/jha21vvv/codyssey-b2-02/pull/6)
- [PR #9: docs: 협업 가이드 리뷰 체크리스트 및 실무 팁 보강 (Closes #8)](https://github.com/jha21vvv/codyssey-b2-02/pull/9)
- [PR #11: docs: 강동하 amend 실습 및 검증 기록 (Closes #10)](https://github.com/jha21vvv/codyssey-b2-02/pull/11)

**작성한 코드 리뷰**
- [안재현 PR #2 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/2) — 토너먼트 엔진 엣지 케이스 지적 (반영됨)
- [안재현 PR #7 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/7)

**리뷰 피드백 반영**
- PR #9에서 김진우의 리뷰 코멘트("문서만 수정하는 경우도 있으니 *변경한 코드* → *변경 사항*으로")를 반영하여 커밋 `444348e` (`docs: Cover documentation changes in review checklist (apply review feedback)`) 작성

**연결 Issue**
- [Issue #5: [FEAT] 한국 음식 128선 데이터셋 및 무작위 토너먼트 로더 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/5)
- [Issue #8: [DOCS] 협업 가이드 리뷰 체크리스트 및 실무 팁 보강](https://github.com/jha21vvv/codyssey-b2-02/issues/8)
- [Issue #10: [DOCS] 강동하 amend 실습 및 실제 수행 기록](https://github.com/jha21vvv/codyssey-b2-02/issues/10)

---

### 김진우 (@wlsdn66597)

**생성 및 머지한 PR**
- [PR #4: feat: Implement multi-player voting and tie-breaker lottery (Closes #3)](https://github.com/jha21vvv/codyssey-b2-02/pull/4) — `src/voting.py`, `src/lottery.py` 신규 구현 (+260줄)
- [PR #17: fix: Reject boolean choice_index in cast_vote (Closes #16)](https://github.com/jha21vvv/codyssey-b2-02/pull/17) — 불리언 우회 입력 검증 버그 수정
- 본 PR: 최종 제출 인덱스 및 트러블슈팅 시나리오 4 실측 로그 기록

**작성한 코드 리뷰**
- [강동하 PR #9 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/9) — *"코드 수정 없이 문서만 수정하는 경우도 있어서 리뷰 체크리스트의 `변경한 코드`를 `변경 사항`으로 수정하는 것이 어떨지 의견 남깁니다"* → **실제로 반영되어 커밋 `444348e` 생성**
- [안재현 PR #12 인라인 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/12) — *"현재 시드를 똑같이 설정하고 실행해도 매번 결과가 달라질 수 있을 것 같습니다"* (시드 재현성 리스크 지적)
- [강동하 PR #11 리뷰](https://github.com/jha21vvv/codyssey-b2-02/pull/11) — amend 실습 기록 검토 후 승인

**연결 Issue**
- [Issue #3: [FEAT] 다인원 순차 턴제 투표 및 동점 추첨 모듈 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/3)
- [Issue #16: [FIX] cast_vote가 불리언 선택 번호를 거부하지 못함](https://github.com/jha21vvv/codyssey-b2-02/issues/16)

---

## 3. 협업 문서

| 문서 | 내용 |
|:---|:---|
| [docs/CONTRIBUTING.md](https://github.com/jha21vvv/codyssey-b2-02/blob/main/docs/CONTRIBUTING.md) | 브랜치 전략(GitHub Flow), 네이밍 규칙, 커밋 컨벤션, PR 규칙, 리뷰 기준 |
| [docs/conflict-resolution.md](https://github.com/jha21vvv/codyssey-b2-02/blob/main/docs/conflict-resolution.md) | 충돌 해결 기록 (인접 라인 충돌 / 비자명 Rename vs Modify 충돌) |
| [docs/troubleshooting-log.md](https://github.com/jha21vvv/codyssey-b2-02/blob/main/docs/troubleshooting-log.md) | Git 트러블슈팅 4종 (`amend` / `reset --soft` / `revert` / `stash`) |
| [SUBMISSION.md](https://github.com/jha21vvv/codyssey-b2-02/blob/main/SUBMISSION.md) | 본 문서. 최종 제출물 인덱스 |

---

## 4. 요구사항 충족 현황

| # | 요구사항 | 충족 내역 |
|:---:|:---|:---|
| 1 | 브랜치 전략 수립 및 문서화 | GitHub Flow 채택. `docs/CONTRIBUTING.md`에 선택 이유 및 네이밍 규칙 명시 |
| 2 | `feature/*` 브랜치 기반 개발 | `feature/ahn-*`, `feature/kang-*`, `feature/kim-*` 전원 준수 |
| 3 | Issue ↔ PR 연동 | 이슈 기반 PR은 본문에 `Closes #N` 기재 (#2→#1, #4→#3, #6→#5, #9→#8, #11→#10, #17→#16). PR #7·#12·#15는 연결 이슈 미발행 |
| 4 | PR 본문 규격 (What/Why/How) | 전 PR 준수 |
| 5 | 1인당 PR 2개 이상 머지 | 안재현 3 / 강동하 3 / 김진우 2 |
| 6 | 1인당 코드 리뷰 2개 이상 (실질 코멘트) | 안재현 2 / 강동하 2 / 김진우 3 |
| 7 | 리뷰 피드백 반영 1회 이상 | 안재현 `b3ae7de` / 강동하 `444348e` |
| 8 | 충돌 해결 2회 이상 (비자명 1회 포함) | 충돌 #1 인접 라인 (`data/food_data.json`, 커밋 `fafaa6d`) / 충돌 #2 비자명 Rename vs Modify (`src/lottery.py` → `src/tie_breaker.py`) |
| 9 | 트러블슈팅 4종 실습 | `amend`(강동하) / `reset --soft`(안재현) / `revert`(안재현·김진우) / `stash`(김진우) |
| 10 | 최종 제출물 인덱스 | 본 문서 |

---

## 5. Git 히스토리 증빙

`git log --oneline --graph` 출력 (main 기준):

```text
*   9461a9b Merge pull request #11 from jha21vvv/feature/kang-amend-practice
|\  
| * 0af6b0d docs: Record amend hashes and verification evidence
| * 075d062 docs: Add amend practice log
* |   93577d1 Merge pull request #9 from jha21vvv/feature/kang-contributing-guide
|\ \  
| * | 444348e docs: Cover documentation changes in review checklist (apply review feedback)
| * | 19dbebf docs: Add review checklist and practical tips
* | |   325d386 Merge pull request #12 from jha21vvv/feature/ahn-game-integration
|\ \ \  
| |_|/  
|/| |   
| * | 0167f77 feat: Integrate game runner and add simulation tests (Closes #4)
|/ /  
* |   a72615f Merge pull request #7 from jha21vvv/feature/ahn-dish
|\ \  
| |/  
|/|   
| *   fafaa6d fix: Resolve merge conflict in food_data.json by keeping both dishes
| |\  
| |/  
|/|   
* |   ddd0834 Merge pull request #4 from jha21vvv/feature/kim-voting-system
|\ \  
| * | d450e85 feat: Implement multi-player turn-based voting and tie-breaker lottery
* | |   31e2c8b Merge pull request #6 from jha21vvv/feature/kang-food-loader
```

- 총 커밋 수: `git rev-list --count --all` 기준 37개
- 모든 기능 브랜치가 PR을 거쳐 `main`에 머지된 GitHub Flow 이력이 그래프에 그대로 남아 있음

---

## 6. 실행 방법

```bash
git clone https://github.com/jha21vvv/codyssey-b2-02.git
cd codyssey-b2-02

# 게임 실행
python src/game.py

# 모듈별 자체 검증
python src/voting.py
python src/tournament.py
python src/food_loader.py

# 테스트
python -m pytest tests/
```
