# KH_faceswap_proj


## 数据集收集

### 爬取谷歌图片

- 代码包：https://github.com/hardikvasa/google-images-download

不过这个版本有bug。

- 已经解决issue的正确版本：https://github.com/Joeclinton1/google-images-download
- 安装方法
```
$ git clone https://github.com/Joeclinton1/google-images-download.git
$ cd google-images-download
$ sudo python setup.py install
```
- 安装chromedriver, https://sites.google.com/chromium.org/driver/downloads?authuser=0

- 命令行执行： 
```
$ googleimagesdownload --keywords "Polar bears" --limit 200 -cd /Users/tianran/Downloads/chromedriver
```

- \[Under Going] 用这种方法姑且准备爬 李卡、婷姐、彭小苒、陈星旭的1000张图。

## 换脸步骤

### 代码安装
已完成

### 人脸模型训练
代码环境调试完成，等待数据

#### 源图像预处理（角度、亮度等多样性手动挑选）
To do

### 目标视频素材准备 
备选素材：
- 东宫（陈星旭，彭小苒），选段未定。
- 太阳的后裔（宋慧乔，宋仲基），选段未定。

### 视频换脸
To do

### 结果调整
To do




