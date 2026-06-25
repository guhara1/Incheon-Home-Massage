import json
from .site import BRAND, BASE_URL, PHONE, AREA_SERVED

_BASE = BASE_URL.rstrip("/")

# 메타 설명 (80자 이내)
DESC = "인천 출장마사지·홈타이 예약 전 송도, 부평, 구월, 청라, 검단, 영종, 주안 생활권을 확인하세요."

# 자주 묻는 질문 (FAQ 스키마) — 지시서 7항
_FAQ = [
    ("인천은 구·군별 페이지를 모두 확인해야 하나요?",
     "구·군별로 대표 생활권, 가까운 역, 예약 기준이 다릅니다. 본인 위치가 속한 구·군 페이지를 먼저 확인하면 방문 가능 지역과 추가 이동비 여부를 정확히 파악할 수 있습니다."),

    ("송도와 연수구 페이지는 어떻게 다른가요?",
     "연수구 페이지는 구 전체 허브 역할을 하고, 송도 페이지는 송도국제도시·인천대입구역·센트럴파크 중심 생활권을 안내합니다. 본인 생활권에 맞는 페이지를 확인하세요."),

    ("부평역과 부평동은 어떻게 나뉘나요?",
     "부평역 페이지는 역세권 접근성 기준이고, 부평동 페이지는 부평시장·부평문화의거리 등 주거·상권 생활권 기준입니다. 방문 주소에 맞는 페이지를 보면 됩니다."),

    ("영종과 인천공항은 따로 확인해야 하나요?",
     "영종은 운서·영종 주거 생활권 기준이고, 인천공항은 공항·숙소·차량 이동 기준 중심입니다. 숙소 이용이라면 인천공항 안내를, 자택이라면 영종 안내를 확인하세요."),

    ("강화군과 옹진군도 방문이 가능한가요?",
     "도심형 지역과 달리 강화군·옹진군은 차량 이동과 사전 예약이 중요합니다. 방문 가능 여부, 추가 이동비, 예약 가능 시간을 미리 확인한 뒤 예약하시기 바랍니다."),

    ("예약 전 꼭 확인해야 할 사항은 무엇인가요?",
     "방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식, 개인정보 처리 기준을 먼저 확인하면 예약 과정이 수월합니다."),
]

_faq_schema = {
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "@id": f"#faq-{i+1}",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a},
        }
        for i, (q, a) in enumerate(_FAQ)
    ],
}

# WebSite 스키마
_website_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": _BASE + "/#website",
    "name": BRAND + " 인천 출장마사지",
    "url": _BASE + "/incheon/",
    "inLanguage": "ko",
    "publisher": {"@id": _BASE + "/#organization"},
}

# WebPage 스키마 (지시서: WebPage)
_webpage_schema = {
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "인천 출장마사지 · 인천 홈타이 지역별 예약 안내",
    "description": DESC,
    "url": _BASE + "/incheon/",
    "inLanguage": "ko",
    "isPartOf": {"@id": _BASE + "/#website"},
    "publisher": {"@id": _BASE + "/#organization"},
    "primaryImageOfPage": {"@id": _BASE + "/#primaryimage"},
}

# ImageObject 스키마 (지시서: ImageObject / 선호 썸네일 지정)
_image_schema = {
    "@context": "https://schema.org",
    "@type": "ImageObject",
    "@id": _BASE + "/#primaryimage",
    "url": _BASE + "/assets/og-image.png",
    "contentUrl": _BASE + "/assets/og-image.png",
    "width": 1200,
    "height": 630,
    "caption": "인천 출장마사지·홈타이 지역별 예약 안내",
}

# BreadcrumbList (메인은 홈만)
_breadcrumb_schema = {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "홈", "item": _BASE + "/incheon/"}
    ],
}

_EXTRA_HEAD = "".join(
    f'<script type="application/ld+json">\n{json.dumps(s, ensure_ascii=False, indent=2)}\n</script>\n'
    for s in (_website_schema, _webpage_schema, _image_schema, _breadcrumb_schema, _faq_schema)
)

