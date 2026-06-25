# Awesome Humanoid Robot 🤖

> 휨로봇의 **0에서 1로의 양산 및 산업화 적용**을 중심으로 한 지식 베이스. 원자재, 부품 공급망, 제조 공정, 설계 공학, AI 및 소프트웨어, 조립 테스트, 양산, 적용 시나리오, 정책 및 규제 등 전 과정을 다룹니다.
>
> **AI4Sci** 방법으로 구축 — 인공지능을 활용한 과학 연구, 문헌 검토 및 산업 인텔리전스 정리.
>
> 🌐 [English](README.md) · [简体中文](README.zh.md) · [한국어](README.ko.md)

---

## 왜 이 프로젝트를 하는가

이 프로젝트는 하나의 핵심 질문을 중심으로 합니다:

> **휨로봇의 0에서 1로의 양산 및 산업화 적용을 어떻게 실현할 것인가?**

연구실에서 작동하는 휨로봇과 대규모로 생산·배치·유지보수 가능한 실제 제품은 전혀 다른 문제입니다. 프로토타입에서 확장 가능한 제품으로 가기 위해서는 시스템의 모든 계층을 넘어서야 합니다:

- **원자재 및 핵심 자원**: 휨로봇은 어떤 광물, 금속, 자재, 화학물질을 소비하는가? 어디에서 오는가? 공급 리스크는 무엇인가?
- **부품 및 서브시스템**: 모터, 감속기, 센서, 배터리, 컴퓨팅 유닛, 엔드 이펙터, 구조물 — 누가 생산하고, 성능은 어떻고, 비용은 얼마인가?
- **제조 공정**: 이 부품들은 어떻게 정밀 가공, 주조, 권선, 조립, 테스트되는가?
- **설계 및 시스템 공학**: 로봇의 형태, 운동학, 동역학, 신뢰성, 안전성은 무엇으로 결정되는가?
- **소프트웨어 및 AI**: 지각, 계획, locomotion, manipulation, 장기 자율을 가능하게 하는 알고리즘은 무엇인가?
- **데이터 및 인프라**: 개발과 검증에 필요한 데이터셋, 시뮬레이터, 미들웨어, 툴체인은 무엇인가?
- **조립, 통합 및 테스트**: 로봇은 어떻게 부품 더미에서 교정되고 검증된 제품이 되는가?
- **양산**: 어떤 공장 설계, 공급망 협력, 수율 관리, 비용 공학이 수천~수만 대 규모를 뒷받침할 수 있는가?
- **적용 및 시장**: 휨로봇이 오늘날 경제적 가치가 있는 산업과 작업은 어디인가? 내일은?
- **정책 및 규제**: 어떤 안전 기준, 인증 체계, 책임 프레임워크, 사회 규범이 배치를 촉진하거나 막는가?

우리는 휨로봇이 단순한 AI 연구 문제가 아니라는 것을 믿습니다. 재료 과학, 정밀 제조, 글로벌 공급망, 소프트웨어 공학, 실제 세계 배치가 연결되는 시스템 문제입니다.

우리는 **AI4Sci** 방법으로 이 전체 여정의 지도를 그립니다. 목표는 단순히 논문이나 제품을 쌓는 것이 아니라, 각 계층이 어떻게 맞물리는지, 병목은 어디에 있는지, 어떤 결정이 휨로봇을 진정한 산업으로 만드는지 이해하는 것입니다.

---

## 다루는 범위

본 프로젝트는 산업 체인 온톨로지에 따라 다음 영역을 다룹니다:

| 영역 | 추적 내용 |
|------|-----------|
| **원자재 및 핵심 자원** | 희토류, 자재, 경량 금속, 복합재료, 반도체, 배터리 화학 |
| **부품 및 서브시스템** | 액추에이터, 모터, 감속기/기어박스, 센서, 배터리, 컴퓨팅 유닛, 엔드 이펙터, 케이블, 구조물 |
| **공급망 및 제조 공정** | 티어1/티어2 공급사, 제조 공정, 품질 관리, 비용 구조, 지역 산업 생태계 |
| **설계 및 공학** | 기계 설계, 운동학, 동역학, 휨 형태, 자유도, 안전 설계 |
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

## 아키텍처 우선 접근법

콘텐츠를 채우기 전에 본 프로젝트는 먼저 **공식 정보 모델**을 구축하여 전체 산업 체인의 엔티티, 관계, 계층, 도메인 및 교차 의존성을 수용합니다.

핵심 아키텍처 결정:

- **그래프 우선**: 엔티티는 노드이고, 관계는 방향성 있는 엣지입니다.
- **이중 태그**: 각 엔티티는 **가치 사슬 계층**(Upstream / Midstream / Intelligence / Validation-Markets)과 **기능적 역할**(재료 / 부품 / 공정 / 시스템 / 지능 / 등)을 모두 가집니다.
- **관계를 일급 객체로**: 교차 도메인 링크는 명시적이고, 유형화되며, 검증 가능합니다.
- **다국어 기본 설계**: 이름, 요약, 설명은 언어 맵으로 저장됩니다.
- **버전 관리 schema**: 항목 및 관계 schema는 버전 관리 및 확장이 가능합니다.
- **YAML frontmatter + Markdown**: 항목은 사람이 읽을 수 있고 기계가 읽을 수 있습니다.

