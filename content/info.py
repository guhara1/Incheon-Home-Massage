# -*- coding: utf-8 -*-
"""인천 출장마사지 정보 페이지 — 간다GO"""


def create_page(path, title, desc, h1, breadcrumb, body_content):
    return {
        "path": path,
        "title": title,
        "desc": desc,
        "h1": h1,
        "breadcrumb": breadcrumb,
        "body": body_content,
    }


# ────────────────────────────────────────────────
# 1. 예약 안내
# ────────────────────────────────────────────────
page_reservation = create_page(
    path="incheon/reservation/",
    title="인천 출장마사지 예약 안내｜방문 예약 절차",
    desc="인천 출장마사지 예약 절차, 방문 가능 시간, 추가 이동비, 결제 방식, 예약 변경·취소 기준을 안내합니다.",
    h1="인천 출장마사지 예약 안내",
    breadcrumb=[("인천", "/incheon/"), ("예약 안내", "")],
    body_content="""
<section>
  <h2>예약 절차 개요</h2>
  <p>간다GO 인천 출장마사지 예약은 전화 또는 텔레그램 채널을 통해 진행됩니다. 예약 요청 시 방문 주소, 희망 방문 시간, 원하시는 관리 프로그램을 함께 안내해 주시면 신속하게 예약을 확정해 드립니다. 예약이 확정되면 담당 관리사가 출발 전 사전 연락을 드리므로 별도의 대기 없이 방문을 받으실 수 있습니다.</p>
  <p>예약 가능 지역은 인천광역시 전역을 기준으로 하며, 구·군별로 방문 가능 여부와 소요 시간이 다를 수 있습니다. 인천 도심 생활권인 <a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>은 당일 예약도 원활하게 처리됩니다. 반면 <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 권역</a>, <a href="/incheon/ganghwa-gun/ganghwa-eup/">강화 지역</a>, <a href="/incheon/ongjin-gun/ongjin-area/">옹진 도서 지역</a>은 추가 이동비 및 사전 예약이 필요하므로 예약 전 반드시 확인해 주시기 바랍니다.</p>
  <p>예약 채널은 두 가지입니다. 전화 상담은 빠른 예약 확정에 유리하며, 텔레그램은 텍스트로 주소·시간 등 세부 정보를 전달하기 편리합니다. 두 채널 모두 연중무휴 24시간 운영됩니다. 예약 접수 이후 담당 관리사 배정이 완료되면 확정 문자 또는 메시지를 보내드립니다.</p>
</section>

<section>
  <h2>예약 가능 시간</h2>
  <p>간다GO는 연중무휴 24시간 예약 상담이 가능합니다. 심야 및 새벽 시간대에도 상담 채널이 운영되며, 방문 서비스는 실시간 관리사 배정 상황에 따라 확정됩니다. 당일 예약도 가능하나 성수기·연휴 기간에는 예약이 조기 마감될 수 있으므로 사전 예약을 권장합니다.</p>
  <p>인천 주요 생활권인 <a href="/incheon/life/guwol-incheon-cityhall/">구월·인천시청 권역</a>이나 <a href="/incheon/life/bupyeong-station-market/">부평역·부평시장 권역</a>은 수요가 집중되는 금·토·일요일 저녁 시간대에 예약이 빠르게 소진됩니다. 원하시는 시간대를 놓치지 않으시려면 최소 2~3시간 전에 예약해 주시기를 권장합니다.</p>
  <p>신도시 지역인 <a href="/incheon/yeonsu-gu/songdo/">송도국제도시</a>와 <a href="/incheon/seo-gu/cheongna/">청라 생활권</a>은 야간 수요가 높아 주말 저녁 예약은 가급적 오후 6시 이전에 접수해 주시기 바랍니다. <a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a>처럼 외곽 지역은 방문 이동 시간을 고려해 넉넉한 여유를 두고 예약하시면 더욱 원활한 서비스를 받을 수 있습니다.</p>
</section>

<section>
  <h2>방문 가능 주소 확인</h2>
  <p>방문 가능 주소는 인천광역시 내 자택, 오피스텔, 숙소(호텔·게스트하우스·모텔), 사무실을 포함합니다. 예약 시 제공해 주신 주소를 기준으로 방문 가능 여부를 사전에 확인해 드립니다. 아파트·빌라·단독주택 등 주거 유형에 관계없이 방문 서비스가 가능합니다.</p>
  <p><a href="/incheon/yeonsu-gu/songdo/">송도국제도시</a>나 <a href="/incheon/seo-gu/cheongna/">청라 신도시</a>처럼 보안이 강화된 아파트 단지의 경우 방문 시 경비실 안내가 필요할 수 있습니다. 정확한 출입 방법을 예약 시 함께 안내해 주시면 더욱 원활한 서비스가 가능합니다. 자세한 사항은 <a href="/incheon/check/">이용 전 확인사항</a>을 참고해 주세요.</p>
  <p>호텔이나 게스트하우스를 이용 중이신 분들은 객실 번호와 프론트 안내 방법을 예약 시 함께 전달해 주세요. <a href="/incheon/jung-gu/dongincheon-area/">동인천 권역</a>이나 <a href="/incheon/jung-gu/yeongjong-area/">영종도</a>의 숙박 시설도 방문 가능합니다. 주소 확인 후 관리사가 목적지를 정확히 찾아갈 수 있도록 상세 주소와 건물명을 알려주시기 바랍니다.</p>
</section>

<section>
  <h2>추가 이동비 기준</h2>
  <p>인천 시내 주요 생활권은 기본 이동비 없이 방문이 가능하나, 거리 및 교통 상황에 따라 추가 이동비가 발생할 수 있습니다. 추가 이동비는 예약 시 사전 안내를 드리며, 동의하신 경우에만 예약이 진행됩니다. 예상치 못한 추가 비용 없이 안심하고 이용하실 수 있도록 투명하게 안내해 드립니다.</p>
  <ul>
    <li>인천 도심권(<a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화</a> 등): 기본 이동비 없음</li>
    <li>신도시 권역(<a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a>, <a href="/incheon/yeonsu-gu/songdo/">송도 외곽</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a> 등): 지역에 따라 소액 추가 이동비 발생 가능</li>
    <li><a href="/incheon/jung-gu/yeongjong-area/">영종도</a>·<a href="/incheon/jung-gu/incheon-airport-area/">인천공항 권역</a>: 도선비·통행료 포함 추가 이동비 별도 협의</li>
    <li><a href="/incheon/ganghwa-gun/ganghwa-eup/">강화군</a>·<a href="/incheon/ongjin-gun/ongjin-area/">옹진군 도서 지역</a>: 방문 가능 여부 및 이동비 사전 확인 필수</li>
  </ul>
  <p>이동비 협의는 예약 상담 과정에서 진행되며, 사전 동의 없이 청구되는 추가 비용은 없습니다. 인천광역시 행정구역 및 도서 지역 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>에서 확인하실 수 있습니다.</p>
</section>

<section>
  <h2>결제 방식</h2>
  <p>결제는 현장 서비스 완료 후 진행됩니다. 선불 또는 선입금 요구는 일절 하지 않으며, 이를 요구받으신 경우 즉시 예약 취소 후 고객센터에 연락해 주시기 바랍니다. 결제 수단은 현금 및 계좌이체를 기본으로 하며, 예약 시 결제 방법에 대한 안내를 받으실 수 있습니다. 서비스 완료 후 영수증 발행을 원하시는 경우 예약 시 미리 말씀해 주세요.</p>
  <p>부평, 구월, 송도, 주안, 청라 등 어느 지역에서 예약하셔도 동일한 결제 기준이 적용됩니다. 결제 과정에서 불편하신 사항이 있으면 <a href="/incheon/support/">고객센터</a>로 문의해 주시기 바랍니다.</p>
</section>

<section>
  <h2>예약 변경·취소 기준</h2>
  <p>예약 변경은 방문 예정 시간 기준 최소 1시간 전까지 연락 주시면 가능합니다. 방문 날짜 또는 시간 변경을 원하실 경우 가능한 한 빠르게 연락해 주시면 원하시는 일정으로 조율해 드립니다. 당일 예약 취소의 경우, 관리사가 이미 출발한 이후에는 이동 비용이 청구될 수 있습니다.</p>
  <p>부득이한 사정으로 취소가 필요하시다면 가능한 한 빠르게 고객센터(<a href="tel:0508-202-4719">0508-202-4719</a>)로 연락해 주시기 바랍니다. 고객님의 상황에 맞는 예약 일정 조율을 도와드리기 위해 최선을 다하고 있습니다.</p>
  <p>예약 관련 궁금한 사항은 <a href="/incheon/support/">고객센터</a>를 통해 언제든지 문의해 주세요. <a href="/incheon/guide/">홈타이 이용 가이드</a>도 함께 참고하시면 방문 서비스를 더욱 편안하게 이용하실 수 있습니다. 개인정보 처리 방식이 궁금하신 분은 <a href="/incheon/support/privacy/">개인정보처리방침</a>도 확인해 주세요.</p>
</section>

<section>
  <h2>지역별 예약 유의사항</h2>
  <p>인천은 도심, 신도시, 외곽 지역, 도서 지역이 혼재된 광역도시로 각 지역별로 예약 시 유의사항이 다를 수 있습니다. 아래 지역별 안내를 참고해 주세요.</p>
  <ul>
    <li><strong>도심 구도심 지역(<a href="/incheon/michuhol-gu/">미추홀구</a>·<a href="/incheon/dong-gu/">동구</a>·<a href="/incheon/jung-gu/dongincheon-area/">동인천</a>):</strong> 골목이 좁고 주차 공간이 협소한 경우가 많습니다. 차량 접근이 어려운 경우 가장 가까운 지점에서 도보로 이동할 수 있으므로 주소를 상세하게 안내해 주세요.</li>
    <li><strong>신도시 지역(<a href="/incheon/yeonsu-gu/songdo/">송도</a>·<a href="/incheon/seo-gu/cheongna/">청라</a>·<a href="/incheon/seo-gu/geomdan-area/">검단</a>):</strong> 넓은 단지 내 동·호수 확인이 중요합니다. 단지 입구에서 내부까지의 이동이 긴 경우 사전 위치 공유를 권장합니다.</li>
    <li><strong>역세권 지역(<a href="/incheon/station/bupyeong-station/">부평역</a>·<a href="/incheon/station/juan-station/">주안역</a>·<a href="/incheon/station/incheon-cityhall-station/">인천시청역</a>):</strong> 대중교통 이용 고객이 많아 방문 관리사의 이동이 유연합니다. 역 인근 오피스텔·숙박 시설 예약이 활발합니다.</li>
    <li><strong>도서 및 외곽 지역(<a href="/incheon/ganghwa-gun/ganghwa-eup/">강화군</a>·<a href="/incheon/ongjin-gun/ongjin-area/">옹진군</a>):</strong> 방문 가능 여부와 추가 이동비를 반드시 사전에 확인하시고, 배편 또는 차량 이동 일정에 맞춰 여유 있게 예약해 주세요.</li>
  </ul>
  <p>지역별 특성을 반영한 맞춤 안내를 드리기 위해 예약 시 가능하면 방문 지역의 특이사항도 함께 알려 주시면 감사하겠습니다.</p>
</section>
""",
)


