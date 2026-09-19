"""한국 음식 JSON 로더 및 토너먼트용 비복원 무작위 샘플러."""

import json
from pathlib import Path
import random


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "food_data.json"


def load_foods() -> list[dict]:
    """실행 디렉터리와 무관하게 기본 데이터셋의 음식 목록을 읽는다.

    각 음식은 id, name, category, desc를 포함한 딕셔너리다.
    파일 읽기 오류와 JSON 파싱 오류는 호출자에게 전달한다.
    """
    with DATA_PATH.open(encoding="utf-8") as file:
        return json.load(file)["foods"]


def sample_foods(count: int = 32) -> list[dict]:
    """8·16·32강에 사용할 음식을 중복 없이 무작위 순서로 반환한다.

    지원하지 않는 개수는 ValueError, 정수가 아닌 값은 TypeError를 낸다.
    데이터가 요청 개수보다 적으면 random.sample이 ValueError를 낸다.
    """
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("음식 개수는 정수여야 합니다.")
    if count not in (8, 16, 32):
        raise ValueError("음식 개수는 8, 16, 32 중 하나여야 합니다.")
    return random.sample(load_foods(), count)


if __name__ == "__main__":
    foods = sample_foods()
    print(f"{len(foods)}강 음식 비복원 추출 완료")
    for index, food in enumerate(foods, start=1):
        print(f"{index:2}. {food['name']} [{food['category']}] — {food['desc']}")
