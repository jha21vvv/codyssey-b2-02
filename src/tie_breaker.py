"""
Lottery Module (동점 제비뽑기 추첨기)
Authored by: 김진우 (Voting & QA Lead)
Part of Codyssey b2-02 Korean Food Tournament.
"""
# 테스트를 위한 설명
import random
from typing import Dict, List, Optional, Sequence, Tuple


def draw_lots(candidates: Sequence[Dict], seed: Optional[int] = None) -> Dict:
    """
    동점 후보 중 무작위로 1개를 추첨한다.

    seed를 주면 동일한 후보 목록에 대해 항상 동일한 결과가 나오므로
    QA 및 테스트에서 재현 가능한 검증이 가능하다.
    """
    if not candidates:
        raise ValueError("추첨할 후보가 없습니다. 최소 1개 이상의 후보가 필요합니다.")

    rng = random.Random(seed) if seed is not None else random
    return rng.choice(list(candidates))


def draw_lots_with_log(
    candidates: Sequence[Dict], seed: Optional[int] = None
) -> Tuple[Dict, List[str]]:
    """
    추첨을 수행하고, 사용자에게 보여줄 진행 로그를 함께 반환한다.
    게임 화면에서 "제비뽑기 진행 중..." 연출에 사용한다.
    """
    winner = draw_lots(candidates, seed=seed)

    log = ["동점입니다! 제비뽑기로 승자를 가립니다."]
    for food in candidates:
        marker = "당첨" if food is winner else "꽝"
        log.append(f"  - {food.get('name', '이름없음')} ... {marker}")
    log.append(f"제비뽑기 결과: '{winner.get('name', '이름없음')}' 승리!")

    return winner, log


if __name__ == "__main__":
    print("=== [1] 기본 추첨 동작 검증 ===")
    tie_candidates = [
        {"id": 1, "name": "김치찌개", "category": "찌개/탕류"},
        {"id": 2, "name": "된장찌개", "category": "찌개/탕류"},
    ]
    picked = draw_lots(tie_candidates)
    assert picked in tie_candidates, "추첨 결과는 반드시 후보 목록 안에 있어야 합니다."
    print(f"[PASS] 추첨 결과 '{picked['name']}' 가 후보 목록 내에 존재")

    print("\n=== [2] 시드 고정 시 재현성 검증 ===")
    first = draw_lots(tie_candidates, seed=42)
    second = draw_lots(tie_candidates, seed=42)
    assert first is second, "동일 시드는 동일한 결과를 반환해야 합니다."
    print(f"[PASS] seed=42 두 번 추첨 결과 동일 ('{first['name']}')")

    print("\n=== [3] 빈 후보 목록 예외 검증 ===")
    try:
        draw_lots([])
        assert False, "빈 후보 목록 추첨 시 ValueError가 발생해야 합니다."
    except ValueError:
        print("[PASS] 빈 후보 목록 추첨 시 ValueError 정상 발생")

    print("\n=== [4] 추첨 로그 출력 검증 ===")
    _, lines = draw_lots_with_log(tie_candidates, seed=7)
    for line in lines:
        print(line)
    assert sum(1 for line in lines if "당첨" in line) == 1, "당첨자는 정확히 1명이어야 합니다."
    print("[PASS] 추첨 로그에 당첨자 1명만 표기됨")

    print("\n[ALL PASS] lottery 모듈 전체 검증 완료!")
