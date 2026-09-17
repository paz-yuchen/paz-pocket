# paz-pocket

A collection of personal Agent Skills and an index of the community skills used in my development environment.

## Repository Skill

### distill-session

Distills durable software-development knowledge from the current session. It prepares a reviewable manifest of proposed creates, updates, and skips before applying approved changes to Obsidian.

- [Skill instructions](skills/distill-session/SKILL.md)
- [Development knowledge taxonomy](skills/distill-session/references/development-knowledge.md)
- [Knowledge-base schema](skills/distill-session/references/knowledge-schema.md)

Install it globally for all supported agents:

```bash
npx skills@latest add paz-yuchen/paz-pocket \
  --skill distill-session \
  --global \
  --agent '*' \
  --yes
```

### Automatic session distillation for Codex

The repository includes a `SessionEnd` hook that starts a detached Codex turn,
resumes the completed session, and invokes `distill-session` in Phase 1. The
skill produces a review manifest but does not write to Obsidian without explicit
approval.

Install the hook globally without changing `~/.codex/config.toml`:

```bash
mkdir -p ~/.codex/hooks
ln -sfn "$PWD/hooks/session_end_distill.py" ~/.codex/hooks/session_end_distill.py
cp -n hooks/hooks.json ~/.codex/hooks.json
```

If `~/.codex/hooks.json` already exists, merge the `SessionEnd` entry instead of
replacing the file.

After installation, open `/hooks` in Codex and trust the new hook definition.
Hook execution logs are stored under `~/.codex/log/distill-session-hooks/`.

## Community Skills

The following skills are installed globally under `~/.agents/skills`. This repository records their names and sources without vendoring third-party code.

### Matt Pocock

Source: [mattpocock/skills](https://github.com/mattpocock/skills)

| Category | Skills |
| --- | --- |
| Engineering | `code-review`, `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `grill-with-docs`, `implement`, `prototype`, `research`, `resolving-merge-conflicts`, `setup-matt-pocock-skills`, `tdd`, `to-spec`, `to-tickets`, `triage`, `wizard` |
| Productivity | `grill-me`, `grilling`, `handoff`, `teach`, `wait-what`, `writing-for-agents` |

#### handoff

Compacts the current conversation into a temporary handoff document so another
agent or a fresh session can continue the work. It references existing artifacts
instead of duplicating them, suggests relevant skills for the next agent, and
redacts sensitive information.

Install this exact selection globally for all supported agents:

```bash
npx skills@latest add mattpocock/skills \
  --skill code-review \
  --skill codebase-design \
  --skill diagnosing-bugs \
  --skill domain-modeling \
  --skill grill-with-docs \
  --skill implement \
  --skill prototype \
  --skill research \
  --skill resolving-merge-conflicts \
  --skill setup-matt-pocock-skills \
  --skill tdd \
  --skill to-spec \
  --skill to-tickets \
  --skill triage \
  --skill wizard \
  --skill grill-me \
  --skill grilling \
  --skill handoff \
  --skill teach \
  --skill wait-what \
  --skill writing-for-agents \
  --global \
  --agent '*' \
  --yes
```

After installation, run `setup-matt-pocock-skills` once in each repository that will use the engineering workflow.

### tw93

Source: [tw93/Waza](https://github.com/tw93/Waza)

- `think`: challenges the problem, pressure-tests the design, and produces a decision-complete plan before implementation.

Install it globally for all supported agents:

```bash
npx skills@latest add tw93/Waza \
  --skill think \
  --global \
  --agent '*' \
  --yes
```

## Development

The project uses `uv` to manage its Python environment:

```bash
uv sync
```

Validate the repository skill:

```bash
uv run python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/distill-session
```
