# ForeverRise 官网

这是 ForeverRise 项目的官方网站，基于 HTML/CSS/JavaScript 构建。

## 项目介绍

ForeverRise 是专为 CS2（Counter-Strike 2）玩家打造的全方位辅助工具集，包含三大核心模块：

### 核心模块

#### 1. ForeverRise CFG
游戏内配置文件，通过控制台 exec 加载使用。
- **自动投掷物（AutoLunpan）** - 支持 Mirage, Dust2, Inferno, Ancient, Vertigo, Nuke 等全部主流地图
- **智能急停（Jiting）** - 6档幅度可调，松手即停
- **自动压枪（NoRecoil）** - AK47 等武器自动压枪
- **跳投/前跳投** - 一键跳投功能
- **手枪速射** - 快速点击高速射击
- **连跳/大跳** - 自动连跳和 JumpBug

#### 2. CS2 Tracer
完整的投掷物训练工具，包含桌面客户端和 DLL 钩子模块。
- 三连抛捕获定位
- 暴力破解落点计算
- 悬浮捕获模式
- 箱体可视化绘制
- CSV 数据导入/导出
- 中英文双语界面

## 技术栈

- 纯 HTML5 + CSS3 + JavaScript
- Google Fonts (Orbitron, Rajdhani, Noto Sans SC)
- CSS 动画和过渡效果
- 响应式设计

## 运行方式

直接在浏览器中打开 `index.html` 文件即可预览。

如需部署，可以使用任何静态网站托管服务：
- GitHub Pages
- Vercel
- Netlify

## 项目结构

```
ForeverRise/
├── website/
│   └── index.html         # 官网首页
├── ForeverRise/
│   ├── CFG 配置文件       # 游戏内自动操作脚本
│   │   ├── AutoLunpan/   # 自动投掷物
│   │   ├── jiting/       # 智能急停
│   │   ├── NoRecoil/     # 自动压枪
│   │   └── ...
│   ├── Function_Preference.cfg  # 功能设置
│   ├── Key_Preference.cfg       # 键位设置
│   └── setup.cfg         # 启动配置
└── cs2_tracer/           # 投掷物逆推工具 (GUI + DLL)
```

## 安装步骤

1. **解压文件** - 将 ForeverRise.zip 压缩包解压到 CS2 配置文件夹 `Counter-Strike Global Offensive\game\csgo\cfg\ForeverRise\`

2. **运行启动器** - 运行目录下的 `完美点我.exe`（有完美平台一定要开着完美平台运行）

3. **修改键位（可选）** - 编辑 `Key_Preference.cfg` 文件修改键位设置

4. **修改功能（可选）** - 编辑 `Function_Preference.cfg` 文件开启/关闭所需功能

5. **添加启动项** - 在游戏启动项中添加：
   ```
   +exec ForeverRise/setup -testscript "../../csgo/cfg/ForeverRise/Ticker/.vtest"
   ```

## 常用键位

| 功能 | 键位 |
|------|------|
| 投掷物 | T |
| 自动压枪 | J |
| 跳投 | L |
| 前跳投 | P |
| 手枪速射 | O |
| 180° 背闪 | K |
| 急停开关 | V |
| 大跳 | K |

## 许可证

本项目仅供学习交流使用，请勿用于任何违规行为。
