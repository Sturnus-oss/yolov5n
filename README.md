# yolov5n

## 在 Windows 上运行（数据集位于 `D:\dataset`）

下面以 Python 脚本 `train_yolov5.py` 为例说明。

### 1. 安装环境

```bash
# 建议 Python 3.8~3.11
python -m venv .venv
.venv\Scripts\activate

pip install --upgrade pip
pip install yolov5
```

> 如果你已经安装了 PyTorch/CUDA，可按你的显卡环境安装对应版本。

### 2. 准备数据集目录

确保你的目录结构类似：

```text
D:\dataset
├─ images
│  ├─ train
│  └─ val
└─ labels
   ├─ train
   └─ val
```

### 3. 配置 `dataset.yaml`

在项目根目录创建（或修改）`dataset.yaml`，推荐使用绝对路径：

```yaml
path: D:/dataset
train: images/train
val: images/val

# 按你的类别数修改
nc: 1
names: ["defect"]
```

> Windows 路径建议写成 `D:/dataset`（正斜杠）以减少转义问题。

### 4. 检查训练脚本

当前 `train_yolov5.py` 已设置：

- `weights="yolov5n.pt"`
- `data="dataset.yaml"`

如果你用 CPU，可把 `device=0` 改成 `device="cpu"`。

### 5. 启动训练

在项目目录执行：

```bash
python train_yolov5.py
```

训练输出默认在：

```text
runs/train/tire_yolov5n_baseline
```

---

## 常见问题

- **报错找不到图片/标签**：先确认 `dataset.yaml` 的 `path` 与 `train/val` 相对路径拼接后实际存在。
- **显存不足（CUDA out of memory）**：把 `batch=4` 调小到 `2` 或 `1`，或减小 `imgsz`。
- **只想快速验证流程**：先把 `epochs` 从 `200` 改成 `5~10` 做冒烟测试。
