# [YOLOv11 Optimization for Efficient Resource Utilization (paper)](https://arxiv.org/abs/2412.14790)
Hi, this is the repository related to the modified YOLOv11 version. Below is a summary of the paper's objective, the model's weights, and other explanations.

# 1- Models weights
- [YOLOv11-small-weed-crops](https://github.com/AREEG94FAHAD/yolov11/blob/main/model%20weights)
- [YOLOv11-medium-BCCD](https://github.com/AREEG94FAHAD/yolov11/blob/main/model%20weights)
- [YOLOv11-large-Underwater pipe](https://github.com/AREEG94FAHAD/yolov11/tree/main/model%20weights)
- [YOLOv11-sm-Aerial](https://github.com/AREEG94FAHAD/yolov11/blob/main/model%20weights)
- [YOLOv11-ml-Brain](https://github.com/AREEG94FAHAD/yolov11/blob/main/model%20weights)
- [YOLOv11-sl-Face](https://github.com/AREEG94FAHAD/yolov11/blob/main/model%20weights)

# 2- Required packages
- ultralytics version 8.3.29 For YOLOv11
- ultralytics version 8.2.29 for YOLOv8
- wandb version 0.19.1

# 3- Object size classifier
This simple program allows you to load label file and type, image size, for example 640x640. Then, by clicking 'Run,' the program will process all object labels, compute their sizes, and classify them according to their size see paper Table 1. [The code](https://github.com/AREEG94FAHAD/yolov11/tree/main/object%20size%20classifier)
![image](https://github.com/user-attachments/assets/cd451a5b-e8d1-4b73-af26-c9eb618d5cf4)


## Citation

If you find this work useful for your research, please consider citing the paper:

```bibtex
@article{rasheed2024yolov11,
  title={YOLOv11 Optimization for Efficient Resource Utilization},
  author={Areeg Fahad Rasheed and M. Zarkoosh},
  journal={arXiv preprint arXiv:2412.14790},
  year={2024}
  dio={https://doi.org/10.48550/arXiv.2412.14790}
}
```

and 

```bibtex
@article{rasheed2025optimized,
  title={Optimized YOLOv8 for multi-scale object detection},
  author={Rasheed, Areeg Fahad and Zarkoosh, M},
  journal={Journal of Real-Time Image Processing},
  volume={22},
  number={1},
  pages={6},
  year={2025},
  publisher={Springer}
}
```



