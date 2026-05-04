"""
YOLOv5n 轮胎缺陷检测 对比实验训练脚本
"""
from yolov5 import train

train.run(
    weights   = "yolov5n.pt",
    data      = "dataset.yaml",
    epochs    = 200,
    imgsz     = 640,
    batch     = 4,
    optimizer = "AdamW",
    patience  = 30,
    project   = "runs/train",
    name      = "tire_yolov5n_baseline",
    exist_ok  = True,
    device    = 0,
)