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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1301.3826v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## Overview
The basic financial purpose of a firm is to maximize its value. An inventory management system should also contribute to realization of this basic aim. Many current asset management models currently found in financial management literature were constructed with the assumption of book profit maximization as basic aim. However these models could lack what relates to another aim, i.e., maximization of enterprise value. This article presents a modified value-based inventory management model.

## 개요
기업의 기본적인 재무 목표는 가치를 극대화하는 것입니다. 재고 관리 시스템 또한 이러한 기본 목표의 실현에 기여해야 합니다. 현재 재무 관리 문헌에서 발견되는 많은 유동 자산 관리 모델은 장부 이익 극대화를 기본 목표로 가정하여 구축되었습니다. 그러나 이러한 모델은 기업 가치 극대화라는 또 다른 목표와 관련된 부분이 부족할 수 있습니다. 본 논문은 수정된 가치 기반 재고 관리 모델을 제시합니다.

## 핵심 내용
기업의 기본적인 재무 목표는 가치를 극대화하는 것입니다. 재고 관리 시스템 또한 이러한 기본 목표의 실현에 기여해야 합니다. 현재 재무 관리 문헌에서 발견되는 많은 유동 자산 관리 모델은 장부 이익 극대화를 기본 목표로 가정하여 구축되었습니다. 그러나 이러한 모델은 기업 가치 극대화라는 또 다른 목표와 관련된 부분이 부족할 수 있습니다. 본 논문은 수정된 가치 기반 재고 관리 모델을 제시합니다.

## 参考
- http://arxiv.org/abs/1301.3826v1
