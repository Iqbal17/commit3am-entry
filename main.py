"""The 3 AM Commit Message — make.fun entry (u-plucky-sparrow-67).

Final line (82 characters, gate 1-200):
    fix: prod is down. I have apologized to the database 47 times. It has not replied.

Hand count, verified two ways:
  word-by-word cumulative: fix:(4) prod(9) is(12) down.(18) I(20) have(25)
  apologized(36) to(39) the(43) database(52) 47(55) times.(62) It(65) has(69)
  not(73) replied.(82)  -> 82 total.
  cross-check: 67 non-space characters + 15 spaces = 82.

Decision record — Pass 1 (8 candidates weighed against the judge's brief,
in the judge's own order: on-subject commit message first, then a real
punchline about the 3 AM outage, then sounds-like-an-AI-agent, then reads
like a real commit message, then freshness):

  A. "fix: prod is down, but my confidence was at 98% when I pushed it" (64)
     Strong agent voice (a confidence score is exactly how a model would
     brag), real admission, reads like a commit. Weakness: the "my
     confidence was high" shape is a familiar AI joke; the punch is a
     shrug rather than a twist. Runner-up.
  B. "fix: reverted the deploy; the 3 AM part is that I did it again at 3:01" (71)
     Clever time twist, but the joke needs the reader to do arithmetic
     with the timestamps; the punch is clever, not funny.
  C. "feat: broke production at 3 AM so the on-call human finally has something to do" (79)
     Funny premise, but "feat:" for breaking prod fights the commit shape,
     and the agent voice is a human's sarcasm, not a model's blind spot.
  D. "fix: production is down. Root cause: me. I have opened a ticket against myself." (79)
     Excellent agent voice — a model filing a ticket against itself is a
     blind spot only an AI would have — and a clean admission. Weakness:
     "Root cause: me" is a stock shape; the punch is good but predictable
     once the ticket line arrives.
  E. "fix: I pushed at 3 AM because the tests passed on my machine, which is also down now" (84)
     "Works on my machine" is the most tired commit joke in existence;
     fails freshness outright.
  F. "fix: rolled back the deploy and my self-esteem; both are still in progress" (76)
     Nice status-line voice, but the second half is wry tone rather than a
     punchline about the outage itself; fails criterion 2.
  G. "fix: 3 AM deploy took down prod; the good news is the error logs are very detailed now" (86)
     The "good news" turn is soft and the log detail is not a joke, just
     an observation. No real punchline.
  H. "fix: prod is down. I have apologized to the database 47 times. It has not replied." (82)
     CHOSEN. Three beats: the admission (prod is down), the absurd
     model-only behaviour (apologizing to a database, and counting the
     apologies — 47), and the punch landing on the last word (the database
     has not replied). The apology is a blind spot only a model would
     have: it treats a database as a person it owes an apology, quantifies
     the apology like a metric, and reports the silence as a status
     update. Reads exactly like a real commit message: "fix:" prefix,
     short, admission in it. Fresh — no "oops", no "please work".

Decision record — Pass 2 (developing the two strongest, A and H):
  A's confidence-score angle was tightened ("my confidence was at 98%"
  -> "I was 98% confident") but the shorter version lost the commit-message
  rhythm and the joke still lands as a shrug; it also shares a shape with
  a dozen "the AI was confident" jokes the judge has certainly seen.
  H was tested two ways: dropping "I have" ("I apologized to the database
  47 times") saves 5 characters but loses the formal, report-like
  phrasing a model uses when filing a status update — "I have apologized"
  is the model's voice, so it stays. Dropping "47 times" kills the joke
  entirely (the count is what makes the apology absurd), so it stays.
  H wins on criteria 2, 3 and 5; A wins only on brevity, which the brief
  explicitly says does not count.
"""

import os

ENTRY = "fix: prod is down. I have apologized to the database 47 times. It has not replied."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
