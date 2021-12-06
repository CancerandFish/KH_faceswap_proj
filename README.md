# KH_faceswap_proj


## 数据集收集阶段

原始数据要求：
- When extracting faces for training, you are looking to gather around **500 to 5000** faces for each subject you wish to train. These should be of a **high quality** and contain **a wide variety of angles, expressions and lighting conditions**.

- **Do not** extract every single frame from a video for training as from frame to frame the faces will be very similar.

### 人工收集
- 卡黄电视剧cut素材（现代剧《逆袭》），视频形式，其余人脸干扰有，需要手动清除。
- 卡黄unit、solo等演唱会focus，已完成，质量好，但光照衣着角度均单一。其余人脸干扰有，需要手动清除。
- 卡黄采访视频。光照衣着角度均单一。其余人脸干扰无。
- 个站微博爬取。形式多样，但精修后过于失真。

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
已完成。

代码来源：https://github.com/deepfakes/faceswap/blob/master/USAGE.md#Gathering-raw-data

版权信息以及约束条件：
- FaceSwap is not for creating inappropriate content.
- FaceSwap is not **for changing faces without consent or with the intent of hiding its use**.
- FaceSwap is not for any illicit, unethical, or questionable purposes.
- FaceSwap exists to experiment and discover AI techniques, for social or political commentary, for movies, and for any number of ethical and reasonable uses.

加粗为争议信息。

### 人脸模型训练
代码环境调试完成，等待数据

#### 源图像预处理（角度、亮度等多样性手动挑选）
To do

### 目标视频素材准备 
备选素材：
- 东宫（陈星旭，彭小苒），选段未定。
- 太阳的后裔（宋慧乔，宋仲基），选段未定。
- 台剧 第一次..花香，新人演员，数据少，难度较大。暂缓进行。

### 视频换脸
To do

### 结果调整
To do