_HERO = """<div class="hero">
  <div class="hero-content">
    <div class="hero-badge">인천광역시 전지역 방문 관리</div>
    <h1 class="hero-title">인천 출장마사지<br><span class="hero-accent">인천 홈타이</span><br>지역별 예약 안내</h1>
    <p class="hero-lead">송도, 부평, 구월, 청라, 검단, 영종, 주안 등 인천 주요 생활권별 방문 가능 지역과 예약 전 확인사항을 안내합니다.</p>
    <div class="hero-cta">
      <a href="#areas" class="btn btn-primary">지역별 안내 보기</a>
      <a href="#stations" class="btn btn-secondary">가까운 역 찾기</a>
      <a href="/incheon/reservation/" class="btn btn-secondary">예약 안내 보기</a>
      <a href="/incheon/check/" class="btn btn-secondary">이용 전 확인사항</a>
    </div>
  </div>
  <div class="hero-stats">
    <div class="stat"><div class="stat-number">10</div><div class="stat-label">구·군별 안내</div></div>
    <div class="stat"><div class="stat-number">32</div><div class="stat-label">지역 페이지</div></div>
    <div class="stat"><div class="stat-number">30</div><div class="stat-label">역세권 안내</div></div>
    <div class="stat"><div class="stat-number">24H</div><div class="stat-label">상담 가능</div></div>
  </div>
</div>"""