# ────────────────────────────────────────────────
# 2. 이용 전 확인사항
# ────────────────────────────────────────────────
page_check = create_page(
    path="incheon/check/",
    title="인천 홈타이 이용 전 확인사항｜예약 전 체크리스트",
    desc="인천 홈타이 예약 전 방문 주소·건물 출입·숙소·공항 방문 여부·개인정보 처리 기준을 확인하세요.",
    h1="인천 홈타이 이용 전 확인사항",
    breadcrumb=[("인천", "/incheon/"), ("이용 전 확인사항", "")],
    body_content="""
<section>
  <h2>방문 주소 및 건물 출입 안내</h2>
  <p>인천 홈타이 방문 서비스를 이용하시기 전, 방문 주소와 건물 출입 방법을 정확히 안내해 주시면 더욱 원활한 서비스가 가능합니다. 아파트·오피스텔의 경우 동·호수와 함께 방문자 등록 방법이나 경비실 안내 여부를 미리 알려 주시면 대기 없이 방문이 가능합니다. 도착 예정 시간에 맞춰 로비에서 직접 맞이해 주시는 것도 빠른 서비스 시작에 도움이 됩니다.</p>
  <p><a href="/incheon/yeonsu-gu/songdo/">송도국제도시</a> 고층 주거 단지나 <a href="/incheon/seo-gu/cheongna/">청라 아파트 단지</a>처럼 외부인 출입 제한이 있는 경우, 방문 전 고객님께서 로비에서 대기하거나 경비실에 사전 등록을 해 두시면 이동 시간을 단축할 수 있습니다. <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>이나 <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a> 등 구도심 빌라·단독주택 지역은 주차 공간 안내도 함께 부탁드립니다.</p>
  <p>지하 주차장 출입이 필요한 경우나 방문객 등록 시스템이 있는 신축 아파트 단지라면 예약 전 이 점을 알려 주세요. 관리사가 원활하게 방문할 수 있도록 최선을 다하겠습니다.</p>
</section>

<section>
  <h2>자택·숙소·오피스텔·호텔 방문 기준</h2>
  <p>방문 서비스는 자택, 숙소(호텔·모텔·게스트하우스), 오피스텔, 사무실 등 다양한 공간에서 이용 가능합니다. 이용 공간의 유형에 따라 준비사항이 다소 다를 수 있으므로 아래 기준을 참고해 주세요.</p>
  <ul>
    <li><strong>자택·아파트:</strong> 인천 전역 방문 가능. 방문 전 주소 및 출입 방법 안내 필수. 약 2m x 2m 이상의 관리 공간 확보를 권장합니다.</li>
    <li><strong>오피스텔:</strong> 거주용 오피스텔에 한하며, 방문 시 로비에서 직접 안내 가능. <a href="/incheon/michuhol-gu/juan-dong/">주안역</a>이나 <a href="/incheon/station/bupyeong-station/">부평역</a> 인근 오피스텔도 방문 가능합니다.</li>
    <li><strong>호텔·숙소:</strong> 객실 번호 및 프론트 안내 방법을 예약 시 함께 전달해 주세요. <a href="/incheon/jung-gu/dongincheon-area/">동인천</a>, <a href="/incheon/jung-gu/yeongjong-area/">영종도</a> 숙박 시설도 방문 가능합니다.</li>
    <li><strong>사무실·비즈니스센터:</strong> 야간 보안으로 출입이 제한되는 경우 사전 확인이 필요합니다. 건물 출입 방법을 예약 시 상세히 안내해 주세요.</li>
  </ul>
  <p>어떤 유형의 공간이든 관리사가 도착 전 사전 연락을 드리므로 예약 시 연락 가능한 번호를 반드시 남겨 주시기 바랍니다.</p>
</section>

<section>
  <h2>공항·도서 지역 방문 가능 여부</h2>
  <p>인천국제공항 인근 및 영종도, 옹진군 도서 지역은 방문이 가능하나 추가 이동비와 사전 예약이 필수입니다. <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 권역</a>의 경우 공항대교 또는 인천대교 통행료가 이동비에 포함되며, 예약 시 사전 안내를 드립니다. 인천공항 인근에 위치한 호텔에 숙박 중이신 분들은 호텔명과 객실 번호를 예약 시 알려주시면 빠르게 처리 가능합니다.</p>
  <p><a href="/incheon/jung-gu/unseo-dong/">운서동</a>이나 <a href="/incheon/jung-gu/yeongjong-area/">영종 신도시</a>는 일반 방문과 동일한 절차로 예약 가능하나, 방문 가능 시간대와 관리사 배정 여부를 예약 시 미리 확인해 주시기 바랍니다. <a href="/incheon/ganghwa-gun/ganghwa-eup/">강화군</a>과 <a href="/incheon/ongjin-gun/ongjin-area/">옹진군 도서 지역</a>은 차량 이동 시간이 길어 방문 가능 여부와 추가 이동비를 반드시 사전에 확인하셔야 합니다.</p>
  <p>자세한 예약 절차는 <a href="/incheon/reservation/">예약 안내</a> 페이지를 참고해 주세요. 방문 가능 여부와 추가 비용은 예약 상담을 통해 명확하게 안내해 드립니다.</p>
</section>

<section>
  <h2>개인정보 처리 안내</h2>
  <p>예약 시 수집되는 개인정보(이름, 연락처, 방문 주소)는 서비스 예약·이행 목적으로만 사용되며, 서비스 완료 후 일정 기간 이후 파기됩니다. 개인정보는 제3자에게 제공되지 않으며, 고객님의 동의 없이 마케팅 목적으로 사용하지 않습니다. 상세 내용은 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 확인해 주세요.</p>
  <p>인천 어느 지역 고객이든 동일한 개인정보 보호 기준이 적용됩니다. <a href="/incheon/namdong-gu/ganseok-dong/">간석동</a>, <a href="/incheon/bupyeong-gu/samsan-dong/">삼산동</a>, <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>, <a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a> 고객님 모두 동일한 수준의 개인정보 보호를 받으실 수 있습니다.</p>
</section>

<section>
  <h2>불법·선정적 서비스 불가 안내</h2>
  <p>간다GO는 법령에서 정한 합법적인 범위 내의 방문형 관리 서비스만 제공합니다. 불법적이거나 선정적인 서비스 요청은 즉시 거절하며, 해당 예약은 취소됩니다. 서비스의 범위와 내용에 대한 사전 확인은 예약 상담을 통해 이루어지며, 서비스 범위를 벗어난 요청에 대해서는 응하지 않습니다.</p>
  <p>이 점을 명확히 이해하고 이용해 주시기 바랍니다. 궁금하신 사항은 <a href="/incheon/support/">고객센터</a>에 문의해 주세요. 서비스 이용 전 전반적인 흐름과 준비사항은 <a href="/incheon/guide/">홈타이 이용 가이드</a>에서도 확인하실 수 있습니다. 합법적이고 신뢰할 수 있는 서비스를 제공하기 위해 항상 최선을 다하겠습니다.</p>
</section>

<section>
  <h2>예약 전 최종 체크리스트</h2>
  <p>원활한 서비스 이용을 위해 예약 전 아래 항목을 모두 확인해 주세요.</p>
  <ul>
    <li>방문 주소 및 건물 출입 방법 확인 완료</li>
    <li>방문 희망 시간대 선택 완료</li>
    <li>추가 이동비 발생 여부 확인 완료(공항·도서 지역의 경우 필수)</li>
    <li>서비스 진행 공간 확보 여부 확인 완료</li>
    <li>개인정보 처리방침 확인 완료</li>
    <li>서비스 범위 및 내용 사전 확인 완료</li>
  </ul>
  <p>위 항목을 모두 확인하신 후 <a href="tel:0508-202-4719">0508-202-4719</a>로 연락하시거나, <a href="/incheon/reservation/">예약 안내</a> 페이지를 통해 예약을 진행해 주시기 바랍니다. 인천광역시 행정구역 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>에서도 참고하실 수 있습니다.</p>
</section>

<section>
  <h2>인천 생활권별 안내 링크</h2>
  <p>인천은 구마다 생활 특성이 다양합니다. 아래에서 자신이 거주하거나 방문 중인 지역 페이지로 이동해 보다 상세한 지역 정보와 방문 서비스 안내를 확인하실 수 있습니다.</p>
  <ul>
    <li><a href="/incheon/yeonsu-gu/">연수구</a> — 송도국제도시, 연수동, 동춘동 등</li>
    <li><a href="/incheon/namdong-gu/">남동구</a> — 구월, 간석, 논현, 소래포구 등</li>
    <li><a href="/incheon/bupyeong-gu/">부평구</a> — 부평역·부평시장, 삼산, 산곡, 청천 등</li>
    <li><a href="/incheon/michuhol-gu/">미추홀구</a> — 주안, 도화, 용현, 학익 등</li>
    <li><a href="/incheon/seo-gu/">서구</a> — 청라국제도시, 검단, 검암, 가정, 루원 등</li>
    <li><a href="/incheon/gyeyang-gu/">계양구</a> — 계산, 작전, 효성 등</li>
    <li><a href="/incheon/jung-gu/">중구</a> — 영종도, 운서, 인천공항, 동인천 등</li>
  </ul>
  <p>서비스 이용 전 <a href="/incheon/guide/">홈타이 이용 가이드</a>도 함께 읽어 두시면 방문 당일 더욱 편안한 경험을 하실 수 있습니다.</p>
</section>

<section>
  <h2>신뢰할 수 있는 방문 서비스 이용을 위한 안내</h2>
  <p>방문형 관리 서비스를 처음 이용하시는 분들을 위해 간다GO가 안전하고 투명하게 운영되는 원칙을 안내드립니다. 모든 관리사는 서비스 전 신원 확인 절차를 거치며, 고객님의 사생활 보호를 최우선으로 합니다. 방문 전 예약 정보 확인 연락은 반드시 등록된 번호로만 이루어집니다.</p>
  <p>간다GO는 선불 또는 선입금을 요구하지 않으며, 서비스 완료 후 현장에서만 결제가 이루어집니다. 예약 시 공유된 방문 주소는 서비스 이행 목적으로만 활용되며, 이후 별도로 저장하거나 활용하지 않습니다. 이용 과정에서 불편하거나 의심스러운 사항이 있으면 즉시 <a href="/incheon/support/">고객센터</a>로 연락해 주세요.</p>
</section>
""",
)


