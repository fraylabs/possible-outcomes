# Fray Labs Outcomes

Public, reusable AI Outcomes and the recipes behind them, published by Fray Labs for [Possible](https://possible.sh).

Each folder contains:

- `outcome.md` — what was made and the original request;
- `prompt.md` — the recorded reusable execution prompt; and
- `outcome.json` — provenance, models, Products, Skills, requirements, file metadata, and an optional recipe.

A recipe collects the recorded agent, pinned skills, references, tools and ordered steps that help another agent reproduce or adapt the result. Unknown details are omitted. Fray-authored backfills explicitly label steps reconstructed from published prompts and artifacts; they are not transcripts of historical agent turns. Existing model provenance, prompts, result limitations and creator credits remain intact. Curated third-party demos retain their disclosed prompts without an invented workflow.

The root [`outcomes.json`](./outcomes.json) is the machine-readable publisher index. Possible reads this repository directly; the canonical source remains here.

## Use with Possible

Use CLI 0.4.0 or newer for manifests containing the optional `recipe` field. The older primary Product/Skill parsing issue in CLI 0.3.0 was fixed in 0.3.1; recipe support is a separate addition.

```shell
npx @fraylabs/possible@0.4.0 add fraylabs/possible-outcomes
npx @fraylabs/possible@0.4.0 use fraylabs/possible-outcomes@digital-photo-frame
```

The `use` command provides the reusable instructions for an agent. Review the recipe, original prompt and stated limits before running it; access to referenced tools and services is still required.

## Opus 5.5 demos

[See ten creator demos and copy their prompts](OPUS-DEMOS.md): neon cities, mini golf, a cursor-following pet, a rocket launch, an interactive robot hand, fluid simulation, a Rube Goldberg machine, a sunset pirate ship, motion design and an explorable pagoda. Each links the original creator and records creator-reported model provenance.

## License

Fray-authored code and text are available under the MIT License. Curated creator prompts and demo media retain their original ownership and are excluded from that grant; see linked sources and each media/NOTICE.md. Referenced third-party Products and Skills retain their respective ownership and licenses.
