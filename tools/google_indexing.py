#!/usr/bin/env python3
"""구글 Indexing API 통보 — 서비스 계정으로 URL 색인/갱신을 요청한다.
(구글은 IndexNow 미참여이므로 구글 즉시 통보는 이 API를 사용한다.)

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console > 설정 > 사용자 및 권한 에서 서비스 계정 이메일을 "소유자"로 추가
  4) pip install google-auth requests

사용법:
  export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
  python3 tools/google_indexing.py                 # tools/urls.txt 전체
  python3 tools/google_indexing.py <URL> [<URL> ...]

참고: 공식 지원 타입은 JobPosting·BroadcastEvent지만 URL_UPDATED 통보는 크롤 우선순위에 도움이 된다.
한도(기본 200/일)를 고려해 새 글·변경 URL 위주로 통보하세요.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def load_urls(args):
    if args:
        return [u.strip() for u in args if u.strip()]
    with open(os.path.join(HERE, "urls.txt"), encoding="utf-8") as f:
        return [ln.strip() for ln in f if ln.strip()]


def main():
    cred = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred or not os.path.exists(cred):
        print("환경변수 GOOGLE_APPLICATION_CREDENTIALS(서비스 계정 JSON 경로)를 설정하세요.")
        sys.exit(1)
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        print("pip install google-auth requests 를 먼저 실행하세요.")
        sys.exit(1)
    import json
    import urllib.request

    creds = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    token = creds.token

    urls = load_urls(sys.argv[1:])
    print(f"구글 Indexing API 통보 대상 {len(urls)}개")
    ok = 0
    for u in urls:
        body = json.dumps({"url": u, "type": "URL_UPDATED"}).encode("utf-8")
        req = urllib.request.Request(
            ENDPOINT, data=body, method="POST",
            headers={"Authorization": f"Bearer {token}",
                     "Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                if r.status == 200:
                    ok += 1
                else:
                    print(f"  [{r.status}] {u}")
        except Exception as e:  # noqa: BLE001
            print(f"  [FAIL] {u} ({e})")
    print(f"완료: {ok}/{len(urls)} 성공")


if __name__ == "__main__":
    main()
