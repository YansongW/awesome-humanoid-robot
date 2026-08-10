---
$id: ent_paper_michalski_value_based_inventory_manageme_2008
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Value-Based Inventory Management
  zh: 基于价值的库存管理
  ko: 가치 기반 재고 관리
summary:
  en: This paper reformulates the EOQ and POQ inventory models using a value-based objective driven by discounted free cash
    flows to the firm (FCFF) and economic value added (EVA), deriving VBEOQ and VBPOQ formulas that account for the cost of
    capital and taxes.
  zh: 本文提出基于价值的库存管理模型，将经济订货量（EOQ）与定期订货量（POQ）模型重构为以企业价值最大化为目标的框架。作者通过引入折现自由现金流（FCFF）和经济增加值（EVA）指标，推导出VBEOQ和VBPOQ公式，将资本成本与税收因素纳入库存决策。
  ko: 본 논문은 기업의 잔여현금흐름(FCFF)과 경제적부가가치(EVA)를 기반으로 한 가치 중심 목표함수를 사용하여 EOQ 및 POQ 재고 모형을 재구성하고 자본비용과 세율을 반영한 VBEOQ 및 VBPOQ 공식을
    도출한다.
domains:
- 05_mass_production
- 03_manufacturing_processes
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- inventory_management
- economic_order_quantity
- production_order_quantity
- value_based_management
- working_capital
- mass_production
- component_procurement
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1301.3826v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: en/ko
    body retranslated from zh deep-read (608 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Value-Based Inventory Management
  url: https://arxiv.org/abs/1301.3826
  date: '2008'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
传统库存管理模型以账面利润最大化为目标，但可能偏离企业价值最大化的根本财务目标。本研究重新审视EOQ与POQ模型，用基于价值的视角替代利润导向的假设。核心创新在于将折现自由现金流（FCFF）和经济增加值（EVA）作为目标函数，推导出VBEOQ和VBPOQ两个新公式。这些公式明确考虑了资本成本与税收对库存决策的影响，使库存管理直接服务于企业价值提升。

## 核心内容
### 研究背景与问题
- 企业基本财务目标是价值最大化，库存管理系统应服务于这一目标
- 现有财务管理文献中的资产模型多基于账面利润最大化假设，可能偏离价值最大化目标

### 方法创新
- 将EOQ（经济订货量）和POQ（定期订货量）模型重构为价值导向框架
- 目标函数从利润最大化改为折现自由现金流（FCFF）与经济增加值（EVA）最大化
- 推导出VBEOQ（基于价值的EOQ）和VBPOQ（基于价值的POQ）公式

### 关键参数
- 资本成本：作为库存持有成本的重要组成部分纳入模型
- 税收影响：在现金流折现过程中考虑税盾效应
- 公式结构：VBEOQ和VBPOQ在传统EOQ/POQ基础上增加了资本成本与税收调整项

### 结论
- 价值导向的库存模型比利润导向模型更符合企业长期财务目标
- 新公式为管理者提供了将库存决策与资本预算、税务规划整合的理论工具
- 该模型适用于资本密集型行业及高税率环境下的库存优化

## 参考
- http://arxiv.org/abs/1301.3826v1

## Overview
Traditional inventory management models aim to maximize book profit, but they may deviate from the fundamental financial goal of maximizing enterprise value. This study re-examines the EOQ and POQ models, replacing profit-oriented assumptions with a value-based perspective. The core innovation lies in using discounted free cash flow (FCFF) and economic value added (EVA) as objective functions, deriving two new formulas: VBEOQ and VBPOQ. These formulas explicitly account for the impact of capital costs and taxes on inventory decisions, enabling inventory management to directly serve the enhancement of enterprise value.

## Content
### Research Background and Problem
- The fundamental financial goal of a firm is value maximization, and inventory management systems should serve this goal
- Asset models in existing financial management literature are mostly based on the assumption of book profit maximization, which may deviate from the goal of value maximization

### Methodological Innovation
- Reconstruct the EOQ (Economic Order Quantity) and POQ (Periodic Order Quantity) models within a value-oriented framework
- Shift the objective function from profit maximization to maximizing discounted free cash flow (FCFF) and economic value added (EVA)
- Derive the VBEOQ (Value-Based EOQ) and VBPOQ (Value-Based POQ) formulas

### Key Parameters
- Cost of capital: incorporated into the model as a significant component of inventory holding costs
- Tax impact: tax shield effects are considered in the cash flow discounting process
- Formula structure: VBEOQ and VBPOQ add adjustments for capital costs and taxes to the traditional EOQ/POQ

### Conclusion
- Value-oriented inventory models align more closely with long-term corporate financial goals than profit-oriented models
- The new formulas provide managers with theoretical tools to integrate inventory decisions with capital budgeting and tax planning
- The model is suitable for inventory optimization in capital-intensive industries and high-tax environments

## 개요
전통적 재고 관리 모델은 장부 이익 극대화를 목표로 하지만, 기업 가치 극대화라는 근본적인 재무 목표에서 벗어날 수 있습니다. 본 연구는 EOQ 및 POQ 모델을 재검토하고, 이익 중심 가정을 가치 기반 관점으로 대체합니다. 핵심 혁신은 할인된 자유 현금 흐름(FCFF)과 경제적 부가가치(EVA)를 목표 함수로 사용하여 VBEOQ와 VBPOQ라는 두 가지 새로운 공식을 도출한 것입니다. 이 공식들은 자본 비용과 세금이 재고 결정에 미치는 영향을 명시적으로 고려하여, 재고 관리가 기업 가치 제고에 직접적으로 기여하도록 합니다.

## 핵심 내용
### 연구 배경 및 문제
- 기업의 기본 재무 목표는 가치 극대화이며, 재고 관리 시스템은 이 목표를 지원해야 함
- 기존 재무 관리 문헌의 자산 모델은 주로 장부 이익 극대화 가정에 기반하여 가치 극대화 목표에서 벗어날 수 있음

### 방법 혁신
- EOQ(경제적 주문량) 및 POQ(정기 주문량) 모델을 가치 중심 프레임워크로 재구성
- 목표 함수를 이익 극대화에서 할인된 자유 현금 흐름(FCFF) 및 경제적 부가가치(EVA) 극대화로 변경
- VBEOQ(가치 기반 EOQ) 및 VBPOQ(가치 기반 POQ) 공식 도출

### 핵심 매개변수
- 자본 비용: 재고 보유 비용의 중요한 구성 요소로 모델에 포함
- 세금 영향: 현금 흐름 할인 과정에서 세금 방패 효과 고려
- 공식 구조: VBEOQ 및 VBPOQ는 전통적 EOQ/POQ에 자본 비용 및 세금 조정 항목을 추가

### 결론
- 가치 중심 재고 모델은 이익 중심 모델보다 기업의 장기 재무 목표에 더 부합함
- 새로운 공식은 관리자가 재고 결정을 자본 예산 및 세무 계획과 통합할 수 있는 이론적 도구를 제공
- 이 모델은 자본 집약적 산업 및 높은 세율 환경에서의 재고 최적화에 적합함