전체 사양은 [`docs/architecture/information_model.md`](docs/architecture/information_model.md) 및 [`data/schema/v1/`](data/schema/v1/)를 참조하세요.

---

## AI4Sci 방법

본 프로젝트는 AI 보조 연구 프로세스를 사용합니다:

1. **체계적인 문헌 및 산업 스캔**: 학술 논문, 특허, 회사 발표, 공급망 보고서, 기술 블로그 추적.
2. **구조화된 추출**: 각 엔티티는 유형, 계층/도메인/역할로 태그되고 출처에 연결됩니다.
3. **교차 검증**: 주장은 원천 출처로 추적되며, 충돌 정보는 명시적으로 표시.
4. **그래프 중심 조직**: 항목과 관계는 지식 그래프를 형성하며, 플랫 리스트가 아닙니다.
5. **인간 검토**: AI가 수집과 종합을 가속화하지만, 모든 고위험 공개 주장은 인간 검토를 거침.

### 워크스트림 택스노미

콘텐츠는 **워크스트림**을 통해 채워집니다. 각 워크스트림은 0→1 지식 트리에 매핑된 집중적이고 병렬화 가능한 AI4Sci 연구 작업이며, `scripts/ai4sci_workstreams/` 아래의 YAML 설정 파일로 정의됩니다.

택스노미는 네 가지 차원으로 구성됩니다:

- **제품 개발 단계**: Definition → Design → Verification Planning → MVP → Testing → EVT → DVT → PVT → Mass Production / Ramp
- **공학 분야**: Hardware, Software & AI, Data Systems, Infra/Cloud/Fleet, Embedded, Mechanical Structure, Simulation, Supply Chain & Manufacturing, Quality & Reliability, Safety & Certification, Applications & Markets, Policy & Ethics
- **지식 유형**: Papers, Datasets, Benchmarks, Technologies, Components, Companies, Reports, Standards
- **이론적 깊이**: Foundation → Principle/Theorem → Formalism → Method/Algorithm → System/Implementation

이를 통해 WBC와 같은 고위층 개념을 QP formulation, KKT conditions, Lagrange multipliers, 그리고 궁극적으로 다변수 미적분학과 선형대수학까지 추적할 수 있습니다.

전체 택스노미는 [`docs/ai4sci/workstream_roadmap.md`](docs/ai4sci/workstream_roadmap.md)에서, 실행 가능한 장기 TODO는 [`docs/ai4sci/WORKSTREAM_TREE.md`](docs/ai4sci/WORKSTREAM_TREE.md)에서, 구체적인 지식 체인 예시는 [`docs/ai4sci/knowledge_chain_examples.md`](docs/ai4sci/knowledge_chain_examples.md)에서 확인하세요.

자세한 내용은 [`docs/ai4sci/`](docs/ai4sci/)를 참조하세요.

---

## 로드맵 및 현재 작업

### 0 단계: 정보 아키텍처 ✅ 완료

콘텐츠를 추가하기 전에 구조적 기반을 구축했습니다.

- [x] 핵심 질문과 온톨로지 영역 정의
- [x] 정보 모델 설계(엔티티, 관계, 계층, 역할)
- [x] 항목 및 관계를 위한 JSON schema 생성
- [x] 모델을 검증할 샘플 엔티티 및 관계 추가
- [x] 검증 스크립트 추가
- [x] 첫 번째 샘플을 기반으로 모델 검증 및 정제

### 1 단계: 온톨로지 확장 ✅ 완료

- [x] 영역별 온톨로지 문서 완성(01–12)
- [x] 각 영역의 교차 도메인 관계 패턴 정의
- [x] 제어 어휘 및 확장 규칙 수립
- [x] 콘텐츠 채우기 전 온톨로지 문서 낶부 검토

### 2 단계: 워크스트림 기반 콘텐츠 채우기 ✅ 진행 중

콘텐츠는 이제 0→1 라이프사이클에 맞춘 병렬 워크스트림을 통해 추가됩니다:

- [x] 첫 멀티 에이전트 워크스트림 배치 실행 (VLA, 기업, 원자재, 교차 도메인)
- [ ] 워크스트림 설정을 라이프사이클 × 도메인 트리 구조로 재구성
- [ ] 우선순위 리프 워크스트림 추가: 전신 제어, MPC, 액추에이터 모듈 설계, 힘/토크 센서, 희토류 자석, 시뮬레이션 플랫폼, 안전 표준
- [x] 양산과 관련된 AI / 모델 콘텐츠 큐레이션(첫 배치: VLA 서베이 + 데이터셋/벤치마크/데이터 엔진)
- [ ] 휨로봇 BOM / 부품 지도 구축
- [ ] 회사 및 공급업체 생태계 매핑
- [ ] 원자재, 제조 공정 및 비용 요인 추적