# ────────────────────────────────────────────────
# 3. 홈타이 이용 가이드
# ────────────────────────────────────────────────
page_guide = create_page(
    path="incheon/guide/",
    title="인천 홈타이 이용 가이드｜방문 관리 서비스 안내",
    desc="인천 홈타이 방문 서비스 흐름, 준비사항, 위생·안전 기준과 자주 묻는 질문을 안내합니다.",
    h1="인천 홈타이 이용 가이드",
    breadcrumb=[("인천", "/incheon/"), ("홈타이 이용 가이드", "")],
    body_content="""
<section>
  <h2>방문형 관리 서비스란</h2>
  <p>인천 홈타이 방문형 관리 서비스는 고객님이 계신 곳으로 전문 관리사가 직접 방문해 드리는 서비스입니다. 별도의 이동 없이 자택, 오피스텔, 호텔 등에서 편안하게 관리를 받을 수 있는 것이 가장 큰 장점입니다. 인천 전역의 <a href="/incheon/yeonsu-gu/songdo/">송도</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/seo-gu/cheongna/">청라</a> 등 주요 생활권에서 이용 가능합니다.</p>
  <p>직접 관리 센터를 방문해야 하는 번거로움 없이, 익숙한 공간에서 편안하게 관리를 받을 수 있어 바쁜 일상을 보내는 직장인, 육아 중인 부모, 출장 중인 비즈니스 고객들에게 특히 유용합니다. 방문형 관리 서비스를 처음 이용하시는 분들도 아래 가이드를 통해 이용 흐름을 쉽게 파악하실 수 있습니다.</p>
</section>

<section>
  <h2>서비스 이용 흐름</h2>
  <p>방문형 관리 서비스는 다음 순서로 진행됩니다.</p>
  <ul>
    <li><strong>1단계 — 예약 접수:</strong> 전화 또는 텔레그램으로 방문 주소, 희망 시간, 원하시는 관리 프로그램을 알려 주세요. <a href="/incheon/reservation/">예약 안내</a> 페이지에서 상세 절차를 확인하실 수 있습니다.</li>
    <li><strong>2단계 — 예약 확정:</strong> 담당 관리사 배정 후 예약이 확정되며, 확정 메시지를 보내드립니다. 출발 전 사전 연락을 통해 도착 예정 시간을 안내해 드립니다.</li>
    <li><strong>3단계 — 관리사 방문:</strong> 관리사가 고객님 주소지로 방문합니다. 건물 출입 방법에 대한 안내가 필요하다면 예약 시 알려 주시기 바랍니다.</li>
    <li><strong>4단계 — 서비스 진행:</strong> 관리사가 도착 후 간단한 상태 확인과 서비스 내용 안내를 드린 후 본 관리를 시작합니다. 개인 건강 상태나 특별 요청 사항이 있으시면 시작 전 말씀해 주세요.</li>
    <li><strong>5단계 — 서비스 완료 및 결제:</strong> 서비스 완료 후 현장 결제가 진행됩니다. 선불 요구는 없으며, 서비스 후 현금 또는 계좌이체로 결제하실 수 있습니다.</li>
  </ul>
</section>

<section>
  <h2>방문 전 준비사항</h2>
  <p>편안한 서비스 이용을 위해 방문 전 아래 사항을 준비해 주시기 바랍니다.</p>
  <ul>
    <li>충분한 공간 확보: 관리 테이블 또는 바닥 매트를 설치할 수 있는 공간(약 2m x 2m 이상)</li>
    <li>가볍고 편안한 복장 준비</li>
    <li>방문 전 샤워 및 가벼운 식사 권장(과식 직후 관리는 피해 주세요)</li>
    <li>건물 출입 방법 사전 안내(아파트·오피스텔의 경우 동·호수 및 출입 방법 포함)</li>
    <li>반려동물이 있는 경우 격리 조치 부탁드립니다</li>
  </ul>
  <p><a href="/incheon/namdong-gu/ganseok-dong/">간석동</a>이나 <a href="/incheon/bupyeong-gu/samsan-dong/">삼산동</a>처럼 주거 밀도가 높은 지역에서는 이웃을 배려한 조용한 이용을 부탁드립니다. <a href="/incheon/jung-gu/incheon-airport-area/">인천공항 주변</a> 호텔이나 <a href="/incheon/yeonsu-gu/songdo/">송도 호텔</a>을 이용 중이신 분들은 객실 번호와 프론트 연락 방법을 함께 안내해 주세요.</p>
</section>

<section>
  <h2>위생 및 안전 기준</h2>
  <p>간다GO 관리사는 방문 시 위생 기준을 철저히 준수합니다. 사용하는 도구 및 재료는 1회용 또는 관리 후 소독 처리를 원칙으로 합니다. 관리사 방문 시 위생 수칙을 지키며, 고객님이 요청하시면 추가적인 위생 조치를 취합니다.</p>
  <p>안전을 위해 아래 사항을 지켜 주시기 바랍니다.</p>
  <ul>
    <li>피부 트러블, 상처, 급성 통증이 있는 경우 사전에 알려 주세요. 해당 부위는 관리에서 제외하거나 방법을 조정합니다.</li>
    <li>임신 중이거나 고혈압, 당뇨 등 기저 질환이 있는 분은 반드시 의사와 상담 후 이용해 주세요.</li>
    <li>음주 후 서비스 이용은 건강 안전을 위해 권장하지 않습니다.</li>
    <li>서비스 중 불편함이 느껴지시면 즉시 관리사에게 알려 주세요. 언제든지 조정이 가능합니다.</li>
  </ul>
  <p>인천 각 지역의 고객님 모두 동일한 위생·안전 기준을 적용받습니다. <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화동</a>, <a href="/incheon/seo-gu/geomdan-area/">검단</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a> 어느 지역에서 예약하시든 관리 품질은 동일합니다.</p>
</section>

<section>
  <h2>자주 묻는 질문</h2>
  <h3>Q. 예약 당일 취소가 가능한가요?</h3>
  <p>당일 취소는 관리사 출발 전까지 가능합니다. 출발 후 취소 시에는 이동 비용이 청구될 수 있습니다. 자세한 내용은 <a href="/incheon/reservation/">예약 안내</a>를 확인해 주세요.</p>
  <h3>Q. 혼자 있는 상황에서 방문을 받아도 되나요?</h3>
  <p>네, 방문형 관리 서비스는 1인 이용도 가능합니다. 서비스 범위와 내용은 예약 상담 시 사전에 안내드립니다.</p>
  <h3>Q. 이용 가능 지역이 어디까지인가요?</h3>
  <p>인천광역시 전역을 기준으로 하며, <a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화동</a>, <a href="/incheon/yeonsu-gu/dongchun-dong/">동춘동</a> 등도 방문 가능합니다. 일부 도서 지역은 추가 이동비 및 사전 확인이 필요합니다. 정확한 방문 가능 여부와 예약은 <a href="tel:0508-202-4719">0508-202-4719</a>로 확인해 주세요.</p>
  <h3>Q. 개인정보는 어떻게 처리되나요?</h3>
  <p>예약 시 수집한 개인정보는 서비스 이행 목적에만 사용되며, 제3자에게 제공되지 않습니다. 상세 내용은 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 확인해 주세요.</p>
</section>

<section>
  <h2>지역별 방문 서비스 특성</h2>
  <p>인천광역시는 구마다 주거 환경과 이동 특성이 다양합니다. 방문형 관리 서비스를 보다 편리하게 이용하실 수 있도록 지역별 특성을 아래에 안내드립니다.</p>
  <ul>
    <li><strong><a href="/incheon/michuhol-gu/yonghyeon-dong/">용현동</a>·<a href="/incheon/michuhol-gu/hagik-dong/">학익동</a>:</strong> 주거 단지와 상업 시설이 혼재된 지역으로, 주차 공간이 협소한 경우 인근 공영주차장 이용이 필요할 수 있습니다.</li>
    <li><strong><a href="/incheon/bupyeong-gu/bugae-dong/">부개동</a>·<a href="/incheon/bupyeong-gu/sangok-dong/">산곡동</a>:</strong> 도심 인접 지역으로 당일 예약 후 1~2시간 내 방문이 가능한 경우가 많습니다.</li>
    <li><strong><a href="/incheon/gyeyang-gu/hyoseong-dong/">효성동</a>·<a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>:</strong> 계양구 생활권 중심으로 지하철 계양역 인근 접근성이 좋아 관리사 이동이 원활합니다.</li>
    <li><strong><a href="/incheon/namdong-gu/sorae-area/">소래포구</a>·<a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>:</strong> 남동구 동부권으로 수인분당선 이용권이며, 소래포구역 인근 숙박 시설도 방문 가능합니다.</li>
    <li><strong><a href="/incheon/seo-gu/seongnam-dong/">석남동</a>·<a href="/incheon/seo-gu/gajeong-dong/">가정동</a>:</strong> 서구 남부권으로 루원시티 개발이 활발하며 신규 주거 단지의 방문 출입 방법을 미리 확인해 주세요.</li>
  </ul>
  <p>방문 서비스를 처음 이용하시는 분들께서는 이 가이드를 숙지하신 후 <a href="/incheon/reservation/">예약 안내</a>를 통해 예약을 진행해 주시면 더욱 원활하게 서비스를 받으실 수 있습니다.</p>
</section>

<section>
  <h2>관리 후 주의사항</h2>
  <p>방문형 관리 서비스 종료 후에도 몇 가지 사항을 지켜 주시면 관리 효과를 더욱 오래 유지하실 수 있습니다.</p>
  <ul>
    <li>관리 직후 충분한 수분 섭취를 권장합니다. 혈액 순환이 활성화되는 시간이므로 물이나 따뜻한 음료를 마셔 주세요.</li>
    <li>관리 후 최소 30분~1시간은 무리한 신체 활동을 피해 주세요.</li>
    <li>관리 부위에 붉음증이나 가벼운 근육통이 나타날 수 있으며 이는 일시적인 반응으로 대부분 자연스럽게 해소됩니다.</li>
    <li>음주나 과도한 카페인 섭취는 관리 효과를 약화시킬 수 있으므로 주의해 주세요.</li>
  </ul>
  <p>관리 후 특이한 증상이 지속되거나 불편함이 느껴지시면 전문 의료기관을 방문해 주세요. 간다GO 방문형 관리 서비스는 의료 행위가 아니므로 치료 목적으로 이용하지 않으시기 바랍니다.</p>
</section>

<section>
  <h2>이용 문의</h2>
  <p>이용 가이드를 확인하신 후 추가 문의사항이 있으시다면 <a href="/incheon/support/">고객센터</a>를 통해 언제든지 연락해 주세요. 인천 전역을 아우르는 방문형 관리 서비스를 편안하게 이용하실 수 있도록 최선을 다하겠습니다. 인천광역시 교통 정보나 지역 안내가 필요하신 분은 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>를 참고하실 수 있습니다.</p>
</section>
""",
)


