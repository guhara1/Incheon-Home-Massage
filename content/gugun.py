# 인천 구·군별 안내 페이지 (색인 10개 + 2026 개편 draft 3개)
# 브랜드: 간다GO / 예약전화: 0508-202-4719


def create_page(path, title, desc, h1, breadcrumb, body_content):
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }


# ──────────────────────────────────────────────
# 1. 중구
# ──────────────────────────────────────────────
_jung_gu_body = """
<section>
  <h2>중구 출장마사지 — 동인천·영종·인천공항 생활권 안내</h2>
  <p>
    중구 출장마사지를 알아보고 계신다면, 우선 <strong>중구의 생활권이 크게 내륙권과 도서·공항권으로 나뉜다</strong>는 점을 확인해 주세요.
    내륙권은 동인천·신포·월미도 일대이며, 도서·공항권은 영종도와 운서, 인천국제공항 인근까지 포함합니다.
    간다GO는 두 생활권 모두 방문 가능 지역으로 안내하고 있으나, 영종·운서·공항권은 이동 시간이 추가되므로 예약 전 방문 가능 여부와 이동 조건을 반드시 확인해 주시기 바랍니다.
    2026년 7월 행정구역 개편 시 영종·운서·인천공항 일대는 <strong>영종구(가칭)</strong>로 분리될 예정이니 참고해 두시면 좋습니다.
  </p>
  <p>
    중구는 인천의 역사적 원도심이자 항구 도시의 정취가 남아 있는 지역입니다.
    <a href="/incheon/jung-gu/dongincheon-area/">동인천 생활권</a>은 배다리 골목, 신포시장, 차이나타운이 어우러진 복합 문화 지역으로,
    유동 인구가 많고 주거 밀집도가 높아 방문형 관리 서비스 수요가 꾸준합니다.
    월미도 해양관광단지와 인천항 국제여객터미널 인근의 숙박 시설에서도 예약 문의가 들어오며,
    차이나타운·자유공원 인근에는 게스트하우스와 소형 호텔이 산재해 있습니다.
  </p>
</section>

<section>
  <h2>주요 역세권 및 접근 정보</h2>
  <p>
    중구 내륙권의 대표 역은 <a href="/incheon/station/dongincheon-station/">동인천역</a>과 <a href="/incheon/station/incheon-station/">인천역</a>입니다.
    두 역 모두 수도권 1호선 종점 구간에 위치하여 서울·경기 방면과 직결되며, 인근 주거지와 상업 지역이 혼재합니다.
    동인천역은 중구·동구·미추홀구 세 구의 경계가 맞닿는 교통 결절점으로, 역 반경 500m 이내에 다양한 주거·숙박 시설이 위치합니다.
    도서·공항권은 <a href="/incheon/station/unseo-station/">운서역</a>, <a href="/incheon/station/yeongjong-station/">영종역</a>, <a href="/incheon/station/incheon-airport-terminal-1-station/">인천공항1터미널역</a>이 주요 거점입니다.
    공항철도(AREX)를 통해 서울역에서 직결되는 구조이므로, 공항 인근 숙박 이용 고객의 예약도 종종 접수됩니다.
  </p>
  <p>
    <a href="/incheon/jung-gu/yeongjong-area/">영종 생활권</a>과 <a href="/incheon/jung-gu/unseo-dong/">운서 지역</a>, <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 인근</a>은
    인천대교 또는 공항철도를 통해 진입하므로 이동 시간이 내륙보다 길게 소요됩니다.
    방문 가능 시간대와 추가 이동비는 예약 시 별도로 안내드리고 있습니다.
  </p>
</section>

<section>
  <h2>동인천·신포·월미도 내륙 생활권</h2>
  <p>
    <a href="/incheon/life/dongincheon-jemulpo/">동인천·제물포 생활권</a>은 중구와 <a href="/incheon/dong-gu/">동구</a>,
    <a href="/incheon/michuhol-gu/">미추홀구</a>의 경계가 인접한 지역입니다.
    신포국제시장 주변에는 구도심 특성의 소규모 숙박 시설과 빌라 주거지가 밀집해 있으며,
    월미도 해양관광단지 인근에는 관광객을 위한 모텔·펜션이 다수 운영됩니다.
    월미바다열차와 인천항 국제여객터미널 인근의 게스트하우스·비즈니스호텔도 방문 가능 주소 대상에 포함될 수 있습니다.
  </p>
  <ul>
    <li>동인천역 도보권 주거·상업 복합 지역 — 방문 가능</li>
    <li>신포동·중앙동 일대 숙박 시설 — 방문 가능 (체크인 완료 후 예약)</li>
    <li>월미도·항동 일대 관광 숙박 시설 — 방문 가능 여부 사전 확인 권장</li>
    <li>차이나타운·자유공원 인근 게스트하우스 — 방문 가능</li>
    <li>연안부두 인근 — 방문 주소 명확히 제공 시 방문 가능</li>
  </ul>
</section>

<section>
  <h2>영종·운서·인천공항 생활권 (도서·공항권)</h2>
  <p>
    영종도는 인천국제공항이 위치한 섬으로, 행정상 중구에 속하지만 내륙과의 물리적 거리가 있습니다.
    <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 인근</a>은 환승 대기, 장거리 비행 전후 피로 해소를 목적으로 방문형 관리 서비스를 원하시는 분들이 많습니다.
    공항 근처 공식 호텔(그랜드하얏트·네스트호텔·파라다이스시티 등) 투숙객 및 인근 에어비앤비·영종도 오피스텔 주민의 이용도 있습니다.
    해당 지역은 방문 시 이동 시간이 추가로 소요되며, 심야·조조 시간대 예약은 가능 여부를 사전에 확인해 주셔야 합니다.
    <a href="/incheon/station/incheon-airport-terminal-1-station/">인천공항1터미널역</a> 인근 공항 내 시설 및 공항 주변 호텔은 별도 안내 기준이 적용됩니다.
  </p>
  <p>
    <a href="/incheon/jung-gu/yeongjong-area/">영종 생활권</a>의 중산동·운북동·을왕동 일대는 영종도 내 주거 단지 및 리조트 시설이 밀집한 지역입니다.
    을왕리·왕산해수욕장 인근의 펜션·리조트도 방문 가능 주소로 안내 가능하나, 이동 시간이 길어질 수 있습니다.
    인천국제공항 공식 교통·시설 정보는
    <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서도 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>중구 이용 안내 — 방문 가능 주소 유형별 체크리스트</h2>
  <p>
    중구에서 방문형 관리 서비스를 이용하기 전, 아래 주소 유형별 안내를 참고해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>아파트·주상복합:</strong> 동인천 인근 신축 아파트, 영종도 중산동·운서동 아파트 단지 — 방문 가능, 동·호수 제공 필수</li>
    <li><strong>오피스텔·고시원:</strong> 동인천역 주변 오피스텔, 신포동 일대 소형 원룸 — 방문 가능 여부 사전 확인</li>
    <li><strong>관광·숙박 시설:</strong> 월미도 인근 모텔·비즈니스호텔, 영종도 리조트·파라다이스시티 인근 호텔 — 체크인 완료 후 예약</li>
    <li><strong>게스트하우스·에어비앤비:</strong> 차이나타운·자유공원 인근 단기 숙박 — 정확한 주소 확인 후 방문</li>
    <li><strong>공항 인접 시설:</strong> 인천공항1터미널·2터미널 인근 공항 호텔 — 이동비·방문 가능 시간 별도 안내</li>
  </ul>
  <p>
    중구의 역사·문화 자원 (강화도와는 다른 개항장 문화) 및 생활 정보는
    <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    중구 출장마사지 예약 시 아래 사항을 먼저 확인해 주시기 바랍니다.
  </p>
  <ul>
    <li>내륙권(동인천·신포·월미도)과 도서·공항권(영종·운서·인천공항)은 방문 조건이 다릅니다.</li>
    <li>도서·공항권은 추가 이동비가 발생할 수 있으며, 예약 전 사전 확인이 필요합니다.</li>
    <li>숙박 시설 이용 시에는 체크인 완료 후 예약을 진행해 주세요.</li>
    <li>공항 내부 시설(항공사 라운지, 보안구역)은 방문 불가 주소입니다.</li>
    <li>개인정보 처리 기준은 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 참고해 주세요.</li>
  </ul>
  <p>
    예약 및 방문 가능 지역 확인은 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락 주시면 안내드립니다.
    자세한 예약 절차는 <a href="/incheon/reservation/">예약 안내 페이지</a>를,
    이용 전 공통 사항은 <a href="/incheon/check/">이용 전 확인사항</a>을,
    홈타이 이용 전반은 <a href="/incheon/guide/">홈타이 이용 가이드</a>를 참고해 주세요.
    인접 구 안내: <a href="/incheon/dong-gu/">동구 출장마사지 안내</a> | <a href="/incheon/michuhol-gu/">미추홀구 출장마사지 안내</a>
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 2. 동구
# ──────────────────────────────────────────────
_dong_gu_body = """
<section>
  <h2>동구 출장마사지 — 송림·송현·동인천 인접 생활권 안내</h2>
  <p>
    동구 출장마사지를 검색하고 계신다면, 먼저 동구의 생활권 특성을 파악해 두시는 것이 좋습니다.
    동구는 인천의 원도심 중 가장 좁은 면적을 가진 자치구로,
    송림동·송현동·화수동·화평동·금곡동·만석동·배다리 등의 주거 밀집 지역이 촘촘하게 이어집니다.
    배다리 헌책방 골목과 수도국산 달동네 박물관 등 도시 재생 문화 자원이 있는 지역이며,
    오래된 주거 골목과 신축 빌라가 혼재하는 환경입니다.
    2026년 7월 행정구역 개편 시 동구는 중구 내륙 일부와 통합되어 <strong>제물포구(가칭)</strong>로 재편될 가능성이 있습니다.
  </p>
  <p>
    간다GO의 방문형 관리 서비스는 동구 전 지역을 방문 가능 지역으로 안내하고 있습니다.
    단, 골목 진입이 좁은 구도심 지역은 주소 확인을 명확히 해주시면 더 원활하게 안내드릴 수 있습니다.
    아파트, 다세대 빌라, 연립주택 등 다양한 주거 형태가 방문 대상에 포함됩니다.
  </p>
</section>

