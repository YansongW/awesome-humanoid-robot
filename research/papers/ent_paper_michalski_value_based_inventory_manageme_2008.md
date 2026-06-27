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
  en: This paper reformulates the EOQ and POQ inventory models using a value-based
    objective driven by discounted free cash flows to the firm (FCFF) and economic
    value added (EVA), deriving VBEOQ and VBPOQ formulas that account for the cost
    of capital and taxes.
  zh: 本文通过以企业自由现金流（FCFF）和经济增加值（EVA）驱动的价值目标重构经济订货量（EOQ）和生产订货量（POQ）模型，推导出考虑资本成本和税率的VBEOQ与VBPOQ公式。
  ko: 본 논문은 기업의 잔여현금흐름(FCFF)과 경제적부가가치(EVA)를 기반으로 한 가치 중심 목표함수를 사용하여 EOQ 및 POQ 재고 모형을
    재구성하고 자본비용과 세율을 반영한 VBEOQ 및 VBPOQ 공식을 도출한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata; full-text review is required before
    marking verified.
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

## Overview

The basic financial purpose of a firm is to maximize its value, yet many inventory management models in the financial management literature were constructed under the assumption of book-profit maximization. Grzegorz Michalski argues that these traditional models may fail to support enterprise-value maximization because they neglect the opportunity cost of capital tied up in inventory. The paper therefore reformulates inventory policy decisions using a value-based framework grounded in discounted free cash flows to the firm (FCFF) and economic value added (EVA).

The main results are two modified models: the value-based economic order quantity (VBEOQ) and the value-based production order quantity (VBPOQ). These formulas incorporate the cost of capital, tax rate, and holding costs into the ordering and production decisions. The paper illustrates the models with numerical examples and shows that ordering or producing less than the traditional EOQ/POQ can increase firm value by reducing the opportunity costs of capital committed to inventory and net working capital.

The analysis is deterministic and limited to single-product inventory decisions, but it explicitly links inventory policy to free cash flow, net working capital, and firm value maximization.

## Key Contributions

- Derives value-based EOQ (VBEOQ) and POQ (VBPOQ) formulas that incorporate the cost of capital, tax rate, and holding costs.
- Shows that ordering or producing less than the traditional EOQ/POQ can increase firm value by reducing opportunity costs of tied-up capital.
- Links inventory policy decisions to free cash flow, net working capital, and firm value maximization.
- Illustrates the models with numerical examples comparing traditional and value-based solutions.

## Relevance to Humanoid Robotics

Efficient value-based inventory management reduces working capital requirements and opportunity costs, which is important for scaling component procurement, production planning, and cash-flow management in humanoid robot mass production. By framing lot-size decisions around enterprise value rather than book profit, the VBEOQ and VBPOQ models can help humanoid robot manufacturers decide how much to order or produce while accounting for the capital cost of holding actuators, sensors, structural parts, and electronic components in inventory.

The method is most relevant to the mass production and manufacturing-process domains, where procurement and production lot sizes directly affect cash flow, storage costs, and the capital efficiency of the supply chain.
