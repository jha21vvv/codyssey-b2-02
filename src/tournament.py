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
    # 단위 테스트 및 시뮬레이션
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
    print(f"\n최종 우승 음식: {champ['name']}!")
