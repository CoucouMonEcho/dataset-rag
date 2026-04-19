from modelscope.hub.snapshot_download import snapshot_download

local_dir = r"D:\Workspace\models\rerank"
# uv pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
snapshot_download(
    model_id="BAAI/bge-reranker-large",
    cache_dir=local_dir,
)

print("下载完成，模型目录：", local_dir)