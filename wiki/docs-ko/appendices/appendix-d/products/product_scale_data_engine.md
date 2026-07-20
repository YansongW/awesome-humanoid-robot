# Scale AI Data Engine

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Scale AI](../companies/company_scale_ai.md) |
| **제품 카테고리** | AI 학습 데이터 플랫폼 / 데이터 라벨링 / RLHF |
| **출시일** | 2016년 |
| **상태** | 상용 / 대규모화 |
| **공식 사이트/출처** | [Scale Data Engine](https://scale.com/data-engine) |

## 제품 개요

Scale Data Engine은 Scale AI의 핵심 제품으로, AI 학습 데이터의 전체 수명 주기(데이터 수집, 선별, 라벨링, 강화 학습 인간 피드백(RLHF) 및 모델 평가)를 포괄합니다. 이 플랫폼은 이미지, 비디오, 3D 포인트 클라우드, 텍스트, 오디오, 센서 융합 등 다중 모드 데이터를 지원하며, 자율 주행, 로봇, 대규모 언어 모델 및 정부 국방 프로젝트의 핵심 인프라입니다.

Data Engine은 Rapid(Scale이 관리 플랫폼과 크라우드소싱/전문가 라벨링 팀 제공) 및 Self-Serve(기업이 Scale 도구와 자체 팀을 활용하여 협업)의 두 가지 서비스 모드를 제공합니다. 플랫폼은 AI 사전 라벨링, 수동 검토, 합의 메커니즘 및 자동화된 품질 검사를 통해 라벨링 품질을 보장하면서 효율성을 향상시킵니다.

2025년, Scale은 Physical AI 프로젝트를 추가로 출시하여, 구체적 지능 및 휴머노이드 로봇을 위한 1인칭 시점 조작 데모 데이터를 수집하고, 로봇 데이터 공급망에서의 핵심 위치를 강화했습니다.

## 제품 이미지

> Scale Data Engine: [공식 자료](https://scale.com/data-engine)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 지원 데이터 유형 | 이미지, 비디오, 3D 포인트 클라우드, 텍스트, 오디오, 센서 융합 | Scale 공식 사이트 |
| 라벨링 기능 | 2D/3D 경계 상자, 의미론적 분할, 키포인트, 궤적, 속성 | Scale 문서 |
| 서비스 모드 | Rapid(관리형) / Self-Serve(자체 서비스) | Scale 공식 사이트 |
| 품질 메커니즘 | AI 사전 라벨링 + 수동 검토 + 합의 메커니즘 | 공개 자료 |
| 규정 준수 인증 | SOC 2 Type II, ISO 27001, FedRAMP High | Scale 공식 사이트 |
| 로봇 데이터 | LiDAR, 카메라, IMU, 촉각 등 다중 센서 라벨링 | Scale 문서 |
| 가격 | 작업 복잡도에 따라 과금 | 공개 보도 |

## 공급망 위치

- **제조사**: [Scale AI](../companies/company_scale_ai.md)
- **핵심 부품/기술 출처**: AWS/Google Cloud/Azure 클라우드 인프라, 글로벌 크라우드소싱 및 전문가 네트워크, AI 사전 라벨링 모델, 데이터 보안 및 규정 준수 체계.
- **하위 응용/고객**: OpenAI, Meta, Microsoft, Google, Toyota, GM, 미국 국방부, 자율 주행 기업, 로봇 기업.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_scale_data_engine`
- 제조사 엔터티: `ent_company_scale_ai`
- 주요 관계:
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_data_engine` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_data_engine`)

## 응용 시나리오

- **자율 주행 인식 학습**: 3D 포인트 클라우드 라벨링, 2D 경계 상자, 차선, 교통 표지판 인식.
- **로봇 파지 및 내비게이션**: 조작 비디오 라벨링, 객체 키포인트, 힘 피드백 데이터 정렬.
- **대규모 언어 모델 RLHF**: 선호도 순위, 안전 평가, 명령어 준수 데이터 세트 구축.
- **국방 정보 분석**: 다중 소스 정보 데이터 라벨링 및 모델 평가.

## 경쟁 비교

| 비교 항목 | Scale Data Engine | Appen | Labelbox |
|--------|-------------------|-------|----------|
| 포지셔닝 | 풀스택 AI 학습 데이터 플랫폼 | 관리형 라벨링 서비스 | 기업 자체 서비스 라벨링 소프트웨어 |
| 핵심 강점 | RLHF, 정부 규정 준수, 로봇 데이터 | 저비용 고용량 | 자체 서비스 유연성 |
| 서비스 모드 | Rapid + Self-Serve | 관리형 중심 | 자체 서비스 중심 |
| 규정 준수 | FedRAMP High, SOC 2 | 비교적 우수 | 비교적 우수 |
| 대표 고객 | 최첨단 AI 연구소, 국방 | 대형 기술 기업 | 중견 기업 |

## 구매 및 배포 권장 사항

- 데이터 양이 방대하고 품질 요구 사항이 높은 자율 주행 또는 로봇 프로젝트의 경우 Rapid 모드를 우선 선택할 수 있습니다.
- 이미 라벨링 팀을 보유하고 데이터 프라이버시를 중시하는 기업의 경우 Self-Serve 모드가 더 통제 가능합니다.
- 정부 또는 국방 프로젝트와 관련된 경우 FedRAMP High 등 규정 준수 자격 및 데이터 격리 요구 사항을 확인해야 합니다.

## 참고 자료

1. [Scale Data Engine 제품 페이지](https://scale.com/data-engine)
2. [Scale AI 공식 사이트](https://scale.com)
3. [Scale Physical AI 블로그](https://scale.com/blog/physical-ai)
4. [Scale AI 자금 조달 및 가치 평가 보도](https://scale.com/blog)
