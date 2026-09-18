# 🍱 한국 음식 128선 식사 추천 이상형 월드컵 (Codyssey b2-02)

> **프로젝트 소개**: 3인 팀(안재현, 강동하, 김진우)으로 구성된 Git 실전 협업 시뮬레이션 저장소입니다.  
> 실제 협업 환경에서 발생하는 **GitHub Flow 브랜치 전략, 이슈-PR 연동, 코드 리뷰 문화, 동일 파일 인접 라인 및 비자명(Rename vs Modify) 충돌 해결, Git 트러블슈팅 4종(`amend`, `reset`, `revert`, `stash`)**을 **"한국 음식 128선 식사 추천 이상형 월드컵"** 게임을 직접 개발하며 체득하고 완벽하게 증빙합니다.

---

## 🌟 GitHub Flow 브랜치 전략 선택 이유 (3줄)

1. **상시 배포 가능한 안정성**: `main` 브랜치를 항상 깨지지 않는 동작 상태로 유지하여 안정성을 극대화합니다.
2. **신속하고 가벼운 개발 사이클**: 복잡한 브랜치 계층 대신 `feature/*` 작업 브랜치를 통해 빠르고 유연하게 기능을 통합합니다.
3. **투명한 피어 리뷰 문화**: 모든 변경사항을 PR 기반으로 검증하고 최소 1인의 승인을 거치도록 강제하여 코드 품질을 보장합니다.

---

## 📂 프로젝트 구조

```text
codyssey-b2-02/
├── data/
│   └── food_data.json              # 강동하: 한국 대표 음식 128선 JSON 데이터셋
├── src/
│   ├── food_loader.py              # 강동하: 음식 데이터 로더 및 32/16/8 무작위 샘플러
│   ├── tournament.py               # 안재현: 32/16/8강 대진표 브래킷 상태머신 엔진
│   ├── voting.py                   # 김진우: 다인원 순차 턴제 투표 집계기
│   └── tie_breaker.py              # 김진우: 짝수 인원 동점 시 제비뽑기 추첨기 (충돌 실습 2)
├── game.py                         # 안재현: 식사 추천 월드컵 메인 통합 실행기
├── docs/                           # 협업 및 실습 필수 문서 3종
│   ├── CONTRIBUTING.md             # 브랜치/커밋/PR/리뷰/충돌 협업 가이드
│   ├── conflict-resolution.md      # 인접 라인 & 비자명 충돌 해결 2회 실습 로그
│   └── troubleshooting-log.md      # amend, reset, revert, stash 트러블슈팅 4종 로그
├── SUBMISSION.md                   # 최종 제출물 종합 인덱스 대시보드
├── PROJECT_10STEP_PLAN.md          # 10단계 실행 플랜 및 기여도 매트릭스
├── TEAM_SCHEDULE.md                # 3인 협업 타임라인 (일요일 15:00 완결)
└── README.md                       # 프로젝트 메인 안내 문서
```

---

## 🎮 게임 실행 방법

Python 3.10 이상 환경에서 별도의 외부 라이브러리 설치 없이 즉시 실행할 수 있습니다:

```bash
# 게임 실행
python game.py
```

- **게임 규칙**:
  1. 참가할 인원 수(1인 혼자 선택 또는 2~8인 단체 투표)를 입력합니다.
  2. 32강, 16강, 8강 중 원하는 토너먼트 규모를 선택합니다.
  3. 매 라운드마다 맞붙는 두 음식 중 더 먹고 싶은 음식에 순차적으로 투표합니다.
  4. 짝수 인원 투표로 동점이 발생하면 **동점 제비뽑기(Tie-Breaker)**가 발동하여 행운의 승자를 추첨합니다.
  5. 결승전 승리를 거머쥔 최종 오늘의 추천 식사 메뉴가 발표됩니다!

---

## 📑 핵심 제출 문서 바로가기

- [SUBMISSION.md](SUBMISSION.md) : 팀원별 PR, 리뷰, 이슈 및 Git Graph 증빙 종합 인덱스
- [CONTRIBUTING.md](docs/CONTRIBUTING.md) : 팀 브랜치 네이밍, 커밋 컨벤션 및 코드 리뷰 규칙
- [conflict-resolution.md](docs/conflict-resolution.md) : 충돌 2회(인접 라인 + 비자명) 해결 기록
- [troubleshooting-log.md](docs/troubleshooting-log.md) : Git 트러블슈팅 4종 실습 로그
