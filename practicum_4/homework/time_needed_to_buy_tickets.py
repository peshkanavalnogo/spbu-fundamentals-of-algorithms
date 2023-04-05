from typing import Any

import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0

    for i in range(len(tickets)):
        seconds_elapsed += min(tickets[i], tickets[k]) if i <= k else min(tickets[i], tickets[k]- 1)
    return seconds_elapsed


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("time_needed_to_buy_tickets_case.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}d. Expected output: {c['output']}")