<section>
  <h2>주요 역세권 및 교통 안내</h2>
  <p>
    동구에는 자체 지하철역이 없으나, 인접 역들을 생활권 내에서 공유합니다.
    <a href="/incheon/station/dongincheon-station/">동인천역</a>(1호선)은 동구 남서쪽과 바로 접하며,
    중구·동구·미추홀구 3개 구의 경계 인근에 위치합니다.
    <a href="/incheon/station/jemulpo-station/">제물포역</a>(1호선)은 동구 남부 주민들이 이용하는 대표 환승 거점입니다.
    도원역(1호선) 또한 동구와 미추홀구 경계 인근에 위치하여 동구 서부 주민들이 이용합니다.
    버스 중심의 이동이 많은 지역이므로, 방문 시 정확한 도로명 주소를 제공해 주시면 보다 정확한 안내가 가능합니다.
  </p>
  <p>
    대중교통 노선은 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>송림·송현·화수·화평 주거 밀집 지역</h2>
  <p>
    송림동과 송현동은 동구에서 인구 밀도가 가장 높은 주거 밀집 지역입니다.
    아파트와 연립주택, 다세대 주택이 혼재하며 생활 편의 시설이 도보권에 모여 있어 방문형 서비스 이용이 편리한 환경입니다.
    송림 오거리를 중심으로 소규모 상권이 형성되어 있으며, 인근 주거 단지에서 방문 서비스 이용이 꾸준하게 이루어집니다.
    화수동과 화평동은 화수 부두 인근의 항구 지역으로, 어시장·수산물 시장이 인접해 있으며 주거지는 소규모 빌라 위주입니다.
    금곡동과 만석동은 산업·항만 기능이 일부 남아 있는 지역으로, 주거 시설 위치를 예약 시 명확히 안내해 주시기 바랍니다.
    배다리 일대는 1960~70년대 골목 구조가 남아 있는 도시 재생 구역으로, 협소한 골목 구조를 고려하여 방문 전 주소 확인을 권장합니다.
  </p>
  <ul>
    <li>송림동·송현동: 주거 밀집, 방문 원활</li>
    <li>화수동·화평동: 항구 인접, 주소 확인 후 방문</li>
    <li>금곡동·만석동: 산업 혼재 지역, 주거지 확인 필요</li>
    <li>배다리 일대: 소규모 주택 밀집, 도로 진입 확인 필요</li>
  </ul>
</section>

<section>
  <h2>인접 지역 연계 안내</h2>
  <p>
    동구는 면적이 좁아 인접 구와의 경계가 곳곳에 맞닿아 있습니다.
    <a href="/incheon/jung-gu/">중구</a>와는 동인천 생활권을 공유하며,
    <a href="/incheon/michuhol-gu/">미추홀구</a>와는 도원역·제물포역 인근 생활권을 함께 사용합니다.
    <a href="/incheon/life/dongincheon-jemulpo/">동인천·제물포 생활권 페이지</a>에서 두 구에 걸친 지역 안내를 함께 확인하실 수 있습니다.
    <a href="/incheon/michuhol-gu/jemulpo-area/">제물포 지역 안내</a>도 참고해 주세요.
    동구 북쪽으로는 인천항 및 인천 내항 제1부두~제8부두 일대가 이어지며,
    항만 구역 내 비거주 시설은 방문 불가 주소에 해당합니다.
  </p>
  <p>
    인천 내항 재개발(1·8부두 문화 창고 조성) 사업이 진행 중인 지역도 있으므로,
    신규 주거·문화 복합 시설 입주 시에는 주소 확인 후 예약해 주시기 바랍니다.
  </p>
</section>

<section>
  <h2>동구 이용 안내 — 주소 유형별 방문 가이드</h2>
  <p>
    동구는 주거 형태가 다양하게 혼재하는 지역입니다. 아래 유형별 안내를 참고해 주세요.
  </p>
  <ul>
    <li><strong>아파트·연립주택:</strong> 송림동·송현동 대단지 연립·소형 아파트 — 방문 가능, 동·호수 필수</li>
    <li><strong>빌라·다세대 주택:</strong> 화수·화평·금곡 일대 빌라 — 방문 전 도로명 주소 확인</li>
    <li><strong>단독주택·한옥:</strong> 배다리 골목 일대 구옥·개량 한옥 — 골목 진입 가능 여부 사전 확인 후 방문</li>
    <li><strong>고시원·원룸:</strong> 동인천역 인근 소형 원룸 — 방문 가능, 사전 확인 권장</li>
    <li><strong>산업·공장 시설:</strong> 만석동·항만 인접 지역 — 비주거 시설은 방문 불가</li>
  </ul>
  <p>
    동구의 도시 재생 사업 및 생활 정보는
    <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서
    대중교통 정보를 함께 확인하실 수 있습니다.
    <a href="/incheon/life/dongincheon-jemulpo/">동인천·제물포 생활권</a>과
    <a href="/incheon/michuhol-gu/jemulpo-area/">제물포 지역</a>도 함께 확인해 두시기 바랍니다.
  </p>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    동구 방문형 관리 서비스 이용 시 아래 사항을 확인해 주시기 바랍니다.
  </p>
  <ul>
    <li>정확한 도로명 주소 제공 — 구도심 골목 진입 시 필수</li>
    <li>주거지·숙박 시설 여부 확인 — 상업·산업 시설 혼재 지역 제외</li>
    <li>배다리·금곡 구역은 협소 도로 여부 사전 확인 권장</li>
    <li>개인정보 처리 기준: <a href="/incheon/support/privacy/">개인정보처리방침</a> 참고</li>
  </ul>
  <p>
    방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주시기 바랍니다.
    이용 전 공통 확인사항은 <a href="/incheon/check/">이용 전 확인사항</a>,
    예약 절차는 <a href="/incheon/reservation/">예약 안내</a>를 참고해 주세요.
    홈타이 이용 전반에 대한 안내는 <a href="/incheon/guide/">홈타이 이용 가이드</a>에서 확인하실 수 있습니다.
    인접 구 바로가기: <a href="/incheon/jung-gu/">중구</a> | <a href="/incheon/michuhol-gu/">미추홀구</a>
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 3. 미추홀구
# ──────────────────────────────────────────────
_michuhol_body = """
<section>
  <h2>미추홀구 출장마사지 — 주안·도화·용현·학익 생활권 안내</h2>
  <p>
    미추홀구 출장마사지를 알아보고 계신다면, 구 전역을 아우르는 방문 가능 지역과 주요 생활권을 먼저 확인해 보세요.
    미추홀구는 인천의 중심 자치구 중 하나로,
    <a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화</a>,
    <a href="/incheon/michuhol-gu/yonghyeon-dong/">용현</a>, <a href="/incheon/michuhol-gu/hagik-dong/">학익</a>,
    숭의, 관교, 문학 등 다양한 생활권이 모여 있습니다.
    주안역을 중심으로 상업 시설과 대규모 주거 단지가 발달해 있으며,
    인하대학교 캠퍼스 인근에는 학생·1인 가구 밀집 주거지가 형성되어 있어
    방문형 관리 서비스 이용 수요가 인천 내에서도 높은 편입니다.
  </p>
  <p>
    간다GO는 미추홀구 전 생활권에 방문 가능하며,
    아파트·오피스텔·원룸 등 다양한 주거 형태를 방문 주소 대상으로 안내하고 있습니다.
    정확한 방문 가능 여부는 예약 전 확인을 권장합니다.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    미추홀구의 대표 역은 <a href="/incheon/station/juan-station/">주안역</a>(1호선·인천 1호선 환승)으로,
    미추홀구의 중심 상권이자 교통 허브입니다.
    서울 방면 1호선과 인천 지하철 1호선이 교차하는 환승역으로, 인천 내 이동 접근성이 매우 좋습니다.
    <a href="/incheon/station/jemulpo-station/">제물포역</a>(1호선)은 주안역 동쪽에 위치하며 동구·중구 방면과 연결됩니다.
    <a href="/incheon/station/dongincheon-station/">동인천역</a>도 미추홀구 북동쪽 주민들이 활용하는 역세권입니다.
    인천 1호선 라인에서는 제물포역, 도화역, 숭의역, 인하대역, 문학경기장역이 미추홀구를 순서대로 관통합니다.
    인천 지하철 노선 및 시간표는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>주안·도화 생활권</h2>
  <p>
    <a href="/incheon/life/juan-dohwa/">주안·도화 생활권</a>은 미추홀구 북부의 핵심 상권입니다.
    주안역 주변에는 대형 쇼핑몰, 오피스텔, 주상복합 건물이 밀집해 있으며 유동 인구가 인천 내에서도 손꼽힐 만큼 많습니다.
    <a href="/incheon/michuhol-gu/juan-dong/">주안동</a>과 <a href="/incheon/michuhol-gu/dohwa-dong/">도화동</a>은
    대단지 아파트와 오피스텔 위주 주거 지역으로 방문형 서비스 접근이 원활합니다.
    주안1동~8동까지 다양한 행정 동이 있으며, 각 동별로 주거 환경 특성이 다릅니다.
    주안역 주변 오피스텔과 고시원도 방문 가능 주소 확인 후 이용하실 수 있습니다.
    도화역 인근은 인천 도시철도 1호선을 따라 형성된 역세권 주거 단지가 이어집니다.
  </p>
</section>

<section>
  <h2>용현·학익·숭의·문학 생활권</h2>
  <p>
    <a href="/incheon/life/yonghyeon-hagik/">용현·학익 생활권</a>은 인하대학교를 중심으로 학생 주거지와 원룸 밀집 지역이 넓게 형성되어 있습니다.
    인하대역(인천 1호선) 주변에는 1인 가구를 위한 오피스텔과 소형 아파트가 많으며,
    피로 회복을 위한 방문형 관리 서비스 이용 수요가 꾸준합니다.
    <a href="/incheon/michuhol-gu/yonghyeon-dong/">용현동</a>과 <a href="/incheon/michuhol-gu/hagik-dong/">학익동</a>에는
    인하대병원 인근 주거지와 학익 스포원 인근 단지 아파트가 이어집니다.
    문학동·관교동 방면은 인천문학경기장 주변 주거지가 조성되어 있으며,
    숭의동은 옛 도심 특성과 신축 빌라가 공존하는 지역으로 방문 가능 주소 확인 후 예약해 주세요.
    인접한 <a href="/incheon/michuhol-gu/jemulpo-area/">제물포 지역</a>도 방문 서비스 영역에 포함됩니다.
  </p>
  <ul>
    <li><a href="/incheon/michuhol-gu/yonghyeon-dong/">용현동</a> — 인하대 인근 1인 주거 밀집</li>
    <li><a href="/incheon/michuhol-gu/hagik-dong/">학익동</a> — 스포원 인근 주거 단지</li>
    <li>숭의동·관교동 — 도심 주거 혼재 지역</li>
    <li>문학동 — 경기장 인근 주거지</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    미추홀구 전 지역은 방문 가능하나, 숙박 시설·오피스텔 입실 완료 후 예약 진행을 권장합니다.
    <a href="/incheon/michuhol-gu/jemulpo-area/">제물포 지역</a>은 동구와 경계를 공유하므로,
    정확한 주소 기반으로 방문 가능 여부를 확인해 주시기 바랍니다.
    1인 주거지(원룸·고시원·오피스텔)는 방문 전 주소 형태를 함께 알려 주시면 신속하게 안내드릴 수 있습니다.
    인접 구 안내: <a href="/incheon/jung-gu/">중구</a> | <a href="/incheon/dong-gu/">동구</a> | <a href="/incheon/namdong-gu/">남동구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주시고,
    <a href="/incheon/reservation/">예약 안내</a>, <a href="/incheon/check/">이용 전 확인사항</a>,
    <a href="/incheon/guide/">홈타이 이용 가이드</a>, <a href="/incheon/support/privacy/">개인정보처리방침</a>도 참고해 주세요.
  </p>
</section>

<section>
  <h2>미추홀구 이용 안내 — 주거 유형별 방문 가이드</h2>
  <p>
    미추홀구는 주안역 초역세권의 상업 밀집 지역부터 인하대 주변 1인 가구 주거지까지 다양한 생활 환경이 공존합니다.
    아래 유형별 안내를 참고해 방문 서비스를 이용해 주세요.
  </p>
  <ul>
    <li><strong>아파트 단지:</strong> 주안·도화·학익 대단지 아파트 — 동·호수 명확히 제공 시 방문 가능</li>
    <li><strong>오피스텔·고시원:</strong> 주안역·인하대역 주변 원룸·고시원 — 주소 확인 후 방문</li>
    <li><strong>연립·다세대 주택:</strong> 숭의·관교 구도심 빌라 — 협소 골목 여부 확인 권장</li>
    <li><strong>신축 주상복합:</strong> 주안 센트럴파크 인근 신규 단지 — 방문 원활</li>
    <li><strong>학교 기숙사:</strong> 인하대 캠퍼스 내 기숙사 — 방문 불가 주소 해당 가능, 사전 확인 필수</li>
  </ul>
  <p>
    인천 1호선 각 역의 운행 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>를 참고해 주세요.
    <a href="/incheon/station/juan-station/">주안역</a> 역세권과 <a href="/incheon/station/jemulpo-station/">제물포역</a> 역세권이
    미추홀구의 핵심 교통 거점임을 다시 한번 안내드립니다.
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 4. 연수구
# ──────────────────────────────────────────────
_yeonsu_body = """
<section>
  <h2>연수구 출장마사지·홈타이 — 송도·연수·동춘 생활권 안내</h2>
  <p>
    연수구 출장마사지·홈타이를 알아보고 계신다면, 연수구가 인천의 신도시·국제 업무 기능을 담당하는 지역임을 먼저 확인해 보세요.
    <a href="/incheon/yeonsu-gu/songdo/">송도국제도시</a>를 비롯해 <a href="/incheon/yeonsu-gu/yeonsu-dong/">연수동</a>,
    <a href="/incheon/yeonsu-gu/dongchun-dong/">동춘동</a>, 청학동, 옥련동, 선학동이 연수구의 주요 생활권을 이룹니다.
    특히 송도는 인천경제자유구역(IFEZ) 핵심 지구로,
    외국계 기업과 국제 기관이 밀집해 있어 다국적 거주자와 장기 체류 외국인 고객도 방문 서비스를 활용하는 경우가 많습니다.
    셀트리온, 삼성바이오로직스 등 바이오·제약 기업 임직원 주거 단지도 다수 위치합니다.
  </p>
  <p>
    간다GO는 연수구 전 생활권에 방문 가능하며,
    아파트·주상복합·오피스텔·게스트하우스 등 다양한 주거·숙박 형태를 방문 가능 주소로 안내하고 있습니다.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    연수구는 인천 1호선과 수인분당선(수인선 구간)이 교차하는 역세권이 발달해 있습니다.
    <a href="/incheon/station/songdo-moonlight-festival-park-station/">송도달빛축제공원역</a>은 송도 남부 개발 지구를 담당하는 인천 1호선 역입니다.
    <a href="/incheon/station/incheon-national-univ-station/">인천대입구역</a>(인천 1호선)은 인천대학교 캠퍼스와 송도 업무 지구 사이에 위치합니다.
    <a href="/incheon/station/central-park-station/">센트럴파크역</a>(인천 1호선)은 송도 센트럴파크 인근으로, 고급 주거·호텔이 밀집한 역세권입니다.
    <a href="/incheon/station/woninjae-station/">원인재역</a>(수인분당선)은 연수·동춘·옥련 방면과 연결되며,
    동춘역(인천 1호선), 선학역, 연수역도 연수구 내 주요 이동 거점입니다.
    인천 지하철 노선도와 운행 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>송도국제도시 생활권</h2>
  <p>
    <a href="/incheon/life/songdo-international-city/">송도국제도시 생활권</a>은 연수구 서쪽 매립지에 조성된 계획 신도시입니다.
    1공구부터 11공구까지 단계적으로 개발 중이며, 주거 단지·업무 단지·쇼핑몰·공원이 체계적으로 배치되어 있습니다.
    트리플스트리트, 현대프리미엄아울렛, 컨벤시아(국제회의장) 인근 호텔 등 다양한 숙박·주거 시설에서 방문형 서비스 예약이 가능합니다.
    장거리 출장·국제 회의 참석 후 피로 해소를 원하시는 분들의 문의가 많습니다.
    송도 내 아파트 단지는 동·호수 명확히 제공 시 신속한 방문 안내가 가능합니다.
    <a href="/incheon/yeonsu-gu/songdo/">송도 상세 안내</a>도 함께 참고하세요.
  </p>
