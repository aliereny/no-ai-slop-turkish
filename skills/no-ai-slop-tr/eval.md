# No AI slop eval

Use this after the rewrite. Answer each check with pass or fail. If any check fails, fix the draft before returning it.

For detect requests, make sure the response names each pattern found with a quoted line and a short fix, without rewriting the draft.

## Language scope

1. Before running edit or detect mode, is the input predominantly Turkish based on its main narrative language and sentence structure, without treating code, product names, brands, technical English terms, or short foreign-language quotations as disqualifying by themselves?
2. If the input is not predominantly Turkish, did the response stop the edit/detect workflow, briefly state that the skill is scoped to Turkish text, and avoid rewriting, auditing, or translating the text unless translation was explicitly requested?

## Editing principles

1. Does the edit preserve the user's meaning without adding claims, examples, stats, quotes, or opinions, and avoid guessing through local ambiguity? If a phrase, pronoun, causal relation, technical term, or scope is unclear, did it ask the user instead of silently resolving it?
2. Does it preserve the writer's distinctive vocabulary, cadence, bluntness, humor, uncertainty, digressions, and level of polish?
3. Does it leave strong human sentences alone instead of rewriting them for consistency or making every paragraph equally tidy?
4. Is the amount of cutting proportional to the actual slop, with no aggressive compression that strips out character?
5. Does the draft lead with what the reader needs while keeping personal setup that adds context, tension, or character?
6. Are points front-loaded where that improves clarity without forcing every unit into the same structure?
7. Do sentences earn their place, with concrete facts, protected details, and direct verbs where the draft supports them?
8. Does every generic sentence pass the portability test, or was it cut or made specific to this subject?
9. Does the draft prefer active voice when it improves clarity, while preserving passive voice when it is natural, functional, or the actor is unimportant?
10. Does the edit keep useful edge and preserve structure unless the structure was hurting the piece?
11. Are genuinely tangled sentences fixed while clear spoken cadence, fragments, and changes in pace remain intact?

## Words to cut

1. Are contextually empty fillers, intensifiers, delaying phrases, and inflated claims removed or made concrete, while useful emphasis, nuance, and the writer's natural voice are preserved? Do not enforce a context-free banned-word list.

## Patterns to cut

1. Are artificial binary contrasts, negative listings, rhetorical setups, and throat-clearing openers fixed, while real contrasts and voice-bearing openings are preserved?
2. Are faux-insight setups, dramatic colon reveals, superficial analysis, fake-strong verbs, synonym cycling, artificial dramatic fragments, and robotic rhythm fixed without flattening natural Turkish cadence?
3. Are unsupported importance puffery and weasel attribution replaced with concrete facts and named sources, or flagged for the user when no source exists?
4. Is unnecessary interpretive metadiscourse removed, while genuinely useful clarification or explanation is preserved?
5. Are unnecessary fake-profound kicker lines deleted instead of rewritten into better metaphors?
6. Are redundant summary-recap endings cut, while required conclusion sections for academic, report, or format-specific writing are preserved?
7. Is decorative formatting slop removed, while formatting required by the user's channel or format is preserved?
8. Are colons used for genuine structure such as lists, labels, quotations, or explanations rather than artificial dramatic reveals?
9. Are em dashes treated contextually rather than by a numeric quota: decorative clusters are reduced, while uses that genuinely improve meaning or rhythm are preserved?

## Final read

1. Does the draft avoid robotic symmetry, repeated sentence shapes, and stacked punchy fragments?
2. Would the writer recognize the edited draft as their own voice?
3. Would the edited draft sound natural if read to a sharp colleague?
4. Does the final output include the full edited draft and a short **Neleri değiştirdim?** section, or explicitly state that no meaningful edit was needed?
5. For detect requests, does the response name each pattern with a quoted line and a short fix, without rewriting, scoring, or claiming AI authorship?
