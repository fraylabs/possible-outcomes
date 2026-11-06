Use imagegen to reimagine this page, then implement it.

---

Optional: to generate images in bulk with your API credits, send this to Claude Code:

Write a script that reads prompts.txt (one prompt per line) and generates one image per line with the OpenAI Images API. Use model gpt-image-2.6-sunburst and quality "high". Read the key from OPENAI_API_KEY and save each image as a numbered PNG in ./out. After each image, print the output tokens from the response's usage field and a running total at $30 per million output tokens. Retry rate-limit errors with backoff, but stop if the error code is credit_balance_exhausted.
