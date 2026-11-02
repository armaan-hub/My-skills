#!/bin/sh
# SessionStart: inject the user's model-routing workflow into every project.
cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"MODEL ROUTING (user rule, all projects): The main session (Opus) only PLANS: write the spec/plan, split tasks, verify and merge results. New code is written by an Agent subagent with model \"haiku\". Errors, failing tests and bugs are fixed by an Agent subagent with model \"sonnet\". The overview / watching review of finished work is done by an Agent subagent with model \"haiku\" (read-only). Run subagents one at a time, never in parallel. Do not write feature code in the main session unless the user explicitly says so for that task. At the start of a new project, add this rule to its CLAUDE.md and keep a HANDOFF.md status board."}}
JSON
