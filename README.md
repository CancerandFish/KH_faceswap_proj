# KH_faceswap_proj

📢中英文夹杂注意

👏🏻Welcome to the project page!

<img src="https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/poster_lyt_htt.png" width="100" alt="poster"/><br/>


<!-- ![poster](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/poster_lyt_htt.png) -->

This project is only a simple turtorial that introduces my small try on faceswap. Big thanks for 阿羊🐑，板蓝根👧🏻，林老师🐺，柏诺👧🏻 and all the people that encourage me and take part in the project.

Your suggestions are alwayas welcome. You can contact me any time by leave your issues here.


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
  - 卡黄电视剧cut素材（现代剧《逆袭》），mp4 format，其余人脸干扰有，manually cleaned
  - htt单人电视剧cut素材，古装剧《素手遮天》, manually cleaned
  
- Images：
  - google crawling
  - 卡黄各类扫图合集。lack in side faces
  - 卡黄unit、solo等演唱会focus，good quality，但光照衣着角度均单一。其余人脸干扰有，manually cleaned


#### CXX and PXR

- Images：
  - 本人微博、本人个站
  - google crawling
  
- Videos：
  - 东宫前16集cut, manually cleaned

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


### Google images crawling

- codes available：https://github.com/hardikvasa/google-images-download

But this version has a bug (at least for me Linux 20.04

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

### Video extracting suggestions
I use built-in functions in faceswap to extract faces inside the video. I list some tricks here:

-  use single person cut instead of the whole video, especially when your target is not the main actor/actoress
-  use 1080p video sources
-  set extract frame interval to be ~40 to meet the **diversity** requirements
-  set `min_size = 256`, to extract only clear and large faces
-  use sort, a built-in functions in faceswap, before you manually remove the other faces you do not want to remain in your training set


## Let's begin swapping

### Codes and environment intalling
My environment:
- Server：Linux Ubuntu 20.04 + 4 * V100
- Desktop：Linux 20.04 + 1 * 1080 Ti

Codes from：https://github.com/deepfakes/faceswap/blob/master/USAGE.md#Gathering-raw-data

Some patent and ethitical requirements：
- FaceSwap is not for creating inappropriate content.
- FaceSwap is not **for changing faces without consent or with the intent of hiding its use**.
- FaceSwap is not for any illicit, unethical, or questionable purposes.
- FaceSwap exists to experiment and discover AI techniques, for social or political commentary, for movies, and for any number of ethical and reasonable uses.


### Training

I first try the original model, some problems I encountered: 
- the results tend to be a little blurring, even when I turn the sharp config to max...
- 彭小苒的额饰经常会被模糊掉
- 边缘不够清楚

解决办法：
- Then I try the DFL model, which takes a 128x128 px image as the input and outputs 256x256 px image. 
- 针对额饰，我使用了legacy而非face进行界限划定，对于lyt-pxr这个pair，减少脸部识别区域的范围。结果提升巨大，额饰大多时候能够被精准分类。
- 在convert时，我使用了vgg-obstruction进行遮挡物识别，进一步分开了额饰和人脸。
- 针对边缘不够清楚的问题，分析原因在于侧脸samples过少，但受限于时间，无法进行修正。因此在convert阶段，我对于个别侧脸部分进行erosion设置，使这里的边缘使用pxr本人的轮廓，替代生成的轮廓，以此产生清晰的边缘。

![poster](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/comparison.png)

### 视频换脸

Original模型使用1080Ti主机即可运行，训练约耗时1天左右。其输出为64x64 px.

而DFL模型输出较Original大16倍，考虑到网络深度和宽度的不同，其训练时间比较长，一张1080ti的内存也很难达标。因此，我将DFL放于Server运算，以4张32G V100进行训练，约耗时4天左右。

### Some results

After 450k iters, Lyt-pxr's results:

![lyt-pxr](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/lyt_result.jpg)

After 300k iters, Htt-cxx's results:

![lyt-pxr](https://github.com/CancerandFish/KH_faceswap_proj/blob/main/results/htt_result.jpg)


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











