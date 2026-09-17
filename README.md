# Fray Labs Outcomes

Public, reusable AI Outcomes published by Fray Labs for [Possible](https://possible.sh).

Each folder contains:

- `outcome.md` — what was made and the original request;
- `prompt.md` — the exact reusable execution prompt; and
- `outcome.json` — provenance, models, Products, Skills, requirements, and file metadata.

The root [`outcomes.json`](./outcomes.json) is the machine-readable publisher index. Possible reads this repository directly; the canonical source remains here.

## Use with Possible

Use CLI 0.3.1 or newer for the current primary Product/Skill manifests:

```shell
npx @fraylabs/possible@0.3.1 add fraylabs/possible-outcomes
npx @fraylabs/possible@0.3.1 use fraylabs/possible-outcomes@digital-photo-frame
```

The `use` command prints the reusable prompt. Review it before giving it to an agent.

## License

Code and text are available under the MIT License. Referenced third-party Products and Skills retain their respective ownership and licenses.
