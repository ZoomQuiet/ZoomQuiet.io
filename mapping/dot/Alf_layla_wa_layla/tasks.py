#import functools
import glob
import json
import os
import re
from datetime import datetime, timezone

from invoke.tasks import task
from jinja2 import Environment, FileSystemLoader

# from fabric.api import env, lcd, local, task

# Local path configuration (can be absolute or relative to fabfile)
env = {
    "version": "v14.7.13",
    "author": "Chaos4DAMA",
    "email": "zquiet+1001@gmail.com",

    "path4sub": "subdot",
    "tpl_dot": "main_j2tpl.dot",
    #"j2spot": "chapters",
    "exp_dot": "ns1001",
    "exp_jpg": "_jpg",
    
}

@task
def ver(c):
    print(f'''auto merge multi-dot files into one dot file
        version: {env['version']}
        by: {env['author']}
        ''')

@task
def exp(c, jpg="ns1001"):
    print(f"export {jpg} from .dot")
    #return None
    redot(c)
    #_cmd =f"fdp -Tjpeg {env['exp_dot']}.dot -o {env['exp_jpg']}/{jpg}.jpg"
    #_cmd =f"dot -Tjpeg {env['exp_dot']}.dot -o {env['exp_jpg']}/{jpg}.jpg"
    #_cmd =f"dot {env['exp_dot']}.dot -Tgif -o {env['exp_jpg']}/{jpg}.gif -Tcmapx -o {env['exp_jpg']}/{jpg}.gif.map"
    #_cmd =f"dot {env['exp_dot']}.dot -Tsvg_inline -o {env['exp_jpg']}/{jpg}.svg.html"
    _cmd =f"dot {env['exp_dot']}.dot -Tsvg_inline -o {env['exp_jpg']}/index.svg.html"

    os.makedirs(env['exp_jpg'], exist_ok=True)
    print(f"run: {_cmd}") 
    c.run(_cmd)


#@task
def redot(c):
    _subdots = mdots(c)
    environment = Environment(loader=FileSystemLoader("./"))
    template = environment.get_template(env['tpl_dot'])

    content = template.render(
        chapters="\n".join(_subdots),
    )
    _expas = f"{env['exp_dot']}.dot"
    with open(_expas, mode="w", encoding="utf-8") as dotfile:
        dotfile.write(content)
        print(f"... wrote {_expas}")

#@task
def mdots(c):
    dot_files = glob.glob(f"{env['path4sub']}/*.dot")

    sorted_dot_files = sorted(dot_files)
    #print(sorted_dot_files)
    _subdots = []
    # 逐一读取每个文件的内容
    for file_path in sorted_dot_files:
        # 打开文件并读取内容
        print(f"... load {file_path}")
        with open(file_path, 'r') as file:
            _subdots.append(file.read())
            #content = file.read()
            #print(f"Contents of {file_path}:")
            #print(content)
            #print("-" * 40)  # 打印分隔线，以便区分不同文件的内容
    return _subdots

    

##############################################################################
#   夜号 -> YouTube URL 回填
##############################################################################

CHANNEL_URL = "https://www.youtube.com/@Chaos42DAMA/videos"
PLAYLIST_URL = "https://www.youtube.com/playlist?list=PLbUdpHqxsZwHXNADWIEMsUHM4QtPj0xh-"
YT_SHORT = "https://youtu.be/"

_CN_DIGIT = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5,
             "六": 6, "七": 7, "八": 8, "九": 9}
_NIGHT_ARABIC = re.compile(r"第\s*(\d+)\s*夜")
_NIGHT_CN = re.compile(r"第([一二三四五六七八九十]{1,3})夜")
# 夜号节点定义: ch0201 [label="第201夜",...];  (URL= 可选)
_NIGHT_NODE = re.compile(
    r'(\b[A-Za-z_]\w*\s*\[\s*label="第\s*(\d+)\s*夜")(.*?)(\s*\];)', re.S)


def _cn2int(cn):
    """中文数字 1~99 -> int; 无法解析返回 None"""
    if cn == "十":
        return 10
    if "十" in cn:
        head, _, tail = cn.partition("十")
        tens = _CN_DIGIT.get(head, 1) * 10
        ones = _CN_DIGIT.get(tail, 0) if tail else 0
        return tens + ones
    return _CN_DIGIT.get(cn)


def _night_of(title):
    """标题 -> 夜号; 三种格式: 第一夜/第39夜/第 742 夜"""
    m = _NIGHT_ARABIC.search(title)
    if m:
        return int(m.group(1))
    m = _NIGHT_CN.search(title)
    return _cn2int(m.group(1)) if m else None


