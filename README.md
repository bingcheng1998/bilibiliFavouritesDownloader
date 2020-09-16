# Bilibili 收藏夹下载器

基于 you-get 实现一键下载Bilibili指定收藏夹下的视频。

## 环境要求

- `Python3` 与 `urllib` 库
- 基于 python 开发的视频下载器 `you-get` （ https://github.com/soimort/you-get ）

如果已经安装有 `python 3`，可直接通过命令行安装 `you-get`。

```
pip3 install you-get
```

## 使用方法

打开 `user_info.py` ，编辑

- 用户id，
- 收藏夹id
- 下载目录
- coockie，

之后直接运行`run.py`即可。

### 如何查看用户id与收藏夹id

形如`https://space.bilibili.com/57626460/favlist?fid=1030308760&ftype=create`, 

- 57626460为用户id
- 1030308760为收藏夹id

## 下载逻辑

1. 在主目录下生成以收藏夹名称命名的目录；
2. 对于收藏夹中的视频，首先爬取所有page的所有视频的list；
3. 然后与sqlite中的文件对照，看是否有重复；
4. 将没有重复的视频连接分别进去，核查是否是分p视频；
5. 对于非分p视频，直接下载；
6. 对于分p视频，新建目录后下载；
7. 对于失效视频，跳过；