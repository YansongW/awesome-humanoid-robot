<div align="center">

# Awesome Humanoid Robot 🤖

**휨로봇의 0에서 1로의 양산 및 산업화 적용을 위한 큐레이션 지식 그래프.**

<p>
  <img src="https://img.shields.io/badge/status-private%20pre--v0.1.0-blueviolet" alt="Status: private pre-v0.1.0" />
  <img src="https://img.shields.io/badge/entries-80-green" alt="80 entries" />
  <img src="https://img.shields.io/badge/relationships-57-brightgreen" alt="57 relationships" />
  <img src="https://img.shields.io/badge/workstreams-16-orange" alt="16 workstreams" />
  <img src="https://img.shields.io/badge/validation-passing-success" alt="Validation passing" />
</p>

🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

</div>

---

## 📌 이 프로젝트는 무엇인가?

**Awesome Humanoid Robot**은 하나의 핵심 질문을 중심으로 구축된 구조화되고 지속적으로 발전하는 지식 베이스입니다:

> **휨로봇의 0에서 1로의 양산 및 산업화 적용을 어떻게 실현할 것인가?**

원자재, 부품, 제조 공정부터 설계 공학, AI, 소프트웨어, 데이터, 조립·테스트, 양산, 적용 시나리오, 시장, 정책 및 규제에 이르는 전체 여정의 모든 단계를 추적합니다. 우리는 단순한 논문 목록이나 제품 목록에 머물지 않고, 휨로봇 산업 전체를 **지식 그래프**로 모델링합니다: 엔티티는 노드이고, 관계는 타입이 지정된 엣지이며, 모든 주장은 출처로 추적 가능합니다.

이 프로젝트는 **AI 보조, 인간 검증** 방식으로 운영됩니다. AI4Sci 파이프라인을 활용해 발견, 추출, 종합을 가속화하지만, 어떤 콘텐츠도 생산 환경으로 승격되기 전에 인간의 검토를 거칩니다.

---

## 🎯 왜 이 프로젝트를 하는가?

휨로봇은 중요한 전환점에 있습니다. 전 세계 연구실은 이미 걷고, 조작하고, 상호작용할 수 있는 로봇을 만들 수 있습니다. 하지만 **데모에서 작동하는 로봇**과 **대규모로 생산·배치·유지보수 가능한 실제 제품**은 전혀 다른 문제입니다.

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

## 🗺️ 여기서 무엇을 찾을 수 있는가?

| 영역 | 추적 내용 |
|------|-----------|
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
| **기초 학문** | 모든 공학 분야를 뒷받침하는 수학, 물리, 화학, 컴퓨터 과학 개념 |

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

1. **체계적인 스캐닝** — 워크스트림이 arXiv, Semantic Scholar 및(계획된) 웹 소스를 검색하여 관련 논문과 산업 인텔리전스를 발견합니다.
2. **관련성 분류** — LLM이 핵심 질문에 따라 각 출처에 점수를 매기고 낮은 관련성 콘텐츠를 필터링합니다.
3. **구조화된 추출** — LLM이 타입이 지정된 항목, 다국어 요약 및 후보 관계를 작성합니다.
4. **임시 저장** — 모든 AI 초안은 `.staging/`에 격리되어 검토를 기다립니다.
5. **인간 검토** — 검토자가 각 초안을 승인, 편집 또는 거부합니다.
6. **통합 및 검증** — 승인된 항목은 `research/` 및 `data/relationships/`로 이동하고 `scripts/validate_entries.py`를 통과해야 합니다.

전체 파이프라인은 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)에 문서화되어 있습니다.

---

## 🚀 빠른 시작

```bash
# 1. 저장소 클론
git clone https://github.com/YansongW/awesome-humanoid-robot.git
cd awesome-humanoid-robot

# 2. 가상 환경 활성화
source .venv/bin/activate

# 3. 현재 지식 그래프 검증
python scripts/validate_entries.py

# 4. 단일 워크스트림 실행 (예: VLA 조사)
python scripts/ai4sci_batch_pipeline.py \
  scripts/ai4sci_workstreams/definition/algorithm_survey/vla.yaml \
  --max-papers 5 --max-workers 2

# 5. 또는 여러 워크스트림을 병렬로 실행
python scripts/ai4sci_orchestrator.py --max-workers 2 --max-batch-workers 1 --max-papers 5

# 6. 임시 출력 검토
python scripts/ai4sci_review.py
```

