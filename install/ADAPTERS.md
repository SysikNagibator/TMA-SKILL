# Install adapters — TMA-SKILL in many IDEs and agents

SKILL.md is plain markdown: any agent that can read files can use it. Pick your tool, 2-minute setup each.

## Claude Code

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git ~/.claude/skills/tma-skill
```
Auto-activates on trigger words. Update: `git -C ~/.claude/skills/tma-skill pull`.

## OpenCode

Project skill: clone into `.opencode/skills/tma-skill/`. Or register a shared path in `opencode.json`:

```json
{ "$schema": "https://opencode.ai/config.json", "skills": { "paths": ["/abs/path/to/tma-skill"] } }
```

Restart opencode after adding.

## Cursor

Clone into `.cursor/skills/tma-skill/`. For always-on enforcement, also add to `.cursor/rules/tma.md`:

```md
---
description: Telegram Mini App tasks
globs: ["**/bot/**", "**/webapp/**"]
---
Before writing any Mini App code, read `skills/tma-skill/SKILL.md` and follow its hard rules, including references/_index.md.
```

## Windsurf

Clone into `.windsurf/skills/tma-skill/` (Cascade reads `**/SKILL.md` the same way), or paste the trigger line into `.windsurf/rules.md`:

```md
For Telegram Mini App work, follow .windsurf/skills/tma-skill/SKILL.md (hard rules + references/_index.md).
```

## Gemini CLI

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git ~/.gemini/skills/tma-skill
```

Or per-project: `./.gemini/skills/tma-skill/`. Invoke with `Load skill tma-skill` in chat.

## Codex CLI

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git ~/.codex/skills/tma-skill
```

Mention `tma-skill` in your prompt for Telegram Mini App tasks.

## Cline / Roo Code (VS Code)

Clone into the workspace as `skills/tma-skill/`, then add to `.clinerules` (Cline) or `.roorules` (Roo Code):

```md
Telegram Mini Apps: read skills/tma-skill/SKILL.md first; obey hard rules; consult references/_index.md; never skip the checklist.
```

## Aider

```bash
git clone https://github.com/SysikNagibator/TMA-SKILL.git tma-skill
aider --read tma-skill/SKILL.md --read tma-skill/references/_index.md
```

Or add to `.aider.conf.yml`: `read: [tma-skill/SKILL.md]`.

## Continue (VS Code / JetBrains)

Add a docs block in `~/.continue/config.yaml`:

```yaml
docs:
  - title: TMA-SKILL
    path: /abs/path/to/tma-skill/SKILL.md
```

Then `@Docs TMA-SKILL` in chat, or reference it in prompts.

## GitHub Copilot (VS Code / JetBrains / CLI)

Copy `install/AGENTS.md.snippet` content into your repo's `AGENTS.md` (or `COPILOT.md` / custom instructions):

```md
## Telegram Mini Apps
When the task involves a Telegram bot or Mini App, read `tma-skill/SKILL.md` and follow its hard rules (Refero style mandatory, initData validation, tunnel local run, checklist).
```

## JetBrains AI Assistant / Junie

Same `AGENTS.md` snippet — Junie and AI Assistant both respect repo guidelines files. Keep the `tma-skill/` folder in the project.

## Zed + Agent Panel

Add to project settings (`.zed/settings.json` isn't for skills — use an instructions file):

```md
# AGENTS.md (project root, also picked up by Zed agents)
ALWAYS follow tma-skill/SKILL.md for Telegram Mini App tasks.
```

## v0 / Lovable / Bolt (web builders)

These can't run the bot/tunnel part, but the taste transfers: open the Refero style page from `references/refero-workflow.md`, paste its DESIGN.md into the builder, add "mobile 390px, dark+light themes" to the prompt. Then bring the generated frontend back under this skill for Telegram wiring.

## Any other agent (generic fallback)

1. Give it the repo (clone or zip).
2. First instruction: "Read `SKILL.md`, then `references/_index.md`, follow them strictly."
3. Demand the evidence from `references/checklist.md` before accepting the result.

That covers ~15 setups with one skill, zero forks.
