"""
Voting Module (다인원 순차 턴제 투표 집계기)
Authored by: 김진우 (Voting & QA Lead)
Part of Codyssey b2-02 Korean Food Tournament.

TournamentEngine이 내어준 한 매치(음식 A vs 음식 B)에 대해
N명의 플레이어가 순서대로 1표씩 행사하고, 그 결과로 승자를 확정한다.
동점이 발생하면 lottery 모듈의 제비뽑기로 승자를 가린다.
"""

from typing import Dict, List, Optional, Tuple

try:
    from src.tie_breaker import draw_lots_with_log
except ImportError:
    try:
        from tie_breaker import draw_lots_with_log
    except ImportError:
        try:
            from src.lottery import draw_lots_with_log
        except ImportError:
            from lottery import draw_lots_with_log


# 승자가 결정된 방식
DECIDED_BY_VOTE = "vote"
DECIDED_BY_LOTTERY = "lottery"


class VotingSession:
    """
    한 매치에 대한 다인원 순차 투표 세션.

    플레이어는 등록된 순서대로 턴이 돌아가며, 자기 차례에만 1표를 행사할 수 있다.
    """

    def __init__(self, players: List[str], match: Tuple[Dict, Dict]):
        if not players:
            raise ValueError("플레이어가 최소 1명 이상 필요합니다.")
        if len(set(players)) != len(players):
            raise ValueError(f"플레이어 이름은 중복될 수 없습니다. 입력: {players}")
        if len(match) != 2:
            raise ValueError("한 매치는 정확히 2개의 음식으로 구성되어야 합니다.")

        self.players = list(players)
        self.match = match
        self.votes: Dict[str, int] = {}   # 플레이어 이름 -> 선택한 음식 인덱스(0 또는 1)
        self.turn_index = 0

    @property
    def current_player(self) -> Optional[str]:
        """현재 투표할 차례인 플레이어. 전원 투표가 끝났으면 None."""
        if self.is_complete:
            return None
        return self.players[self.turn_index]

    @property
    def is_complete(self) -> bool:
        return self.turn_index >= len(self.players)

    def cast_vote(self, player: str, choice_index: int) -> None:
        """
        현재 차례인 플레이어의 표를 기록하고 다음 턴으로 넘긴다.

        choice_index: 0 = 매치의 첫 번째 음식, 1 = 두 번째 음식
        """
        if self.is_complete:
            raise ValueError("이미 모든 플레이어의 투표가 완료되었습니다.")
        if player != self.current_player:
            raise ValueError(
                f"지금은 '{self.current_player}'의 차례입니다. '{player}'는 투표할 수 없습니다."
            )
        if choice_index not in (0, 1):
            raise ValueError(f"선택 번호는 0 또는 1이어야 합니다. 입력값: {choice_index}")

        self.votes[player] = choice_index
        self.turn_index += 1

    def tally(self) -> Dict[str, int]:
        """음식 이름별 득표 수를 집계한다."""
        counts = {food["name"]: 0 for food in self.match}
        for choice_index in self.votes.values():
            counts[self.match[choice_index]["name"]] += 1
        return counts

    def is_tie(self) -> bool:
        """전원 투표 완료 기준으로 동점 여부를 판별한다."""
        if not self.is_complete:
            raise ValueError("모든 플레이어가 투표를 마쳐야 동점 여부를 판별할 수 있습니다.")
        counts = list(self.tally().values())
        return counts[0] == counts[1]

    def resolve_winner(self, seed: Optional[int] = None) -> Tuple[Dict, str, List[str]]:
        """
        투표 결과로 승자를 확정한다.

        반환값: (승자 음식 dict, 결정 방식, 진행 로그)
        승자 dict는 TournamentEngine.advance_winner()에 그대로 넘길 수 있다.
        """
        if not self.is_complete:
            raise ValueError(
                f"아직 {len(self.players) - self.turn_index}명이 투표하지 않았습니다."
            )

        counts = self.tally()
        log = [f"투표 결과: {counts[self.match[0]['name']]} : {counts[self.match[1]['name']]}"]

        if self.is_tie():
            winner, lottery_log = draw_lots_with_log(self.match, seed=seed)
            return winner, DECIDED_BY_LOTTERY, log + lottery_log

        winner_name = max(counts, key=counts.get)
        winner = next(food for food in self.match if food["name"] == winner_name)
        log.append(f"'{winner_name}' 가 과반 득표로 승리!")
        return winner, DECIDED_BY_VOTE, log