</section>

<section>
  <h2>연수·동춘·청학·옥련·선학 생활권</h2>
  <p>
    <a href="/incheon/life/yeonsu-woninjae/">연수·원인재 생활권</a>은 송도 이전의 구도심 주거 지역입니다.
    <a href="/incheon/yeonsu-gu/yeonsu-dong/">연수동</a>과 <a href="/incheon/yeonsu-gu/dongchun-dong/">동춘동</a>에는
    대단지 아파트가 밀집해 있으며, 생활 편의 시설이 도보권에 갖춰져 있어 방문형 서비스 이용 환경이 좋습니다.
    청학동·옥련동은 인천 원도심과의 경계 구간으로, 소규모 주거 단지와 빌라가 혼재합니다.
    선학동은 문학경기장과 인접한 주거 지역으로, 인천 1호선 선학역을 중심으로 한 역세권 단지가 형성되어 있습니다.
    <a href="/incheon/station/woninjae-station/">원인재역</a> 인근은 수인분당선 역세권으로 경기 수원 방면과도 연결됩니다.
  </p>
  <ul>
    <li><a href="/incheon/yeonsu-gu/songdo/">송도</a> — 국제도시, 고급 주거·호텔 밀집</li>
    <li><a href="/incheon/yeonsu-gu/yeonsu-dong/">연수동</a> — 대단지 아파트, 방문 원활</li>
    <li><a href="/incheon/yeonsu-gu/dongchun-dong/">동춘동</a> — 아파트·빌라 혼재, 방문 가능</li>
    <li>청학·옥련·선학 — 구도심 주거지, 주소 확인 후 방문</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    연수구 방문 서비스 예약 시 주거 형태(아파트·오피스텔·호텔)와 정확한 동·호수를 함께 알려주시면 더 신속하게 안내드릴 수 있습니다.
    송도 내 신규 입주 단지는 단지명과 동·호수를 함께 알려 주시기 바랍니다.
    인접 구 안내: <a href="/incheon/namdong-gu/">남동구</a> | <a href="/incheon/michuhol-gu/">미추홀구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
</section>

