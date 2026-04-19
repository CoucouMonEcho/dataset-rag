from modelscope.hub.snapshot_download import snapshot_download

# 下载模型到当前目录下的 models/bge-m3 文件夹
# uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
model_dir = snapshot_download('BAAI/bge-m3', cache_dir='D:\Workspace/models')
print(f"模型已下载到: {model_dir}")