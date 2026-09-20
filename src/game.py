"""
Korean Food Tournament Game Runner
Authored by: Ahn Jaehyun (Lead Architect)
Part of Codyssey b2-02 Korean Food Tournament Game.

Integrates:
- food_loader.py (Data loading and random sampling)
- tournament.py (Bracket management and round state machine)
- voting.py (Turn-based multi-player voting and tie-breaker lottery)
"""

import sys
import argparse
from typing import List, Dict, Optional, Tuple

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    from src.food_loader import sample_foods, load_foods
    from src.tournament import TournamentEngine
    from src.voting import VotingSession, DECIDED_BY_VOTE, DECIDED_BY_LOTTERY
except ImportError:
    from food_loader import sample_foods, load_foods
    from tournament import TournamentEngine
    from voting import VotingSession, DECIDED_BY_VOTE, DECIDED_BY_LOTTERY


class FoodWorldCupGame:
    """
    한국 음식 128선 식사 추천 이상형 월드컵 메인 게임 실행기
    """

    def __init__(self, round_size: int = 16, players: Optional[List[str]] = None):
        if round_size not in (8, 16, 32):
            raise ValueError(f"지원하는 라운드 크기는 8, 16, 32강입니다. (입력: {round_size})")

        self.round_size = round_size
        self.players = players if players else ["참가자1"]
        self.foods = sample_foods(self.round_size)
        self.engine = TournamentEngine(self.foods)

    def print_header(self) -> None:
        player_list_str = ", ".join(self.players)
        print("=" * 65)
        print("    [한국 음식 128선 식사 추천 이상형 월드컵]")
        print("=" * 65)
        print(f"* 토너먼트 규모: {self.round_size}강")
        print(f"* 참여 플레이어: {player_list_str} (총 {len(self.players)}명)")
        print("-" * 65)

    def run_cli(self) -> Dict:
        """콘솔 대화형 인터랙티브 모드로 게임 진행"""
        self.print_header()

        current_round = ""
        while not self.engine.is_tournament_finished():
            round_name = self.engine.current_round_name
            if round_name != current_round:
                current_round = round_name
                print(f"\n===== [ {current_round} 개막! (총 {self.engine.total_matches_in_round}경기) ] =====")

            match = self.engine.get_current_match()
            if not match:
                break

            match_no = self.engine.current_match_index + 1
            food_a, food_b = match
            print(f"\n[{current_round} {match_no}경기]")
            print(f"  [1] {food_a['name']} ({food_a['category']}) - {food_a['desc']}")
            print(f"  [2] {food_b['name']} ({food_b['category']}) - {food_b['desc']}")

            session = VotingSession(self.players, match)

            for player in self.players:
                while True:
                    try:
                        prompt = f"  >> [{player}] 선택 (1 또는 2 입력): "
                        raw = input(prompt).strip()
                        choice = int(raw) - 1
                        if choice not in (0, 1):
                            print("     [오류] 1 또는 2만 입력해 주세요.")
                            continue
                        session.cast_vote(player, choice)
                        break
                    except (ValueError, EOFError):
                        session.cast_vote(player, 0)
                        break

            winner, method, logs = session.resolve_winner()
            for log_line in logs:
                print(f"     {log_line}")

            print(f"  * 승자: [{winner['name']}] 다음 라운드 진출!")
            self.engine.advance_winner(winner)

        champion = self.engine.get_final_champion()
        self.print_champion(champion)
        return champion

    def run_simulation(self, random_seed: Optional[int] = 42) -> Dict:
        """자동 시뮬레이션 모드 (단위 테스트 및 빠른 검증용)"""
        import random
        rng = random.Random(random_seed)

        self.print_header()
        current_round = ""

        while not self.engine.is_tournament_finished():
            round_name = self.engine.current_round_name
            if round_name != current_round:
                current_round = round_name
                print(f"\n===== [ {current_round} 진행 ] =====")

            match = self.engine.get_current_match()
            if not match:
                break

            match_no = self.engine.current_match_index + 1
            food_a, food_b = match
            print(f"  [{current_round} {match_no}경기] {food_a['name']} vs {food_b['name']}")

            session = VotingSession(self.players, match)
            for player in self.players:
                choice = rng.choice([0, 1])
                session.cast_vote(player, choice)

            winner, method, logs = session.resolve_winner()
            reason = "다수결 투표" if method == DECIDED_BY_VOTE else "동점 제비뽑기"
            print(f"    -> 승자: {winner['name']} ({reason})")
            self.engine.advance_winner(winner)

        champion = self.engine.get_final_champion()
        self.print_champion(champion)
        return champion

    def print_champion(self, champion: Dict) -> None:
        print("\n" + "=" * 65)
        print("        *** 오늘의 최종 우승 추천 음식! ***")
        print("=" * 65)
        print(f"  * 이름: {champion['name']}")
        print(f"  * 카테고리: {champion['category']}")
        print(f"  * 설명: {champion['desc']}")
        print("=" * 65)


def main():
    parser = argparse.ArgumentParser(description="한국 음식 128선 이상형 월드컵")
    parser.add_argument("--round", type=int, default=8, choices=[8, 16, 32], help="토너먼트 강수 (8, 16, 32)")
    parser.add_argument("--players", nargs="+", default=["안재현", "강동하", "김진우"], help="플레이어 목록")
    parser.add_argument("--interactive", action="store_true", help="대화형 CLI 플레이 모드")
    parser.add_argument("--seed", type=int, default=42, help="시뮬레이션 랜덤 시드")
    args = parser.parse_args()

    game = FoodWorldCupGame(round_size=args.round, players=args.players)
    if args.interactive:
        game.run_cli()
    else:
        game.run_simulation(random_seed=args.seed)


if __name__ == "__main__":
    main()