PAGE = {
    "path": "incheon/",
    "title": "인천 출장마사지｜송도·부평·구월·청라 홈타이 지역 안내",
    "desc": DESC,
    "h1": "인천 출장마사지 · 인천 홈타이 지역별 예약 안내",
    "hero": _HERO,
    "breadcrumb": [],
    "extra_head": _EXTRA_HEAD,
    "body": """
<section id="criteria">
  <h2>인천에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
  <p>인천광역시는 2군·8구로 구성된 도시로, 구·군별 생활권 차이가 매우 큰 것이 특징입니다. 인천 출장마사지·홈타이를 예약하기 전에는 본인 위치가 어느 구·군의 어느 생활권에 속하는지, 가장 가까운 지하철역이 무엇인지, 그리고 기본 방문권 안에 있는지를 먼저 확인하는 것이 가장 중요합니다.</p>
  <p>송도와 연수는 송도국제도시·센트럴파크를 중심으로 한 국제도시·주거 생활권이고, 구월과 인천시청 주변은 행정·상권 중심 생활권입니다. 부평과 주안은 부평역·주안역을 중심으로 한 역세권 검색 의도가 강하고, 청라와 검단은 신도시형 생활권 검색이 많습니다. 영종과 인천공항은 공항·숙소·차량 이동 기준이 중요하며, 강화와 옹진은 사전 방문 가능 여부와 추가 이동비 확인이 필요한 지역입니다.</p>
  <p>인천의 행정 구역과 생활권 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>에서, 지하철 역세권·노선 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사</a>에서 확인할 수 있습니다. 본 페이지는 이러한 행정·교통 생활권을 기준으로 방문 가능 지역과 예약 전 확인사항을 정리한 안내 페이지입니다.</p>
  <p><strong>2026년 7월 1일 행정체제 개편</strong>으로 제물포구·영종구·검단구가 출범할 예정이므로, 본 안내는 현재 2군·8구 구조를 기준으로 하되 개편 이후 생활권 변화도 함께 고려하여 작성되었습니다.</p>
</section>

<section id="coverage">
  <h2>인천 구·군별 방문 가능 지역 안내</h2>
  <p>인천 10개 구·군별 대표 생활권과 가까운 역을 확인하고, 본인 위치에 맞는 구·군 페이지에서 자세한 방문 기준을 확인하세요.</p>
  <div class="card-grid">
    <a href="/incheon/jung-gu/" class="card"><h3>중구</h3><p>동인천, 영종, 운서, 인천공항 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/dong-gu/" class="card"><h3>동구</h3><p>송림, 송현, 동인천 인접 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/michuhol-gu/" class="card"><h3>미추홀구</h3><p>주안, 도화, 용현, 학익 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/yeonsu-gu/" class="card"><h3>연수구</h3><p>송도, 연수, 동춘, 원인재 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/namdong-gu/" class="card"><h3>남동구</h3><p>구월, 간석, 논현, 소래 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/bupyeong-gu/" class="card"><h3>부평구</h3><p>부평역, 부평시장, 삼산, 산곡 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/gyeyang-gu/" class="card"><h3>계양구</h3><p>계산, 작전, 계양역, 귤현 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/seo-gu/" class="card"><h3>서구</h3><p>청라, 검단, 검암, 루원, 석남 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/ganghwa-gun/" class="card"><h3>강화군</h3><p>강화읍, 길상, 화도, 교동 생활권</p><span class="card-arrow">→</span></a>
    <a href="/incheon/ongjin-gun/" class="card"><h3>옹진군</h3><p>영흥, 자월, 백령, 대청 도서 생활권</p><span class="card-arrow">→</span></a>
  </div>
</section>

<section id="areas">
  <h2>인천 대표 지역별 방문 가능 지역 안내</h2>
  <p>인천에서 출장마사지·홈타이 검색 수요가 높은 대표 지역입니다. 각 지역은 대표 생활권과 인접 역을 중심으로 안내합니다.</p>
  <div class="card-grid">
    <a href="/incheon/yeonsu-gu/songdo/" class="card"><h3>송도</h3><p>송도국제도시, 인천대입구역, 센트럴파크 생활권</p></a>
    <a href="/incheon/namdong-gu/guwol-dong/" class="card"><h3>구월동</h3><p>인천시청, 예술회관, 인천터미널 인접 생활권</p></a>
    <a href="/incheon/bupyeong-gu/bupyeong-dong/" class="card"><h3>부평동</h3><p>부평역, 부평시장, 부평구청 인접 생활권</p></a>
    <a href="/incheon/michuhol-gu/juan-dong/" class="card"><h3>주안동</h3><p>주안역, 도화동, 미추홀구 중심 생활권</p></a>
    <a href="/incheon/seo-gu/cheongna/" class="card"><h3>청라</h3><p>청라국제도시, 청라국제도시역, 루원 인접 생활권</p></a>
    <a href="/incheon/seo-gu/geomdan-area/" class="card"><h3>검단</h3><p>검단신도시, 검단사거리역, 완정역 생활권</p></a>
    <a href="/incheon/jung-gu/yeongjong-area/" class="card"><h3>영종</h3><p>운서역, 영종역, 인천공항 인접 생활권</p></a>
    <a href="/incheon/namdong-gu/nonhyeon-dong/" class="card"><h3>논현동</h3><p>인천논현역, 소래포구역, 남동 인접 생활권</p></a>
    <a href="/incheon/gyeyang-gu/gyesan-dong/" class="card"><h3>계산동</h3><p>계산역, 경인교대입구역, 작전동 인접 생활권</p></a>
    <a href="/incheon/jung-gu/dongincheon-area/" class="card"><h3>동인천</h3><p>동인천역, 신포, 제물포 인접 생활권</p></a>
  </div>
</section>

<section id="stations">
  <h2>인천 주요 지하철역별 홈타이 안내</h2>
  <p>인천 주요 지하철역별로 인접 생활권과 예약 전 확인사항을 안내합니다. 환승역은 노선별로 나누지 않고 역명 기준 1개 안내로 정리했습니다.</p>
  <div class="card-grid">
    <a href="/incheon/station/bupyeong-station/" class="card"><h3>부평역</h3><p>부평동, 부평시장, 부개동 인접권</p></a>
    <a href="/incheon/station/juan-station/" class="card"><h3>주안역</h3><p>주안동, 도화동 인접권</p></a>
    <a href="/incheon/station/incheon-cityhall-station/" class="card"><h3>인천시청역</h3><p>구월동, 간석동 인접권</p></a>
    <a href="/incheon/station/songdo-moonlight-festival-park-station/" class="card"><h3>송도달빛축제공원역</h3><p>송도국제도시 생활권</p></a>
    <a href="/incheon/station/incheon-national-univ-station/" class="card"><h3>인천대입구역</h3><p>송도, 센트럴파크 인접권</p></a>
    <a href="/incheon/station/woninjae-station/" class="card"><h3>원인재역</h3><p>연수동, 동춘동 인접권</p></a>
    <a href="/incheon/station/gyeyang-station/" class="card"><h3>계양역</h3><p>귤현, 박촌 인접권</p></a>
    <a href="/incheon/station/geomam-station/" class="card"><h3>검암역</h3><p>검암동, 아라 인접권</p></a>
    <a href="/incheon/station/cheongna-international-city-station/" class="card"><h3>청라국제도시역</h3><p>청라, 루원 인접권</p></a>
    <a href="/incheon/station/geomdan-sageori-station/" class="card"><h3>검단사거리역</h3><p>검단, 마전 인접권</p></a>
    <a href="/incheon/station/dongincheon-station/" class="card"><h3>동인천역</h3><p>신포, 중구 내륙 인접권</p></a>
    <a href="/incheon/station/incheon-airport-terminal-1-station/" class="card"><h3>인천공항1터미널역</h3><p>영종, 공항 숙소 생활권</p></a>
  </div>
</section>

<section id="lifestyle">
  <h2>인천 생활권별 예약 기준</h2>
  <p>생활권 안내는 구·군 페이지와 역세권 페이지 사이를 연결하는 중간 허브입니다. 지역과 역을 묶어 더 정확한 방문 주소와 이동 시간을 확인할 수 있습니다.</p>
  <div class="card-grid">
    <a href="/incheon/life/songdo-international-city/" class="card">송도국제도시 생활권</a>
    <a href="/incheon/life/guwol-incheon-cityhall/" class="card">구월·인천시청 생활권</a>
    <a href="/incheon/life/bupyeong-station-market/" class="card">부평역·부평시장 생활권</a>
    <a href="/incheon/life/juan-dohwa/" class="card">주안·도화 생활권</a>
    <a href="/incheon/life/cheongna-international-city/" class="card">청라국제도시 생활권</a>
    <a href="/incheon/life/geomdan-newtown/" class="card">검단신도시 생활권</a>
    <a href="/incheon/life/yeongjong-unseo/" class="card">영종·운서 생활권</a>
    <a href="/incheon/life/incheon-airport/" class="card">인천공항 생활권</a>
  </div>
</section>

<section id="longtail">
  <h2>인천 지역·역세권·생활권별 롱테일 안내</h2>
  <p>인천 출장마사지·홈타이는 같은 구 안에서도 생활권마다 방문 동선과 예약 기준이 다릅니다. 아래에서 본인 위치와 가까운 주제로 들어가면 해당 지역의 방문 가능 지역과 예약 전 확인사항을 더 자세히 확인할 수 있습니다.</p>
  <h3>연수·남동·미추홀 생활권</h3>
  <p><a href="/incheon/yeonsu-gu/songdo/">송도국제도시 센트럴파크 인근 방문 가능 지역</a>, <a href="/incheon/yeonsu-gu/yeonsu-dong/">연수동 원인재역 인접 생활권</a>, <a href="/incheon/yeonsu-gu/dongchun-dong/">동춘동 청학동 주거 생활권</a>을 비롯해 <a href="/incheon/namdong-gu/guwol-dong/">구월동 인천시청·예술회관 상권 생활권</a>, <a href="/incheon/namdong-gu/ganseok-dong/">간석동 간석오거리역 인접권</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동 소래포구 인접 주거권</a>, <a href="/incheon/michuhol-gu/juan-dong/">주안동 주안역 중심 생활권</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화동 제물포역 인접권</a>, <a href="/incheon/michuhol-gu/yonghyeon-dong/">용현동 인하대역 인접권</a>, <a href="/incheon/michuhol-gu/hagik-dong/">학익동 문학경기장역 인접권</a>을 안내합니다.</p>
  <h3>부평·계양 생활권</h3>
  <p><a href="/incheon/bupyeong-gu/bupyeong-dong/">부평동 부평시장·부평문화의거리 생활권</a>, <a href="/incheon/bupyeong-gu/bugae-dong/">부개동 부개역 인접권</a>, <a href="/incheon/bupyeong-gu/samsan-dong/">삼산동 삼산체육관역 인접권</a>, <a href="/incheon/bupyeong-gu/sangok-dong/">산곡동 산곡역 주거권</a>, <a href="/incheon/bupyeong-gu/cheongcheon-dong/">청천동 갈산 인접권</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동 경인교대입구역 인접권</a>, <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동 작전역 인접권</a>, <a href="/incheon/gyeyang-gu/hyoseong-dong/">효성동 차량 이동권</a>으로 들어가면 역세권 접근성과 주차·건물 출입 기준을 확인할 수 있습니다.</p>
  <h3>서구·중구 생활권</h3>
  <p><a href="/incheon/seo-gu/cheongna/">청라국제도시 청라국제도시역 생활권</a>, <a href="/incheon/seo-gu/geomdan-area/">검단신도시 검단사거리역 생활권</a>, <a href="/incheon/seo-gu/geomam-dong/">검암동 아라뱃길 인접권</a>, <a href="/incheon/seo-gu/gajeong-dong/">가정동 루원시티 인접권</a>, <a href="/incheon/seo-gu/luwon-area/">루원 가정역 생활권</a>, <a href="/incheon/seo-gu/seongnam-dong/">석남동 서구청역 인접권</a>과 함께 <a href="/incheon/jung-gu/yeongjong-area/">영종 운서 주거 생활권</a>, <a href="/incheon/jung-gu/unseo-dong/">운서동 영종역 인접권</a>, <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 숙소·차량 이동 기준 안내</a>, <a href="/incheon/jung-gu/dongincheon-area/">동인천 신포·제물포 인접권</a>, <a href="/incheon/michuhol-gu/jemulpo-area/">제물포역 도화 인접권</a>을 확인하세요.</p>
  <h3>역세권·생활권 허브로 빠르게 찾기</h3>
  <p>역 기준으로는 <a href="/incheon/station/incheon-national-univ-station/">인천대입구역 송도 방문 가능 지역</a>, <a href="/incheon/station/woninjae-station/">원인재역 연수·동춘 인접권</a>, <a href="/incheon/station/incheon-terminal-station/">인천터미널역 구월 상권</a>, <a href="/incheon/station/soraepogu-station/">소래포구역 논현 인접권</a>, <a href="/incheon/station/geomam-station/">검암역 청라·아라 인접권</a>, <a href="/incheon/station/dongincheon-station/">동인천역 중구 내륙권</a>을, 생활권 기준으로는 <a href="/incheon/life/yeonsu-woninjae/">연수·원인재 생활권</a>, <a href="/incheon/life/nonhyeon-sorae/">논현·소래 생활권</a>, <a href="/incheon/life/yonghyeon-hagik/">용현·학익 생활권</a>, <a href="/incheon/life/samsan-bupyeong-gu-office/">삼산·부평구청 생활권</a>, <a href="/incheon/life/sangok-cheongcheon/">산곡·청천 생활권</a>, <a href="/incheon/life/gyesan-jakjeon/">계산·작전 생활권</a>, <a href="/incheon/life/luwon-gajeong/">루원·가정 생활권</a>, <a href="/incheon/life/dongincheon-jemulpo/">동인천·제물포 생활권</a>을 확인할 수 있습니다. 강화·옹진 등 도서·외곽 지역은 <a href="/incheon/ganghwa-gun/">강화군 사전 확인형 안내</a>와 <a href="/incheon/ongjin-gun/">옹진군 도서 지역 안내</a>에서 차량 이동·사전 예약 기준을 먼저 확인하세요.</p>
</section>

<section id="check">
  <h2>인천 홈타이 예약 전 확인사항</h2>
  <p>예약을 진행하기 전에 다음 항목을 먼저 확인하면 방문 과정이 훨씬 수월합니다. 자세한 내용은 <a href="/incheon/check/">이용 전 확인사항</a>과 <a href="/incheon/guide/">홈타이 이용 가이드</a>에서 확인하세요.</p>
  <ul>
    <li><strong>방문 가능 주소 확인</strong> — 자택·숙소·오피스텔 등 정확한 방문 주소와 건물 유형 확인</li>
    <li><strong>예약 가능 시간 확인</strong> — 희망 시간대 방문 가능 여부 사전 확인</li>
    <li><strong>추가 이동비 여부 확인</strong> — 기본 방문권 외 추가 이동비 발생 여부</li>
    <li><strong>건물 출입 방식 확인</strong> — 공동현관·자동문·경비 출입 방식</li>
    <li><strong>자택·숙소·오피스텔·호텔 이용 기준 확인</strong> — 방문 장소 기준</li>
    <li><strong>공항·도서 지역 방문 가능 여부 확인</strong> — 영종·인천공항·강화·옹진 등</li>
    <li><strong>결제 방식 확인</strong> — 현금·계좌이체·카드 등 가능한 결제 수단</li>
    <li><strong>예약 변경·취소 기준 확인</strong> — 변경·취소 절차 및 기준</li>
    <li><strong>개인정보 처리 기준 확인</strong> — 개인정보 수집·이용·보관 방식</li>
    <li><strong>불법·선정적 서비스 불가 안내</strong> — 건전한 방문 관리 서비스만 제공</li>
  </ul>
</section>

<section id="faq">
  <h2>인천 출장마사지 자주 묻는 질문</h2>
  <dl class="faq-list">
    <dt id="faq-1">인천은 구·군별 페이지를 모두 확인해야 하나요?</dt>
    <dd>구·군별로 대표 생활권, 가까운 역, 예약 기준이 다릅니다. 본인 위치가 속한 구·군 페이지를 먼저 확인하면 방문 가능 지역과 추가 이동비 여부를 정확히 파악할 수 있습니다.</dd>
    <dt id="faq-2">송도와 연수구 페이지는 어떻게 다른가요?</dt>
    <dd>연수구 페이지는 구 전체 허브 역할을 하고, 송도 페이지는 송도국제도시·인천대입구역·센트럴파크 중심 생활권을 안내합니다. 본인 생활권에 맞는 페이지를 확인하세요.</dd>
    <dt id="faq-3">부평역과 부평동은 어떻게 나뉘나요?</dt>
    <dd>부평역 페이지는 역세권 접근성 기준이고, 부평동 페이지는 부평시장·부평문화의거리 등 주거·상권 생활권 기준입니다. 방문 주소에 맞는 페이지를 보면 됩니다.</dd>
    <dt id="faq-4">영종과 인천공항은 따로 확인해야 하나요?</dt>
    <dd>영종은 운서·영종 주거 생활권 기준이고, 인천공항은 공항·숙소·차량 이동 기준 중심입니다. 숙소 이용이라면 인천공항 안내를, 자택이라면 영종 안내를 확인하세요.</dd>
    <dt id="faq-5">강화군과 옹진군도 방문이 가능한가요?</dt>
    <dd>도심형 지역과 달리 강화군·옹진군은 차량 이동과 사전 예약이 중요합니다. 방문 가능 여부, 추가 이동비, 예약 가능 시간을 미리 확인한 뒤 예약하시기 바랍니다.</dd>
    <dt id="faq-6">예약 전 꼭 확인해야 할 사항은 무엇인가요?</dt>
    <dd>방문 가능 주소, 예약 가능 시간, 추가 이동비 여부, 건물 출입 방식, 결제 방식, 개인정보 처리 기준을 먼저 확인하면 예약 과정이 수월합니다.</dd>
  </dl>
</section>
"""
}
