# How to Add a CAPTCHA Solver MCP Tool to Langroid

[English](../../README.md) · [中文](README.md)

## Introduction

[CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=langroid-captcha-solver-mcp-tool&utm_content=repository-readme) integration example. 本项目展示如何为 Langroid 添加受控的验证码处理工具。仅用于获准的 QA、RPA 和自有网页流程。

## 安全边界 / Safety boundary

- 明确授权后才运行；
- 最多一次尝试并设置超时；
- 结果无效或不确定时转人工；
- 测试只使用本地 fixture，不调用真实 API。

完整安装、代码和 Responsible Use 说明请参阅 [English README](../../README.md)。

## Conclusion

该示例保留授权、尝试预算、结果验证和人工停止边界。生产接入请遵循官方 [CapSolver](https://www.capsolver.com/?utm_source=github&utm_medium=referral&utm_campaign=langroid-captcha-solver-mcp-tool&utm_content=repository-readme) 文档。

## Disclosure

Developer sharing CapSolver integration examples.

## License

MIT；完整许可证见英文仓库根目录。
