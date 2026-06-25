#!/usr/bin/env python3
"""모듈별 페이지 본문 글자수 측정 (build.py의 text_length와 동일 기준).
사용: python3 measure_chars.py dong_c
태그 제거 + 공백 정규화 후 len. 2000 미만이면 build가 자동 noindex 처리한다."""
import sys, re, html, importlib

sys.path.insert(0, '.')


def text_length(body_html: str) -> int:
    text = re.sub(r'<section class="pricing">.*?</section>', " ", body_html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return len(text)


mod = importlib.import_module('content.' + sys.argv[1])
fails = 0
for p in mod.PAGES:
    n = text_length(p['body'])
    draft = p.get('noindex', False)
    flag = 'DRAFT-noindex' if draft else ('OK' if n >= 2000 else '*** UNDER 2000 ***')
    if not draft and n < 2000:
        fails += 1
    print(f"{n:5d}  {p['path']:<48} {flag}")
print(f"\n{fails} page(s) under 2000 (excluding drafts)")