### 3 단계: 검증 및 공개 릴리스

- [ ] schema에 따라 초기 항목 검증
- [ ] 주장과 출처에 대한 낶부 검토
- [ ] v0.1.0 및 기여 가이드라인 게시

---

## 프로젝트 상태 및 릴리스 전략

> **현재 단계**: 비공개 연구 및 프레임워크 구축.  
> **공개 목표**: 온톨로지, 초기 콘텐츠, 검증 프로세스 완료 후 `v0.1.0` 릴리스.

| 단계 | 목표 | 가시성 |
|------|------|--------|
| v0.1.0 이전 | 온톨로지 구축, 초기 항목 채우기, 검증 워크플로우 확립 | **비공개** |
| v0.1.0 | 공개 및 커뮤니티 공동 창작 | **공개** |
| v0.1.0 이후 | 지속적 업데이트, 분기별 릴리스, 영역별 심화 | 공개 |

v0.1.0 이전까지 본 저장소는 비공개입니다. 모든 콘텐츠는 초안으로 취급되며 공개 전 검증이 필요합니다.

---

## 디렉토리 구조

```
awesome-humanoid-robot/
├── README.md                          # 영문 메인 문서
├── README.zh.md                       # 중국어 간체
├── README.ko.md                       # 한국어
├── docs/
│   ├── project_charter.md             # 프로젝트 헌장 (영문)
│   ├── project_charter.zh.md          # 프로젝트 헌장 (중국어 간체)
│   ├── project_charter.ko.md          # 프로젝트 헌장 (한국어)
│   ├── ontology/
│   │   ├── 00_overview.md             # 산업 체인 온톨로지 지도 (영문)
│   │   ├── 00_overview.zh.md          # 산업 체인 온톨로지 지도 (중국어 간체)
│   │   ├── 00_overview.ko.md          # 산업 체인 온톨로지 지도 (한국어)
│   │   ├── 01_raw_materials.md        # 원자재 및 핵심 자원 (.zh.md 포함)
│   │   ├── 02_components_supply_chain.md
│   │   ├── 03_manufacturing_processes.md
│   │   ├── 04_assembly_integration_testing.md
│   │   ├── 05_mass_production.md
│   │   ├── 06_design_engineering.md
│   │   ├── 07_ai_models_algorithms.md
│   │   ├── 08_software_middleware.md
│   │   ├── 09_data_datasets.md
│   │   ├── 10_evaluation_benchmarks.md
│   │   ├── 11_applications_markets.md
│   │   ├── 12_policy_regulation_ethics.md
│   │   └── session_status.md          # 현재 세션 상태 및 다음 작업
│   ├── architecture/
│   │   ├── 00_analysis_before_design.md
│   │   └── information_model.md       # 공식 데이터 아키텍처
│   └── ai4sci/
│       ├── literature_review_pipeline.md
│       ├── verification_criteria.md
│       ├── workstream_roadmap.md      # 0→1 지식 택스노미
│       ├── WORKSTREAM_TREE.md         # 장기 워크스트림 TODO
│       └── knowledge_chain_examples.md # 거시에서 미시로의 이론 체인 예시
├── research/
│   ├── materials/                     # 원자재 항목
│   ├── components/                    # 부품 항목
│   ├── companies/                     # 회사 프로필 및 산업 지도
│   ├── papers/                        # 논문 노트
│   └── datasets/                      # 데이터셋 노트
├── data/
│   ├── schema/v1/                     # JSON Schema
│   │   ├── entry_schema.json
│   │   └── relationship_schema.json
│   └── relationships/                 # 독립 관계 파일
└── scripts/                           # AI4Sci 보조 스크립트
    ├── ai4sci_lib/                    # 재사용 가능한 파이프라인 단계
    ├── ai4sci_workstreams/            # 워크스트림 YAML 설정
    ├── ai4sci_paper_pipeline.py
    ├── ai4sci_review.py
    ├── ai4sci_batch_pipeline.py
    ├── ai4sci_orchestrator.py
    ├── ai4sci_status.py
    └── validate_entries.py
```

---

## 사용 시나리오

- **연구원**: 문제 영역과 산업 계층별로 휨로봇 최신 동향 파악.
- **창업자 / 투자자**: 공급망을 그리고, 공백을 발견하며, 경쟁사를 추적.
- **엔지니어**: 자신의 서브시스템과 관련된 부품 공급사, 시뮬레이션 도구, 데이터셋, 벤치마크 발견.
- **정책 입안자**: 규제 및 윤리 환경 이해.

---

## 기여

> 공개 기여 가이드는 `v0.1.0`에 공개됩니다.

그때까지 콘텐츠는 핵심 팀이 AI4Sci를 활용하여 정리합니다. 본 비공개 저장소에 접근 권한이 있다면:

- 출처 링크와 검증 상태를 포함하여 항목을 추가하세요.
- 불확실하거나 상충되는 주장을 표시하세요.
- [`docs/architecture/information_model.md`](docs/architecture/information_model.md)의 항목 형식과 관계 유형을 따르세요.

---

## 라이선스

공개 전 확정.
