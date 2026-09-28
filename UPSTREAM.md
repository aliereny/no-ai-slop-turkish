# Upstream relationship

This repository is a Turkish-specific fork of [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop).

## Current baseline

- Upstream repository: `petergyang/no-ai-slop`
- Baseline commit: `000650b156983f5159695b441477f4e63b25dc85`
- Fork repository: `aliereny/no-ai-slop-turkish`

## Parallelism contract

1. Keep the high-level upstream repository layout, plugin packaging flow, and release workflow parallel where practical.
2. Use `no-ai-slop-turkish` as the plugin/package identity.
3. Use `no-ai-slop-tr` as the skill identity and `/no-ai-slop-tr` as the user-facing command.
4. Scope the skill to predominantly Turkish writing. Non-Turkish input should not run the edit/detect workflow.
5. Port future upstream behavior changes semantically rather than overwriting Turkish-specific rules.
6. Preserve the upstream MIT license and attribution.

The Turkish slop taxonomy, examples, and eval criteria are maintained as language-specific content and may intentionally diverge from upstream.