자격 증명 설정 방법은 [`docs/ai4sci/literature_review_pipeline.md`](docs/ai4sci/literature_review_pipeline.md)를 참조하세요.

---

## 📊 프로젝트 통계

| 지표 | 수량 |
|------|------|
| 생산급 항목 | 80 |
| 관계 | 57 |
| 워크스트림 설정 | 16 |
| 온톨로지 도메인 | 12 + `00_foundations` |
| 지원 언어 | 영 / 중 / 한 |
| 검증 상태 | ✅ 통과 |

---

## 🛣️ 로드맵

| 단계 | 목표 | 상태 |
|------|------|------|
| **Phase 0** | 정보 아키텍처, Schema, 검증 메커니즘 | ✅ 완료 |
| **Phase 1** | 도메인별 온톨로지 문서(01–12) | ✅ 완료 |
| **Phase 2** | 워크스트림 기반 콘텐츠 채우기 | 🔄 진행 중 |
| **Phase 3** | 낶부 검토, 검증 워크플로우, v0.1.0 공개 릴리스 | ⏳ 계획 |

전체 워크스트림 TODO는 [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md)에서, 최신 세션 기록은 [`docs/session_status.md`](docs/session_status.md)에서 확인하세요.

---

## 👥 누구를 위한 것인가?

- **연구원** — 문제 영역과 산업 계층별로 휨로봇 최신 동향 파악.
- **엔지니어** — 자신의 서브시스템과 관련된 부품 공급사, 시뮬레이션 도구, 데이터셋, 벤치마크 발견.
- **창업자 / 투자자** — 공급망을 그리고, 공백을 발견하며, 경쟁사를 추적.
- **제조 및 운영** — 공장 설계, 수율, 비용 요인 및 확장 트레이드오프 이해.
- **정책 입안자** — 규제, 안전 및 윤리 환경 이해.

---

## 🤝 기여

> 공개 기여 가이드는 `v0.1.0`에 공개됩니다.

그때까지 콘텐츠는 핵심 팀이 AI4Sci를 활용하여 정리합니다. 본 비공개 저장소에 접근 권한이 있다면:

- 출처 링크와 검증 상태를 포함하여 항목을 추가하세요.
- 불확실하거나 상충되는 주장을 표시하세요.
- [`docs/ontology/`](docs/ontology/) 및 [`docs/architecture/information_model.md`](docs/architecture/information_model.md)의 항목 형식과 관계 유형을 따르세요.

---

## 📂 디렉토리 구조

```
awesome-humanoid-robot/
├── README.md                          # 영문 메인 문서
├── README.zh.md                       # 중국어 간체
├── README.ko.md                       # 한국어(본 파일)
├── docs/
│   ├── project_charter.md             # 프로젝트 헌장
│   ├── ontology/                      # 산업 체인 온톨로지 문서(01–12 + 개요)
│   ├── architecture/                  # 정보 모델 및 사전 설계 분석
│   └── ai4sci/                        # AI4Sci 파이프라인 문서 및 워크스트림 택스노미
├── research/                          # 생산급 지식 베이스 항목
│   ├── foundations/                   # 수학, 물리, 화학, 컴퓨터 과학 개념
│   ├── materials/                     # 원자재
│   ├── components/                    # 부품 및 서브시스템
│   ├── companies/                     # 회사 프로필 및 산업 지도
│   ├── papers/                        # 논문 노트
│   └── datasets/                      # 데이터셋 노트
├── data/
│   ├── schema/v1/                     # JSON Schema
│   └── relationships/                 # 독립 관계 파일
├── scripts/                           # AI4Sci 보조 스크립트
│   ├── ai4sci_lib/                    # 재사용 가능한 파이프라인 단계
│   ├── ai4sci_workstreams/            # 워크스트림 YAML 설정
│   ├── ai4sci_paper_pipeline.py
│   ├── ai4sci_batch_pipeline.py
│   ├── ai4sci_orchestrator.py
│   ├── ai4sci_review.py
│   ├── ai4sci_status.py
│   └── validate_entries.py
└── .staging/                          # AI 생성 초안, 인간 검토 대기 중
```

---

## 📜 라이선스

공개 전 확정.

---

<div align="center">

**호기심과 엄격함으로构建 — 우리는 휨로봇이 더 많은 데모가 아니라 지도가 필요하다고 믿습니다.**

</div>
