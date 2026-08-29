// 모기에그 대량생산 — 검증된 공신력 데이터 팩 (수치 임의 생성 금지)
window.VERIFIED_CARDS = 
{
  "version": "1.0",
  "audience": "40~60대",
  "fact_policy": "모든 수치는 공공·공식 통계 기반 (AI가 수치를 임의 생성하지 않음)",
  "categories": [
    { "id": "finance", "label": "재테크·자산", "emoji": "💰", "color": "#1d4ed8" },
    { "id": "pension", "label": "노후·연금", "emoji": "🏦", "color": "#0d9488" },
    { "id": "retire", "label": "은퇴·고용·수명", "emoji": "🧭", "color": "#ea580c" },
    { "id": "tax", "label": "세금·상속", "emoji": "📑", "color": "#7c3aed" },
    { "id": "health", "label": "건강·의료·사회", "emoji": "🩺", "color": "#16a34a" }
  ],
  "cards": [
    {
      "id": "asset-grade",
      "category": "finance",
      "emoji": "💰",
      "title": "자산 등급 총정리",
      "subtitle": "대한민국 가구, 당신의 자산은 어디쯤?",
      "items": [
        { "head": "순자산 3억원 미만", "body": "전체 가구의 56.9% · 가구 절반 이상" },
        { "head": "순자산 3억~10억원 미만", "body": "약 32% · 중간층 구간" },
        { "head": "순자산 10억원 이상", "body": "10.9% · 상위 10% 진입" },
        { "head": "중위 순자산", "body": "2억 4,000만원 · 가구 절반의 기준선" },
        { "head": "평균 순자산", "body": "4억 4,894만원 · 상위층이 끌어올린 값" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "average-trap",
      "category": "finance",
      "emoji": "📊",
      "title": "평균의 함정",
      "subtitle": "평균 자산 5.4억? 실제 절반은 2.4억 미만",
      "items": [
        { "head": "가구 평균 자산", "body": "5억 4,022만원" },
        { "head": "가구 중위 순자산", "body": "2억 4,000만원" },
        { "head": "평균-중위 격차", "body": "약 2억원 · 평균이 현실을 왜곡" },
        { "head": "시사점", "body": "SNS 속 '억대 자산'은 일부의 이야기" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "asset-debt-net",
      "category": "finance",
      "emoji": "🏠",
      "title": "자산·부채·순자산 한눈에",
      "subtitle": "우리집 재무 상태, 평균과 비교하면?",
      "items": [
        { "head": "평균 자산", "body": "5억 4,022만원 (전년 +2.5%)" },
        { "head": "평균 부채", "body": "9,128만원 (전년 -0.6% · 첫 감소)" },
        { "head": "평균 순자산", "body": "4억 4,894만원 (+3.1%)" },
        { "head": "부채 보유 가구", "body": "60.7%" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "fin-vs-real",
      "category": "finance",
      "emoji": "🏢",
      "title": "금융자산 vs 실물자산",
      "subtitle": "한국 가구 자산은 부동산 중심",
      "items": [
        { "head": "금융자산", "body": "24.8% · 1억 3,378만원" },
        { "head": "실물자산", "body": "75.2% · 4억 644만원" },
        { "head": "특징", "body": "자산의 4분의 3이 부동산 등 실물" },
        { "head": "유의점", "body": "부동산 편중은 유동성 리스크" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "income-quintile-asset",
      "category": "finance",
      "emoji": "⚖️",
      "title": "소득 분위별 자산 격차",
      "subtitle": "소득이 자산을 결정한다",
      "items": [
        { "head": "소득 5분위 평균 자산", "body": "12억 3,780만원" },
        { "head": "소득 1분위 평균 자산", "body": "1억 6,948만원" },
        { "head": "격차", "body": "7.3배 (전년 6.8배 → 확대)" },
        { "head": "시사점", "body": "자산 격차가 해마다 벌어지는 중" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "net-asset-polarization",
      "category": "finance",
      "emoji": "📈",
      "title": "순자산 양극화",
      "subtitle": "상위 20%가 하위 20%의 42배",
      "items": [
        { "head": "순자산 5분위", "body": "16억 2,291만원" },
        { "head": "순자산 1분위", "body": "3,859만원" },
        { "head": "격차", "body": "42.1배 (전년 39배 → 확대)" },
        { "head": "순자산 지니계수", "body": "0.612 (전년 +0.007)" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "household-debt",
      "category": "finance",
      "emoji": "💳",
      "title": "가구 부채 현황",
      "subtitle": "빚은 얼마나, 누가 지고 있나",
      "items": [
        { "head": "평균 부채", "body": "9,128만원 · 사상 첫 감소" },
        { "head": "소득 5분위 부채", "body": "2억 529만원" },
        { "head": "소득 1분위 부채", "body": "1,975만원" },
        { "head": "부채 보유 가구", "body": "60.7%" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "korea-rich-criteria",
      "category": "finance",
      "emoji": "👑",
      "title": "한국 부자의 기준",
      "subtitle": "금융자산 10억, 그리고 그 위",
      "items": [
        { "head": "한국 부자", "body": "금융자산 10억 이상 46만 1천명 · 인구 0.9%" },
        { "head": "부자 스스로의 기준", "body": "총자산 100억 이상" },
        { "head": "10억~100억 미만", "body": "42만 2천명 (91.5%)" },
        { "head": "300억 이상", "body": "1만명 돌파" }
      ],
      "source": "KB금융지주 '2024 한국 부자 보고서'"
    },
    {
      "id": "rich-asset-building",
      "category": "finance",
      "emoji": "🌱",
      "title": "부자의 자산 축적법",
      "subtitle": "종잣돈 7.4억, 언제 어떻게?",
      "items": [
        { "head": "종잣돈 규모", "body": "평균 7억 4천만원" },
        { "head": "종잣돈 마련 시점", "body": "평균 42세" },
        { "head": "축적 기반", "body": "사업소득 32.8% + 부동산 투자 26.3%" },
        { "head": "시사점", "body": "근로소득 저축만으로는 한계" }
      ],
      "source": "KB금융지주 '2024 한국 부자 보고서'"
    },
    {
      "id": "single-household-asset",
      "category": "finance",
      "emoji": "🧍",
      "title": "1인 가구 자산",
      "subtitle": "혼자 사는 집의 현실",
      "items": [
        { "head": "1인 가구 평균 자산", "body": "2억 2천만원" },
        { "head": "1인 가구 중앙값", "body": "9천만원" },
        { "head": "평균-중앙값 격차", "body": "상위 1인 가구가 평균을 끌어올림" },
        { "head": "시사점", "body": "1인 가구 절반은 자산 9천만원 이하" }
      ],
      "source": "통계청·한국은행·금융감독원 '2025 가계금융복지조사'"
    },
    {
      "id": "nps-payout",
      "category": "pension",
      "emoji": "🏦",
      "title": "국민연금 수령액 총정리",
      "subtitle": "나는 월 얼마나 받게 될까?",
      "items": [
        { "head": "평균 수령액", "body": "월 약 67만원 (66만 9,523원)" },
        { "head": "20년 이상 가입자", "body": "평균 월 108만원" },
        { "head": "최대 수령액", "body": "약 296만원" },
        { "head": "부부 합산 평균", "body": "월 111만원" }
      ],
      "source": "국민연금공단 (2025)"
    },
    {
      "id": "nps-distribution",
      "category": "pension",
      "emoji": "📉",
      "title": "국민연금 수령액 분포",
      "subtitle": "10명 중 4명은 40만원 미만",
      "items": [
        { "head": "월 100만원 이상", "body": "전체의 13.55%" },
        { "head": "월 20만~40만원", "body": "39.68% · 가장 많은 구간" },
        { "head": "현실", "body": "수급자 10명 중 4명은 40만원 미만" },
        { "head": "유의점", "body": "가입 기간·소득에 따라 천차만별" }
      ],
      "source": "국민연금공단 (2025년 7월)"
    },
    {
      "id": "retirement-cost-gap",
      "category": "pension",
      "emoji": "🕳️",
      "title": "노후 생활비 vs 국민연금",
      "subtitle": "연금만으로는 턱없이 부족",
      "items": [
        { "head": "부부 필요 생활비", "body": "월 240만~340만원" },
        { "head": "국민연금 부부 합산", "body": "평균 월 111만원" },
        { "head": "부족분", "body": "최소 100만~200만원 이상" },
        { "head": "시사점", "body": "퇴직연금·개인연금 필수" }
      ],
      "source": "국민연금연구원 등 공신력 조사"
    },
    {
      "id": "nps-start-age",
      "category": "pension",
      "emoji": "🎂",
      "title": "국민연금 수령 나이",
      "subtitle": "출생연도에 따라 달라요",
      "items": [
        { "head": "1957~60년생", "body": "만 62세부터" },
        { "head": "1961~64년생", "body": "만 63세부터" },
        { "head": "1965~68년생", "body": "만 64세부터" },
        { "head": "1969년생 이후", "body": "만 65세부터" }
      ],
      "source": "국민연금공단"
    },
    {
      "id": "nps-early",
      "category": "pension",
      "emoji": "⏳",
      "title": "조기노령연금",
      "subtitle": "최대 5년 먼저, 대신 감액",
      "items": [
        { "head": "조기 수령", "body": "지급개시보다 최대 5년 먼저" },
        { "head": "1961~64년생", "body": "58세부터 조기 수령 가능" },
        { "head": "주의", "body": "먼저 받는 만큼 연금액 감액" },
        { "head": "판단 기준", "body": "수령 기간·건강·수입 고려" }
      ],
      "source": "국민연금공단"
    },
    {
      "id": "basic-pension",
      "category": "pension",
      "emoji": "🤲",
      "title": "기초연금 총정리",
      "subtitle": "65세 이상 하위 70% 대상",
      "items": [
        { "head": "2026 기준연금액", "body": "월 최대 34만 9,700원" },
        { "head": "2025년 기준", "body": "34만 2,510원 → 인상" },
        { "head": "단독가구", "body": "소득인정액 247만원 이하" },
        { "head": "부부가구", "body": "395만 2천원 이하" }
      ],
      "source": "보건복지부"
    },
    {
      "id": "pension-tax-credit",
      "category": "pension",
      "emoji": "🧾",
      "title": "연금저축 vs IRP 절세",
      "subtitle": "연 900만원, 최대 148만원 돌려받기",
      "items": [
        { "head": "연금저축 단독", "body": "연 600만원 세액공제" },
        { "head": "IRP 합산", "body": "연 900만원까지" },
        { "head": "최대 환급", "body": "약 148만원 (16.5% 구간 기준)" },
        { "head": "공제율", "body": "소득 구간별 12~16.5%" }
      ],
      "source": "국세청 연금계좌 세액공제"
    },
    {
      "id": "housing-pension",
      "category": "pension",
      "emoji": "🔑",
      "title": "주택연금 총정리",
      "subtitle": "집은 그대로, 연금은 매달",
      "items": [
        { "head": "가입 조건", "body": "만 55세 이상 · 부부합산 공시가격 12억 이하 1주택" },
        { "head": "60세 · 5억 주택", "body": "월 약 105만원" },
        { "head": "70세 · 5억 주택", "body": "월 약 154만원" },
        { "head": "보장", "body": "평생 거주 + 국가 지급보증" }
      ],
      "source": "한국주택금융공사"
    },
    {
      "id": "nps-premium",
      "category": "pension",
      "emoji": "💸",
      "title": "국민연금 보험료",
      "subtitle": "월 얼마를 내고 있나",
      "items": [
        { "head": "보험료율", "body": "9% (직장가입자 본인 4.5% + 회사 4.5%)" },
        { "head": "기준소득월액", "body": "39만~617만원 (2025)" },
        { "head": "월 납부액", "body": "35,100원~555,300원" },
        { "head": "원리", "body": "소득이 높을수록 많이 내고 많이 받음" }
      ],
      "source": "국민연금공단"
    },
    {
      "id": "retirement-age",
      "category": "pension",
      "emoji": "🚪",
      "title": "은퇴 나이 총정리",
      "subtitle": "법정 정년 60세, 현실은?",
      "items": [
        { "head": "주된 일자리 퇴직", "body": "평균 49.4세 (2024, 55~64세 기준)" },
        { "head": "법정 정년", "body": "60세" },
        { "head": "현실", "body": "정년보다 약 10년 먼저 퇴직" },
        { "head": "시사점", "body": "소득 공백기를 대비해야" }
      ],
      "source": "한국보건사회연구원"
    },
    {
      "id": "retirement-reality",
      "category": "retire",
      "emoji": "🧭",
      "title": "정년 vs 현실",
      "subtitle": "정년까지 일하는 사람은 10% 미만",
      "items": [
        { "head": "정년 퇴직", "body": "9.6%" },
        { "head": "원치 않는 조기퇴직", "body": "41.3% (권고사직·정리해고 등)" },
        { "head": "정년제 운영 사업장", "body": "22%" },
        { "head": "규모별 격차", "body": "300인 이상 94.3% vs 30인 미만 19.5%" }
      ],
      "source": "고용노동부·미래에셋투자와연금센터"
    },
    {
      "id": "elderly-employment",
      "category": "retire",
      "emoji": "🛠️",
      "title": "65세 이상 고용률",
      "subtitle": "OECD 1위의 빛과 그림자",
      "items": [
        { "head": "65세 이상 고용률", "body": "37.3% (2023)" },
        { "head": "OECD 비교", "body": "평균 13.6% · 일본 25.3% → 한국 1위" },
        { "head": "65세 이상 인구", "body": "20.3% · 초고령사회 진입" },
        { "head": "원인", "body": "낮은 공적연금 소득" }
      ],
      "source": "국민연금연구원·OECD"
    },
    {
      "id": "elderly-work-reason",
      "category": "retire",
      "emoji": "💼",
      "title": "고령층이 일하는 이유",
      "subtitle": "생활비 보탬이 절반 이상",
      "items": [
        { "head": "생활비 보탬", "body": "54.4%" },
        { "head": "일하는 즐거움", "body": "36.1%" },
        { "head": "희망 근로 연령", "body": "평균 73.4세" },
        { "head": "시사점", "body": "생계형 노동이 압도적" }
      ],
      "source": "통계청 경제활동인구조사"
    },
    {
      "id": "post-retire-job-quality",
      "category": "retire",
      "emoji": "🧱",
      "title": "은퇴 후 일자리 질",
      "subtitle": "재취업은 대부분 비정규직",
      "items": [
        { "head": "60~64세 임시·일용직", "body": "37.1%" },
        { "head": "60~64세 단순노무직", "body": "약 20%" },
        { "head": "65~69세 단순노무직", "body": "약 26%" },
        { "head": "시사점", "body": "연령이 높을수록 일자리 질 하락" }
      ],
      "source": "한국보건사회연구원"
    },
    {
      "id": "minimum-wage",
      "category": "retire",
      "emoji": "💰",
      "title": "최저임금 2026",
      "subtitle": "시간급 10,320원",
      "items": [
        { "head": "시간급", "body": "10,320원 (전년 +290원 · +2.9%)" },
        { "head": "월 환산", "body": "2,156,880원 (월 209시간 기준)" },
        { "head": "2025년", "body": "10,030원" },
        { "head": "적용", "body": "업종 구분 없이 모든 사업장" }
      ],
      "source": "최저임금위원회"
    },
    {
      "id": "life-expectancy",
      "category": "retire",
      "emoji": "🕰️",
      "title": "기대수명 총정리",
      "subtitle": "우리는 얼마나 살까",
      "items": [
        { "head": "기대수명", "body": "83.7년" },
        { "head": "남성", "body": "80.8년" },
        { "head": "여성", "body": "86.6년" },
        { "head": "남녀 격차", "body": "5.8년 · 감소 추세" }
      ],
      "source": "통계청 '2024 생명표'"
    },
    {
      "id": "life-at-60",
      "category": "retire",
      "emoji": "🌅",
      "title": "60세 이후 기대여명",
      "subtitle": "은퇴 후에도 20년 이상",
      "items": [
        { "head": "60세 기대여명", "body": "남 23.7년 / 여 28.4년" },
        { "head": "40세 기대여명", "body": "남 41.9년 / 여 47.4년" },
        { "head": "시사점", "body": "노후 자금은 20~30년치가 필요" },
        { "head": "준비", "body": "은퇴 시점을 기준으로 설계" }
      ],
      "source": "통계청 '2024 생명표'"
    },
    {
      "id": "healthy-life",
      "category": "retire",
      "emoji": "💚",
      "title": "건강수명 총정리",
      "subtitle": "아프지 않고 사는 기간은?",
      "items": [
        { "head": "건강수명", "body": "65.5년 (유병기간 제외)" },
        { "head": "아픈 기간", "body": "남 16.2년 / 여 20.2년" },
        { "head": "비교", "body": "기대수명 83.7년 중 건강하게 65.5년" },
        { "head": "시사점", "body": "건강 관리가 곧 노후 준비" }
      ],
      "source": "통계청 '2024 생명표'"
    },
    {
      "id": "inheritance-tax",
      "category": "tax",
      "emoji": "📑",
      "title": "상속세 총정리 (2025 개편)",
      "subtitle": "달라진 세율과 공제",
      "items": [
        { "head": "최고세율", "body": "50% → 40%로 인하" },
        { "head": "10% 구간", "body": "2억원 이하로 확대" },
        { "head": "자녀공제", "body": "1인 5,000만 → 5억원" },
        { "head": "일괄공제", "body": "5억원 유지" }
      ],
      "source": "기획재정부 '2024 세법개정'"
    },
    {
      "id": "spouse-deduction",
      "category": "tax",
      "emoji": "👫",
      "title": "배우자 상속공제",
      "subtitle": "최소 5억, 최대 30억",
      "items": [
        { "head": "배우자공제", "body": "최소 5억 ~ 최대 30억원" },
        { "head": "일괄공제", "body": "5억원" },
        { "head": "예시", "body": "10억 상속 시 공제 10억 → 세금 0원 가능" },
        { "head": "유의점", "body": "배우자 사망 후 재상속 부담 고려" }
      ],
      "source": "국세청"
    },
    {
      "id": "pension-income-tax",
      "category": "tax",
      "emoji": "🧮",
      "title": "연금 수령 시 과세",
      "subtitle": "연금으로 받으면 세금이 줄어요",
      "items": [
        { "head": "연금소득세", "body": "3.3~5.5%" },
        { "head": "조건", "body": "만 55세 이후 + 가입 5년 이상" },
        { "head": "일시금 수령", "body": "퇴직소득세 등 더 높은 세율" },
        { "head": "전략", "body": "연금 한도 내 분할 수령이 유리" }
      ],
      "source": "국세청"
    },
    {
      "id": "pension-early-withdraw",
      "category": "tax",
      "emoji": "⚠️",
      "title": "연금계좌 중도인출",
      "subtitle": "해지하면 세금 폭탄",
      "items": [
        { "head": "세액공제 받은 금액", "body": "인출 시 16.5% 기타소득세" },
        { "head": "공제 안 받은 원금", "body": "페널티 없이 인출 가능" },
        { "head": "운용수익", "body": "과세 대상" },
        { "head": "원칙", "body": "연금계좌는 해지하지 말 것" }
      ],
      "source": "국세청"
    },
    {
      "id": "health-cap",
      "category": "health",
      "emoji": "🩺",
      "title": "건강보험 본인부담상한제",
      "subtitle": "1년 의료비, 이 이상은 안 내도 됨",
      "items": [
        { "head": "상한액 범위", "body": "최저 89만원(1분위) ~ 최고 826만원(10분위)" },
        { "head": "요양병원 120일 초과", "body": "최고 1,074만원" },
        { "head": "초과분", "body": "건보공단이 환급" },
        { "head": "대상", "body": "소득 분위별 10단계" }
      ],
      "source": "국민건강보험공단 (2025)"
    },
    {
      "id": "longterm-care-grade",
      "category": "health",
      "emoji": "🧓",
      "title": "장기요양보험 등급",
      "subtitle": "1등급부터 인지지원까지",
      "items": [
        { "head": "등급", "body": "1~5등급 + 인지지원등급" },
        { "head": "대상", "body": "65세 이상 또는 노인성 질환(치매 등) 65세 미만" },
        { "head": "1등급", "body": "일상생활 전적으로 타인 도움 필요" },
        { "head": "신청", "body": "국민건강보험공단에 등급 신청" }
      ],
      "source": "보건복지부"
    },
    {
      "id": "longterm-care-cost",
      "category": "health",
      "emoji": "🏥",
      "title": "장기요양 본인부담",
      "subtitle": "내가 내는 비용은 얼마?",
      "items": [
        { "head": "재가급여(방문요양)", "body": "본인부담 15%" },
        { "head": "시설급여(요양시설)", "body": "본인부담 20%" },
        { "head": "기초생활수급자", "body": "0%" },
        { "head": "감경", "body": "소득·재산 따라 40~60% 감경" }
      ],
      "source": "보건복지부·국민건강보험공단 (2025)"
    },
    {
      "id": "life-vs-health-gap",
      "category": "health",
      "emoji": "⏱️",
      "title": "기대수명 vs 건강수명",
      "subtitle": "약 18년은 질병과 함께",
      "items": [
        { "head": "기대수명", "body": "83.7년" },
        { "head": "건강수명", "body": "65.5년" },
        { "head": "격차", "body": "약 18년" },
        { "head": "여성 아픈 기간", "body": "20.2년" }
      ],
      "source": "통계청 '2024 생명표'"
    },
    {
      "id": "super-aged-society",
      "category": "health",
      "emoji": "🏛️",
      "title": "초고령사회 진입",
      "subtitle": "65세 이상 20% 시대",
      "items": [
        { "head": "65세 이상 인구", "body": "20.3%" },
        { "head": "의미", "body": "초고령사회(20% 이상) 진입" },
        { "head": "영향", "body": "연금·의료·일자리 전반 변화" },
        { "head": "대비", "body": "개인 차원의 노후 설계 필수" }
      ],
      "source": "국민연금연구원"
    },
    {
      "id": "household-income",
      "category": "health",
      "emoji": "🧾",
      "title": "가구 소득 총정리",
      "subtitle": "평균과 중위, 실제 소득은?",
      "items": [
        { "head": "평균 소득", "body": "7,185만원" },
        { "head": "중위 소득", "body": "5,681만원" },
        { "head": "처분가능소득", "body": "5,864만원" },
        { "head": "시사점", "body": "가구 절반은 연 5,700만원 이하" }
      ],
      "source": "통계청·한국은행·금융감독원 '2024 가계금융복지조사'"
    },
    {
      "id": "rich-3-engines",
      "category": "health",
      "emoji": "🚀",
      "title": "부자 자산증식 3대 동력",
      "subtitle": "KB가 분석한 부자의 공통점",
      "items": [
        { "head": "① 소득잉여자금", "body": "벌고 남긴 돈을 투자로 전환" },
        { "head": "② 자산 배분 전략", "body": "금융자산 → 일정 규모 후 부동산 전환" },
        { "head": "③ 부채 활용", "body": "레버리지 전략 구사" },
        { "head": "시사점", "body": "저축→투자→배분의 선순환" }
      ],
      "source": "KB금융지주 '2024 한국 부자 보고서'"
    },
    {
      "id": "nps-vs-minimum-living",
      "category": "health",
      "emoji": "📏",
      "title": "국민연금 vs 최저생계비",
      "subtitle": "연금은 최저생계비의 절반도 안 됨",
      "items": [
        { "head": "국민연금 평균", "body": "월 66만원 (2024)" },
        { "head": "1인 가구 최저생계비", "body": "월 134만원" },
        { "head": "비교", "body": "연금이 최저생계비의 절반도 못 미침" },
        { "head": "시사점", "body": "추가 소득·자산이 필수" }
      ],
      "source": "국민연금연구원 (2024)"
    }
  ]
}
;
