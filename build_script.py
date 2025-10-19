import os
import subprocess
import sys
import shutil

def build_app():
    print("🚀 开始构建AI应用...")
    
    # 确保模板目录存在
    os.makedirs('templates', exist_ok=True)
    
    # 检查必要文件
    required_files = ['main.py', 'requirements.txt', 'config.json', 'templates/index.html']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ 缺少必要文件: {file}")
            return False
    
    # 安装PyInstaller（如果尚未安装）
    try:
        import PyInstaller
    except ImportError:
        print("📦 安装PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # 构建命令 - Mac版本
    build_cmd = [
        'pyinstaller',
        '--name=AI智能助手',
        '--onefile',
        '--windowed',
        '--add-data=templates:templates',
        '--add-data=config.json:.',
        'main.py'
    ]
    
    print("🔨 开始打包...")
    result = subprocess.run(build_cmd)
    
    if result.returncode == 0:
        print("✅ 打包成功！")
        print("📁 可执行文件位置: dist/AI智能助手")
        return True
    else:
        print("❌ 打包失败")
        return False

if __name__ == "__main__":
    build_app()
