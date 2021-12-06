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
$googleimagesdownload --keywords "Polar bears" --limit 200 -cd /Users/tianran/Downloads/chromedriver
```

- \[TO DO\] 用这种方法姑且准备爬 李卡、婷姐、彭小苒、陈星旭的1000张图。

## 换脸步骤

### 代码安装 

### 人脸模型训练

#### 图像预处理（角度、亮度等多样性手动挑选）