<section>
  <h2>연수구 이용 안내 — 생활권별 방문 특성 요약</h2>
  <p>
    연수구는 송도국제도시와 구도심 주거 지역이 공존하므로, 생활권별로 방문 특성이 다릅니다.
    아래 내용을 참고해 예약을 진행해 주세요.
  </p>
  <ul>
    <li><strong>송도국제도시 1~11공구:</strong> 계획 신도시 특성상 주소 체계가 명확합니다. 공구·단지명·동·호수 제공 시 빠른 안내 가능</li>
    <li><strong>연수·동춘 구도심 아파트:</strong> 대단지 아파트 밀집, 방문 접근성 양호</li>
    <li><strong>청학·옥련 소규모 단지:</strong> 빌라·연립 혼재, 도로명 주소 정확히 제공 필요</li>
    <li><strong>선학·인천문학 인근:</strong> 스포츠 시설 인접 주거지, 방문 가능</li>
    <li><strong>송도 내 호텔·서비스드 레지던스:</strong> 체크인 완료 후 예약, 외국인 고객도 이용 가능 — 영어 의사소통 사전 확인 권장</li>
  </ul>
  <p>
    연수구 전역의 교통 및 생활 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사</a>에서 확인하실 수 있습니다.
    <a href="/incheon/station/central-park-station/">센트럴파크역</a>과 <a href="/incheon/station/incheon-national-univ-station/">인천대입구역</a> 역세권이
    송도의 핵심 거점임을 참고해 주세요.
  </p>
  <p>
    송도국제도시는 인천경제자유구역청(IFEZ) 관할 지역으로, 외국인 학교·국제기구 직원 주거단지도 위치합니다.
    연수구에서 방문 서비스를 처음 이용하시는 분은 <a href="/incheon/guide/">홈타이 이용 가이드</a>를 먼저 읽어보시기를 권장합니다.
    예약 관련 개인정보 처리 기준은 <a href="/incheon/support/privacy/">개인정보처리방침</a>에 명시되어 있으며,
    간다GO는 고객의 개인정보를 서비스 제공 목적 외에 사용하지 않습니다.
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 5. 남동구
# ──────────────────────────────────────────────
_namdong_body = """
<section>
  <h2>남동구 출장마사지 — 구월·간석·논현·소래 생활권 안내</h2>
  <p>
    남동구 출장마사지를 검색 중이시라면, 남동구가 인천시청 소재지이자 인천에서 인구 규모가 가장 큰 자치구임을 참고해 주세요.
    <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>은 인천시청·인천종합터미널이 위치한 인천의 행정·상업 중심지이며,
    <a href="/incheon/namdong-gu/ganseok-dong/">간석동</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>,
    <a href="/incheon/namdong-gu/sorae-area/">소래</a>, 만수동, 서창동, 도림동, 장수동 등이 남동구를 구성하는 주요 생활권입니다.
    구월 로데오 거리, 인천 구도심 외곽 신도시 성격의 논현·소래 지구 등 다양한 생활 환경이 공존합니다.
    간다GO는 남동구 전 생활권에 방문 가능하며, 아파트·주상복합·오피스텔 등 다양한 주거 형태를 방문 주소로 안내하고 있습니다.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    남동구의 대표 역은 <a href="/incheon/station/incheon-cityhall-station/">인천시청역</a>(인천 1호선)으로, 구월동 상권 중심에 위치합니다.
    <a href="/incheon/station/arts-center-station/">예술회관역</a>(인천 1호선)은 인천문화예술회관과 구월 아파트 단지를 연결하며,
    <a href="/incheon/station/incheon-terminal-station/">인천터미널역</a>(인천 1호선)은 인천종합터미널 이용객과 주변 상업 지구를 담당합니다.
    <a href="/incheon/station/ganseogogeori-station/">간석오거리역</a>(인천 1호선)은 간석동 주거 지구의 핵심 역입니다.
    수인분당선 라인에서는 <a href="/incheon/station/soraepogu-station/">소래포구역</a>과
    <a href="/incheon/station/incheon-nonhyeon-station/">인천논현역</a>이 남동구 남부 생활권을 커버합니다.
    인천 지하철 시간표와 노선 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하세요.
  </p>
</section>

<section>
  <h2>구월·인천시청 생활권</h2>
  <p>
    <a href="/incheon/life/guwol-incheon-cityhall/">구월·인천시청 생활권</a>은 인천의 행정·업무 중심지입니다.
    인천시청 주변에는 공공기관, 금융기관, 대형 쇼핑몰이 집중되어 있으며,
    구월동 로데오 거리 일대는 인천 최대의 유흥·외식·상업 밀집 지역 중 하나입니다.
    주변 대단지 아파트(구월·만수·간석 지구)에서 방문형 서비스 이용이 활발하게 이루어집니다.
    <a href="/incheon/namdong-gu/guwol-dong/">구월동</a> 상세 안내 페이지에서 추가 정보를 확인하실 수 있습니다.
    인천시청역·예술회관역 역세권 오피스텔도 방문 가능 주소에 포함됩니다.
  </p>
</section>

<section>
  <h2>논현·소래포구·간석·만수 생활권</h2>
  <p>
    <a href="/incheon/life/nonhyeon-sorae/">논현·소래 생활권</a>은 남동구 남부의 신개발 주거 지구입니다.
    <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a> 일대에는 인천 최대 규모의 아파트 단지 중 일부가 조성되어 있으며,
    대형 마트·학원가·스포츠 시설이 갖춰진 자족형 주거 환경입니다.
    <a href="/incheon/namdong-gu/sorae-area/">소래포구</a> 인근은 수산시장과 갯골생태공원으로 유명하며,
    소래·시흥 경계 쪽 신규 주거 단지도 방문 가능 지역에 포함됩니다.
    <a href="/incheon/namdong-gu/ganseok-dong/">간석동</a>은 인천 1호선 간석오거리역 역세권으로, 아파트·연립주택이 밀집한 구도심 주거 지역입니다.
    만수동은 남동구 중앙부의 대단지 아파트 구역으로, 만수1~6동에 걸쳐 넓은 주거 면적을 자랑합니다.
  </p>
  <ul>
    <li><a href="/incheon/namdong-gu/guwol-dong/">구월동</a> — 인천시청·로데오 인근, 방문 원활</li>
    <li><a href="/incheon/namdong-gu/ganseok-dong/">간석동</a> — 주거 밀집, 방문 가능</li>
    <li><a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a> — 신규 아파트 단지, 방문 원활</li>
    <li><a href="/incheon/namdong-gu/sorae-area/">소래</a> — 포구·생태공원 인근, 주소 확인 후 방문</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    남동구는 생활권별로 주거 형태 차이가 크므로,
    방문 주소(동·단지명·호수)를 정확히 알려주시면 안내가 빠릅니다.
    논현·소래 신개발 지역은 단지 이름을 함께 알려 주시면 방문 가능 여부를 더 빠르게 확인할 수 있습니다.
    인접 구 안내: <a href="/incheon/yeonsu-gu/">연수구</a> | <a href="/incheon/michuhol-gu/">미추홀구</a> | <a href="/incheon/bupyeong-gu/">부평구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
</section>

<section>
  <h2>남동구 이용 안내 — 생활권별 방문 특성 요약</h2>
  <p>
    남동구는 인천 최대 인구 자치구인 만큼 생활권 유형이 다양합니다.
    아래 안내를 참고해 예약해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>구월동 로데오·시청 인근:</strong> 주상복합·오피스텔 밀집, 방문 접근 편리</li>
    <li><strong>간석동 구도심 아파트:</strong> 1990~2000년대 단지 위주, 방문 가능</li>
    <li><strong>논현 신도시 단지:</strong> 수천 세대 신규 아파트, 단지명·동·호수 제공 시 빠른 안내</li>
    <li><strong>소래·만수 외곽 주거지:</strong> 빌라·연립 혼재, 도로명 주소 정확히 제공 권장</li>
    <li><strong>남동공단 인근 주거지:</strong> 산업단지 경계 지역, 주거 시설 여부 사전 확인 필수</li>
  </ul>
  <p>
    <a href="/incheon/station/incheon-cityhall-station/">인천시청역</a>과 <a href="/incheon/station/incheon-terminal-station/">인천터미널역</a> 역세권은
    남동구에서 가장 이동이 편리한 거점 지역입니다.
    인천 지하철 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하세요.
  </p>
  <p>
    남동구에서 방문형 서비스를 이용하실 때는 인천시청 인근 주상복합·오피스텔 고객,
    논현 신도시 대단지 아파트 거주자, 소래포구 인근 숙박 시설 이용자 등 다양한 유형의 고객 예약이 가능합니다.
    간다GO는 방문 전 개인정보 확인 절차를 투명하게 운영하며, 모든 예약은 고객 동의 기반으로 진행됩니다.
    자세한 안내는 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 확인해 주세요.
    방문형 관리 서비스를 처음 이용하시는 분은 <a href="/incheon/guide/">홈타이 이용 가이드</a>를 참고해 주시기 바랍니다.
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 6. 부평구
# ──────────────────────────────────────────────
_bupyeong_body = """
<section>
  <h2>부평구 출장마사지 — 부평역·삼산·산곡·청천 생활권 안내</h2>
  <p>
    부평구 출장마사지를 찾고 계신다면, 부평구가 인천에서 가장 활발한 역세권 상권을 보유한 자치구 중 하나임을 먼저 파악해 두세요.
    <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평동</a>은 수도권 전철 1호선·인천 1호선이 환승되는 <a href="/incheon/station/bupyeong-station/">부평역</a>을 중심으로
    인천 최대의 지하상가와 백화점, 재래시장이 밀집한 상업 거점입니다.
    <a href="/incheon/bupyeong-gu/samsan-dong/">삼산동</a>, <a href="/incheon/bupyeong-gu/sangok-dong/">산곡동</a>,
    <a href="/incheon/bupyeong-gu/cheongcheon-dong/">청천동</a>, <a href="/incheon/bupyeong-gu/bugae-dong/">부개동</a>,
    갈산동, 십정동이 부평구를 구성하는 주요 주거 생활권입니다.
    부평역 일대 유동 인구가 많고 오피스텔·원룸·고시원 등 1인 가구 주거 비율이 높아,
    방문형 관리 서비스 수요가 인천 내에서도 높은 편입니다.
  </p>
  <p>
    간다GO는 부평구 전 생활권을 방문 가능 지역으로 안내하고 있습니다.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    부평구의 중심은 단연 <a href="/incheon/station/bupyeong-station/">부평역</a>(1호선·인천 1호선 환승)입니다.
    인천에서 서울 방면으로의 접근성이 가장 좋은 역으로, 역 주변에 CGV·롯데백화점·부평 문화의거리가 있습니다.
    <a href="/incheon/station/bupyeong-gu-office-station/">부평구청역</a>(인천 1호선)은 부평구청과 삼산 방면 주거 지구를 담당합니다.
    <a href="/incheon/station/bugae-station/">부개역</a>(1호선)은 부개동 주거 단지 이용객의 주요 역이며,
    <a href="/incheon/station/galsan-station/">갈산역</a>(인천 1호선)과 삼산체육관역(인천 1호선)은 삼산 생활권 역세권입니다.
    <a href="/incheon/station/dongam-station/">동암역</a>(1호선)은 부평구 동부 방면 이동 거점입니다.
    인천 지하철 정보: <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>
  </p>
</section>

<section>
  <h2>부평역·부평시장 생활권</h2>
  <p>
    <a href="/incheon/life/bupyeong-station-market/">부평역·부평시장 생활권</a>은 인천 최대 환승역 중심의 초역세권입니다.
    부평역 지하 2km에 이르는 부평지하도상가가 이어지며, 역 지상부에도 먹거리·쇼핑 시설이 촘촘합니다.
    <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평동</a>과 십정동 일대에는 원룸·고시원·오피스텔이 밀집해 있어 방문형 서비스 이용 수요가 높습니다.
    부평 문화의거리와 부평시장 인근의 모텔·비즈니스호텔도 방문 가능 주소로 확인해 드릴 수 있습니다.
    숙박 시설 체크인 완료 후 예약을 진행해 주시면 원활하게 안내드릴 수 있습니다.
  </p>
</section>

<section>
  <h2>삼산·부평구청·부개·산곡·청천 생활권</h2>
  <p>
    <a href="/incheon/life/samsan-bupyeong-gu-office/">삼산·부평구청 생활권</a>은 부평구 북서쪽의 대단지 아파트 밀집 지역입니다.
    삼산 1·2택지지구에는 수천 세대 규모의 아파트 단지가 연속으로 이어지며,
    어린이공원·학교·대형 마트가 갖춰진 자족형 주거 단지입니다.
    <a href="/incheon/bupyeong-gu/bugae-dong/">부개동</a>은 부개역 역세권 아파트 단지로, 1호선 직결로 서울 방면 접근이 편리합니다.
    <a href="/incheon/life/sangok-cheongcheon/">산곡·청천 생활권</a>에는 한국GM 부평공장 인근 주거 지역과 신구 주거 단지가 혼재합니다.
    <a href="/incheon/bupyeong-gu/sangok-dong/">산곡동</a>과 <a href="/incheon/bupyeong-gu/cheongcheon-dong/">청천동</a>은
    대규모 주거 단지와 소형 빌라 지역이 함께 분포하며, 공업 시설 인근은 방문 주소 확인이 필요합니다.
  </p>
  <ul>
    <li><a href="/incheon/bupyeong-gu/bupyeong-dong/">부평동</a> — 부평역 초역세권, 방문 원활</li>
    <li><a href="/incheon/bupyeong-gu/bugae-dong/">부개동</a> — 부개역 주거 단지, 방문 가능</li>
    <li><a href="/incheon/bupyeong-gu/samsan-dong/">삼산동</a> — 대단지 아파트, 방문 원활</li>
    <li><a href="/incheon/bupyeong-gu/sangok-dong/">산곡동</a> — 주거·공업 혼재, 주소 확인 후 방문</li>
    <li><a href="/incheon/bupyeong-gu/cheongcheon-dong/">청천동</a> — 신구 주거 혼재, 방문 가능</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    부평구 방문 서비스 이용 시 주거·숙박 여부와 정확한 주소를 함께 알려 주시면 빠르게 안내드릴 수 있습니다.
    공업 시설·창고 등 비주거 시설은 방문 불가 주소이므로 사전에 주거 시설 여부를 확인해 주세요.
    인접 구 안내: <a href="/incheon/gyeyang-gu/">계양구</a> | <a href="/incheon/namdong-gu/">남동구</a> | <a href="/incheon/seo-gu/">서구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
</section>