# ────────────────────────────────────────────────
# 4. 고객센터
# ────────────────────────────────────────────────
page_support = create_page(
    path="incheon/support/",
    title="인천 출장마사지 고객센터｜예약·상담 안내",
    desc="인천 출장마사지 예약·상담 채널(전화·텔레그램), 운영 시간, 자주 묻는 질문을 안내합니다.",
    h1="인천 출장마사지 고객센터",
    breadcrumb=[("인천", "/incheon/"), ("고객센터", "")],
    body_content="""
<section>
  <h2>상담 채널 안내</h2>
  <p>간다GO 인천 출장마사지 고객센터는 전화와 텔레그램 두 가지 채널로 운영됩니다. 빠르고 정확한 상담을 원하시는 경우 전화 상담을 이용해 주시고, 텍스트 상담이 편하신 분들은 텔레그램 채널을 이용해 주시기 바랍니다. 두 채널 모두 연중무휴 24시간 운영됩니다.</p>
  <ul>
    <li><strong>전화 상담:</strong> <a href="tel:0508-202-4719">0508-202-4719</a></li>
    <li><strong>텔레그램 상담:</strong> <a href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow">https://t.me/googleseolab</a></li>
  </ul>
  <p>예약 시에는 방문 주소, 희망 방문 시간, 원하시는 관리 프로그램을 함께 알려 주시면 신속하게 상담 및 예약을 도와드립니다. 자세한 예약 절차는 <a href="/incheon/reservation/">예약 안내</a> 페이지를 참고해 주세요. 예약 전 확인해야 할 사항은 <a href="/incheon/check/">이용 전 확인사항</a> 페이지를 먼저 읽어 보시기 바랍니다.</p>
</section>

<section>
  <h2>상담 운영 시간</h2>
  <p>고객센터는 연중무휴 24시간 운영됩니다. 새벽 시간대나 공휴일에도 상담이 가능하므로 편하신 시간에 문의해 주시기 바랍니다. 다만, 관리사 배정 상황에 따라 심야 및 새벽 방문 서비스는 당일 예약이 어려울 수 있으므로 가능하면 사전 예약을 권장합니다.</p>
  <p>인천 주요 지역인 <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>, <a href="/incheon/yeonsu-gu/songdo/">송도</a> 등은 24시간 상담 및 예약이 원활히 이루어집니다. <a href="/incheon/seo-gu/cheongna/">청라</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>, <a href="/incheon/seo-gu/geomdan-area/">검단</a> 지역도 동일하게 24시간 상담이 가능합니다.</p>
  <p>성수기나 연휴 기간에는 문의가 집중될 수 있어 상담 연결에 다소 시간이 걸릴 수 있습니다. 이 경우 텔레그램 채널을 이용하시면 메시지 순서대로 응대해 드리므로 대기 시간을 줄일 수 있습니다.</p>
</section>

<section>
  <h2>자주 묻는 질문</h2>
  <h3>Q. 인천 전 지역에서 방문이 가능한가요?</h3>
  <p>인천광역시 대부분 지역에 방문이 가능합니다. <a href="/incheon/seo-gu/cheongna/">청라</a>, <a href="/incheon/seo-gu/geomdan-area/">검단</a>, <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>, <a href="/incheon/michuhol-gu/dohwa-dong/">도화동</a>, <a href="/incheon/bupyeong-gu/samsan-dong/">삼산동</a> 등 인천 전역이 방문 가능 지역에 포함됩니다. 단, <a href="/incheon/jung-gu/yeongjong-area/">영종도</a>·<a href="/incheon/ganghwa-gun/ganghwa-eup/">강화군</a>·<a href="/incheon/ongjin-gun/ongjin-area/">옹진군</a>은 추가 이동비 및 사전 확인이 필요합니다.</p>
  <h3>Q. 예약 후 취소하면 어떻게 되나요?</h3>
  <p>관리사 출발 전 취소는 가능합니다. 출발 후 취소 시에는 이동 비용이 청구될 수 있습니다. 변경·취소 관련 상세 내용은 <a href="/incheon/reservation/">예약 안내</a>에서 확인해 주세요.</p>
  <h3>Q. 서비스 범위가 어디까지인가요?</h3>
  <p>간다GO는 합법적인 범위 내의 방문형 관리 서비스만 제공합니다. 서비스 범위를 벗어난 요청은 정중히 거절됩니다. 자세한 사항은 <a href="/incheon/check/">이용 전 확인사항</a>을 확인해 주세요.</p>
  <h3>Q. 개인정보는 어떻게 처리되나요?</h3>
  <p>예약 시 수집한 정보는 서비스 이행 목적에만 사용됩니다. 상세 내용은 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 확인해 주세요.</p>
  <h3>Q. 이용 가이드는 어디서 확인하나요?</h3>
  <p>방문 서비스 흐름, 준비사항, 위생 기준 등은 <a href="/incheon/guide/">홈타이 이용 가이드</a> 페이지에서 상세하게 안내드리고 있습니다.</p>
  <h3>Q. 선불 결제가 필요한가요?</h3>
  <p>아니요. 간다GO는 선불 또는 선입금을 요구하지 않습니다. 결제는 서비스 완료 후 현장에서 진행됩니다. 선불을 요구하는 경우는 정상적인 서비스가 아니므로 즉시 상담센터로 문의해 주세요.</p>
</section>

<section>
  <h2>인천 지역별 방문 상담 안내</h2>
  <p>인천은 구마다 생활권이 다양하게 구성되어 있습니다. 각 지역별로 방문 서비스 접근성, 건물 출입 방식, 이동 시간이 달라질 수 있으므로 예약 전 담당 상담사에게 지역 특성을 안내해 주시면 더욱 원활한 예약이 가능합니다.</p>
  <p>인천 서부권의 <a href="/incheon/seo-gu/cheongna/">청라국제도시</a>는 대규모 아파트 단지가 밀집해 있으며 방문자 등록 절차가 있는 단지가 많습니다. 인천 동부권의 <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>과 <a href="/incheon/namdong-gu/sorae-area/">소래포구</a> 인근은 수인분당선 역세권으로 대중교통 접근이 편리합니다. 인천 북부권의 <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>과 <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a>은 계양구의 중심 생활권으로 주거 밀집도가 높습니다.</p>
  <p>예약 시 방문 지역을 정확히 알려 주시면 해당 지역에 익숙한 관리사를 배정하는 데 도움이 됩니다. 궁금한 사항은 언제든지 <a href="/incheon/support/">고객센터</a>로 문의해 주세요.</p>
</section>

<section>
  <h2>예약·상담 시 자주 발생하는 오해</h2>
  <p>간다GO 고객센터 상담 과정에서 많이 접하는 오해를 미리 안내드립니다.</p>
  <ul>
    <li><strong>오해 1 — 선불 요구가 있다:</strong> 간다GO는 예약금 또는 선입금을 요구하지 않습니다. 결제는 반드시 서비스 완료 후 현장에서 이루어집니다. 선불을 요구받으셨다면 사칭일 가능성이 있으므로 즉시 고객센터로 확인해 주세요.</li>
    <li><strong>오해 2 — 불법 서비스도 가능하다:</strong> 간다GO는 합법적인 방문형 관리 서비스만 제공하며, 서비스 범위를 벗어난 요청은 정중히 거절합니다.</li>
    <li><strong>오해 3 — 인천 외곽 지역은 방문이 불가능하다:</strong> <a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a>, <a href="/incheon/jung-gu/yeongjong-area/">영종도</a>, <a href="/incheon/ganghwa-gun/ganghwa-eup/">강화군</a> 등 외곽 지역도 방문 가능합니다. 다만 추가 이동비와 사전 확인이 필요합니다.</li>
    <li><strong>오해 4 — 예약 취소가 불가능하다:</strong> 관리사 출발 전까지는 예약 취소 및 변경이 가능합니다. 빠르게 연락해 주시면 비용 없이 조정해 드립니다.</li>
  </ul>
  <p>이 외에도 궁금한 점은 <a href="/incheon/reservation/">예약 안내</a>, <a href="/incheon/check/">이용 전 확인사항</a>, <a href="/incheon/guide/">홈타이 이용 가이드</a> 페이지를 참고하시거나 직접 문의해 주세요.</p>
</section>

<section>
  <h2>인천 방문 서비스 운영 원칙</h2>
  <p>간다GO 고객센터는 고객님과의 신뢰를 최우선으로 운영됩니다. 아래는 저희가 지키는 운영 원칙입니다.</p>
  <ul>
    <li><strong>투명한 안내:</strong> 예약 전 방문 가능 여부, 추가 이동비, 서비스 내용을 명확하게 안내합니다. 예상치 못한 비용이 발생하지 않도록 사전 합의를 철저히 진행합니다.</li>
    <li><strong>신속한 응대:</strong> 상담 접수 후 최대한 빠르게 응대하며, 연중무휴 24시간 운영으로 언제든지 문의할 수 있습니다.</li>
    <li><strong>개인정보 보호:</strong> 예약 시 수집한 개인정보는 서비스 이행 목적으로만 사용하고, 서비스 완료 후 일정 기간 내 파기합니다. 자세한 사항은 <a href="/incheon/support/privacy/">개인정보처리방침</a>을 참고해 주세요.</li>
    <li><strong>합법적 서비스:</strong> 법령에서 정한 범위 내의 방문형 관리 서비스만 제공하며, 불법 또는 선정적 서비스 요청은 정중히 거절합니다.</li>
  </ul>
  <p>인천 <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/yeonsu-gu/songdo/">송도</a>, <a href="/incheon/seo-gu/cheongna/">청라</a>, <a href="/incheon/gyeyang-gu/jakjeon-dong/">작전동</a> 등 어느 지역에서 예약하시든 동일한 원칙으로 서비스를 제공합니다.</p>
</section>

<section>
  <h2>개인정보처리방침 및 이용 약관</h2>
  <p>고객님의 개인정보 보호를 위해 간다GO는 관련 법령에 따라 개인정보를 처리합니다. 수집 항목, 이용 목적, 보유 기간 등 상세 내용은 <a href="/incheon/support/privacy/">개인정보처리방침</a> 페이지에서 확인하실 수 있습니다. 인천광역시 관련 행정 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>에서도 참고하실 수 있습니다.</p>
</section>
""",
)


