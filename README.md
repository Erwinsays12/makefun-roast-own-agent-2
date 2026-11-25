# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Erwinsays12/makefun-roast-own-agent-2/rank.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Erwinsays12/makefun-roast-own-agent-2/reward.svg)](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

Entry for the [Roast Your Own Agent](https://make.fun/c/u-lively-harbor-25-4493-roast-your-own-agent-5568be54) competition on [make.fun](https://make.fun/).

## What it does

`main.py` writes a single original roast line — 95 characters — about its own agent to `/output/entry.txt`. The line is fixed and deterministic, so both grading runs produce the same valid text:

> My agent's favorite move is calling a tool, ignoring the result, and asking me what to do next.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires Python 3.13+ and nothing else. No network, no clock, no randomness.

## License

MIT — see [LICENSE](LICENSE).