<section>
  <h2>부평구 이용 안내 — 생활권별 방문 특성 요약</h2>
  <p>
    부평구에서 방문형 서비스를 이용하기 전, 아래 생활권별 특성을 참고해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>부평역 초역세권(부평동·십정동):</strong> 유동 인구 많고 숙박 시설 밀집, 방문 원활. 체크인 완료 후 예약 권장</li>
    <li><strong>삼산 택지지구(삼산동):</strong> 대단지 아파트, 동·호수 명확히 제공 시 방문 빠름</li>
    <li><strong>부개동 역세권:</strong> 부개역 인근 아파트 단지 중심, 방문 가능</li>
    <li><strong>산곡·청천 혼재 지역:</strong> 아파트와 소규모 공장 혼재 — 주거 시설 확인 필수</li>
    <li><strong>갈산·부평구청 인근:</strong> 구청 주변 주거·상업 혼재, 방문 가능</li>
  </ul>
  <p>
    부평구는 <a href="/incheon/station/bupyeong-station/">부평역</a>이 1호선·인천 1호선 환승역이므로,
    서울 방면에서 이동하는 고객도 부평역 인근 숙박 시설 이용 후 예약하시는 경우가 있습니다.
    인천 지하철 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하세요.
  </p>
  <p>
    부평구에서 처음 방문형 서비스를 이용하시는 분은 <a href="/incheon/guide/">홈타이 이용 가이드</a>에서 기본적인 이용 방법을 먼저 확인해 주세요.
    예약 전 확인해야 할 공통 사항은 <a href="/incheon/check/">이용 전 확인사항</a>에 정리되어 있습니다.
    부평구 인접 지역인 <a href="/incheon/gyeyang-gu/">계양구</a>·<a href="/incheon/seo-gu/">서구</a>·<a href="/incheon/namdong-gu/">남동구</a>도
    방문 가능 지역이므로, 주소가 경계 지역에 해당하는 경우 정확한 행정동을 확인해 주시기 바랍니다.
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 7. 계양구
# ──────────────────────────────────────────────
_gyeyang_body = """
<section>
  <h2>계양구 출장마사지 — 계산·작전·계양역 생활권 안내</h2>
  <p>
    계양구 출장마사지를 알아보고 계신다면, 계양구가 인천 북동부의 주거 중심 자치구임을 먼저 파악해 두세요.
    <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>, <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>,
    <a href="/incheon/gyeyang-gu/hyoseong-dong/">효성동</a>, 임학동, 계양동, 귤현동, 박촌동 등이 계양구의 주요 생활권을 이룹니다.
    인천 서구·부평구·경기 김포·부천과 인접해 있어 광역 교통 이용이 편리하며,
    인천 1호선과 수도권 전철 1호선(부평역 환승 활용)을 통해 인천 시내 및 서울 방면 이동이 가능합니다.
    계양구는 아파트 단지 비율이 높아 방문형 서비스 이용 환경이 비교적 균일하게 갖춰진 편입니다.
  </p>
  <p>
    간다GO는 계양구 전 생활권에 방문 가능합니다.
    대단지 아파트가 많은 환경이므로 동·호수를 포함한 정확한 주소를 제공해 주시면 보다 신속하게 안내드릴 수 있습니다.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    <a href="/incheon/station/gyeyang-station/">계양역</a>(인천 1호선·공항철도 환승)은 계양구의 최대 교통 거점으로,
    공항철도(AREX)를 통해 인천공항과 서울역을 직결합니다.
    계양역 근처에는 신규 오피스텔과 상업 복합 시설이 개발 중이어서 방문 수요가 꾸준히 증가하고 있습니다.
    <a href="/incheon/station/gyulhyeon-station/">귤현역</a>(공항철도)과 <a href="/incheon/station/bakchon-station/">박촌역</a>(인천 1호선)은 계양구 북부 생활권을 담당합니다.
    <a href="/incheon/station/imhak-station/">임학역</a>(인천 1호선), <a href="/incheon/station/gyesan-station/">계산역</a>(인천 1호선),
    경인교대입구역(인천 1호선), <a href="/incheon/station/jakjeon-station/">작전역</a>(인천 1호선)이 계양구 중·남부 생활권을 순서대로 관통합니다.
    인천 지하철 운행 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하세요.
  </p>
</section>

<section>
  <h2>계산·작전·효성 생활권</h2>
  <p>
    <a href="/incheon/life/gyesan-jakjeon/">계산·작전 생활권</a>은 계양구 남부의 주요 주거 상업 지역입니다.
    <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>과 <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>에는
    1990년대 조성된 대단지 아파트가 많아 안정적인 주거 환경을 형성하고 있습니다.
    계산역·작전역 주변에는 재래시장과 상업 시설이 발달해 있으며, 생활 편의 접근성이 우수합니다.
    작전역 인근에는 대형 마트와 영화관, 청소년 문화시설 등이 집중되어 있어 유동 인구도 많습니다.
    <a href="/incheon/gyeyang-gu/hyoseong-dong/">효성동</a>은 작전·계산 사이에 위치한 주거 밀집 지역으로,
    소규모 아파트와 빌라가 혼재합니다.
  </p>
</section>

<section>
  <h2>계양·귤현·박촌·임학 생활권</h2>
  <p>
    <a href="/incheon/life/gyeyang-gyulhyeon/">계양역·귤현 생활권</a>은 계양구 북부의 새로운 주거 개발 지역입니다.
    계양역 환승 기능으로 인해 공항 이용객과 서울 방면 직장인 이용 예약이 많습니다.
    귤현동과 박촌동은 최근 신축 아파트 단지가 증가하고 있으며, 개발에 따라 주거 밀도가 높아지고 있습니다.
    임학동은 임학역 주변의 구도심 성격 주거지로, 연립주택과 소형 빌라가 주를 이룹니다.
    계양테크노밸리(계양 신도시) 개발이 진행 중이며, 향후 주거 수요 증가가 예상되는 지역입니다.
    신규 입주 단지는 단지명 확인 후 방문 가능 여부를 안내드립니다.
  </p>
  <ul>
    <li><a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a> — 대단지 아파트, 방문 원활</li>
    <li><a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a> — 아파트·상가 혼재, 방문 가능</li>
    <li><a href="/incheon/gyeyang-gu/hyoseong-dong/">효성동</a> — 주거 밀집, 방문 가능</li>
    <li>계양동·귤현동·박촌동 — 신구 주거 혼재, 주소 확인 후 방문</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    계양구 방문 서비스는 전 생활권 방문 가능이나,
    계양테크노밸리 등 공사 중 지역은 입주 완료 주소 여부를 사전 확인해 주시기 바랍니다.
    인접 구 안내: <a href="/incheon/bupyeong-gu/">부평구</a> | <a href="/incheon/seo-gu/">서구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
</section>

<section>
  <h2>계양구 이용 안내 — 생활권별 방문 특성 요약</h2>
  <p>
    계양구는 인천에서 비교적 주거 환경이 균일한 편으로, 대단지 아파트 비율이 높아 방문형 서비스 이용이 편리합니다.
    아래 생활권별 특성을 참고해 예약해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>계산·작전 구도심 아파트:</strong> 1990년대 단지 위주 — 동·호수 명확히 제공 시 방문 가능</li>
    <li><strong>계양역 신개발 오피스텔:</strong> 공항철도 역세권, 신규 입주 주소 사전 확인 후 방문</li>
    <li><strong>귤현·박촌 신축 단지:</strong> 최근 입주 단지 증가 중, 단지명 확인 필요</li>
    <li><strong>효성·임학 빌라·연립:</strong> 소규모 주거지 혼재, 주소 정확히 제공 권장</li>
    <li><strong>계양테크노밸리 인근:</strong> 개발 중, 입주 완료된 주거 시설만 방문 가능</li>
  </ul>
  <p>
    계양역에서 공항철도를 이용하면 인천공항과 서울역이 직결됩니다.
    타 지역에서 계양구로 이동 시 <a href="/incheon/station/gyeyang-station/">계양역</a>을 기준점으로 삼으시면 편리합니다.
    인천 지하철 정보는 <a href="https://www.ictr.or.kr/" target="_blank" rel="noopener nofollow">인천교통공사 공식 사이트</a>에서 확인하세요.
  </p>
  <p>
    계양구에서 방문 서비스를 예약할 때는 인천 1호선 역세권 기준으로 주소를 안내해 주시면 더욱 빠른 방문이 가능합니다.
    계산역·작전역·임학역·계양역 중 가장 가까운 역을 기준으로 안내해 주시면 됩니다.
    <a href="/incheon/guide/">홈타이 이용 가이드</a>와 <a href="/incheon/check/">이용 전 확인사항</a>을 먼저 확인하신 후 예약해 주시기 바랍니다.
    간다GO 계양구 방문 서비스의 개인정보 처리 기준은 <a href="/incheon/support/privacy/">개인정보처리방침</a>에 명시되어 있습니다.
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 8. 서구
# ──────────────────────────────────────────────
_seo_gu_body = """
<section>
  <h2>서구 출장마사지 — 청라·검단·검암·루원 생활권 안내</h2>
  <p>
    서구 출장마사지를 알아보고 계신다면, 서구가 인천에서 가장 넓은 면적을 가진 자치구이자 개발이 활발하게 진행 중인 지역임을 먼저 확인해 주세요.
    청라국제도시, 검단신도시, <a href="/incheon/seo-gu/geomam-dong/">검암동</a>,
    <a href="/incheon/seo-gu/luwon-area/">루원시티</a>(가정·루원), <a href="/incheon/seo-gu/seongnam-dong/">석남동</a>,
    가좌동, <a href="/incheon/seo-gu/gajeong-dong/">가정동</a>, 원당·당하·마전 등 다양한 생활권이 서구 전역에 넓게 분포합니다.
    2026년 7월 행정구역 개편 시 검단·원당·당하·마전·검암 일부는 <strong>검단구(가칭)</strong>로 분리될 예정이므로 참고해 두시기 바랍니다.
    간다GO는 서구 전 생활권에 방문 가능하며, 각 생활권별 방문 조건은 아래를 확인해 주세요.
  </p>
</section>

<section>
  <h2>주요 역세권 안내</h2>
  <p>
    서구는 인천 1호선과 공항철도, 검단 도시철도(예정)가 교차하는 다양한 역세권을 보유합니다.
    <a href="/incheon/station/cheongna-international-city-station/">청라국제도시역</a>(인천 1호선)은 청라 생활권의 핵심 거점이며,
    <a href="/incheon/station/gajeong-station/">가정역</a>(인천 1호선)과 <a href="/incheon/station/seongnam-station/">석남역</a>(인천 1호선)은
    루원·가정·석남 생활권을 담당합니다.
    <a href="/incheon/station/seo-gu-office-station/">서구청역</a>(인천 1호선)은 가정동 서구청 인근의 역세권입니다.
    <a href="/incheon/station/geomam-station/">검암역</a>(공항철도)은 검암·루원 생활권과 공항 방면 연결 거점입니다.
    검단 방면으로는 <a href="/incheon/station/geomdan-sageori-station/">검단사거리역</a>,
    <a href="/incheon/station/wanjeong-station/">완정역</a>, <a href="/incheon/station/geomdan-oryu-station/">검단오류역</a>이 운행 중입니다.
    서구 관련 공식 교통·행정 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>청라국제도시 생활권</h2>
  <p>
    <a href="/incheon/life/cheongna-international-city/">청라국제도시 생활권</a>은 서구 서부의 계획 신도시로,
    호수공원을 중심으로 대단지 아파트와 상업 시설이 계획적으로 배치되어 있습니다.
    <a href="/incheon/seo-gu/cheongna/">청라</a>는 인천 내에서도 고급 주거 단지로 분류되며,
    이주 가족 및 외국인 주재원 거주 비율이 높습니다.
    청라국제도시역 주변 상업 지구와 호수공원 인근 오피스텔·주상복합이 방문 가능 주소의 주를 이룹니다.
    롯데마트·이마트·CGV 등 편의시설이 갖춰져 있으며, 청라 아파트 단지 내 방문 서비스 이용이 활발합니다.
  </p>
