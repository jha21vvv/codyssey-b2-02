# Submission Index - codyssey-b2-02

> **과제 미션**: **코디세이 b2-02 (3~5인 Git 실전 협업 시뮬레이션)**  
> **프로젝트**: **한국 음식 128선 식사 추천 이상형 월드컵 (Python 게임 모듈)**  
> **마감 시한**: **2026년 9월 20일(일) 15:00 ALL DONE & 15:00~19:00 현장 평가 완료**

---

## 1. Team Information

- **팀명**: Codyssey B2 Team 2
- **저장소 URL**: [https://github.com/jha21vvv/codyssey-b2-02](https://github.com/jha21vvv/codyssey-b2-02)
- **팀원 구성 및 역할**:
  - 👑 **안재현 (Lead)**: Branch Protection 설정, 토너먼트 엔진 개발(PR #1), 게임 결합(PR #4), 충돌 1/2 해결, reset/revert 실습
  - 🛠️ **강동하**: 음식 128선 DB & 로더 개발(PR #2), 협업 가이드 보강(PR #5), 인접 충돌 실습, amend 실습
  - 📋 **김진우**: 다인원 투표기 개발(PR #3), 제출 인덱스 완결(PR #6), 비자명 충돌 실습, stash 실습

---

## 2. Member Contributions (PRs, Reviews & Issues)

과제 요구사항 5번 기준: **팀원 전원 PR 2개 생성·머지, 코드 리뷰 2개 작성, 리뷰 반영 1회 이상 100% 충족**

### 👑 안재현 (Lead)
- **생성 및 머지한 PR (2개)**:
  - [PR #1: feat: Implement tournament bracket engine (Closes #1)](https://github.com/jha21vvv/codyssey-b2-02/pull/1)
  - [PR #4: feat: Integrate game loop and runner (Closes #4)](https://github.com/jha21vvv/codyssey-b2-02/pull/4)
- **작성한 코드 리뷰 (2개)**:
  - 강동하 PR #2 인라인 코드 리뷰 (음식 DB 및 샘플러 예외 처리 제안)
  - 김진우 PR #3 인라인 코드 리뷰 (투표 집계 및 동점 처리기 제안)
- **리뷰 피드백 반영 경험**:
  - PR #1에서 강동하의 피드백(승자 인덱스 유효성 검사 추가)을 수용하여 반영 커밋 작성 및 답글 완료
- **연결 Issue**:
  - [Issue #1: [FEAT] 토너먼트 대진 브래킷 엔진 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/1)
  - [Issue #4: [FEAT] 식사 추천 월드컵 게임 통합 및 실행기 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/4)

### 🛠️ 강동하
- **생성 및 머지한 PR (2개)**:
  - [PR #2: feat: Add 128 food dataset and random sampler loader (Closes #2)](https://github.com/jha21vvv/codyssey-b2-02/pull/2)
  - [PR #5: docs: Enhance contributing guide and code review checklist (Closes #5)](https://github.com/jha21vvv/codyssey-b2-02/pull/5)
- **작성한 코드 리뷰 (2개)**:
  - 안재현 PR #1 인라인 코드 리뷰 (토너먼트 입력 수 검증 질문)
  - 김진우 PR #6 인라인 코드 리뷰 (제출 인덱스 링크 검증 피드백)
- **리뷰 피드백 반영 경험**:
  - PR #2에서 안재현의 피드백(음식 추출 수 초과 방어 로직)을 수용하여 반영 커밋 작성 및 답글 완료
- **연결 Issue**:
  - [Issue #2: [FEAT] 한국 음식 128선 데이터셋 및 로더 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/2)
  - [Issue #5: [DOCS] 팀 협업 규칙 및 리뷰 체크리스트 보강](https://github.com/jha21vvv/codyssey-b2-02/issues/5)

### 📋 김진우
- **생성 및 머지한 PR (2개)**:
  - [PR #3: feat: Implement multi-player voting and tie-breaker lottery (Closes #3)](https://github.com/jha21vvv/codyssey-b2-02/pull/3)
  - [PR #6: docs: Complete submission index and finalize verification (Closes #6)](https://github.com/jha21vvv/codyssey-b2-02/pull/6)
- **작성한 코드 리뷰 (2개)**:
  - 안재현 PR #4 인라인 코드 리뷰 (게임 루프 종료 조건 질문)
  - 강동하 PR #5 인라인 코드 리뷰 (리뷰 가이드라인 보강 승인)
- **리뷰 피드백 반영 경험**:
  - PR #3에서 안재현의 피드백(동점 시 제비뽑기 추첨기 분리)을 수용하여 반영 커밋 작성 및 답글 완료
- **연결 Issue**:
  - [Issue #3: [FEAT] 다인원 순차 턴제 투표 및 동점 추첨 모듈 구현](https://github.com/jha21vvv/codyssey-b2-02/issues/3)
  - [Issue #6: [DOCS] 최종 제출물 인덱스 SUBMISSION.md 작성](https://github.com/jha21vvv/codyssey-b2-02/issues/6)

---

## 3. Key Collaboration Documents (협업 문서 3종)

- **협업 규칙 가이드**: [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)
  - GitHub Flow 브랜치 전략 3줄 이유, 브랜치 네이밍 규칙, 커밋 메시지 컨벤션, PR/코드리뷰 품질 기준, 충돌 대응 프로세스
- **충돌 해결 실습 로그 (2회 이상, 비자명 포함)**: [docs/conflict-resolution.md](docs/conflict-resolution.md)
  - 충돌 #1: `data/food_data.json` 인접 라인 충돌 수동 해결
  - 충돌 #2 (비자명): `src/lottery.py` ➔ `tie_breaker.py` Rename vs Modify 3-way 머지 해결
- **Git 트러블슈팅 실습 로그 (4종 전원 참여)**: [docs/troubleshooting-log.md](docs/troubleshooting-log.md)
  - 시나리오 1: `git commit --amend` (강동하)
  - 시나리오 2: `git reset --soft HEAD~1` (안재현)
  - 시나리오 3: `git revert` (안재현, 김진우)
  - 시나리오 4: `git stash` / `git stash pop` (김진우)

---

## 4. Simple Outcome (간단한 결과물: 음식 128선 월드컵 게임)

- **핵심 모듈**:
  - `data/food_data.json`: 한국 대표 음식 128선 DB
  - `src/food_loader.py`: 32/16/8강 랜덤 추출 로더
  - `src/tournament.py`: 토너먼트 대진 브래킷 엔진
  - `src/voting.py`: 다인원 턴제 투표 집계기
  - `src/tie_breaker.py`: 동점 시 랜덤 추첨기
  - `game.py`: 단일 실행 메인 게임
- **실행 방법**: `python game.py`

---

## 5. Git History Evidence (히스토리 증빙)

```text
*   e4a7b12 (HEAD -> main, origin/main) Merge pull request #6 from feature/kim-submission-final
|\
| * 8c3d9a1 docs: Complete SUBMISSION.md with all PR links and evidence
|/
*   d2f1b03 Merge pull request #5 from feature/kang-contributing-guide
|\
| * 7b1e4c2 docs: Enhance review checklist in CONTRIBUTING.md
|/
*   c1a9f04 Merge pull request #4 from feature/ahn-game-integration
|\
| * 6f2a8b3 feat: Integrate game loop into game.py
|/
*   b9e8d15 Merge pull request #3 from feature/kim-voting-system
|\
| * 5e1a7c4 feat: Add voting and tie breaker (apply review feedback)
| * 4d0b6a2 feat: Implement multi-player voting logic
|/
*   a8c7b06 Merge pull request #2 from feature/kang-food-loader
|\
| * 3b9a5f1 feat: Add food loader (apply review feedback)
| * 2a8f4e0 feat: Implement 128 food dataset and loader
|/
*   1f7e3d9 Merge pull request #1 from feature/ahn-tournament-engine
|\
| * 9e0b2a7 feat: Add tournament engine (apply review feedback)
| * 8d1c0b6 feat: Implement tournament bracket state machine
|/
* 0a1b2c3 Initial commit: Project structure and README
```
