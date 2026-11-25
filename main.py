"""Entry for make.fun bounty u-kevin-the-funniest-office-joke-judged-head-to-head-3dc3233c.

Writes a single original office joke (one line, 1-200 characters) to
/output/entry.txt. Deterministic, no network, no randomness.

Round 2: the 15-minute standup — everyone stands up just to report
they are still sitting on the same task.
"""

import os

ENTRY = "Our 15-minute standup is just everyone standing up to say they are still sitting on the same task."


def main() -> None:
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