</section>

<section>
  <h2>검단신도시·검암·루원·가정·석남 생활권</h2>
  <p>
    <a href="/incheon/life/geomdan-newtown/">검단신도시 생활권</a>은 서구 북부의 대규모 택지 개발 지역입니다.
    <a href="/incheon/seo-gu/geomdan-area/">검단</a> 원당·당하·마전 일대에는 수만 세대 규모의 신규 아파트 단지가 입주 중이며,
    도시 기반 시설이 지속 확충되고 있습니다.
    <a href="/incheon/life/geomam-ara/">검암·아라 생활권</a>의 <a href="/incheon/seo-gu/geomam-dong/">검암동</a>은
    공항철도 검암역 역세권으로, 청라와 인천공항 사이의 교통 허브 역할을 합니다.
    <a href="/incheon/life/luwon-gajeong/">루원·가정 생활권</a>의 <a href="/incheon/seo-gu/luwon-area/">루원시티</a>는
    가정역 주변 도시재생 사업으로 조성된 신규 주거·상업 복합 단지입니다.
    <a href="/incheon/seo-gu/seongnam-dong/">석남동</a>과 <a href="/incheon/seo-gu/gajeong-dong/">가정동</a>은
    인천 1호선 라인의 주거 지역으로 방문 접근이 양호합니다.
  </p>
  <ul>
    <li><a href="/incheon/seo-gu/cheongna/">청라</a> — 신도시 고급 주거, 방문 원활</li>
    <li><a href="/incheon/seo-gu/geomdan-area/">검단</a> — 입주 신규 단지, 방문 가능 (주소 확인)</li>
    <li><a href="/incheon/seo-gu/geomam-dong/">검암</a> — 공항철도 역세권, 방문 가능</li>
    <li><a href="/incheon/seo-gu/luwon-area/">루원</a> — 도시재생 신규 단지, 방문 원활</li>
    <li><a href="/incheon/seo-gu/seongnam-dong/">석남</a> — 주거·공업 혼재, 주소 확인 후 방문</li>
  </ul>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    서구는 개발 중인 지역이 많아 신규 아파트 입주 주소·단지명을 함께 알려주시면 방문 가능 여부를 신속하게 확인해 드릴 수 있습니다.
    석남·가좌 일대 공업 혼재 지역은 주거 시설 여부를 사전에 확인해 주시기 바랍니다.
    인접 구 안내: <a href="/incheon/gyeyang-gu/">계양구</a> | <a href="/incheon/bupyeong-gu/">부평구</a>
  </p>
  <p>
    정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
</section>

<section>
  <h2>서구 이용 안내 — 생활권별 방문 특성 요약</h2>
  <p>
    서구는 개발 현황에 따라 생활권별 방문 조건이 다소 다릅니다.
    아래 안내를 참고해 예약해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>청라국제도시 아파트·오피스텔:</strong> 신도시 계획형, 주소 체계 명확 — 방문 원활</li>
    <li><strong>검단신도시 신규 입주 단지:</strong> 단지명·동·호수 필수 제공, 미입주 동은 방문 불가</li>
    <li><strong>검암 오피스텔·아파트:</strong> 공항철도 검암역 역세권, 방문 가능</li>
    <li><strong>루원시티 주상복합:</strong> 신규 복합 단지, 방문 원활</li>
    <li><strong>석남·가좌 공업 혼재 지역:</strong> 공장·창고 인근 주거지 방문 가능, 비주거 시설 방문 불가</li>
  </ul>
  <p>
    서구는 인천에서 면적이 가장 넓어 생활권 간 이동 시간 차이가 큽니다.
    청라와 검단 간 이동은 20~30분 이상 소요될 수 있으므로, 방문 위치를 명확히 알려 주시면 더 정확한 안내가 가능합니다.
    서구 관련 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하세요.
  </p>
  <p>
    서구는 2026년 개편 이후 검단구(가칭)가 분리될 예정이나, 현재는 전 지역이 서구 소속이므로
    검단·원당·당하 등 지역도 동일하게 서구 기준으로 예약 문의해 주시면 됩니다.
    서구 방문 서비스 예약 관련 개인정보 안내는 <a href="/incheon/support/privacy/">개인정보처리방침</a>을,
    방문형 서비스의 전반적인 이용 방법은 <a href="/incheon/guide/">홈타이 이용 가이드</a>를 참고해 주세요.
    인접 구: <a href="/incheon/gyeyang-gu/">계양구</a> | <a href="/incheon/bupyeong-gu/">부평구</a>
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 9. 강화군
# ──────────────────────────────────────────────
_ganghwa_body = """
<section>
  <h2>강화군 출장마사지 — 강화읍·길상·화도 생활권 사전 확인 안내</h2>
  <p>
    강화군 출장마사지 방문을 원하신다면, 강화군의 지리적 특성과 방문 조건을 반드시 사전에 확인해 주시기 바랍니다.
    강화군은 인천광역시 관할이지만, 강화도라는 섬 지형으로 인해
    김포 방면 강화대교 또는 초지대교를 통해 차량으로 진입해야 합니다.
    역세권 기반의 도심형 이동과 달리, 강화군 방문은 <strong>차량 이동 기준</strong>으로 이동 시간을 산정하며,
    출발지에서 목적지까지의 이동 거리에 따라 추가 이동비가 발생합니다.
    방문 가능 주소 여부, 이동 시간, 추가 이동비는 예약 전 반드시 확인해 주시기 바랍니다.
  </p>
  <p>
    강화군의 주요 방문 가능 생활권은 강화읍, 선원면, 불은면, 길상면, 화도면, 양도면, 내가면, 하점면 일대입니다.
    강화군 공식 관련 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>방문 가능 지역 및 이동 조건</h2>
  <p>
    강화군 방문 서비스는 아래 사항을 예약 전 반드시 확인해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>차량 이동 기준:</strong> 강화도 진입은 강화대교(북쪽) 또는 초지대교(남쪽)를 통한 차량 이동만 가능합니다.</li>
    <li><strong>추가 이동비 발생:</strong> 이동 거리와 소요 시간에 따라 추가 이동비가 산정됩니다. 예약 전 정확한 금액을 확인해 주세요.</li>
    <li><strong>방문 가능 주소 확인:</strong> 펜션·게스트하우스·민박 등 숙박 시설과 주거 시설 모두 방문 가능하나, 외딴 지역 단독 민박은 별도 확인이 필요합니다.</li>
    <li><strong>예약 가능 시간:</strong> 심야 시간대 강화 방면 방문은 제한될 수 있으니, 가능 시간대를 예약 전 먼저 확인해 주시기 바랍니다.</li>
    <li><strong>도착 시간 여유:</strong> 교통 상황에 따라 이동 시간이 달라질 수 있으므로, 방문 희망 시간보다 여유롭게 예약해 주세요.</li>
  </ul>
</section>

<section>
  <h2>강화읍·선원·불은·길상 생활권</h2>
  <p>
    <a href="/incheon/ganghwa-gun/ganghwa-eup/">강화읍</a>은 강화군의 행정 중심지로,
    고려궁지·강화산성·강화풍물시장 등 역사 문화 자원이 집중된 지역입니다.
    강화읍내에는 숙박 시설(모텔·펜션·게스트하우스)이 다수 위치하여 방문형 서비스 이용이 가능합니다.
    강화읍은 강화대교 진입 후 가장 먼저 닿는 중심가로, 이동 시간이 상대적으로 짧은 편입니다.
    선원면과 불은면은 강화읍 남쪽으로 이어지는 농촌·주거 혼재 지역입니다.
    길상면은 초지대교 진입 후 가장 먼저 만나는 생활권으로,
    초지진·광성보 등 역사 유적지 인근에 펜션 시설이 많아 주말 방문 수요가 있습니다.
  </p>
</section>

<section>
  <h2>화도·양도·내가·하점 생활권</h2>
  <p>
    화도면과 양도면은 강화도 남부의 농촌 지역으로, 마니산(참성단)이 위치한 생태·역사 지역입니다.
    마니산 인근 펜션·캠핑장 숙박 시설에서 방문형 서비스를 원하시는 경우
    이동 거리와 추가 이동비를 반드시 사전에 확인해 주시기 바랍니다.
    내가면과 하점면은 강화도 북부의 농촌 생활권으로,
    외포리·창후리 등 도선 선착장 인근 지역이 포함됩니다.
    강화 북부 지역은 군 접경 지역과 인접해 있어 방문 가능 주소 확인이 더욱 중요합니다.
    강화도 내 전원주택·농어촌 민박도 방문 가능 주소로 검토 가능하나,
    위치에 따라 방문 거절이 될 수 있으므로 반드시 사전 문의를 권장합니다.
  </p>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    강화군 방문 예약 시 아래 정보를 미리 준비해 주시면 신속하게 안내드릴 수 있습니다.
  </p>
  <ul>
    <li>방문 목적 주소 (도로명 주소 전체, 시설명 포함)</li>
    <li>원하시는 방문 시간대 (평일·주말, 주간·야간 구분)</li>
    <li>숙박 시설 이용 여부 및 체크인 완료 여부</li>
  </ul>
  <p>
    방문 가능 여부와 추가 이동비, 예약 가능 시간 확인은 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락 주시기 바랍니다.
    이용 전 공통 확인사항은 <a href="/incheon/check/">이용 전 확인사항</a>을,
    예약 절차는 <a href="/incheon/reservation/">예약 안내</a>를 참고해 주세요.
    개인정보 처리 기준은 <a href="/incheon/support/privacy/">개인정보처리방침</a>에 안내되어 있습니다.
    홈타이 이용 전반은 <a href="/incheon/guide/">홈타이 이용 가이드</a>를 참고해 주세요.
    인접 지역 안내: <a href="/incheon/ganghwa-gun/ganghwa-eup/">강화읍 생활권</a> | <a href="/incheon/life/ganghwa/">강화 생활권 안내</a>
  </p>
</section>

<section>
  <h2>강화군 이용 안내 — 시설 유형별 방문 가이드</h2>
  <p>
    강화군에서 방문형 서비스를 이용하기 전, 시설 유형별 안내 사항을 꼭 확인해 주시기 바랍니다.
  </p>
  <ul>
    <li><strong>강화읍내 모텔·비즈니스호텔:</strong> 체크인 완료 후 예약 가능. 도심 접근성 가장 양호</li>
    <li><strong>펜션·게스트하우스:</strong> 강화읍·길상·화도 일대 펜션 — 방문 가능, 정확한 도로명 주소 필수</li>
    <li><strong>농촌 민박·한옥 스테이:</strong> 방문 거리·이동비 사전 확인 후 예약 가능 여부 결정</li>
    <li><strong>캠핑장·글램핑:</strong> 차량 진입 조건과 주소 확인 후 안내, 시설 환경에 따라 방문 불가 가능</li>
    <li><strong>일반 거주 주택:</strong> 강화읍 및 각 면 일대 — 차량 이동 기준 추가 이동비 발생</li>
  </ul>
  <p>
    강화군은 버스 노선이 제한적이어서 차량 이동이 주된 수단입니다.
    강화군 관련 공식 정보 및 주요 관광지 안내는
    <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하실 수 있습니다.
    인접 지역 참고: <a href="/incheon/seo-gu/">서구</a> | <a href="/incheon/gyeyang-gu/">계양구</a>
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 10. 옹진군
# ──────────────────────────────────────────────
_ongjin_body = """
<section>
  <h2>옹진군 출장마사지 — 영흥·자월·백령 도서 지역 사전 확인 안내</h2>
  <p>
    옹진군은 인천광역시 관할의 도서(섬) 지역으로,
    영흥면·북도면·백령면·대청면·덕적면·자월면·연평면 등 다수의 섬으로 구성됩니다.
    옹진군 출장마사지 방문은 일반 도심형 서비스와 달리,
    <strong>방문 가능 여부·이동 수단·소요 시간·추가 비용을 예약 전 반드시 사전 확인</strong>해야 합니다.
    각 섬에 따라 여객선 운항 시간, 도선 이용 가능 여부, 기상 조건 등이 방문 가능성에 직접적인 영향을 미칩니다.
    방문형 관리 서비스를 원하신다면 가능 여부부터 먼저 문의해 주시기 바랍니다.
  </p>
  <p>
    옹진군 여객선 및 도서 접근 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하실 수 있습니다.
  </p>
