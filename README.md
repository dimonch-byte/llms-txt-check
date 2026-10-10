# llms-txt-check
`python3 llms_txt_check.py https://your-site.com [--fail]` fetches `/llms.txt` from **your** site and checks the [llmstxt.org](https://llmstxt.org) shape: H1 title, `>` summary, `##` sections, `- [Title](url)` link lines, and that it isn't your SPA's HTML fallback. stdlib only.

It checks shape, nothing more. No file guarantees that AI tools will cite or rank you.

*Disclosure: I build [CiteKit](https://citekit.adjudi.com/?utm_source=github&utm_medium=readme&utm_campaign=citekit-intent-w2&utm_content=llms-txt-check) ($19), which generates llms.txt plus FAQ/Organization JSON-LD from your pages. This script is free (MIT).*