if __name__ == "__main__":
    mock_match = (
        {"id": 1, "name": "김치찌개", "category": "찌개/탕류", "desc": "칼칼한 묵은지"},
        {"id": 2, "name": "된장찌개", "category": "찌개/탕류", "desc": "구수한 손맛"},
    )
    players = ["진우", "재현", "동하", "민수"]

    print("=== [1] 4인 순차 투표 해피 패스 (3:1) ===")
    session = VotingSession(players, mock_match)
    for player, choice in zip(players, [0, 0, 1, 0]):
        print(f"[{player}의 차례] -> '{mock_match[choice]['name']}' 선택")
        session.cast_vote(player, choice)

    winner, method, log = session.resolve_winner()
    for line in log:
        print(line)
    assert method == DECIDED_BY_VOTE, "3:1 상황은 투표로 결정되어야 합니다."
    assert winner["name"] == "김치찌개", "3표를 받은 김치찌개가 승자여야 합니다."
    print(f"[PASS] 다수결 승자 = '{winner['name']}' (방식: {method})\n")

    print("=== [2] 4인 2:2 동점 -> 제비뽑기 승격 ===")
    tie_session = VotingSession(players, mock_match)
    for player, choice in zip(players, [0, 1, 0, 1]):
        tie_session.cast_vote(player, choice)

    assert tie_session.is_tie(), "2:2는 동점으로 판별되어야 합니다."
    tie_winner, tie_method, tie_log = tie_session.resolve_winner(seed=42)
    for line in tie_log:
        print(line)
    assert tie_method == DECIDED_BY_LOTTERY, "동점은 제비뽑기로 결정되어야 합니다."
    assert tie_winner in mock_match, "추첨 승자는 매치 안의 음식이어야 합니다."
    print(f"[PASS] 동점 추첨 승자 = '{tie_winner['name']}' (방식: {tie_method})\n")

    print("=== [3] 예외 상황 방어 검증 ===")
    try:
        VotingSession([], mock_match)
        assert False, "빈 플레이어 목록은 ValueError여야 합니다."
    except ValueError:
        print("[PASS] 플레이어 0명 입력 시 ValueError 정상 발생")

    try:
        VotingSession(["진우", "진우"], mock_match)
        assert False, "중복 이름은 ValueError여야 합니다."
    except ValueError:
        print("[PASS] 플레이어 이름 중복 시 ValueError 정상 발생")

    guard_session = VotingSession(players, mock_match)
    try:
        guard_session.cast_vote("재현", 0)
        assert False, "차례가 아닌 플레이어의 투표는 ValueError여야 합니다."
    except ValueError:
        print("[PASS] 턴 순서 위반 투표 시 ValueError 정상 발생")

    try:
        guard_session.cast_vote("진우", 5)
        assert False, "범위 밖 선택 번호는 ValueError여야 합니다."
    except ValueError:
        print("[PASS] 잘못된 선택 번호(5) 입력 시 ValueError 정상 발생")

    try:
        guard_session.resolve_winner()
        assert False, "투표 미완료 상태의 승자 확정은 ValueError여야 합니다."
    except ValueError:
        print("[PASS] 전원 투표 전 승자 확정 요청 시 ValueError 정상 발생")

    print("\n=== [4] 동일 시드 재현성 검증 ===")
    results = []
    for _ in range(2):
        s = VotingSession(players, mock_match)
        for player, choice in zip(players, [0, 1, 0, 1]):
            s.cast_vote(player, choice)
        results.append(s.resolve_winner(seed=42)[0]["name"])
    assert results[0] == results[1], "동일 시드는 동일한 추첨 결과를 내야 합니다."
    print(f"[PASS] seed=42 동점 추첨 2회 결과 동일 ('{results[0]}')")

    print("\n[ALL PASS] voting 모듈 전체 검증 완료!")
