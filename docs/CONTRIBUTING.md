# Contributing Guide

> **팀명**: Codyssey B2 Team 2  
> **저장소**: [https://github.com/jha21vvv/codyssey-b2-02](https://github.com/jha21vvv/codyssey-b2-02)  
> **프로젝트**: Python 핵심 유틸리티 모음 및 Git 실전 협업

---

## 1. 브랜치 전략 (GitHub Flow)

우리 팀은 가볍고 신속하며 상시 배포 가능한 **GitHub Flow** 브랜치 전략을 채택합니다.

- **`main` 브랜치**:
  - 항상 배포 가능한 안정적인 상태(Production Ready)를 유지합니다.
  - `main` 브랜치에 직접 커밋 푸시하는 것은 Branch Protection Rule에 의해 엄격히 금지됩니다.
- **`feature/*` 브랜치**:
  - 모든 신규 기능 개발, 버그 수정, 문서 작성은 `feature/*` 브랜치에서 격리되어 진행됩니다.
  - 작업 완료 후 반드시 Pull Request(PR)를 발행하여 코드 리뷰 승인을 받아야 `main`에 머지할 수 있습니다.

### 💡 우리 팀이 GitHub Flow를 선택한 이유 (3줄)
1. **단순하고 명확한 흐름**: 복잡한 릴리즈/핫픽스 브랜치 분기 없이 기능 단위 브랜치와 `main`만 운용하여 협업 오버헤드를 최소화합니다.
2. **배포 상시성 보장**: `main`은 언제든 배포 및 시연 가능한 깨끗한 상태를 유지하여 개발 안정성을 극대화합니다.
3. **PR 중심 품질 관리**: 모든 코드 변경이 PR을 통한 최소 1인 이상의 동료 리뷰(Approval)를 거치도록 강제하여 코드 결함을 조기 차단합니다.

---

## 2. 브랜치 네이밍 규칙

브랜치는 담당자와 작업 목적이 명확히 드러나도록 아래 형식을 준수합니다:

- **형식**: `feature/<작성자이름>-<작업내용>`
- **예시**:
  - `feature/ahn-math-utils` (안재현의 수학 유틸리티 개발)
  - `feature/kang-string-utils` (강동하의 문자열 유틸리티 개발)
  - `feature/kim-date-utils` (김진우의 날짜 유틸리티 개발)
  - `feature/kim-submission-final` (김진우의 최종 제출 인덱스 작성)

---

## 3. 커밋 메시지 컨벤션

커밋 메시지는 변경 대상과 이유를 누구나 명확히 유추할 수 있도록 표준 접두사를 사용합니다.

### 허용 접두사 (Type)
- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `docs:` 문서 수정 및 추가 (`README.md`, `docs/*` 등)
- `refactor:` 코드 리팩토링 (기능 변경 없는 구조 개선)
- `test:` 테스트 코드 추가 및 수정
- `chore:` 빌드, 설정, 패키지 매니저 관련 변경

### 🚫 의미 없는 커밋 메시지 금지 기준
다음과 같은 커밋 메시지는 엄격히 금지되며, 발견 시 리뷰 단계에서 반려 또는 `amend`로 정정합니다:
1. **변경 대상을 유추할 수 없는 단어만 있는 경우**: `update`, `fix`, `temp`, `wip`, `final`, `test`, `asdf` 등
2. **무엇을/왜 바꿨는지 드러나지 않는 경우**: `bug fix`, `edit file`, `change code` 등 (구체적 대상/효과 없음)
3. **올바른 예시**:
   - `feat: Add clamp and statistics functions in math_utils`
   - `fix: Handle negative index in truncate_words`
   - `docs: Add branch protection guide to CONTRIBUTING.md`

---

## 4. PR (Pull Request) 작성 규칙

모든 PR은 아래 표준 항목을 반드시 포함해야 합니다:

### PR 본문 필수 항목
```markdown
## 연결 이슈
- Closes #<이슈번호>

## 변경 사항 (What)
- 변경한 파일 목록 및 핵심 기능 요약

## 변경 이유 (Why)
- 이 작업을 수행한 목적 및 배경 설명

## 테스트 / 검증 (How)
- [ ] 단위 테스트(doctest / unittest) 실행 확인
- [ ] 충돌 가능성 체크 및 로컬 브랜치 최신화
```

### 병합(Merge) 조건
1. **최소 1명 이상의 승인 (Approve)** 필수
2. 모든 대화 스레드(Review Comments) 해결 완료
3. 충돌(Conflict)이 없는 상태 확인

---

## 5. 코드 리뷰 규칙 (최소 품질 기준)

코드 리뷰는 단순한 형식적 승인 절차가 아닌, 상호 성장과 버그 예방의 핵심 도구입니다.

1. **"LGTM / 좋아요" 단독 코멘트 절대 금지**:
   - 승인 시에도 코드의 장점이나 배운 점을 구체적으로 언급합니다.
2. **구체적 파일 및 라인 근거 피드백**:
   - 특정 라인에 인라인 코멘트를 달아 경계값 처리, 예외 상황, 성능/보안 리스크, 대안을 제안합니다.
   - 예시: `"src/utils/math_utils.py 24번 라인: 빈 리스트가 전달될 경우 ZeroDivisionError가 발생할 수 있습니다. 리스트 길이를 사전에 체크하는 방어 로직을 제안합니다."`
3. **상호작용 필수**:
   - 리뷰어의 피드백에 대해 작성자는 피드백 반영 커밋(`apply review feedback`)을 올리거나 기술적 근거를 담은 답글을 달아야 합니다.

---

## 6. 충돌(Conflict) 발생 시 기본 대응 흐름

1. **상황 공유**: 충돌 발생 시 슬랙/구두로 상대 작업자에게 즉시 공유합니다.
2. **로컬 병합 및 마커 확인**:
   ```bash
   git checkout feature/my-feature
   git fetch origin
   git merge origin/main
   # CONFLICT 발생 확인 -> 충돌 마커 확인
   ```
3. **수동 충돌 해결**: 양쪽의 작업 의도를 보존하는 최선의 해결책(Keep both / Refactor)을 적용하여 파일 편집.
4. **머지 커밋 생성**:
   ```bash
   git add <충돌해결파일>
   git commit -m "fix: Resolve merge conflict in <파일명>"
   git push origin feature/my-feature
   ```
5. **문서 기록**: 해결 과정을 [docs/conflict-resolution.md](conflict-resolution.md)에 상세히 기록합니다.
