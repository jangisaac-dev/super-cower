# Installing `super-cower`

## 1. Clone the repository

Clone this repository anywhere you want to keep as the source of truth for the
skill.

## 2. Link it into Codex skill discovery

From the repository root:

```bash
mkdir -p ~/.agents/skills
rm -f ~/.agents/skills/super-cower
ln -s "$PWD" ~/.agents/skills/super-cower
```

If you prefer not to use `rm -f`, manually remove the old symlink or directory
first.

## 3. Ensure multi-agent support is enabled

Check `~/.codex/config.toml` and make sure it includes:

```toml
[features]
multi_agent = true
```

## 4. Add one routing line to your global `AGENTS.md`

Append this snippet to `~/.codex/AGENTS.md`:

```markdown
## Super Cower Routing
- For general software-development work, prefer `super-cower`. If the user explicitly requests a different workflow or says not to use TDD or subagents, follow the user.
```

## 5. Restart Codex

Restart Codex so the skill is re-discovered.

## Verify

```bash
ls -la ~/.agents/skills/super-cower
python3 scripts/validate_skills.py
```

The first command should show a symlink pointing at this repository. The second
command should report that the skill package is valid.
