# Wiki / KG 实体图片补全 TODO

## 背景

2026-07-01 在准备推送 Wiki 更新时，发现 `wiki/docs/appendices/appendix-d/` 和 `wiki/docs/kg/entities/` 中有大量 `placehold.co` / `via.placeholder.com` 占位图片以及“图片来源：待补充”等占位说明。

为避免页面上出现无效占位图，本次提交已将这些占位图统一替换为指向官方资料的文字引用，格式如下：

```markdown
> Tesla Optimus Gen 2：请访问 [官方资料](https://www.tesla.com) 查看。
```

## 待完成事项

后续需要人工为每个产品/公司/零部件补充**稳定、可公开访问**的真实图片 URL，并替换上述文字引用。

### 涉及范围

- `wiki/docs/appendices/appendix-d/`：约 642 处占位图
- `wiki/docs/kg/entities/`：约 674 处占位图
- 合计：约 1316 处

### 如何替换

在对应 Markdown 文件中搜索：

```text
请访问 [官方资料]
```

将类似：

```markdown
> Tesla Optimus Gen 2：请访问 [官方资料](https://www.tesla.com) 查看。
```

替换为：

```markdown
![Tesla Optimus Gen 2](https://example.com/real-image-url.jpg)

> 图片来源：[Tesla 官方资料](https://www.tesla.com)。
```

建议优先使用：

1. 企业官网或官方新闻稿中的公开图片 URL
2. 产品手册 / 媒体资料包中的图片
3. Wikimedia Commons 等可公开引用的图库

避免使用容易失效或禁止热链的 CDN 图片。

## 完成标准

- `wiki/docs/` 中不再存在 `> ...：请访问 [官方资料] ... 查看。` 形式的引用
- 所有页面均有真实、可正常加载的图片
- 本文件随最后一批图片替换一起删除

## 检索命令

```bash
rg '请访问 \[官方资料\]' wiki/docs/
```
