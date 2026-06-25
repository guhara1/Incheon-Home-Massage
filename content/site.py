# 인천시 출장마사지 사이트 공통 설정

BASE_URL = "https://incheon-home-massage.pages.dev"

BRAND = "간다GO"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 외부 문의 채널 (텔레그램)
TELEGRAM_URL = "https://t.me/googleseolab"

AREA_SERVED = "인천광역시"
SERVICE_AREA_TEXT = "인천광역시 전지역"

# ── 검색엔진 등록·색인 ──────────────────────────────
# 네이버 서치어드바이저 사이트 소유확인 메타 (홈 포함 전 페이지 출력)
NAVER_SITE_VERIFICATION = "449daf38d5eb7a0e419cf743b7ba0a542bb6335e"
# 구글 서치콘솔 메타 토큰이 있으면 입력 (없으면 빈 문자열 → 출력 안 함)
GOOGLE_SITE_VERIFICATION = ""

# IndexNow 키 (빙·네이버·얀덱스 등 즉시 색인 통보용)
# 루트에 <키>.txt 파일로도 게시되어 소유 확인에 사용된다.
INDEXNOW_KEY = "246497306624e87a1aad9965d295f98c"

# RSS 피드 메타
RSS_TITLE = "간다GO 인천 출장마사지·홈타이"
RSS_DESC = "인천 구·군·지역·역세권·생활권별 방문 가능 지역과 예약 전 확인사항 안내"

# ── 기본 요금(코스) ─────────────────────────────────
# 모든 페이지 하단에 공통 가격표로 출력되고 Offer 스키마로도 사용된다.
PRICING = [
    {"name": "60분 코스", "min": "60분", "price": 90000,
     "desc": "핵심 부위 위주 가벼운 이완", "featured": False},
    {"name": "90분 코스", "min": "90분", "price": 150000,
     "desc": "전신 균형 표준 구성·아로마 포함", "featured": True},
    {"name": "120분 코스", "min": "120분", "price": 180000,
     "desc": "구석구석 집중하는 프리미엄 구성", "featured": False},
]

# 상단 메뉴 — 키워드 반복 없음, 지역명·역명만 표시 (지시서 4항)
NAV = [
    ("인천 홈", "/", []),
    ("구·군별 안내", "/", [
        ("중구", "/jung-gu/"),
        ("동구", "/dong-gu/"),
        ("미추홀구", "/michuhol-gu/"),
        ("연수구", "/yeonsu-gu/"),
        ("남동구", "/namdong-gu/"),
        ("부평구", "/bupyeong-gu/"),
        ("계양구", "/gyeyang-gu/"),
        ("서구", "/seo-gu/"),
        ("강화군", "/ganghwa-gun/"),
        ("옹진군", "/ongjin-gun/"),
    ]),
    ("지역별 안내", "/", [
        ("송도", "/yeonsu-gu/songdo/"),
        ("구월동", "/namdong-gu/guwol-dong/"),
        ("논현동", "/namdong-gu/nonhyeon-dong/"),
        ("주안동", "/michuhol-gu/juan-dong/"),
        ("부평동", "/bupyeong-gu/bupyeong-dong/"),
        ("계산동", "/gyeyang-gu/gyesan-dong/"),
        ("청라", "/seo-gu/cheongna/"),
        ("검단", "/seo-gu/geomdan-area/"),
        ("영종", "/jung-gu/yeongjong-area/"),
        ("동인천", "/jung-gu/dongincheon-area/"),
    ]),
    ("역세권 안내", "/", [
        ("부평역", "/station/bupyeong-station/"),
        ("주안역", "/station/juan-station/"),
        ("인천시청역", "/station/incheon-cityhall-station/"),
        ("송도달빛축제공원역", "/station/songdo-moonlight-festival-park-station/"),
        ("인천대입구역", "/station/incheon-national-univ-station/"),
        ("원인재역", "/station/woninjae-station/"),
        ("계양역", "/station/gyeyang-station/"),
        ("검암역", "/station/geomam-station/"),
        ("청라국제도시역", "/station/cheongna-international-city-station/"),
        ("검단사거리역", "/station/geomdan-sageori-station/"),
        ("동인천역", "/station/dongincheon-station/"),
        ("인천공항1터미널역", "/station/incheon-airport-terminal-1-station/"),
    ]),
    ("생활권 안내", "/", [
        ("송도국제도시", "/life/songdo-international-city/"),
        ("구월·인천시청", "/life/guwol-incheon-cityhall/"),
        ("부평역·부평시장", "/life/bupyeong-station-market/"),
        ("주안·도화", "/life/juan-dohwa/"),
        ("청라국제도시", "/life/cheongna-international-city/"),
        ("검단신도시", "/life/geomdan-newtown/"),
        ("영종·운서", "/life/yeongjong-unseo/"),
        ("인천공항", "/life/incheon-airport/"),
    ]),
    ("예약 안내", "/reservation/", []),
    ("이용 전 확인사항", "/check/", []),
    ("홈타이 이용 가이드", "/guide/", []),
    ("고객센터", "/support/", [
        ("개인정보처리방침", "/support/privacy/"),
    ]),
]