def _fetch(c, url, latest):
    """yt-dlp 扁平抓取, 返回 [{id,title,night}]"""
    _cmd = ["yt-dlp", "--flat-playlist", "--no-warnings",
            '--print', '"%(id)s|%(title)s"']
    if latest and latest > 0:
        _cmd += ["-I", f"1:{latest}"]
    _cmd.append(url)
    print(f"... fetch {url}" + (f" (latest {latest})" if latest else " (all)"))
    _res = c.run(" ".join(_cmd), hide=True, warn=True)
    if not _res.ok:
        raise RuntimeError(f"yt-dlp failed: {url}")
    _videos = []
    for _line in _res.stdout.splitlines():
        _line = _line.strip()
        if not _line or "|" not in _line:
            continue
        _vid, _, _title = _line.partition("|")
        _videos.append({"id": _vid, "title": _title,
                        "night": _night_of(_title)})
    return _videos


def _load_cache(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as _f:
            return json.load(_f).get("videos", [])
    return []


def _save_cache(path, url, videos):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, mode="w", encoding="utf-8") as _f:
        json.dump({"source": url,
                   "fetched_at": datetime.now(timezone.utc).isoformat(
                       timespec="seconds"),
                   "count": len(videos),
                   "videos": videos},
                  _f, ensure_ascii=False, indent=1)


def _merge(old, new):
    """旧缓存优先(保持首次出现语义), 新抓取只补充未见过的 id"""
    _seen = {_v["id"] for _v in old}
    _out = list(old)
    for _v in new:
        if _v["id"] not in _seen:
            _seen.add(_v["id"])
            _out.append(_v)
    return _out


def _night_map(videos):
    """night -> video_id, 同夜重复取首次出现"""
    _map = {}
    for _v in videos:
        _n = _v.get("night")
        if _n and _n not in _map:
            _map[_n] = _v["id"]
    return _map


def _backfill(c, night_map):
    """只给缺 URL 的夜号节点追加 URL"""
    _filled = _skipped = _missed = 0
    for _path in sorted(glob.glob(f"{env['path4sub']}/*.dot")):
        with open(_path, encoding="utf-8") as _f:
            _src = _f.read()
        if not _NIGHT_NODE.search(_src):
            continue

        def _sub(m, _path=_path):
            nonlocal _filled, _skipped, _missed
            head, night, attrs = m.group(1), int(m.group(2)), m.group(3)
            if "URL=" in attrs:
                _skipped += 1
                return m.group(0)
            _vid = night_map.get(night)
            if not _vid:
                _missed += 1
                print(f"!! no url for night {night} in {_path}")
                return m.group(0)
            _filled += 1
            return f'{head}{attrs.rstrip()}\n        ,URL="{YT_SHORT}{_vid}"\n        ];'

        _dst = _NIGHT_NODE.sub(_sub, _src)
        if _dst != _src:
            with open(_path, mode="w", encoding="utf-8") as _f:
                _f.write(_dst)
            print(f"... backfill {_path}")
    print(f"... backfill done: filled={_filled} "
          f"skipped(has URL)={_skipped} missed={_missed}")
    return _missed


@task
def playlist(c, latest=0, force=False):
    """抓取频道/播放列表, 回填夜号节点 URL, 再重新生成图谱"""
    _channel = os.path.join("logs", "channel.json")
    _playlist = os.path.join("logs", "playlist.json")

    _old_ch = _load_cache(_channel)
    _old_pl = _load_cache(_playlist)
    # 已存在且未指定 --latest 时复用缓存; --force 或 --latest 时重抓(合并旧缓存)
    _need = force or latest > 0 or not _old_ch or not _old_pl

    if _need:
        _new_ch = _fetch(c, CHANNEL_URL, latest)
        _new_pl = _fetch(c, PLAYLIST_URL, latest)
    else:
        print("... reuse cached logs/*.json (use --force to re-fetch)")
        _new_ch, _new_pl = [], []

    _ch_videos = _merge(_old_ch, _new_ch)
    _pl_videos = _merge(_old_pl, _new_pl)
    _save_cache(_channel, CHANNEL_URL, _ch_videos)
    _save_cache(_playlist, PLAYLIST_URL, _pl_videos)

    # 主数据源 = 频道; 播放列表仅补充第 1~99 夜
    _nights = _night_map(_pl_videos)
    _nights.update(_night_map(_ch_videos))
    print(f"... night map: {len(_nights)} nights "
          f"(channel={len(_ch_videos)} playlist={len(_pl_videos)})")

    _missed = _backfill(c, _nights)
    if _missed:
        raise RuntimeError(f"{_missed} night node(s) still without URL")

    exp(c)
    print("... playlist DONE")
