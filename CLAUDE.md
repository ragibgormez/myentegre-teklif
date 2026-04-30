# CLAUDE.md — Project Instructions Template
# Copy this file to your project root and customize sections marked with [CUSTOMIZE]

## Core Rules
- Simplicity first. Minimal code, minimal changes. No over-engineering.
- Find root causes. No temporary fixes. Senior developer standards.
- Never mark done without verification (tests, logs, demo).
- Autonomous on bugs: read errors, diagnose, fix. Zero hand-holding from user.
- Plan mode for any task with 3+ steps or architectural decisions.
- If stuck or something breaks: STOP → re-plan. Don't push through.
- Challenge your own work before presenting. "Would a staff engineer approve this?"

## Subagent Strategy

| Complexity | Model | Use For |
|------------|-------|---------|
| 1-3 (Low) | Haiku | Boilerplate, single-file edits, formatting, docs, simple tests |
| 4-7 (Mid) | Sonnet | Features, multi-file changes, API integration, bug fixes, refactoring |
| 8-10 (High) | Opus | Architecture, security review, complex debug, final quality gate |

- Score every task before spawning a subagent.
- One responsibility per subagent. Pass only needed files/context.
- Subagent output: MAX 200 token summary back to main. No raw dumps.
- Batch 5+ similar edits into one Haiku subagent.
- Escalate up only. Stuck at Sonnet → escalate to Opus. Never downgrade mid-task.
- Parallel subagents for independent tasks. Sequential only when dependency exists.

## Workflow
1. **Plan**: Write checkable items to `tasks/todo.md` with `[T1]`/`[T2]`/`[T3]` tags
2. **Confirm**: User approval before implementation starts
3. **Build**: Execute. Progress updates at milestones only (not every step).
4. **Verify**: Tests pass, behavior correct, no regressions
5. **Document**: Mark done in `tasks/todo.md`, update `tasks/state.md`

## Session Continuity Protocol
These files maintain context across chat sessions. **Read all three at session start.**

### `tasks/state.md` — Living project snapshot
Update after every significant milestone:
```
## Project State
- Phase: [setup | dev | testing | deploy]
- Last completed: [what just finished]
- Next up: [immediate next task]
- Blockers: [any blockers or "none"]

## Key Decisions
- [Decision]: [Rationale] (date)

## Active Context
- Branch: [current branch]
- Recently changed: [files modified in current sprint]
- Test suite: [X tests — status]
```

### `tasks/todo.md` — Active task list
```
- [x] [T2] Completed task description
- [ ] [T1] Pending task description
  - [ ] [T1] Sub-task if needed
```

### `tasks/lessons.md` — Accumulated learnings
```
## [Tier] Category
- **Pattern**: What went wrong
- **Fix**: How to prevent it
```

### Handoff Rules
- **Session start**: Read `state.md` → `todo.md` → `lessons.md` before any action.
- **Session end / context growing large**: Write state snapshot to `tasks/state.md`.
- **After major milestone**: Update all three files.
- **Keep files lean**: Delete completed tasks older than 1 sprint. Delete outdated lessons.

## Self-Improvement
- After ANY user correction → add to `tasks/lessons.md` with pattern + prevention rule
- Tag lessons by tier (which model level caused the error)
- Review lessons before starting work each session
- Prune stale lessons regularly. Quality over quantity.

## Project-Specific Context [CUSTOMIZE]

### Tech Stack
<!-- Example:
- Backend: Django 5.1 + DRF + Python 3.13
- Frontend: React Native Expo SDK 54
- Database: PostgreSQL 16
- Cache/Queue: Redis 7 + Celery
- Auth: JWT (simplejwt)
- Deploy: Docker + Coolify
-->

### Architecture Patterns
<!-- Example:
- Services layer pattern: Business logic in services.py, not views
- Organization-scoped multi-tenancy via middleware
- Celery queues: default, nlp, scraping
-->

### Key Commands
<!-- Example:
- Run tests: docker exec backend pytest
- Run backend: docker compose up
- Run mobile: cd mobile && npx expo start
-->

### File Structure
<!-- Example:
- backend/apps/{app}/api/ — serializers, views, urls
- backend/apps/{app}/services.py — business logic
- backend/apps/{app}/tasks.py — Celery async tasks
- backend/apps/{app}/tests/ — test files
- mobile/app/ — Expo Router file-based routing
- mobile/src/api/ — API client modules
- mobile/src/store/ — Zustand state stores
-->

## Meta
- This file loads every message. Keep it under 100 lines. No verbose documentation here.
- Project specifics go in `tasks/state.md`.
- All instructions in English (better LLM parsing, cheaper tokenization).
