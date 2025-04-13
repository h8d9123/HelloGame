import os
import subprocess

def build_resources():
    # 获取当前目录
    resources_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 构建资源文件
    qrc_file = os.path.join(resources_dir, "res.qrc")
    output_file = os.path.join(resources_dir, "res_qrc.py")
    
    subprocess.run(["pyside6-rcc", qrc_file, "-o", output_file])

if __name__ == "__main__":
    build_resources()