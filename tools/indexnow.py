#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스 등 IndexNow 참여 엔진에 URL을 통보한다.

사용법:
  python3 tools/indexnow.py                 # tools/urls.txt 의 모든 URL 통보(첫 일괄 통보)
  python3 tools/indexnow.py https://incheon-home-massage.pages.dev/yeonsu-gu/songdo/ ...
                                            # 특정 URL만 통보(글 올릴 때마다)

동작:
  - api.indexnow.org 공용 엔드포인트로 1회 제출하면 참여 엔진에 전파된다.
  - 네이버(searchadvisor)·빙에도 직접 제출을 추가로 시도한다(중복 통보는 무해).
  - 키는 사이트 루트의 <키>.txt 로 게시되어 있어 소유 확인이 자동 처리된다.

주의: 실제 네트워크 통보이므로 배포(빌드 결과 푸시)가 끝난 뒤 실행하세요.
"""
import json
import os
import sys
import urllib.request

# ── 설정 (사이트에 맞게 자동 로드) ─────────────────────────
HOST = "incheon-home-massage.pages.dev"
KEY = "246497306624e87a1aad9965d295f98c"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",       # 공용(참여 엔진 전파)
    "https://www.bing.com/indexnow",            # 빙
    "https://searchadvisor.naver.com/indexnow",  # 네이버
]

HERE = os.path.dirname(os.path.abspath(__file__))


def load_urls(args):
    if args:
        return [u.strip() for u in args if u.strip()]
    path = os.path.join(HERE, "urls.txt")
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def submit(endpoint, urls):
    payload = json.dumps({
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read(200).decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, e.read(200).decode("utf-8", "ignore")
    except Exception as e:  # noqa: BLE001
        return None, str(e)


def main():
    urls = load_urls(sys.argv[1:])
    if not urls:
        print("통보할 URL이 없습니다. 먼저 python3 build.py 를 실행하세요.")
        return
    # IndexNow 1회 제출 한도 10,000개 — 청크 분할
    chunks = [urls[i:i + 10000] for i in range(0, len(urls), 10000)]
    print(f"통보 대상 {len(urls)}개 URL, 엔드포인트 {len(ENDPOINTS)}개")
    for ep in ENDPOINTS:
        for ch in chunks:
            code, body = submit(ep, ch)
            ok = code in (200, 202)
            print(f"  [{'OK' if ok else 'FAIL'}] {ep} -> {code} {body[:80]}")


if __name__ == "__main__":
    main()
