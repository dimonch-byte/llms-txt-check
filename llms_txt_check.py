#!/usr/bin/env python3
"""llms-txt-check: does your own site serve a spec-shaped /llms.txt (llmstxt.org)? stdlib only. Shape check, not a ranking tool."""
import sys, re, urllib.request, urllib.parse
def main():
    base=sys.argv[1].rstrip("/"); u=urllib.parse.urljoin(base+"/","/llms.txt"); probs=[]
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"llms-txt-check/1.0"}),timeout=20)
        body=r.read(500_000).decode("utf-8","replace"); ct=r.headers.get("content-type","")
    except Exception as e:
        print(f"FAIL {u}: {e}"); body=None
    if body is not None:
        lines=body.splitlines()
        if "html" in ct or body.lstrip().lower().startswith("<!doctype"): probs.append("served as HTML (probably your SPA fallback, not a real file)")
        if not lines or not lines[0].startswith("# "): probs.append("first line should be '# Site name' (H1)")
        if not any(l.startswith("> ") for l in lines[:6]): probs.append("no '> one-line summary' blockquote near the top")
        if not any(l.startswith("## ") for l in lines): probs.append("no '## Section' headings with file lists")
        links=re.findall(r"^- \[[^\]]+\]\(([^)]+)\)",body,re.M)
        if not links: probs.append("no '- [Title](url): note' link lines")
        print(f"{u}: {len(lines)} lines, {len(links)} links")
    else: probs.append("no /llms.txt")
    for p in probs: print("FAIL", p)
    if not probs: print("PASS: spec-shaped llms.txt")
    else: print("\nShape check only; no file guarantees AI citations or rankings. Free full check (llms.txt + FAQ/Organization JSON-LD): https://citekit.adjudi.com/?utm_source=github&utm_medium=cli&utm_campaign=citekit-intent-w2&utm_content=llms-txt-check")
    sys.exit(1 if probs and "--fail" in sys.argv else 0)
if __name__=="__main__": main()
