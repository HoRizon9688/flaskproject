# -*- coding: utf-8 -*-
# @Project: flaskProject
# @Author: HoRizon
# @Time: 2021/5/31 18:46

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image
import numpy as np
import sqlite3


database = sqlite3.connect('movie250.db')
cursor = database.cursor()
sql = '''select brief from movie250'''
data = cursor.execute(sql)
text = ''
for i in data:
    text = text + i[0]
cursor.close()
database.close()
# 分词
cut = jieba.cut(text)
string = ' '.join(cut)

# print(string)

img = Image.open(r'.\static\assets\img\acg.jpg')  # 打开遮罩图片
img_array = np.array(img)  # 将图片上转换为数组
stopwords = set(STOPWORDS)
stopwords.add('的')
wc = WordCloud(background_color='white', mask=img_array, font_path='msyh.ttc',
               stopwords=stopwords)
wc.generate_from_text(string)
image_colors = ImageColorGenerator(img_array)

# 绘制图片
plt.figure(figsize=(1.2, 1), dpi=1200)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')  # 不显示坐标轴
plt.show()
# plt.savefig(r'.\static\assets\img\word.jpg')