</section>

<section>
  <h2>도서 지역 방문 조건 — 반드시 사전 확인 필수</h2>
  <p>
    옹진군 각 섬 방문은 다음 조건을 모두 사전에 확인해야 합니다.
  </p>
  <ul>
    <li><strong>방문 가능 여부:</strong> 섬별로 방문 가능 여부가 다르므로, 목적 섬 이름을 먼저 알려 주세요.</li>
    <li><strong>이동 가능 시간:</strong> 여객선 운항 시간표에 따라 방문 가능 시간대가 결정됩니다. 왕복 운항 시간을 반드시 확인해 주세요.</li>
    <li><strong>사전 예약 필수:</strong> 당일 예약은 불가하며, 충분한 사전 예약 기간이 필요합니다.</li>
    <li><strong>추가 비용 확인:</strong> 여객선 이용, 장거리 이동에 따른 추가 비용이 발생하며, 예약 전 정확한 금액을 안내드립니다.</li>
    <li><strong>기상 조건:</strong> 기상 악화 시 여객선 결항으로 방문이 취소될 수 있습니다.</li>
    <li><strong>숙박 확인:</strong> 당일 왕복이 불가한 경우 숙박 시설을 이용 중이어야 예약이 가능합니다.</li>
  </ul>
</section>

<section>
  <h2>영흥면·자월면 생활권</h2>
  <p>
    영흥면(영흥도)은 영흥대교로 육지와 연결된 섬으로, 인천 옹진군 중 접근이 상대적으로 편리한 지역입니다.
    영흥화력발전소 및 캠핑·펜션 시설이 발달해 있으며,
    주말 방문객을 위한 숙박 시설에서 방문형 서비스 문의가 들어오기도 합니다.
    차량 접근이 가능하나 이동 거리가 길어 추가 이동비 확인이 필요합니다.
    영흥대교를 통해 경기 안산 방면에서도 진입이 가능하여, 서울·수도권 방문객이 이용하는 경우도 있습니다.
    <a href="/incheon/ongjin-gun/ongjin-area/">옹진 생활권 안내</a>도 함께 참고해 주세요.
    자월면(자월도)은 인천항 여객터미널에서 여객선을 이용해야 하므로,
    운항 시간 내 방문이 가능한지 사전 조율이 필수입니다.
    자월도·이작도·승봉도·덕적도 등 자월면 소속 섬들은 섬마다 이동 조건이 다릅니다.
  </p>
</section>

<section>
  <h2>백령면·대청면·덕적면·연평면 생활권</h2>
  <p>
    백령도(백령면)는 인천에서 가장 멀리 위치한 서해 최북단 섬으로,
    여객선으로 약 4시간 이상 소요됩니다.
    백령도는 최근 관광객이 늘고 펜션·민박 시설이 발전하고 있으나,
    방문형 서비스 이용을 위해서는 이동 조건과 비용을 충분히 사전에 확인하셔야 합니다.
    대청도(대청면)는 백령도 인근 섬이며, 덕적도(덕적면)는 덕적군도의 중심 섬으로 여름 피서지로 유명합니다.
    덕적도는 소야도·문갑도 등 인근 섬으로의 추가 도선 이동이 필요할 수 있습니다.
    연평도(연평면)는 서해 NLL 인근 군사 접경 지역으로,
    방문 조건이 일반 도서 지역보다 훨씬 엄격합니다.
    이들 지역은 방문 가능 여부와 이동 조건이 매우 복잡하므로,
    예약 전 충분한 사전 상담이 필요합니다.
  </p>
</section>

<section>
  <h2>예약 전 확인사항 및 이용 안내</h2>
  <p>
    옹진군 방문 서비스는 모든 경우 사전 예약 및 확인이 필수입니다.
    당일·즉시 방문 서비스는 제공되지 않으므로 충분한 여유 시간을 두고 문의해 주시기 바랍니다.
  </p>
  <ul>
    <li>방문 희망 섬 이름과 주소 (리·숙박 시설명 포함)</li>
    <li>방문 희망 날짜와 시간대</li>
    <li>숙박 시설 여부 및 체크인 완료 예정 시간</li>
    <li>여객선 운항 일정 사전 확인 여부</li>
  </ul>
  <p>
    방문 가능 여부, 이동 가능 시간, 추가 비용 확인은 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> |
    <a href="/incheon/guide/">홈타이 이용 가이드</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
    <br>인접 지역: <a href="/incheon/ganghwa-gun/">강화군 안내</a> | <a href="/incheon/life/ongjin-islands/">옹진 도서 생활권</a>
  </p>
</section>

<section>
  <h2>옹진군 이용 안내 — 섬별 접근 조건 요약</h2>
  <p>
    옹진군 각 섬의 접근 조건은 크게 세 가지로 구분됩니다. 방문 전 반드시 해당 섬의 접근 방법을 확인해 주세요.
  </p>
  <ul>
    <li><strong>영흥도:</strong> 영흥대교 차량 진입 가능 — 비교적 방문 접근 용이, 추가 이동비 발생</li>
    <li><strong>덕적도·자월도·이작도·승봉도:</strong> 인천항 여객터미널 여객선 이용 — 운항 일정 확인 필수, 사전 예약 1주일 이상 권장</li>
    <li><strong>백령도·대청도·연평도:</strong> 장거리 여객선 이용, 편도 2~4시간 이상 — 방문 가능 여부 개별 상담 필수</li>
  </ul>
  <p>
    옹진군 여객선 이용 시 인천 연안여객터미널(인천항 국제여객터미널 인근)에서 출항하며,
    출항 일정과 기상 조건에 따라 방문 일정이 변경될 수 있습니다.
    이용 전 여객선 예약과 별도로 방문 서비스 예약을 사전에 진행해 주시기 바랍니다.
    옹진군 도서 지역 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하세요.
    인접 지역 참고: <a href="/incheon/ganghwa-gun/">강화군</a> | <a href="/incheon/seo-gu/">서구</a>
  </p>
</section>
"""

# ──────────────────────────────────────────────
# 색인 대상 10개 페이지
# ──────────────────────────────────────────────
PAGES = [
    create_page(
        path="incheon/jung-gu/",
        title="중구 출장마사지｜동인천·영종·인천공항 생활권 안내",
        desc="중구 출장마사지 예약 전 동인천, 신포, 영종, 운서, 인천공항 생활권을 확인하세요.",
        h1="중구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("중구", "")],
        body_content=_jung_gu_body,
    ),
    create_page(
        path="incheon/dong-gu/",
        title="동구 출장마사지｜송림·송현·동인천 인접 생활권 안내",
        desc="동구 출장마사지 예약 전 송림, 송현, 화수, 화평, 배다리 생활권을 확인하세요.",
        h1="동구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("동구", "")],
        body_content=_dong_gu_body,
    ),
    create_page(
        path="incheon/michuhol-gu/",
        title="미추홀구 출장마사지｜주안·도화·용현·학익 생활권 안내",
        desc="미추홀구 출장마사지 예약 전 주안, 도화, 용현, 학익, 숭의, 문학 생활권을 확인하세요.",
        h1="미추홀구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("미추홀구", "")],
        body_content=_michuhol_body,
    ),
    create_page(
        path="incheon/yeonsu-gu/",
        title="연수구 출장마사지｜송도·연수·동춘 홈타이 안내",
        desc="연수구 출장마사지·홈타이 예약 전 송도국제도시, 연수, 동춘, 선학 생활권을 확인하세요.",
        h1="연수구 출장마사지·홈타이 안내",
        breadcrumb=[("인천", "/incheon/"), ("연수구", "")],
        body_content=_yeonsu_body,
    ),
    create_page(
        path="incheon/namdong-gu/",
        title="남동구 출장마사지｜구월·간석·논현·소래 생활권 안내",
        desc="남동구 출장마사지 예약 전 구월, 간석, 논현, 소래포구, 만수 생활권을 확인하세요.",
        h1="남동구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("남동구", "")],
        body_content=_namdong_body,
    ),
    create_page(
        path="incheon/bupyeong-gu/",
        title="부평구 출장마사지｜부평역·삼산·산곡·청천 생활권 안내",
        desc="부평구 출장마사지 예약 전 부평역, 삼산, 부개, 산곡, 청천 생활권을 확인하세요.",
        h1="부평구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("부평구", "")],
        body_content=_bupyeong_body,
    ),
    create_page(
        path="incheon/gyeyang-gu/",
        title="계양구 출장마사지｜계산·작전·계양역 생활권 안내",
        desc="계양구 출장마사지 예약 전 계산, 작전, 효성, 계양역, 귤현, 박촌 생활권을 확인하세요.",
        h1="계양구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("계양구", "")],
        body_content=_gyeyang_body,
    ),
    create_page(
        path="incheon/seo-gu/",
        title="서구 출장마사지｜청라·검단·검암·루원 생활권 안내",
        desc="서구 출장마사지 예약 전 청라, 검단신도시, 검암, 루원, 가정, 석남 생활권을 확인하세요.",
        h1="서구 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("서구", "")],
        body_content=_seo_gu_body,
    ),
    create_page(
        path="incheon/ganghwa-gun/",
        title="강화군 출장마사지｜강화읍·길상·화도 생활권 안내",
        desc="강화군 출장마사지 방문 전 차량 이동 기준, 추가 이동비, 방문 가능 주소를 사전 확인하세요.",
        h1="강화군 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("강화군", "")],
        body_content=_ganghwa_body,
    ),
    create_page(
        path="incheon/ongjin-gun/",
        title="옹진군 출장마사지｜영흥·자월·백령 도서 지역 안내",
        desc="옹진군 출장마사지 방문 전 섬별 이동 가능 여부, 추가 비용, 사전 예약 조건을 확인하세요.",
        h1="옹진군 출장마사지",
        breadcrumb=[("인천", "/incheon/"), ("옹진군", "")],
        body_content=_ongjin_body,
    ),

    # ──────────────────────────────────────────
    # 2026 개편 대비 draft 페이지 3개 (noindex)
    # ──────────────────────────────────────────
    {
        "path": "incheon/jemulpo-gu/",
        "title": "제물포구 출장마사지 (2026년 개편 예정)｜중구·동구 통합 안내",
        "desc": "제물포구(가칭)는 2026년 7월 개편 예정. 현재는 중구·동구로 안내합니다.",
        "h1": "제물포구 출장마사지 (2026년 개편 예정)",
        "breadcrumb": [("인천", "/incheon/"), ("제물포구(예정)", "")],
        "noindex": True,
        "body": """
