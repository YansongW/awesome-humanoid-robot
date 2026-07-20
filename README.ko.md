<div align="center">

# Awesome Humanoid Robot 🤖

**휴머노이드 로봇의 0에서 1로의 양산 및 산업화 적용을 위한 큐레이션 다국어 지식 그래프.**

<p>
  <img src="https://img.shields.io/badge/status-public%20v0.1.0-success" alt="Status: public v0.1.0" />
  <img src="https://img.shields.io/badge/entries-2144-green" alt="2144 entries" />
  <img src="https://img.shields.io/badge/relationships-5687-brightgreen" alt="5687 relationships" />
  <img src="https://img.shields.io/badge/languages-zh%2Fen%2Fko-blue" alt="Languages: zh/en/ko" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 **라이브 사이트**: [kg.rounds-tech.com](https://kg.rounds-tech.com)  
🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

⭐ 이 프로젝트가 연구나 개발에 도움이 된다면 Star를 눌러주세요. 더 많은 연구자와 개발자가 발견하는 데 도움이 됩니다.

</div>

---

## 📌 이 프로젝트는 무엇인가?

**Awesome Humanoid Robot**은 하나의 핵심 질문을 중심으로 구축된 구조화되고 지속적으로 발전하는 오픈소스 지식 베이스입니다:

> **휴머노이드 로봇의 0에서 1로의 양산 및 산업화 적용을 어떻게 실현할 것인가?**

원자재, 부품, 제조 공정부터 설계 공학, AI, 소프트웨어, 데이터, 조립·테스트, 양산, 적용 시나리오, 시장, 정책 및 규제에 이르는 전체 여정의 모든 단계를 추적합니다. 우리는 단순한 논문 목록이나 제품 목록에 머물지 않고, 휴머노이드 로봇 산업 전체를 **지식 그래프**로 모델링합니다: 엔티티는 노드이고, 관계는 타입이 지정된 엣지이며, 모든 주장은 출처로 추적 가능합니다.

**v0.1.0**에서 프로젝트는 연구 파이프라인에서 제품화된 지식 서비스로 발전했습니다:

- 🌐 공개된 다국어 웹사이트 **[kg.rounds-tech.com](https://kg.rounds-tech.com)**: 검색, 인터랙티브 관계 그래프, 연계 Wiki 제공.
- 📖 리포지토리 내 **Wiki**: *Humanoid Robots: From Mine to Market*에서 파생된 체계적이고 장별로 전개되는 서술 콘텐츠.
- 🔗 Wiki 장과 KG 엔티티 간 양방향 링크: 서술 읽기와 구조화된 데이터 탐색을 자연스럽게 오갈 수 있습니다.

이 프로젝트는 **AI 보조, 인간 검증** 방식으로 운영됩니다. AI4Sci 파이프라인을 활용해 발견, 추출, 종합을 가속화하지만, 어떤 콘텐츠도 생산 환경으로 승격되기 전에 인간의 검토를 거칩니다.

---

## 🧭 세 가지 사용법: 검색 · 학습 · 제작

이 시스템은 세 개의 층으로 구성되어 각각 다른 질문에 답합니다:

| 층 | 답하는 질문 | 입구 |
|----|-----------|------|
| 🔍 **검색** — 지식 그래프 | "무엇이 있는가? 누가 만드는가? 무엇과 연결되는가?" | [kg.rounds-tech.com/search/](https://kg.rounds-tech.com/search/) · [그래프](https://kg.rounds-tech.com/graph/) |
| 📖 **학습** — Wiki 교과서 | "왜 이렇게 동작하는가? 조각들이 어떻게 맞물리는가?" | [kg.rounds-tech.com/wiki/](https://kg.rounds-tech.com/wiki/) |
| 🛠️ **제작** — 0→1 로드맵 | "내 예산과 실력으로 다음에 무엇을 해야 하는가?" | [kg.rounds-tech.com/roadmap/](https://kg.rounds-tech.com/roadmap/) |

**0→1 로드맵**은 모든 것을 하나로 잇는 층입니다: 네 단계(기초 다지기 → 관절 하나 → 이족 플랫폼 → 완전한 휴로봇)와 액추에이터/센서/컴퓨팅/시뮬레이션 네 권의 선정 매뉴얼. 모든 단계는 세 부분 구조——*무엇을 할지*, *왜인지*(지식 카드 링크), *내 상황에서 어떻게 분석할지*——이며 검수 기준과 트러블슈팅 표를 갖춥니다. 로드맵에 참여하는 카드에는 단계 배지가 표시되어 해당 단계로 돌아갈 수 있습니다. 모든 제작 안내는 실제 출처가 있는 오픈소스 플랫폼 조사(ToddlerBot, Berkeley Humanoid Lite, Upkie, OpenLoong 등, `data/roadmap/research/` 참조)에 기반하며, 실기 검증을 거치지 않은 이론적 안내임을 명시합니다.

---

## ✨ v0.1.0 하이라이트

- 🌐 **라이브 제품 사이트** — [kg.rounds-tech.com](https://kg.rounds-tech.com): 중/영/한 3개 언어 UI, 전문 검색, 인터랙티브 Cytoscape 그래프, 연계 Wiki.
- 📖 **리포지토리 내 Wiki** — *Humanoid Robots: From Mine to Market*에서 파생된 30개 서술 장 + 7개 부록, 경고 상자, Mermaid 다이어그램, KaTeX 수식 렌더링.
- 🗂️ **2,144개 검증된 KG 엔티티** 및 **5,687개 타입 지정 관계**, 원자재부터 시장 적용까지 전체 스택을 커버.
- 🔄 **자동화 CI/CD** — `main` 브랜치 푸시마다 GitHub Actions가 사이트를 빌드하여 GitHub Pages에 배포.
- 🛡️ **강화된 배포** — 동시성 제어와 깨끗한 `gh-pages` 브랜치 재생성으로 경쟁 상태로 인한 푸시 실패 방지.
- 🧩 **핵심 비논문 엔티티 본문 보강** — Wiki 장에서 추출하거나 엔티티 메타데이터를 확장하여 233개 critical 비논문 엔티티에 概述/核心内容/参考 구조화 본문 추가.
- 🌏 **누락된 영문 이름 및 요약 기계 번역** — `names.en` / `summary.en`이 누락된 모든 공정 및 논문 엔트리를 기계 번역하고 인간 검토 대상으로 표시.
- 📝 **중요 논문 엔트리 본문 보강 완료** — 215개 논문 유형 critical 엔티티에 메타데이터 기반 DeepSeek 생성의 概述/核心内容/参考 구조화 본문이 추가되었으며, 품질 감사 critical 0건으로 개선.

---

## 🎯 왜 이 프로젝트를 하는가?

휴머노이드 로봇은 중요한 전환점에 있습니다. 전 세계 연구실은 이미 걷고, 조작하고, 상호작용할 수 있는 로봇을 만들 수 있습니다. 하지만 **데모에서 작동하는 로봇**과 **대규모로 생산·배치·유지보수 가능한 실제 제품**은 전혀 다른 문제입니다.

이 간극은 단순한 AI 문제가 아니라 **시스템 공학 문제**입니다. 이는 다음을 모두 연결합니다:

- 🪨 **재료 과학** — 희토류 자재, 배터리 화학, 경량 합금
- ⚙️ **정밀 제조** — 기계 가공, 권선, 주조, 조립, 품질 관리
- 🌐 **글로벌 공급망** — Tier-1/Tier-2 공급업체, 지역 산업 생태계, 비용 구조
- 🧠 **AI 및 소프트웨어** — VLA, 월드 모델, 제어, 계획, sim-to-real
- 📊 **데이터 인프라** — 데이터셋, 시뮬레이터, 벤치마크, 함대 원격 측정
- 🏭 **양산 제조** — 공장 설계, 수율 최적화, BOM 비용 공학
- ⚖️ **정책과 사회** — 안전 기준, 인증, 책임, 노동 시장 영향

오늘날 이러한 계층에 대한 정보는 학술 논문, 회사 볼보, 분해 보고서, 산업 분석 및 기술 블로그에 흩어져 있습니다. 연구자, 엔지니어, 창업자, 투자자, 정책 입안자 모두 **단일하고 구조화되며 검증 가능한 지도**가 부족합니다: 각 부분이 어떻게 맞물리는지, 병목이 어디에 있는지, 성공을 결정하는 트레이드오프는 무엇인지.

이 프로젝트가 바로 그 지도입니다.

> 우리의 목표는 모든 논문을 수집하는 것이 아니라, **광산에서 시장까지의 완전한 여정**을 이해하고, 그 이해를 검증 가능하고 재사용 가능하며 커뮤니티가 함께 유지할 수 있도록 만드는 것입니다.

---

## 🌐 제품: KG 웹사이트

`website/` 디렉터리는 지식 그래프의 정적 제품 수준 프론트엔드를 빌드합니다.

**라이브 URL**: [https://kg.rounds-tech.com](https://kg.rounds-tech.com)

v0.1.0 기능:

- **3개 언어 인터페이스** — 헤더의 언어 전환으로 독립된 `zh`, `en`, `ko` 사이트 이동.
- **영역 탐색** — 산업 영역 또는 엔티티 타입별로 그래프 탐색.
- **전문 검색** — 클라이언트 사이드 검색, 타입 필터 및 언어 인식 레이블.
- **인터랙티브 관계 그래프** — Cytoscape.js 기반 클러스터 뷰와 전체 그래프 뷰.
- **엔티티 페이지** — 요약, 영역, 계층, 관계, 관련 엔티티 및 연결된 Wiki 장.
- **통합 Wiki** — 30개 장 + 7개 부록, 경고 상자, Mermaid 다이어그램, KaTeX 수식 렌더링.

로컬 빌드:

```bash
cd website
pip install -r requirements.txt
python3 -m builder.build
# 로컬 서버 실행
python3 -m http.server 8080 --directory dist
```

실험적인 FastAPI 백엔드(자연어 Q&A)는 `web/`에 있으며, 자세한 내용은 [`web/README.md`](web/README.md)를 참조하세요.

---

## 🗺️ 여기서 무엇을 찾을 수 있는가?

| 영역 | 추적 내용 |
|------|-----------|
| **기초 학문** | 모든 공학 분야를 뒷받침하는 수학, 물리, 화학, 컴퓨터 과학 개념 |
| **원자재 및 핵심 자원** | 희토류, 자재, 경량 금속, 복합재료, 반도체, 배터리 화학 |
| **부품 및 서브시스템** | 액추에이터, 모터, 감속기/기어박스, 센서, 배터리, 컴퓨팅 유닛, 엔드 이펙터, 케이블, 구조물 |
| **공급망 및 제조 공정** | 티어1/티어2 공급사, 제조 공정, 품질 관리, 비용 구조, 지역 산업 생태계 |
| **설계 및 공학** | 기계 설계, 운영학, 동역학, 휨 형태, 자유도, 안전 설계 |
| **조립, 통합 및 테스트** | 생산 라인, 교정, 시스템 통합, 테스트 벤치, 검증 프로토콜 |
| **양산 및 확장** | 공장 설계, 생산 램프, 단위 경제성, BOM 분석, 수율 최적화 |
| **AI, 모델 및 알고리즘** | VLA, 월드 모델, locomotion 정책, manipulation 정책, 계획, sim-to-real, SLAM, 텔레오퍼레이션 |
| **소프트웨어 및 미들웨어** | ROS 2, 실시간 OS, 시뮬레이션 스택, 디지털 트윈, 함대 관리, 데이터 파이프라인 |
| **데이터 및 데이터셋** | 텔레오퍼레이션 데이터, 모션 캡처, 시뮬레이션 데이터, 멀티모달 데이터셋, 데이터 라이선스 |
| **평가 및 벤치마크** | 시뮬레이션 벤치마크, 실제 작업, 하드웨어 인 더 루프 테스트, 안전 기준 |
| **적용 및 시장** | 제조, 물류, 의료, 가정, 리테일, 연구, 국방, 엔터테인먼트 |
| **회사 및 산업 생태계** | 스타트업, 완성차 업체, 부품 공급사, 연구 기관, 투자, 파트너십 |
| **정책, 규제 및 윤리** | 안전 기준, 책임, 노동 시장 영향, 프라이버시, 인간-로봇 상호작용 규범 |

---

## 🏗️ 아키텍처 우선 접근법

콘텐츠를 채우기 전에, 우리는 먼저 전체 산업 체인을 그래프로 표현할 수 있는 공식 정보 모델을 구축했습니다.

- **그래프 우선**: 엔티티는 노드이고, 관계는 방향성 있고 타입이 지정된 엣지입니다.
- **이중 태그**: 각 엔티티는 **가치 사슬 계층**(Foundations / Upstream / Midstream / Intelligence / Validation-Markets)과 **기능적 역할**(재료 / 부품 / 공정 / 시스템 / 지능 / 등)을 모두 가집니다.
- **기초 학문 도메인**: 수학, 물리, 화학, 컴퓨터 과학 등 공학 전반에 걸쳐 공유되는 주제는 `00_foundations`에 할당됩니다.
- **관계를 일급 객체로**: 교차 도메인 링크는 명시적이고, 유형화되며, 검증 가능합니다.
- **다국어 기본 설계**: 이름, 요약, 설명은 언어 맵으로 저장됩니다(영 / 중 / 한).
- **버전 관리 schema**: 항목 및 관계 schema는 버전 관리 및 확장이 가능합니다.
- **세분화된 이론적 깊이**: 방정식, 연산자, 변수, 상수, 알고리즘, 근사 방법이 모두 명시적 노드가 될 수 있습니다.
- **YAML frontmatter + Markdown**: 항목은 사람이 읽을 수 있고 기계가 읽을 수 있습니다.

전체 사양은 [`docs/architecture/information_model.md`](docs/architecture/information_model.md) 및 [`data/schema/v1/`](data/schema/v1/)를 참조하세요.

---

## ⚙️ 작동 방식: AI4Sci + 인간 검토

1. **체계적인 스캐닝** — 워크스트림이 arXiv, Semantic Scholar 및 웹 소스를 검색하여 관련 논문과 산업 인텔리전스를 발견합니다.
2. **관련성 분류** — LLM이 핵심 질문에 따라 각 출처에 점수를 매기고 낮은 관련성 콘텐츠를 필터링합니다.
3. **구조화된 추출** — LLM이 타입이 지정된 항목, 다국어 요약 및 후보 관계를 작성합니다.
4. **임시 저장** — 모든 AI 초안은 `.staging/`에 격리되어 검토를 기다립니다.
5. **자율 검토** — `scripts/ai4sci_autonomous_review.py`가 schema, 출처 및 중복 항목을 확인하고 높은 신뢰도의 초안을 자동으로 보관합니다.
6. **인간 검토** — 검토자가 남은 큐를 검사하고 경계 사례를 거부하거나 미세 조정합니다.
7. **통합 및 검증** — 승인된 항목은 `research/` 및 `data/relationships/`로 이동하고 `scripts/validate_entries.py`를 통과해야 합니다.

일일 수집 파이프라인 실행:

```bash
bash scripts/ingest_all_sources.sh
```

프레임워크 문서는 [`docs/ingestion/README.md`](docs/ingestion/README.md)를, 레거시 AI4Sci 파이프라인은 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)를 참조하세요.

---

## 🚀 빠른 시작

```bash
# 1. 저장소 클론
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. 주요 작업 확인 (감사/빌드/GUI/로드맵 체크)
make help

# 3. 지식 그래프 감사 (품질 + 연결성 지표)
make kg

# 4. 제품 웹사이트 빌드 및 로컬 미리보기
make serve          # http://127.0.0.1:8080

# 5. 로컬 GUI 실행 (검색, 서브그래프 시각화, LLM Q&A)
make gui            # http://127.0.0.1:8000

# 6. 로드맵 페이지 편집 후 로드맵↔카드 바인딩 재생성
make roadmap-check

# 7. 통합 인제스천 파이프라인 실행 (일일 cron)
python -m ingestion.pipeline --all
```

자격 증명 설정은 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)와 [`web/README.md`](web/README.md)를 참조하세요.

---

## 📊 프로젝트 통계

| 지표 | 수량 |
|------|------|
| 프로덕션 엔티티 | 2,144 |
| 관계 | 5,687 |
| 고립 개체 | < 2% |
| 온톨로지 도메인 | 13 (12 + `00_foundations`) |
| 엔티티 유형 | 24 |
| Wiki 챕터 | 30 |
| Wiki 부록 | 7 |
| 0→1 로드맵 페이지 | 9 (개요 + 4단계 + 4매뉴얼) |
| 오픈소스 로봇 엔티티 | 10 (태그: `open_source`) |
| 로드맵 바인딩 카드 | 94 |
| 지원 언어 | 중 / 영 / 한 |
| 검증 상태 | ✅ 통과 |
| 품질 감사 | 2,136 ok / 8 warning / 0 critical |

---

## 🛣️ 로드맵

| 단계 | 목표 | 상태 |
|------|------|------|
| **Phase 0** | 정보 아키텍처, schema, 검증 | ✅ 완료 |
| **Phase 1** | 영역별 온톨로지 문서(01–12) | ✅ 완료 |
| **Phase 2** | 워크스트림 기반 콘텐츠 채우기 및 schema/관계 진화 | ✅ 완료 |
| **Phase 2.5** | 제품 수준 정적 웹사이트(검색, 그래프, Wiki) | ✅ 완료 |
| **Phase 3** | 공개 v0.1.0 릴리스(오픈소스 + 라이브) | ✅ 완료 |
| **Phase 3.5** | 0→1 제작 로드맵 층: 로드맵 페이지 9개, 오픈소스 로봇 엔티티 10개, 카드 바인딩 94개, 관계 체계화(엣지 1,063 → 5,687, 고립 개체 80.6% → 1.7%) | ✅ 완료 |
| **Phase 4** | 콘텐츠 완성도: 공백 보충, 기초 학문 심화, Wiki–KG 링크 확장 | 🔄 진행 중 |
| **Phase 5** | 검증 워크플로우, 커뮤니티 기여, v0.2.0 | ⏳ 계획 중 |

전체 워크스트림 TODO는 [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md)를, 최신 세션 기록은 [`docs/session_status.md`](docs/session_status.md)를 참조하세요.

---

## 👥 누구를 위한 것인가?

- **연구자** — 문제 영역과 산업 계층별로 정리된 최신 연구 동향 확인.
- **엔지니어** — 담당 서브시스템과 관련된 부품 공급사, 시뮬레이션 도구, 데이터셋 및 벤치마크 발견.
- **창업자 / 투자자** — 공급망 매핑, 공백 식별, 경쟁사 추적.
- **제조 및 운영** — 공장 설계, 수율, 비용 동인 및 확장 트레이드오프 이해.
- **정책 입안자** — 규제, 안전 및 윤리 환경 이해.

---

## 🤝 기여하기

공개 기여 가이드는 Phase 5에서 게시될 예정입니다. 그때까지:

- 콘텐츠는 핵심 팀이 AI4Sci 지원下 큐레이션합니다.
- 접근 권한이 있다면 출처 링크와 검증 상태를 포함한 항목을 추가하세요.
- 불확실하거나 상충되는 주장은 issue로 표시하세요.
- [`docs/ontology/`](docs/ontology/)의 온톨로지 구조와 [`docs/architecture/information_model.md`](docs/architecture/information_model.md)의 항목 형식을 따르세요.

---

## 📂 디렉터리 구조

```
awesome-humanoid-robot/
├── README.md                          # 본 파일
├── README.zh.md                       # 简体中文
├── README.ko.md                       # 한국어
├── LICENSE                            # MIT 라이선스(코드)
├── docs/
│   ├── project_charter.md             # 프로젝트 범위, 원칙, 거버넌스
│   ├── WIKI-KG-SYNC.md                # Wiki ↔ KG 동기화 워크플로우
│   ├── ontology/                      # 산업链 온톨로지 문서(01–12 + 개요)
│   ├── architecture/                  # 정보 모델 및 사전 설계 분석
│   └── ai4sci/                        # AI4Sci 파이프라인 문서 및 워크스트림 분류
├── research/                          # 프로덕션 지식 베이스 항목
│   ├── foundations/                   # 수학, 물리, 화학, 컴퓨터 과학 개념
│   ├── materials/                     # 원자재
│   ├── components/                    # 부품 및 서브시스템
│   ├── companies/                     # 회사 프로필 및 산업 생태계
│   ├── papers/                        # 논문 노트
│   └── datasets/                      # 데이터셋 노트
├── data/
│   ├── schema/v1/                     # JSON Schema
│   ├── relationships/                 # 독립 관계 파일
│   └── wiki-chapter-mapping.yaml      # Wiki 장 ↔ KG 엔티티 매핑
├── wiki/                              # 리포지토리 내 Wiki 소스(Markdown + MkDocs 설정)
│   ├── docs/chapters/                 # 30개 서술 장
│   ├── docs/appendices/               # 7개 부록
│   └── mkdocs.yml                     # MkDocs 설정
├── website/                           # 제품 수준 정적 웹사이트 빌더 및 자산
│   ├── builder/                       # Python 정적 사이트 생성기
│   ├── templates/                     # Jinja2 HTML 템플릿
│   ├── src/                           # CSS / JS 자산
│   └── dist/                          # 생성된 사이트(git 무시)
├── web/                               # 실험적 FastAPI Q&A 백엔드
│   ├── app.py
│   ├── kg_store.py
│   ├── llm_qa.py
│   └── README.md
├── scripts/                           # AI4Sci 보조 스크립트
│   ├── ai4sci_lib/
│   ├── ai4sci_workstreams/
│   ├── ai4sci_paper_pipeline.py
│   ├── ai4sci_batch_pipeline.py
│   ├── ai4sci_orchestrator.py
│   ├── ai4sci_review.py
│   ├── ai4sci_status.py
│   └── validate_entries.py
└── .staging/                          # 인간 검토 대기 중인 AI 초안
```

---

## 📜 라이선스

- **코드**(빌더, 스크립트, 웹사이트 프론트엔드 등): [MIT](LICENSE)
- **Wiki 콘텐츠**(`wiki/`): [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<div align="center">

**Built with curiosity, rigor, and a belief that humanoid robotics needs a map, not just more demos.**

</div>
