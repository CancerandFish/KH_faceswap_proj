# KH_faceswap_proj

Chinese version follows English version.

Welcome to the project page!

![poster](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/poster_lyt_htt.png)

This project is only a simple turtorial that introduces my small try on faceswap.

Your suggestions are alwayas welcome. 


本项目仅以教育、学习为目的进行. 欢迎任何建议.

我觉得这个项目应该奖励我两斤决明子泡茶喝（






<!-- ## 需要人工的地方

婷姐八图
- 微博八图
- 生写照片八图
- 洗图

cxx数据集处理
- 下载一些陈星旭cut资源 我来处理人脸
- 筛陈星旭训练集（删除其他人物、不合格人脸等

花香
- 视频资源下载（mp4格式 质量尽量好 譬如无标等）
- 两位女主微博、facebook等八图

## 进度



### 总进度 -->

<!-- 12.9

在450k iter时停止了original model的训练，并进行测试（感谢0老师提供视频源文件

第一测结果不好，主要问题总结：

1. 面部不够清晰。
2. 背景边缘也跟着人脸被模糊。
3. 额饰

针对以上问题提出的解决方法：

1. 换模型，original model 的input和output均为64x。现在改用Dlight (128px input, 128-384px output), Dlight is a higher resolution model based on the dfaker variant, focusing on upscaling the faces, with custom upscalers. This is the newest model and is very easily configurable. 最新而且easy.
2. 加了vgg-clear mask后，面部轮廓和background轮廓可以清楚分开。这个算是已经确认解决。
3. 额饰这里……姑且调了legacy比例，试试看吧。

12.8

- 收集帝后资源：生写扫图、夜蝶mv等 （感谢阿羊 柏诺！

- 清洗帝后图包。
  - 李卡饭拍扫图共提取+1357张

- 收集陈星旭彭小苒资源：微博个站等 （感谢阿羊！
  - 彭小苒图包

- 提取夜蝶mv帝后图片，混在一起还需要人工分，不好。
  - 尝试加mask进行分类提取 - 变慢了。
  - 帧间差距太小 - 代码自动skip，5帧留1.
  - 清洗后约收集帝后各+200张


12.7

- 摸了

12.6 

- 爬取‘李艺彤’图片，命令1000，成功702；清洗后：490~

- 爬取‘snh48 黄婷婷’图片，命令3000，成功755；清洗后：402 （清洗感谢林老师

- 爬取‘黄婷婷’图片。on going。

- 爬取‘陈星旭’图片。草，他这么糊吗不至于啊，只爬出了470+图片，目测四分之一还带着张婧仪。

- 爬取‘彭小苒’图片。462张。行吧，你俩也挺配。

<!-- - 爬取‘Song Hye-gyo’图片， -->

<!-- - 爬取‘林辰唏’。。

- 爬取‘程予希’。。 -->



<!-- 






### 李卡-pxr 训练进度
![1209调试图](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/12091321-Training%20-%20'S':%20Save%20Now.%20'R':%20Refresh%20Preview.%20'M':%20Toggle%20Mask.%20'ENTER':%20Save%20and%20Quit_screenshot_09.12.2021.png)

12.9. 

14:02 停了一下训练，试图验证一下结果。

Iterations: 473579, loss A: 0.03037; loss B: 0.03123

\[Saved models\] Average loss since last save: face_a: 0.02618, face_b: 0.02572 --> -->


## Training samples collection

Some tips for face data:

As required/suggested by faceswap official guidelines, we are asked to gather 

- around **500 to 5000** faces for each subject
- should be of a **high quality** and contain **a wide variety of angles, expressions and lighting conditions**.
- **do not** extract every single frame from a video for training as from frame to frame the faces will be very similar.

So in this section, we first start to introduce our face sources, each of which is followed by the invloved collecting methods in detail. 

As lyt and htt is so bonded together ❤️, their parts will be merged. 

### Source collection

#### Lyt and Htt

- Video:
  - 卡黄电视剧cut素材（现代剧《逆袭》），视频形式，其余人脸干扰有，需要手动清除。
  - htt单人电视剧cut素材，古装剧《素手遮天》
  - 卡黄unit、solo等演唱会focus，质量好，但光照衣着角度均单一。其余人脸干扰有，需要手动清除。

- Images：
  - google爬取
  - 卡黄各类扫图合集。侧脸太少。

#### CXX and PXR

- Images：
  - 本人微博、本人个站
  - google爬取
  
- Videos：
  - 东宫前16集cut

#### Summary

|Name|Number of Valid Training Samples|Source|
|--|--|--|
|lyt|2055-3200|谷歌、图包、夜蝶mv、逆袭|
|htt|707|谷歌、夜蝶mv|
||2074|sushou|
||809|nixi_02_34|
||404|nixi_35_over|
||305|scanned pictures|
|pxr|2315|谷歌、weibo|
|cxx|1212|donggong|
||1762|weibo, google|


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

### 代码安装与环境配置
环境配置：

- Server：Linux Ubuntu 20.04 + 4 * V100
- Desktop：Linux 20.04 + 1 * 1080 Ti

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

- \[*\]角度多样性手动筛选

### 目标视频素材准备 
备选素材：
- 东宫（陈星旭，彭小苒），\[*\]选段未定。
- 太阳的后裔（宋慧乔，宋仲基），\[*\]选段未定。
- 台剧 第一次..花香，新人演员，数据少，难度较大。暂缓进行。

### 视频换脸
训练约耗时数天。

To do

### 结果调整
To do




## 附录
### 人工清洗手册（ver0 初步）

所有图片命名规则：数字序号+图片名+扩展名。以数字序号进行组内统一识别，切勿更改。后缀名多样，不影响处理结果。

根据百度网盘链接下载图包，处理给定序号图片。

具体地，请：
- 删除**不合格**图片（解释附后）
- 重新上传百度网盘（需压缩）。

不合格图片定义（以李卡文件夹下图片为例）：

- 图片不含文件夹命名之人物（如：李卡图包中某图无李卡）
- 图片中含有除李卡外的其他人的正、侧脸
- 视觉上过于糊，无法辨认出是否是李卡本人
- 图片中的李卡带着面具、口罩；面部识别区无法辨认
- 图片中有且只有李卡，但此李卡来自于手游卡面
- 图片有且只有李卡，但此李卡是个照片、生写转拍

⚠️警告：小心鞠婧祎、赵粤、lyt、曾艳芬、纸片人、帝后合照……

### 人工清洗手册（ver1 进阶）

具体地，请：
- **处理** 而非 直接**删除不合格**图片
  - 图片不含文件夹命名之人物（如：李卡图包中某图无李卡），直接**删掉**。
  - 图片中含有李卡、以及除李卡外的其他人，请适当裁剪至只剩李卡脸一人。
- 标注侧脸图片
  - 若本图片的角度**非绝对正脸**，即，左或右偏转约45度，请复制它，至单独文件夹，以‘xx’文件夹为例，请命名为‘xx-侧脸’。
- 重新上传百度网盘（无需压缩）。






链接：https://pan.baidu.com/s/1xQQ_Gnpq2pxT9naFK3GLzA 
提取码：kh48 
陈星旭的也好了



