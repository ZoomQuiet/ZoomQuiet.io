# 1001夜

## 华彩

### 256

…当他进去时，一种不可名状的快乐的波涛，激烈地、温柔地荡漾着她，一种奇异的惊心动魄的感觉开始蔓延着，蔓延着，开展着，直到最后的，极度的、盲目的洪流奔泻，她完全被淹没在了快乐的波涛之中……

## 环境搭建与迁移到其它主机

`subdot/` 下各 `.dot` 只存图谱结构；夜号节点的 YouTube URL 由 `tasks.py`
的 `playlist` 任务从公开数据源回填，合并后的 `ns1001.dot` 与 HTML 产物由
`invoke` 重新生成。换一台机器只需装好下面三类依赖即可复现。

### 依赖

| 依赖 | 版本 | 说明 |
| ------ | ------ | ------ |
| uv | 最新 | Python 包/虚拟环境管理，本目录所有命令都经 `uv run` 执行 |
| Graphviz | >= 10.0.1 | `dot` 命令；本机实测 16.1.0，需支持 `-Tsvg_inline` |
| yt-dlp | 最新 | 抓取 YouTube 频道/播放列表元数据，系统级安装即可（无需 cookie） |

Python 侧依赖见 `pyproject.toml`（`invoke`、`jinja2`，`requires-python >= 3.11`），
由 `uv run` 自动装入本目录 `.venv/`，无需手动 `pip install`。

Graphviz 若用源码构建（发行包版本过低时），注意启用 Lua 插件支持并在安装后注册：

```sh
cmake -DENABLE_LTDL=ON -DCMAKE_INSTALL_LIBDIR=<prefix>/lib ..
make && make install
dot -c          # 注册插件，否则 -Tsvg_inline 等格式不可用
dot -V          # 校验版本
```

### 常用命令

```sh
uv run invoke ver                          # 校验环境与版本
uv run invoke exp                          # 合并 subdot/*.dot -> ns1001.dot 并导出 HTML
uv run invoke playlist                     # 全量抓取并回填缺失 URL，再重新生成
uv run invoke playlist --latest 10         # 只对比最新 10 条（增量校验用）
uv run invoke playlist --force             # 忽略缓存强制重抓
```

`playlist` 是幂等的：已有 `URL=` 的夜号节点一律跳过，只给缺 URL 的节点追加
`,URL="https://youtu.be/<id>"`；同一夜重复视频取首次出现。

### 数据源

* 频道（主数据源）：`https://www.youtube.com/@Chaos42DAMA/videos`
* 播放列表（第 1~99 夜补充）：`https://www.youtube.com/playlist?list=PLbUdpHqxsZwHXNADWIEMsUHM4QtPj0xh-`

标题夜号解析兼容三种写法：`第一夜/…`（中文数字，仅播放列表）、`第39夜:`（无空格）、
`《一千零一夜》第 742 夜:`（带空格，频道）。

### 缓存与产物位置

| 路径 | 是否入库 | 内容 |
| ------ | ---------- | ------ |
| `logs/channel.json` | 是 | 频道抓取缓存，含 `fetched_at` 时间戳 |
| `logs/playlist.json` | 是 | 播放列表抓取缓存，含 `fetched_at` 时间戳 |
| `ns1001.dot` | 是 | 合并后的完整图谱（`redot` 生成） |
| `_jpg/` | 否（见 `.gitignore`） | `index.svg.html` 等导出产物 |
| `.venv/` | 否 | 本地虚拟环境，由 `uv run` 自动创建 |
| `uv.lock` | 是 | 依赖锁，保证换主机后 `uv run` 装到同一套版本 |

缓存存在且未指定 `--latest` 时直接复用；`--force` 或 `--latest N` 会重新抓取并与旧缓存
合并（旧条目优先，仅补充未见过的视频 ID），因此增量抓取不会丢掉历史夜号映射。
