# PCAP流量回放平台功能概览

## 项目概述

PCAP Replay 是一个 Spring Boot 应用，读取 PCAP 网络抓包文件，解析数据包并回放到 RabbitMQ 消息队列。提供 Web UI 进行环境和流量管理。

## 技术架构

```
Pcap4jProcessor → UnpackStrategyFactory → UnpackStrategy (Ethernet/IPv4/TCP/UDP)
                                    ↓
                             PackageEvent model
                                    ↓
                            RabbitMQService → RabbitMQ sinks
```

- **前端**: Thymeleaf 模板 + 静态 HTML/CSS/JS
- **后端**: Spring Boot + Spring Data JPA + MySQL
- **消息队列**: RabbitMQ

---

## 功能模块

| 功能 | 入口URL | 说明 |
|------|---------|------|
| [[测试环境入口]] |  | 测试环境管理与配置 |
| [[场站运维监控]] |  | 山西场站地图可视化与运维 |
| [[流量分发控制]] |  | PCAP流量源与测试环境分发 |