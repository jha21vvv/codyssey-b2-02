"""
Tournament Engine Module
Authored by: 안재현 (Lead Architect)
Part of Codyssey b2-02 Korean Food Tournament.
"""

from typing import List, Dict, Tuple, Optional


class TournamentEngine:
    """
    32강 / 16강 / 8강 토너먼트 대진 브래킷 상태 머신
    """
    def __init__(self, foods: List[Dict]):
        if len(foods) not in (8, 16, 32, 64, 128):
            raise ValueError(f"음식 개수는 2의 거듭제곱이어야 합니다. 현재: {len(foods)}개")
        self.initial_foods = list(foods)
        self.current_round_foods = list(foods)
        self.next_round_foods: List[Dict] = []
        self.current_match_index = 0
        self.history: List[Dict] = []

    @property
    def current_round_name(self) -> str:
        count = len(self.current_round_foods)
        if count == 2:
            return "결승전"
        elif count == 4:
            return "준결승 (4강)"
        return f"{count}강"

    @property
    def total_matches_in_round(self) -> int:
        return len(self.current_round_foods) // 2

    def get_current_match(self) -> Optional[Tuple[Dict, Dict]]:
        if self.is_tournament_finished():
            return None
        idx = self.current_match_index * 2
        return (self.current_round_foods[idx], self.current_round_foods[idx + 1])

    def advance_winner(self, winner: Dict) -> bool:
        """
        현재 매치의 승자를 다음 라운드 진출 목록에 추가
        반환값: 해당 라운드가 모두 끝나서 다음 라운드로 전환되었으면 True
        """
        match = self.get_current_match()
        if not match:
            raise ValueError("진행할 매치가 없습니다.")
        if winner not in match:
            raise ValueError(f"승자 {winner.get('name')}는 현재 대진 매치에 포함되어 있지 않습니다.")

        self.next_round_foods.append(winner)
        self.history.append({
            "round": self.current_round_name,
            "match": self.current_match_index + 1,
            "food_a": match[0],
            "food_b": match[1],
            "winner": winner
        })
        self.current_match_index += 1

        # 현재 라운드의 모든 매치가 끝났을 때
        if self.current_match_index >= self.total_matches_in_round:
            if len(self.next_round_foods) > 1:
                self.current_round_foods = list(self.next_round_foods)
                self.next_round_foods = []
                self.current_match_index = 0
                return True
            else:
                return True
        return False

    def is_tournament_finished(self) -> bool:
        return len(self.current_round_foods) == 1 or (
            len(self.current_round_foods) == 2 and len(self.next_round_foods) == 1
        )

    def get_final_champion(self) -> Optional[Dict]:
        if len(self.current_round_foods) == 1:
            return self.current_round_foods[0]
        if len(self.next_round_foods) == 1 and len(self.current_round_foods) == 2:
            return self.next_round_foods[0]
        return None


if __name__ == "__main__":
    # 1. 기본 8강 해피 패스 시뮬레이션
    print("=== [1] 기본 8강 토너먼트 시뮬레이션 ===")
    mock_foods = [
        {"id": i, "name": f"음식_{i}", "category": "한식", "desc": "설명"}
        for i in range(1, 9)
    ]
    engine = TournamentEngine(mock_foods)
    print(f"시작 라운드: {engine.current_round_name}")
    while not engine.is_tournament_finished():
        match = engine.get_current_match()
        if not match:
            break
        print(f"[{engine.current_round_name} {engine.current_match_index+1}경기] {match[0]['name']} vs {match[1]['name']}")
        engine.advance_winner(match[0])

    champ = engine.get_final_champion()
    print(f"최종 우승 음식: {champ['name']}!\n")

    # 2. 코드 리뷰 반영 엣지 케이스 테스트 (Reviewed by Deviskido in PR #1)
    print("=== [2] 코드 리뷰 피드백 반영 엣지 케이스 검증 (Deviskido 제안) ===")

    # [엣지 케이스 1]: 빈 리스트 및 7개(비 2의 거듭제곱) 입력 시 ValueError 검증
    try:
        TournamentEngine([])
        assert False, "빈 리스트 입력 시 ValueError가 발생해야 합니다."
    except ValueError:
        print("[PASS] 빈 리스트 초기화 시 ValueError 정상 발생")

    try:
        TournamentEngine([{"id": i, "name": f"음식_{i}"} for i in range(7)])
        assert False, "7개 아이템 입력 시 ValueError가 발생해야 합니다."
    except ValueError:
        print("[PASS] 7개(비 2의 거듭제곱) 초기화 시 ValueError 정상 발생")

    # [엣지 케이스 2]: 대진에 없는 무효 승자 전달 시 ValueError 및 상태 불변성 검증
    engine_edge = TournamentEngine(mock_foods)
    initial_match_idx = engine_edge.current_match_index
    initial_next_round_len = len(engine_edge.next_round_foods)
    invalid_winner = {"id": 999, "name": "대진에_없는_음식"}

    try:
        engine_edge.advance_winner(invalid_winner)
        assert False, "대진 매치에 없는 승자 전달 시 ValueError가 발생해야 합니다."
    except ValueError:
        assert engine_edge.current_match_index == initial_match_idx, "예외 발생 시 매치 인덱스가 유지되어야 합니다."
        assert len(engine_edge.next_round_foods) == initial_next_round_len, "예외 발생 시 진출자 목록이 변경되지 않아야 합니다."
        print("[PASS] 무효 승자 전달 시 ValueError 발생 및 상태 불변(State Unchanged) 확인")

    # [엣지 케이스 3]: 16강(15경기) 및 32강(31경기) 히스토리 레코드 수 검증
    # 16강 (8 + 4 + 2 + 1 = 15경기)
    foods_16 = [{"id": i, "name": f"음식_{i}"} for i in range(1, 17)]
    engine_16 = TournamentEngine(foods_16)
    while not engine_16.is_tournament_finished():
        m = engine_16.get_current_match()
        engine_16.advance_winner(m[0])
    assert len(engine_16.history) == 15, f"16강 경기 수는 15여야 합니다. 현재: {len(engine_16.history)}"
    print(f"[PASS] 16강 총 경기 기록 수 = {len(engine_16.history)}경기 (기대값: 15)")

    # 32강 (16 + 8 + 4 + 2 + 1 = 31경기)
    foods_32 = [{"id": i, "name": f"음식_{i}"} for i in range(1, 33)]
    engine_32 = TournamentEngine(foods_32)
    while not engine_32.is_tournament_finished():
        m = engine_32.get_current_match()
        engine_32.advance_winner(m[0])
    assert len(engine_32.history) == 31, f"32강 경기 수는 31여야 합니다. 현재: {len(engine_32.history)}"
    print(f"[PASS] 32강 총 경기 기록 수 = {len(engine_32.history)}경기 (기대값: 31)")

    print("\n[ALL PASS] 모든 코드 리뷰 피드백 검증 완료! (100% Pass)")
