#!/usr/bin/env python3
"""사이트맵 핑 — 검색엔진에 sitemap.xml 갱신을 알린다.

주의(2026 기준): 구글·빙의 sitemap ping(GET ping?sitemap=) 엔드포인트는 공식 폐지되었다.
가장 빠른 색인 경로는 (1) Search Console·서치어드바이저에 sitemap 등록,
(2) IndexNow(tools/indexnow.py) 즉시 통보다. 이 스크립트는 보조용이며,
폐지된 엔드포인트는 자동으로 건너뛴다.

사용법: python3 tools/ping_sitemap.py
"""
import urllib.parse
import urllib.request

SITEMAP = "https://incheon-home-massage.pages.dev/sitemap.xml"

# 현재 유효성이 낮거나 폐지된 엔드포인트(보조 목적). 실패는 무해.
TARGETS = [
    # 구글: 2023년 ping 폐지 → Search Console 등록 권장
    # 빙: ping 폐지 → IndexNow 권장
    "https://webmaster.yandex.com/ping?sitemap={s}",
]


def main():
    print("권장: Search Console·네이버 서치어드바이저에 sitemap 등록 + IndexNow 통보")
    for t in TARGETS:
        url = t.format(s=urllib.parse.quote(SITEMAP, safe=""))
        try:
            with urllib.request.urlopen(url, timeout=20) as r:
                print(f"  [{r.status}] {url}")
        except Exception as e:  # noqa: BLE001
            print(f"  [skip] {url} ({e})")


if __name__ == "__main__":
    main()