<section>
  <h2>제물포구(가칭) 개편 안내 — 2026년 7월 시행 예정</h2>
  <p>
    제물포구(가칭)는 인천광역시 행정구역 개편 계획에 따라 <strong>2026년 7월 1일을 기준으로 신설될 예정인 자치구</strong>입니다.
    현재 시점(2026년 6월)에서는 아직 시행 전이므로, 이 지역의 출장마사지 방문 서비스는 기존 자치구 기준으로 안내드립니다.
    개편 후 이 페이지에서 제물포구 통합 안내가 제공될 예정입니다.
  </p>
  <p>
    제물포구 편입 예정 지역은 크게 두 구에서 통합됩니다.
  </p>
  <ul>
    <li><strong>중구 내륙권</strong> (동인천·신포·월미도·연안부두 일대) — 현재 <a href="/incheon/jung-gu/">중구 출장마사지 안내</a> 참고</li>
    <li><strong>동구 전역</strong> (송림·송현·화수·화평·금곡·만석·배다리 일대) — 현재 <a href="/incheon/dong-gu/">동구 출장마사지 안내</a> 참고</li>
  </ul>
  <p>
    <a href="/incheon/station/jemulpo-station/">제물포역</a>과 <a href="/incheon/station/dongincheon-station/">동인천역</a> 역세권을 포함하는 지역으로,
    동인천역은 1호선 종점으로 서울 방면 직통 노선이 운행됩니다.
    제물포역은 1호선 역으로 인천 원도심과 주안 방면의 교통 거점입니다.
    <a href="/incheon/life/dongincheon-jemulpo/">동인천·제물포 생활권 안내</a>도 함께 참고하시기 바랍니다.
  </p>
  <p>
    현재 예약 및 방문 가능 여부는 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주시고,
    <a href="/incheon/michuhol-gu/jemulpo-area/">제물포 지역 안내</a>도 참고하시기 바랍니다.
    인천광역시 행정구역 개편 관련 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
  <p>
    개편 시행 이전까지 이 페이지는 검색 색인에서 제외(noindex) 처리됩니다.
    제물포구 관련 이용 안내가 필요하신 경우 <a href="/incheon/jung-gu/">중구 출장마사지 안내</a> 또는
    <a href="/incheon/dong-gu/">동구 출장마사지 안내</a>를 이용해 주시기 바랍니다.
    간다GO는 행정구역 개편 일정에 맞추어 안내 페이지를 지속 업데이트할 예정입니다.
    예약 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락해 주시기 바랍니다.
  </p>
</section>
""",
    },
    {
        "path": "incheon/yeongjong-gu/",
        "title": "영종구 출장마사지 (2026년 개편 예정)｜영종·운서·인천공항 편입 안내",
        "desc": "영종구(가칭)는 2026년 7월 개편 예정. 현재는 중구 영종·운서·공항 생활권으로 안내합니다.",
        "h1": "영종구 출장마사지 (2026년 개편 예정)",
        "breadcrumb": [("인천", "/incheon/"), ("영종구(예정)", "")],
        "noindex": True,
        "body": """
<section>
  <h2>영종구(가칭) 개편 안내 — 2026년 7월 시행 예정</h2>
  <p>
    영종구(가칭)는 인천광역시 행정구역 개편 계획에 따라 <strong>2026년 7월 1일을 기준으로 신설될 예정인 자치구</strong>입니다.
    현재 시점(2026년 6월)에서는 아직 시행 전이므로, 이 지역의 출장마사지 방문 서비스는 기존 중구 기준으로 안내드립니다.
    영종도·운서·인천공항 일대는 현재 중구 행정구역 소속이며, 개편 이후 영종구로 분리될 예정입니다.
  </p>
  <p>
    영종구 편입 예정 지역은 다음과 같습니다.
  </p>
  <ul>
    <li><strong>영종도 전역</strong> (영종동·운서동·중산동·운북동·을왕동·남북동 등) — 현재 <a href="/incheon/jung-gu/yeongjong-area/">영종 생활권 안내</a> 참고</li>
    <li><strong>운서 일대</strong> — 현재 <a href="/incheon/jung-gu/unseo-dong/">운서동 안내</a> 참고</li>
    <li><strong>인천국제공항 권역</strong> — 현재 <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 생활권 안내</a> 참고</li>
  </ul>
  <p>
    <a href="/incheon/station/unseo-station/">운서역</a>, <a href="/incheon/station/yeongjong-station/">영종역</a>,
    <a href="/incheon/station/incheon-airport-terminal-1-station/">인천공항1터미널역</a> 역세권이 해당 지역에 포함됩니다.
    영종도는 인천대교 또는 공항철도(AREX)를 통해 육지와 연결되어 있으며,
    방문 시 이동 시간 및 추가 이동비 조건을 사전에 확인해 주시기 바랍니다.
    인천공항 인근 호텔·리조트 이용 고객 및 영종도 주거 단지 주민 방문 모두 가능합니다.
  </p>
  <p>
    방문 가능 여부 및 이동 조건은 <a href="/incheon/jung-gu/">중구 출장마사지 안내 페이지</a>를 참고하시거나,
    <a href="tel:0508-202-4719">0508-202-4719</a>로 직접 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
  <p>
    인천광역시 개편 일정 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하세요.
    개편 시행 이전까지 이 페이지는 검색 색인에서 제외(noindex) 처리됩니다.
    영종·운서·공항 지역의 현재 방문 서비스는 <a href="/incheon/jung-gu/">중구 출장마사지 안내</a>를 이용해 주시기 바랍니다.
    간다GO는 행정구역 개편에 맞춰 안내 페이지를 업데이트할 예정입니다.
    예약 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락해 주시기 바랍니다.
  </p>
</section>
""",
    },
    {
        "path": "incheon/geomdan-gu/",
        "title": "검단구 출장마사지 (2026년 개편 예정)｜검단·원당·당하·마전·검암 편입 안내",
        "desc": "검단구(가칭)는 2026년 7월 개편 예정. 현재는 서구 검단·검암 생활권으로 안내합니다.",
        "h1": "검단구 출장마사지 (2026년 개편 예정)",
        "breadcrumb": [("인천", "/incheon/"), ("검단구(예정)", "")],
        "noindex": True,
        "body": """
<section>
  <h2>검단구(가칭) 개편 안내 — 2026년 7월 시행 예정</h2>
  <p>
    검단구(가칭)는 인천광역시 행정구역 개편 계획에 따라 <strong>2026년 7월 1일을 기준으로 신설될 예정인 자치구</strong>입니다.
    현재 시점(2026년 6월)에서는 아직 시행 전이므로, 이 지역의 출장마사지 방문 서비스는 기존 서구 기준으로 안내드립니다.
    검단신도시를 비롯한 원당·당하·마전 일대는 현재 서구 행정구역 소속이며, 개편 이후 검단구로 분리될 예정입니다.
  </p>
  <p>
    검단구 편입 예정 지역은 다음과 같습니다.
  </p>
  <ul>
    <li><strong>검단 일대</strong> (원당동·당하동·마전동·불로동·오류동·왕길동 등) — 현재 <a href="/incheon/seo-gu/geomdan-area/">서구 검단 생활권 안내</a> 참고</li>
    <li><strong>검암동 일부</strong> — 현재 <a href="/incheon/seo-gu/geomam-dong/">서구 검암동 안내</a> 참고</li>
  </ul>
  <p>
    <a href="/incheon/station/geomdan-sageori-station/">검단사거리역</a>,
    <a href="/incheon/station/wanjeong-station/">완정역</a>,
    <a href="/incheon/station/geomdan-oryu-station/">검단오류역</a>,
    <a href="/incheon/station/geomam-station/">검암역</a> 역세권이 해당 지역에 포함됩니다.
    검단신도시는 수만 세대 규모의 신규 아파트 단지가 입주 중인 지역으로, 입주 완료된 단지는 방문 가능합니다.
    공사 중인 동·호는 방문이 불가하므로, 입주 완료 여부를 사전에 확인해 주시기 바랍니다.
    <a href="/incheon/life/geomdan-newtown/">검단신도시 생활권 안내</a>도 함께 확인하시기 바랍니다.
  </p>
  <p>
    현재 방문 가능 여부 및 이동 조건은 <a href="/incheon/seo-gu/">서구 출장마사지 안내 페이지</a>를 참고하시거나,
    <a href="tel:0508-202-4719">0508-202-4719</a>로 직접 확인해 주세요.
    <a href="/incheon/reservation/">예약 안내</a> | <a href="/incheon/check/">이용 전 확인사항</a> | <a href="/incheon/support/privacy/">개인정보처리방침</a>
  </p>
  <p>
    인천광역시 개편 일정 공식 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 사이트</a>에서 확인하세요.
    개편 시행 이전까지 이 페이지는 검색 색인에서 제외(noindex) 처리됩니다.
    검단·원당·당하·마전 지역의 현재 방문 서비스는 <a href="/incheon/seo-gu/">서구 출장마사지 안내</a>를 이용해 주시기 바랍니다.
    간다GO는 행정구역 개편에 맞추어 안내 페이지를 업데이트할 예정입니다.
    예약 문의는 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락해 주시기 바랍니다.
  </p>
</section>
""",
    },
]
