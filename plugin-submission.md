# No AI Slop Türkçe plugin submission

## Positioning

No AI Slop Türkçe is the Turkish-specific fork of [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop). It preserves the upstream plugin architecture while separating the Turkish package and skill identity.

## Scope

- Plugin/package name: `no-ai-slop-turkish`
- Skill name and command: `no-ai-slop-tr` / `/no-ai-slop-tr`
- Language scope: predominantly Turkish writing only
- Upstream structure, packaging, and release flow stay parallel where practical

The Turkish-specific slop taxonomy and full eval rewrite are intentionally out of scope for this foundation change.

## Directory publication gate

Version `0.1.0` is a foundation release and should not be submitted to the public plugin directory yet. Submit only after the Turkish-specific slop taxonomy, examples, and corresponding eval coverage have landed.

A successful `scripts/build_plugin.py` run validates this repository's package contract and selected directory constraints; it is not a substitute for the platform's final submission validation.

## Starter prompts

1. @No AI Slop Türkçe (metin)
2. @No AI Slop Türkçe bu metinde AI slop var mı? (metin)

## Negative test cases

1. Given a predominantly English draft, do not run edit or detect mode. Briefly state that the skill is scoped to Turkish text and leave the draft unchanged.
2. Do not translate non-Turkish input unless the user explicitly asks for translation.

## Release notes

Version 0.1.0 establishes the independent Turkish plugin identity, renames the skill to `no-ai-slop-tr`, updates package/build paths, and points metadata to the Turkish fork. It is not intended for public directory submission until the Turkish taxonomy and eval coverage are complete.
