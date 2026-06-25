# 인천 구·군별 대표 동(법정동) → 가장 관련 있는 기존 안내 페이지 매핑
# 목적: 구(허브) 페이지에서 대표 동을 노출하고 내부링크로 연결(구글 SEO·크롤링·UX).
# 원칙:
#   - 1동·2동·3동 등 번호 행정동은 대표 동(법정동) 1개로만 묶는다(도어웨이·중복 방지).
#   - 동마다 얇은 페이지를 새로 만들지 않고, 대표 동·생활권 페이지로 연결한다.

ADMIN_DONG = {
    "jung-gu/": {
        "title": "중구",
        "groups": [
            ("내륙(동인천) 생활권", "/jung-gu/dongincheon-area/",
             ["신포동", "연안동", "신흥동", "도원동", "율목동"]),
            ("영종 생활권", "/jung-gu/yeongjong-area/", ["영종동"]),
            ("운서 생활권", "/jung-gu/unseo-dong/", ["운서동"]),
            ("용유·공항 생활권", "/jung-gu/incheon-airport-area/", ["용유동"]),
        ],
    },
    "dong-gu/": {
        "title": "동구",
        "groups": [
            ("동인천 인접 생활권", "/jung-gu/dongincheon-area/",
             ["만석동", "화수동", "화평동", "송현동"]),
            ("제물포 인접 생활권", "/michuhol-gu/jemulpo-area/",
             ["송림동", "금곡동", "창영동"]),
        ],
    },
    "michuhol-gu/": {
        "title": "미추홀구",
        "groups": [
            ("주안 생활권", "/michuhol-gu/juan-dong/", ["주안동"]),
            ("도화 생활권", "/michuhol-gu/dohwa-dong/", ["도화동"]),
            ("용현·숭의 생활권", "/michuhol-gu/yonghyeon-dong/", ["용현동", "숭의동"]),
            ("학익·문학·관교 생활권", "/michuhol-gu/hagik-dong/", ["학익동", "문학동", "관교동"]),
            ("제물포 인접 생활권", "/michuhol-gu/jemulpo-area/", ["제물포"]),
        ],
    },
    "yeonsu-gu/": {
        "title": "연수구",
        "groups": [
            ("송도국제도시 생활권", "/yeonsu-gu/songdo/", ["송도동"]),
            ("연수·옥련·선학 생활권", "/yeonsu-gu/yeonsu-dong/", ["연수동", "옥련동", "선학동"]),
            ("동춘·청학 생활권", "/yeonsu-gu/dongchun-dong/", ["동춘동", "청학동"]),
        ],
    },
    "namdong-gu/": {
        "title": "남동구",
        "groups": [
            ("구월 생활권", "/namdong-gu/guwol-dong/", ["구월동"]),
            ("간석·만수 생활권", "/namdong-gu/ganseok-dong/", ["간석동", "만수동"]),
            ("논현 생활권", "/namdong-gu/nonhyeon-dong/", ["논현동", "고잔동", "도림동"]),
            ("소래·서창 생활권", "/namdong-gu/sorae-area/", ["서창동", "장수동", "운연동"]),
        ],
    },
    "bupyeong-gu/": {
        "title": "부평구",
        "groups": [
            ("부평역·부평시장 생활권", "/bupyeong-gu/bupyeong-dong/", ["부평동", "십정동"]),
            ("부개·일신 생활권", "/bupyeong-gu/bugae-dong/", ["부개동", "일신동"]),
            ("삼산·갈산 생활권", "/bupyeong-gu/samsan-dong/", ["삼산동", "갈산동"]),
            ("산곡 생활권", "/bupyeong-gu/sangok-dong/", ["산곡동"]),
            ("청천 생활권", "/bupyeong-gu/cheongcheon-dong/", ["청천동"]),
        ],
    },
    "gyeyang-gu/": {
        "title": "계양구",
        "groups": [
            ("계산·계양 생활권", "/gyeyang-gu/gyesan-dong/",
             ["계산동", "계양동", "임학동", "병방동"]),
            ("작전·서운 생활권", "/gyeyang-gu/jakjeon-dong/", ["작전동", "서운동", "동양동"]),
            ("효성 생활권", "/gyeyang-gu/hyoseong-dong/", ["효성동"]),
        ],
    },
    "seo-gu/": {
        "title": "서구",
        "groups": [
            ("청라국제도시 생활권", "/seo-gu/cheongna/", ["청라동"]),
            ("검단신도시 생활권", "/seo-gu/geomdan-area/",
             ["검단동", "당하동", "원당동", "마전동", "불로동", "대곡동", "왕길동", "오류동", "아라동"]),
            ("검암·경서 생활권", "/seo-gu/geomam-dong/", ["검암동", "경서동", "연희동"]),
            ("가정·루원 생활권", "/seo-gu/gajeong-dong/", ["가정동"]),
            ("석남·가좌 생활권", "/seo-gu/seongnam-dong/",
             ["석남동", "신현동", "원창동", "가좌동"]),
        ],
    },
    "ganghwa-gun/": {
        "title": "강화군",
        "groups": [
            ("강화 방문 가능 지역", "/ganghwa-gun/ganghwa-eup/",
             ["강화읍", "선원면", "불은면", "길상면", "화도면", "양도면",
              "내가면", "하점면", "양사면", "송해면", "교동면", "삼산면", "서도면"]),
        ],
    },
    "ongjin-gun/": {
        "title": "옹진군",
        "groups": [
            ("옹진 도서 방문 가능 지역", "/ongjin-gun/ongjin-area/",
             ["영흥면", "북도면", "백령면", "대청면", "덕적면", "자월면", "연평면"]),
        ],
    },
}


def render_admin_dong(path: str) -> str:
    """구·군 페이지에 붙일 '대표 동(행정동) 안내' 섹션 HTML을 만든다.
    번호 동은 대표 동으로 묶고, 가장 관련 있는 기존 안내 페이지로 내부링크를 건다."""
    data = ADMIN_DONG.get(path)
    if not data:
        return ""
    gu = data["title"]
    parts = [
        '<section id="admin-dong">',
        f"<h2>{gu} 동별 방문 안내</h2>",
        f"<p>{gu}의 주요 동을 생활권별로 정리했습니다. 본인 주소지의 동을 확인하고, "
        f"가장 가까운 방문 안내 페이지에서 방문 가능 지역과 예약 전 확인사항을 살펴보세요. "
        f"1동·2동 등 번호로 나뉜 동은 대표 동 한 곳으로 묶어 안내하며, 동마다 얇은 페이지를 "
        f"따로 만들지 않고 실제 생활권 단위 페이지로 연결합니다.</p>",
    ]
    for group_title, target, dongs in data["groups"]:
        links = " · ".join(
            f'<a href="{target}">{d} 방문 가능 지역</a>' for d in dongs
        )
        parts.append(f"<h3>{group_title}</h3><p class=\"dong-links\">{links}</p>")
    parts.append("</section>")
    return "".join(parts)
