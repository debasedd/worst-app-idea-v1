#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence, at most 240 characters, pitching the worst and
most useless app idea imaginable, to /output/entry.txt:

    SniffR is an AI app that smells your leftovers through your phone
    screen and tells you, with total confidence, whether they expired
    last Tuesday or are simply having a bad day.

Why it fails most brilliantly, against the judge's brief:
- It names a specific app and what it uselessly does: SniffR smells
  your leftovers through your phone screen. A product that sounds
  real, a founder who sounds certain, a function nobody needs.
- The uselessness is funny through absurd logic and deadpan
  confidence: the app is totally confident about a verdict no one
  asked for, and its two possible answers are equally useless -
  "expired last Tuesday" (information your nose already gave you)
  or "simply having a bad day" (a diagnosis, for food).
- The mismatch is perfect: a phone screen cannot smell anything,
  and even if it could, the problem it solves does not exist -
  everyone already opens the container and sniffs it themselves,
  for free, in one second.
- It is tight: one sentence, no padding, 176 characters, inside the
  240-character limit, and retellable in one breath.
"""

import os

LINE = "SniffR is an AI app that smells your leftovers through your phone screen and tells you, with total confidence, whether they expired last Tuesday or are simply having a bad day."


def main() -> None:
    # Self-check the brief's gate before writing: UTF-8 text, 1-240
    # characters, not only white space, a single line.
    encoded = LINE.encode("utf-8")
    assert 1 <= len(LINE) <= 240, "entry must be 1-240 characters"
    assert LINE.strip() == LINE and "\n" not in LINE
    # One sentence, pitched as one idea: exactly one terminal period,
    # no abbreviation dots smuggled in, no double spaces.
    assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be one sentence"
    assert "  " not in LINE
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    # Plain write: the grader reads /output/entry.txt as another user,
    # so the file must keep the default readable mode (a mkstemp file
    # is 0600 and the grader's output rule rejects it).
    with open(out_path, "wb") as f:
        f.write(encoded)
    # Deterministic readable mode whatever the sandbox umask is, so
    # the grader can read the entry as another user.
    os.chmod(out_path, 0o644)
    with open(out_path, "rb") as f:
        assert f.read() == encoded, "entry.txt does not match LINE"
    print(f"{LINE} ({len(encoded)} chars)")


if __name__ == "__main__":
    main()
