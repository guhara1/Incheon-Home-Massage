# 인천 출장마사지 사이트

인천광역시 전지역 방문 관리 서비스(출장마사지·홈타이) 안내 정적 사이트입니다.

**상호**: 간다GO
**예약전화**: 0508-202-4719
**문의(텔레그램)**: https://t.me/googleseolab

## 구조

- **정적 HTML 사이트** — 어느 호스팅(Cloudflare Pages, GitHub Pages, 웹서버)에서든 그대로 서빙 가능
- **build.py** + **content/** — 페이지를 Python으로 정의하고 정적 HTML 생성
- **생성물** — 각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`

```
build.py                     # 빌드 스크립트 (헤더/푸터/스키마 자동 주입)
content/
  site.py                   # 상호·전화·도메인·메뉴·텔레그램 URL
  root.py                   # 루트(/) → /incheon/ 리다이렉트
  main.py                   # 인천 메인 페이지 (/incheon/)
  gugun.py                  # 구·군별 페이지 10개 + 2026 개편 대비 draft 3개(noindex)
  dong_a.py / dong_b.py / dong_c.py   # 지역(동) 페이지 32개
  stations_a.py / stations_b.py       # 역세권 페이지 30개
  life_a.py / life_b.py               # 생활권 페이지 20개
  info.py                   # 예약·확인사항·가이드·고객센터·개인정보처리방침
assets/
  style.css                 # 프리미엄 옵시디언+앰버골드 / 오렌지 / Pretendard / 컴포넌트 오버레이
  nav.js                    # 모바일 네비게이션
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (지시서 반영)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리
- 현재 **2군·8구** 구조로 색인. 2026-07-01 개편 대비 **제물포구·영종구·검단구**는 `noindex` draft로 준비
- 메뉴·URL에 "출장마사지" 반복 없음 — 핵심 키워드는 Title/H1/첫 문단/Description에서만 사용
- 환승역은 **역명 기준 1개 URL**, 출구별 페이지 없음, 번호 동 대량 생성 없음
- 모든 페이지 본문은 고유 작성 (지역명만 바꾼 복붙 없음)
- **내부링크 롱테일 강화**: 메인 → 구·군 → 동 → 역 → 생활권 허브 구조
- 강화군·옹진군은 도심형이 아닌 **사전 확인형**(방문 가능 여부·추가 이동비·차량 이동) 안내

## 스키마 (모든 페이지)

- 전역: `Organization`(방문형 사이트이므로 LocalBusiness 미사용)
- 일반 페이지: `WebPage` + `BreadcrumbList`
- 메인: `WebSite` + `WebPage` + `ImageObject`(선호 썸네일) + `BreadcrumbList` + `FAQPage`

## 디자인

- **프리미엄 팔레트**: 옵시디언 잉크 배경 + 앰버골드 디테일 + 오렌지 #FF6B35 액센트
- **컴포넌트 오버레이**: 글래스 섹션 카드, 골드 그라데이션 보더, 호버 글로우
- **Pretendard 폰트**, 반응형, 접근성(WAI-ARIA), 정적 HTML(빠른 로딩)
- **푸터 오렌지 CTA**: 웹사이트 제작문의·제휴문의 버튼(텔레그램 연결)

## 검색엔진 등록·즉시 색인

빌드 시 자동 생성: `sitemap.xml`(lastmod 포함), `rss.xml`, `robots.txt`, IndexNow 키 파일(`<키>.txt`), `tools/urls.txt`.
모든 페이지 `<head>`에 네이버 소유확인 메타가 출력된다.

**1) 소유 확인·사이트맵 등록 (가장 중요)**
- 네이버 서치어드바이저: 사이트 등록 → (메타 자동 출력됨) 확인 → `sitemap.xml`·`rss.xml` 제출
- 구글 서치콘솔: 사이트 등록 → `sitemap.xml` 제출. 구글 메타 토큰이 있으면 `content/site.py`의 `GOOGLE_SITE_VERIFICATION`에 입력 후 재빌드
- 빙 웹마스터: 사이트 등록(구글 서치콘솔 가져오기 가능) → `sitemap.xml` 제출

**2) IndexNow 즉시 통보 (빙·네이버·얀덱스) — 글 올릴 때마다**
```bash
python3 build.py                                   # 빌드(키 파일·urls.txt 갱신)
# 배포(푸시) 후:
python3 tools/indexnow.py                           # 전체 일괄 통보(첫 통보)
python3 tools/indexnow.py https://incheon-home-massage.pages.dev/yeonsu-gu/songdo/   # 특정 URL만
```
- 키: `246497306624e87a1aad9965d295f98c` (루트 `<키>.txt`로 게시되어 소유 자동 확인)

**3) 구글 즉시 통보 (구글은 IndexNow 미참여) — 선택**
```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json
python3 tools/google_indexing.py                    # tools/urls.txt 전체
```
서비스 계정을 서치콘솔 "소유자"로 추가해야 함. `tools/ping_sitemap.py`는 보조용(구글·빙 sitemap ping은 폐지됨).

## 배포 전 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경(현재 incheon-home-massage.pages.dev)
2. `python3 build.py` 재실행
3. 위 "검색엔진 등록·즉시 색인" 절차 수행
4. 2026년 개편 후 제물포구·영종구·검단구 색인·리디렉션·canonical 조정
