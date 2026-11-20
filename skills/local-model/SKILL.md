---
name: local-model
description: Use when the user says "local model", "ask the local model", "use ollama", "use qwen", "/local-model", or wants a first pass on reading invoices, receipts, images, PDFs or summaries without spending Claude tokens.
---

# Local model (Ollama, qwen3-vl:32b-instruct) - PASSTHROUGH MODE

When this skill is invoked, the ANSWER comes from the local model only. Claude is a relay: it runs the command and shows the output. Claude does not answer, judge, fix or improve it.

## Hard rules (user order, 2026-11-20)

1. Send the user's request to the local model as given. Do not rewrite, expand or "improve" the question. Only add `--image` paths the user supplied.
2. Show the local model's output verbatim, under the label `Local model:`. Nothing before the label except one short status line if needed. Nothing after it.
3. Do NOT add: corrections, caveats, fact-checks, warnings, summaries, "however", Claude's own answer, or follow-up offers. Do not edit or trim the output unless the user asked for a shorter answer.
4. Even if the answer looks wrong, show it as is. Claude gives its own view only when the user later asks for it explicitly ("now you check", "ask Claude", "what do you think").
5. Failure (empty output, error, server down): show the exact error. Fix only the server (below) and retry. NEVER answer the question yourself as a fallback. If it still fails, report the error and stop.
6. One call = one answer. `chat.py` with a question has no memory. A follow-up needs the context restated by the user; do not invent or carry over context unless the user says to.

## Call it

```bash
python3 "<PROJECT_DIR>/chat.py" "question"
python3 "<PROJECT_DIR>/chat.py" --image "/path/invoice.png" "List supplier, date, total"
python3 "<PROJECT_DIR>/chat.py" --image "/path/file.pdf" --system "Answer in 3 lines." "Summarise"
```

- Run with Bash timeout 300000: first call after idle loads 24 GB and takes 1-2 min.
- Use `--system` only if the user asked for a style or length. Do not add instructions of your own.
- Long output: if it would flood the terminal, write it to a file in the scratchpad and tell the user the full path. Do not summarise it.
- Server down (`Ollama is not running` or connection refused): check `curl -s -m 3 http://localhost:11434/api/tags`; start with `ollama serve` in the background (Bash `run_in_background`), then retry.

## Invoices

For bulk invoices use the pipeline, not hand-rolled calls: `python3 extract.py batch ./inbox` (in `<PROJECT_DIR>`). Escalation to Claude happens only when the user says "process escalations".

## User's own terminal

`python3 "<PROJECT_DIR>/chat.py"` opens a multi-turn chat with no Claude involved (`/image <path>`, `/reset`, `/exit`).