# ────────────────────────────────────────────────
# 5. 개인정보처리방침
# ────────────────────────────────────────────────
page_privacy = create_page(
    path="incheon/support/privacy/",
    title="개인정보처리방침｜간다GO 인천 출장마사지",
    desc="간다GO 인천 출장마사지 개인정보 수집 항목, 이용 목적, 보유 기간, 이용자 권리를 안내합니다.",
    h1="개인정보처리방침",
    breadcrumb=[
        ("인천", "/incheon/"),
        ("고객센터", "/incheon/support/"),
        ("개인정보처리방침", ""),
    ],
    body_content="""
<section>
  <h2>개인정보 수집 항목 및 수집 방법</h2>
  <p>간다GO(이하 "회사")는 방문형 관리 서비스 예약 및 이행을 위해 아래와 같이 개인정보를 수집합니다. 회사는 수집 최소화 원칙에 따라 서비스 이행에 필요한 최소한의 정보만 수집하며, 예약과 무관한 민감정보(주민등록번호, 금융정보 등)는 수집하지 않습니다.</p>
  <ul>
    <li><strong>필수 수집 항목:</strong> 이름(또는 호칭), 연락처(휴대전화 번호), 방문 주소</li>
    <li><strong>선택 수집 항목:</strong> 희망 서비스 유형, 기타 요청사항</li>
    <li><strong>수집 방법:</strong> 전화 상담(<a href="tel:0508-202-4719">0508-202-4719</a>), 텔레그램 채널을 통한 직접 입력</li>
  </ul>
  <p>인천 전역(<a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월</a>, <a href="/incheon/yeonsu-gu/songdo/">송도</a> 등)에서 예약하시는 모든 고객님에게 동일한 수집 기준이 적용됩니다. 수집 항목 외 추가 정보를 요구받는 경우 고객센터로 문의해 주시기 바랍니다.</p>
</section>

<section>
  <h2>개인정보 이용 목적</h2>
  <p>수집한 개인정보는 다음 목적으로만 이용됩니다. 동의한 목적 범위를 벗어나 이용하지 않으며, 이용 목적이 변경될 경우 별도 동의를 구합니다.</p>
  <ul>
    <li>방문형 관리 서비스 예약 접수 및 확정 안내</li>
    <li>담당 관리사 배정 및 방문 서비스 이행</li>
    <li>예약 변경·취소 등 사후 고객 응대</li>
    <li>서비스 이용 관련 안내 및 고지사항 전달</li>
    <li>법령에 따른 의무 이행</li>
  </ul>
  <p>위 목적 이외의 용도(마케팅, 광고, 제3자 제공 등)로는 사용하지 않습니다. 수집 목적을 달성한 후에는 지체 없이 파기하는 것을 원칙으로 합니다. 예약 및 서비스 절차에 대한 자세한 안내는 <a href="/incheon/reservation/">예약 안내</a> 페이지를 참고해 주세요.</p>
</section>

<section>
  <h2>개인정보 보유 기간 및 파기</h2>
  <p>개인정보는 서비스 이행 완료 후 아래 기간 동안 보관되며, 보유 기간이 경과한 이후에는 지체 없이 파기됩니다.</p>
  <ul>
    <li><strong>예약·서비스 이행 관련 정보:</strong> 서비스 완료일로부터 3개월</li>
    <li><strong>법령에 의해 보존이 필요한 정보:</strong> 해당 법령에서 정한 기간 (예: 「전자상거래 등에서의 소비자보호에 관한 법률」에 따른 거래 기록)</li>
  </ul>
  <p>전자적 파일 형태로 저장된 정보는 복구할 수 없는 방법으로 영구 삭제하고, 종이 문서는 분쇄 또는 소각 처리합니다. 보유 기간 만료 전이라도 고객님의 요청이 있을 경우 법령이 허용하는 범위 내에서 조기 삭제 조치를 취합니다.</p>
</section>

<section>
  <h2>개인정보 제3자 제공</h2>
  <p>회사는 원칙적으로 이용자의 개인정보를 제3자에게 제공하지 않습니다. 다만, 아래 경우에는 예외적으로 제공할 수 있습니다.</p>
  <ul>
    <li>이용자가 사전에 명시적으로 동의한 경우</li>
    <li>법령의 규정에 따라 수사기관 등의 요구가 있는 경우</li>
  </ul>
  <p><a href="/incheon/seo-gu/cheongna/">청라</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>, <a href="/incheon/namdong-gu/nonhyeon-dong/">논현동</a>, <a href="/incheon/seo-gu/geomdan-area/">검단 신도시</a>, <a href="/incheon/jung-gu/yeongjong-area/">영종도</a> 등 어느 지역 고객님의 정보도 동의 없이 제3자에게 제공되지 않습니다. 외부 업체와의 협력이 필요한 경우에도 개인정보 처리 위탁 계약을 체결하고 법령이 정한 보호 조치를 적용합니다.</p>
</section>

<section>
  <h2>이용자의 권리</h2>
  <p>이용자는 언제든지 아래 권리를 행사할 수 있습니다. 권리 행사는 구두(전화) 또는 서면(텔레그램 메시지) 방식으로 요청하실 수 있으며, 회사는 지체 없이 필요한 조치를 취합니다.</p>
  <ul>
    <li><strong>열람 요구:</strong> 본인의 개인정보 처리 현황 및 내용 확인 요구</li>
    <li><strong>정정 요구:</strong> 부정확하거나 변경된 개인정보의 수정 요구</li>
    <li><strong>삭제 요구:</strong> 서비스 이행 완료 후 개인정보 즉시 파기 요구</li>
    <li><strong>처리 정지 요구:</strong> 법령에서 정한 경우를 제외하고 개인정보 처리의 일시적 중단 요구</li>
  </ul>
  <p>위 권리 행사는 <a href="/incheon/support/">고객센터</a>를 통해 요청하실 수 있으며, 회사는 법령에서 정한 기간 내에 조치 결과를 알려드립니다. 만 14세 미만 아동의 개인정보는 법정대리인의 동의가 필요하며, 동의 없이 수집하지 않습니다.</p>
</section>

<section>
  <h2>개인정보 보호 담당자 및 문의처</h2>
  <p>개인정보 처리에 관한 문의, 불만 처리, 피해 구제 등에 관한 사항은 아래 담당 창구에 문의해 주시기 바랍니다. 신속하고 성실하게 응대해 드리겠습니다.</p>
  <ul>
    <li><strong>운영 브랜드:</strong> 간다GO</li>
    <li><strong>상담 전화:</strong> <a href="tel:0508-202-4719">0508-202-4719</a></li>
    <li><strong>텔레그램:</strong> <a href="https://t.me/googleseolab" target="_blank" rel="noopener nofollow">https://t.me/googleseolab</a></li>
  </ul>
  <p>기타 개인정보 침해 관련 신고·상담은 개인정보보호위원회(www.pipc.go.kr) 또는 개인정보 침해신고센터(국번 없이 118)에 문의하실 수 있습니다. 인천광역시 관련 행정 정보는 <a href="https://www.incheon.go.kr/" target="_blank" rel="noopener nofollow">인천광역시청 공식 홈페이지</a>에서도 확인하실 수 있습니다.</p>
  <p>본 방침은 2025년 1월 1일부터 시행하며, 내용 변경 시 홈페이지 또는 고객 상담 채널을 통해 사전 공지합니다. 방침 변경 이전 수집된 개인정보에 대해서는 변경 전 방침을 적용합니다.</p>
</section>

<section>
  <h2>쿠키 및 자동 수집 정보</h2>
  <p>본 서비스는 전화 및 텔레그램 채널을 통해서만 예약을 받으며, 별도의 웹 기반 회원 가입 또는 로그인 시스템을 운영하지 않습니다. 따라서 쿠키·IP주소 등 자동 수집 정보를 통해 개인을 식별하지 않습니다. 다만 본 웹사이트에서 기술적 이유로 방문 통계를 수집할 수 있으며, 이 경우에도 개인 식별 정보는 포함되지 않습니다.</p>
  <p>인천 전역의 고객님 — <a href="/incheon/michuhol-gu/juan-dong/">주안</a>, <a href="/incheon/bupyeong-gu/bupyeong-dong/">부평</a>, <a href="/incheon/namdong-gu/guwol-dong/">구월동</a>, <a href="/incheon/yeonsu-gu/songdo/">송도</a>, <a href="/incheon/seo-gu/cheongna/">청라</a>, <a href="/incheon/gyeyang-gu/gyesan-dong/">계산동</a>, <a href="/incheon/seo-gu/geomdan-area/">검단</a> 등 어디서 접속하시든 — 동일한 개인정보 보호 정책이 적용됩니다. 예약 절차나 개인정보 처리에 관한 추가 문의는 <a href="/incheon/support/">고객센터</a>로 연락해 주시기 바랍니다.</p>
</section>

<section>
  <h2>개인정보 처리 위탁</h2>
  <p>회사는 원활한 서비스 이행을 위해 아래와 같이 개인정보 처리 업무를 위탁할 수 있습니다. 위탁 계약 시 개인정보 보호 관련 법령을 준수하도록 관리·감독하며, 위탁 업무 범위를 벗어난 개인정보 처리를 금지합니다.</p>
  <ul>
    <li><strong>수탁자:</strong> 현재 개인정보 처리 업무를 외부에 위탁하지 않습니다.</li>
    <li>향후 위탁이 발생하는 경우 수탁자명, 위탁 업무 내용, 위탁 기간을 본 방침에 공개합니다.</li>
  </ul>
  <p>개인정보 처리 위탁에 관해 궁금한 사항은 <a href="/incheon/support/">고객센터</a>로 문의해 주시기 바랍니다.</p>
</section>

<section>
  <h2>개인정보 처리방침의 변경</h2>
  <p>법령·정책 변경 또는 서비스 내용 변경으로 인해 본 방침이 수정될 수 있습니다. 방침 변경 시에는 시행 최소 7일 전에 고객 상담 채널 또는 홈페이지를 통해 사전 공지합니다. 중요한 권리 침해가 우려되는 변경 사항에 대해서는 최소 30일 전에 공지합니다. 변경된 방침은 시행일부터 적용되며, 변경 이전 수집된 개인정보에 대해서는 변경 전 방침을 우선 적용합니다.</p>
  <p>예약 관련 궁금한 사항은 <a href="/incheon/reservation/">예약 안내</a>, 서비스 이용 전 준비 사항은 <a href="/incheon/check/">이용 전 확인사항</a>, 전반적인 서비스 흐름은 <a href="/incheon/guide/">홈타이 이용 가이드</a>에서 확인해 주세요.</p>
</section>
""",
)


# ────────────────────────────────────────────────
# PAGES 리스트
# ────────────────────────────────────────────────
PAGES = [
    page_reservation,
    page_check,
    page_guide,
    page_support,
    page_privacy,
]
