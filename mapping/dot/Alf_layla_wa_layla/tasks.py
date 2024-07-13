#import functools
import glob
import os

from invoke import task
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
    
}

@task
def ver(c):
    print(f'''auto merge multi-dot files into one dot file
        version: {env['version']}
        by: {env['author']}
        ''')

@task
def exp(c):
    redot(c)
    _cmd =f"dot -Tjpeg {env['exp_dot']}.dot -o {env['exp_dot']}.jpg"
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

    