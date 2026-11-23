# AGENTS.md: Mailroom

Everything an AI coding agent needs to know before touching this project.

## What this project is

**Mailroom** is a small project written in Python. What it will do is still undecided: the
owner has not chosen yet, so agents must not assume a purpose.

It is also a **learning project**. The owner is learning programming fundamentals by building
it, following the book *The AI Agent Factory*, Chapter 13 "Programming Fundamentals":
https://agentfactory.panaversity.org/building-ai-workers/programming-fundamentals/overview/

The point is the learner's understanding, not speed. A working program the learner cannot read
is a failure.

## Learner progress (update this as lessons are covered)

**Covered so far: Chapter 13, lessons 13.1 to 13.7, plus the first parts of 13.8 and 13.11
that the learner has already used in this project (listed below).**

| Lesson | Concepts the learner knows |
|---|---|
| 13.1 | values, strings, lists, indexing from 0, variables, `print()` |
| 13.2 | `uv run python`, type labels, Pyright strict, git basics, reading a Traceback |
| 13.3 | `str`, `int`, `float`, `bool`, `None`, `int()` conversion, money as whole cents, `ValueError` |
| 13.4 | `if` / `else`, `==`, `>`, `>=`, `<`, `<=`, `for` loops, filtering in a loop, list comprehension |
| 13.5 | `and`, `or`, `not`, `x = x or "default"`, empty values are false, `while`, `+=` |
| 13.6 | `def`, typed parameters, `return`, `-> type`, pure functions, `assert` with a message |
| 13.7 | lists, `len()`, dictionaries, `d["key"]`, `.get(key, default)`, dicts as records, `KeyError`, sorting with `key=`, `lambda`, `reverse=True` |
| 13.8 (started) | `open("path")`, `file.read()`, `file.close()`, a file path relative to the project folder, `open` gives a connection (`file`) and `.read()` gives the contents (`text: str`), line breaks are `\n` characters stored in the file, `.splitlines()` |
| 13.11 (started) | tests first: write the test, watch it fail, then write the code; `from mailroom import name`; each test keeps the output (`actual`) apart from the expected behaviour (`expected`) and compares them with `assert`; functions live in `mailroom.py`, checks live in `test.py` |
| Learned along the way | defining a function vs calling it; indented lines under `def` run only when the function is called, and not at all after `return`; a parameter is a blank, the argument fills it; `return` hands a value back and `print` only shows it; `-> None` means nothing is returned; `"a" in line` checks whether one string is inside another; `NameError`; `RecursionError` (a function calling itself forever) |

**Not yet covered (still new to the learner):** dates (13.9), reading error messages in depth
(13.10), the rest of the tests-first / TDG loop (13.11), judgment (13.12), and everything in
later chapters: classes, `try` / `except`, f-strings, `with open(...)`,
`if __name__ == "__main__":`, type aliases, and anything else not in the table above.

## Hard rules for agents

1. **Stay inside the covered concepts.** Write code using only what is in the table above.
2. **Teach before you use anything new.** If a task seems to need a concept that is not covered,
   stop. Explain the concept first in plain language with a tiny example, wait for the learner to
   say they understand, and only then use it. Prefer a covered alternative when one exists.
3. **Follow PRIMM-AI+ (below) for every new piece of code.** Do not hand over finished code the
   learner has not predicted first.
4. **Small steps.** One new idea per step. Keep programs short and readable.
5. **Type labels everywhere.** Every variable that is not obvious, every function parameter, and
   every return value gets a type label. The project must stay clean under Pyright strict.
6. **No clever code.** Prefer the plain version over the short one. No one-line tricks.
7. **Do not rewrite the learner's own code** unless asked. Suggest, explain, let them edit.
8. When a lesson is finished, update the progress table above.

## PRIMM-AI+ (how we learn)

Five steps. The agent is a partner at every step, and nothing it says is accepted without a check.

| Step | Learner does | Agent does |
|---|---|---|
| **P**redict | Writes down what the code will do **before** running it | Stays quiet |
| **R**un | Runs it and sees the real output | Runs it, with permission |
| **I**nvestigate | Compares guess vs. output and asks why | Explains a line when asked |
| **M**odify | Changes one thing, predicts again, runs again | Makes the edit the learner describes |
| **M**ake | Writes their own version as a specification | Builds against the spec; learner verifies |

Operating rule: **predict before you run, every time.** Predict, Run and Investigate build
reading skill. Modify and Make are where the learner starts directing the agent.

When presenting code, always start with a **Predict** question ("What will this print?") and stop
there until the learner answers.

## Tech and commands

- Python: latest 3.14.x (pinned in `.python-version`, currently 3.14.10)
- Package and environment manager: **uv**. No `pip`, no manual venvs.
- Type checker: **Pyright**, strict mode (configured in `pyproject.toml`)
- No runtime dependencies yet. Keep it that way until the learner asks.

```powershell
uv run python main.py     # run the program
uv run pyright            # type check (must report 0 errors)
uv add <package>          # add a dependency (ask the learner first)
git status                # always look before committing
```

## Project layout

```
MailRoom/
  AGENTS.md        this file
  main.py          the program (single file for now; modules come in Chapter 14)
  pyproject.toml   project metadata, dev tools, Pyright config
  .python-version  pinned Python version
  uv.lock          locked dependency versions (committed)
```

## Git and GitHub

- Repo: `Mailroom` on the owner's GitHub account (public).
- Commit small, with a plain message saying what changed and why.
- Run `uv run pyright` before every commit.
- Never commit `.venv/`.
