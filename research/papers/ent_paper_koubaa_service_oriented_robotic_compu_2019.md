---
$id: ent_paper_koubaa_service_oriented_robotic_compu_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Service-Oriented Robotic Computing for Cloud Robotics
  zh: 面向云机器人技术的服务导向机器人计算
  ko: 클라우드 로보틱스를 위한 서비스 지향 로봇 컴퓨팅
summary:
  en: A survey of service-oriented architecture and Web services for cloud robotics, distinguishing the virtualization of
    robotic systems from computation offloading to cloud-based services.
  zh: 'In this article, we present an overview of the use of service-oriented architecture and Web services in developing
    robotics applications and software integrated with the Internet and the Cloud. This is a recent trend that emerged since
    2010 from the concept of cloud robotics, which leverages the use of cloud infrastructures for robotics applications following
    a service-oriented architecture approach. In particular, we distinguish two main categories: (\textit{i.}) virtualization
    of robotics systems and (\textit{ii.}) computation offloading from robots to cloud-based services. We discuss the ma'
  ko: 본 논문은 서비스 지향 아키텍처와 웹 서비스를 활용한 클라우드 로보틱스를 개괄하며, 로봇 시스템 가상화와 클라우드 기반 서비스로의 계산 오프로딩을 구분한다.
domains:
- 08_software_middleware
- 05_mass_production
- 02_components
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
tags:
- cloud_robotics
- service_oriented_architecture
- web_services
- computation_offloading
- robot_virtualization
- ros
- middleware
- rest
- soap
- websockets
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1901.08173v2.
sources:
- id: src_001
  type: paper
  title: Service-Oriented Robotic Computing for Cloud Robotics
  url: https://arxiv.org/abs/1901.08173
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
In this article, we present an overview of the use of service-oriented architecture and Web services in developing robotics applications and software integrated with the Internet and the Cloud. This is a recent trend that emerged since 2010 from the concept of cloud robotics, which leverages the use of cloud infrastructures for robotics applications following a service-oriented architecture approach. In particular, we distinguish two main categories: (\textit{i.}) virtualization of robotics systems and (\textit{ii.}) computation offloading from robots to cloud-based services. We discuss the main approaches proposed in the literature to design robotics systems through the Web and their integration to the cloud through a service-oriented computing framework.

## 核心内容
In this article, we present an overview of the use of service-oriented architecture and Web services in developing robotics applications and software integrated with the Internet and the Cloud. This is a recent trend that emerged since 2010 from the concept of cloud robotics, which leverages the use of cloud infrastructures for robotics applications following a service-oriented architecture approach. In particular, we distinguish two main categories: (\textit{i.}) virtualization of robotics systems and (\textit{ii.}) computation offloading from robots to cloud-based services. We discuss the main approaches proposed in the literature to design robotics systems through the Web and their integration to the cloud through a service-oriented computing framework.

## 参考
- http://arxiv.org/abs/1901.08173v2

## Overview
In this article, we present an overview of the use of service-oriented architecture and Web services in developing robotics applications and software integrated with the Internet and the Cloud. This is a recent trend that emerged since 2010 from the concept of cloud robotics, which leverages the use of cloud infrastructures for robotics applications following a service-oriented architecture approach. In particular, we distinguish two main categories: (\textit{i.}) virtualization of robotics systems and (\textit{ii.}) computation offloading from robots to cloud-based services. We discuss the main approaches proposed in the literature to design robotics systems through the Web and their integration to the cloud through a service-oriented computing framework.

## Content
In this article, we present an overview of the use of service-oriented architecture and Web services in developing robotics applications and software integrated with the Internet and the Cloud. This is a recent trend that emerged since 2010 from the concept of cloud robotics, which leverages the use of cloud infrastructures for robotics applications following a service-oriented architecture approach. In particular, we distinguish two main categories: (\textit{i.}) virtualization of robotics systems and (\textit{ii.}) computation offloading from robots to cloud-based services. We discuss the main approaches proposed in the literature to design robotics systems through the Web and their integration to the cloud through a service-oriented computing framework.

## 개요
본 논문에서는 서비스 지향 아키텍처와 웹 서비스를 활용하여 인터넷 및 클라우드와 통합된 로봇 애플리케이션 및 소프트웨어를 개발하는 방법에 대한 개요를 제시합니다. 이는 2010년 이후 클라우드 로보틱스 개념에서 등장한 최근 트렌드로, 서비스 지향 아키텍처 접근 방식을 따라 로봇 애플리케이션에 클라우드 인프라를 활용하는 것입니다. 특히, 우리는 두 가지 주요 범주를 구분합니다: (\textit{i.}) 로봇 시스템의 가상화와 (\textit{ii.}) 로봇에서 클라우드 기반 서비스로의 연산 오프로딩입니다. 또한, 웹을 통해 로봇 시스템을 설계하고 서비스 지향 컴퓨팅 프레임워크를 통해 클라우드에 통합하기 위해 문헌에서 제안된 주요 접근 방식을 논의합니다.

## 핵심 내용
본 논문에서는 서비스 지향 아키텍처와 웹 서비스를 활용하여 인터넷 및 클라우드와 통합된 로봇 애플리케이션 및 소프트웨어를 개발하는 방법에 대한 개요를 제시합니다. 이는 2010년 이후 클라우드 로보틱스 개념에서 등장한 최근 트렌드로, 서비스 지향 아키텍처 접근 방식을 따라 로봇 애플리케이션에 클라우드 인프라를 활용하는 것입니다. 특히, 우리는 두 가지 주요 범주를 구분합니다: (\textit{i.}) 로봇 시스템의 가상화와 (\textit{ii.}) 로봇에서 클라우드 기반 서비스로의 연산 오프로딩입니다. 또한, 웹을 통해 로봇 시스템을 설계하고 서비스 지향 컴퓨팅 프레임워크를 통해 클라우드에 통합하기 위해 문헌에서 제안된 주요 접근 방식을 논의합니다.
