# Scale AI / Scale AI

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Scale AI |
| **영문명** | Scale AI |
| **본사** | 미국 캘리포니아주 샌프란시스코 |
| **설립일** | 2016년 |
| **공식 웹사이트** | [https://scale.com](https://scale.com) |
| **공급망 단계** | AI/로봇 데이터 라벨링, 데이터 엔진, 모델 평가, RLHF |
| **기업 속성** | 스타트업 (미상장) |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Scale AI 공식 웹사이트, Scale 블로그, 공개 투자 보도 |

## 회사 소개

Scale AI는 글로벌 선도적인 AI 훈련 데이터 인프라 기업으로, 핵심 제품인 Scale Data Engine은 데이터 수집, 선별, 라벨링, 강화 학습 인간 피드백(RLHF) 및 모델 평가의 전체 수명 주기를 포괄합니다.

플랫폼은 이미지, 비디오, 3D 포인트 클라우드, 텍스트, 오디오, 센서 융합 등 다중 모드 데이터를 지원하며, 자율 주행, 로봇, 대규모 언어 모델(LLM) 및 정부 국방 프로젝트에 광범위하게 사용됩니다. Scale은 Rapid(Scale이 플랫폼과 라벨러 팀을 관리하여 완료)와 Self-Serve(기업이 Scale 도구와 자체 팀을 협력하여 사용)의 두 가지 모드를 제공합니다. 2025년, Scale은 Physical AI 프로젝트를 출시하여 임베디드 인텔리전스와 로봇 훈련을 위한 1인칭 시연 데이터를 특별히 수집합니다.

2025년 6월, Meta는 143억 달러에 Scale AI의 지분 49%를 인수하여 회사 가치는 290억 달러에 도달했습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|-----------|----------|-----------|-----------|
| AI 훈련 데이터 엔진 | 전체 수명 주기 데이터 플랫폼 | Scale Data Engine | 자율 주행, 로봇, LLM |
| 생성형 AI 데이터 | RLHF, 미세 조정, 선호도 정렬 | Scale Generative AI Data Engine | 대규모 언어 모델, 다중 모드 모델 |
| 정부 및 국방 | 안전한 AI 의사 결정 플랫폼 | Scale Donovan | 국방 정보, 지휘 결정 |
| 모델 테스트 평가 | 레드 팀 테스트, 안전 평가 | Scale Test & Evaluation | 최첨단 모델 안전 |
| 물리적 AI 데이터 | 로봇 조작 시연 데이터 | Scale Physical AI | 휴머노이드 로봇, 임베디드 인텔리전스 |

## 대표 제품

### Scale Data Engine

> Scale Data Engine: [공식 자료](https://scale.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 지원 데이터 유형 | 이미지, 비디오, 3D 포인트 클라우드, 텍스트, 오디오, 센서 융합 | Scale 공식 웹사이트 |
| 라벨링 능력 | 2D/3D 경계 상자, 의미론적 분할, 키포인트, 궤적, 속성 | Scale 문서 |
| 서비스 모드 | Rapid(관리형) / Self-Serve(셀프 서비스) | Scale 공식 웹사이트 |
| 품질 메커니즘 | AI 사전 라벨링 + 수동 검토 + 합의 메커니즘 | 공개 자료 |
| 규정 준수 인증 | SOC 2 Type II, ISO 27001, FedRAMP High | Scale 공식 웹사이트 |
| 로봇 데이터 | LiDAR, 카메라, IMU, 촉각 등 다중 센서 라벨링 지원 | Scale 문서 |
| 가격 | 작업 복잡도에 따라 과금 (작업당 몇 센트에서 수 달러) | 공개 보도 |

**기술적 하이라이트**: AI 보조 사전 라벨링, 다중 모드 데이터 파이프라인, 엔터프라이즈급 품질 및 보안 규정 준수, 자율 주행 및 로봇 전용 도구 체인, 글로벌 크라우드소싱 및 전문가 검토 네트워크.

**적용 시나리오**: 자율 주행 인식 모델 훈련, 로봇 파지/내비게이션 데이터 라벨링, 대규모 언어 모델 RLHF, 의료 영상 및 국방 정보 분석.

### Scale Physical AI

> Scale Physical AI: [공식 자료](https://scale.com)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 데이터 유형 | 1인칭 시점(POV) 조작 시연 비디오 | Scale 뉴스 |
| 수집 방식 | 글로벌 계약자가 장비를 착용하여 수집 | 공개 보도 |
| 작업 시나리오 | 가사, 조립, 운반, 도구 사용 | Scale 블로그 |
| 라벨링 내용 | 동작 분할, 객체 상호작용, 힘 피드백, 언어 명령 | 공개 자료 |
| 대상 모델 | 휴머노이드 로봇 / 임베디드 인텔리전스 VLA 모델 | Scale 뉴스 |
| 가격 | 기업 맞춤형 | 공식 문의 |

**기술적 하이라이트**: 임베디드 인텔리전스를 위한 대규모 인간 조작 데이터 수집, 다중 시점 및 다중 모드 동기화, 동작-언어-시각 정렬, 모방 학습 및 강화 학습 훈련 지원.

**적용 시나리오**: 휴머노이드 로봇 가사 작업 훈련, 산업 조립 기술 학습, 서비스 로봇 상호작용 전략, 로봇 기반 모델 데이터 공급.

## 공급망 위치

- **상류 핵심 부품/소재**: AWS/Google Cloud/Azure 클라우드 인프라, 글로벌 크라우드소싱 및 전문가 라벨링 네트워크, AI 사전 라벨링 모델, 데이터 보안 및 규정 준수 체계.
- **하류 고객/적용 시나리오**: OpenAI, Meta, Microsoft, Google, Toyota, GM, 미국 국방부, 자율 주행 기업, 로봇 기업.
- **주요 경쟁사/대상**: Appen, Labelbox, Surge AI, Tesla 자체 라벨링 팀, Covariant 데이터 플라이휠.

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_scale_ai`
- 제품/플랫폼 엔터티: `ent_product_scale_data_engine`, `ent_product_scale_physical_ai`
- 주요 관계:
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_data_engine` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_data_engine`)
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_physical_ai` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_physical_ai`)

## 참고 자료

1. [Scale AI 공식 웹사이트](https://scale.com)
2. [Scale Data Engine 제품 페이지](https://scale.com/data-engine)
3. [Scale Physical AI 블로그](https://scale.com/blog/physical-ai)
4. [Scale AI 투자 및 가치 평가 보도](https://scale.com/blog)
