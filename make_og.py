"""SNS共有用の画像 docs/og.png（1200x630）を作る。作品画像は使わず図形と文字だけ。"""
from PIL import Image, ImageDraw, ImageFont
W, H = 1200, 630
im = Image.new("RGB", (W, H), "#15161a")
d = ImageDraw.Draw(im)
for i, c in enumerate(["#6b4eff", "#9d8bff", "#ff7a59", "#ffc857"]):
    d.ellipse((760 + i * 70, 120 + i * 60, 1060 + i * 70, 420 + i * 60), outline=c, width=10)
font = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"
f1, f2 = ImageFont.truetype(font, 92), ImageFont.truetype(font.replace("W8", "W4"), 36)
d.text((80, 200), "AIデザイン", font=f1, fill="#ffffff")
d.text((80, 310), "実践ラボ", font=f1, fill="#9d8bff")
d.text((80, 450), "ロゴ・SNS画像・チラシをAIで作る実践ガイド", font=f2, fill="#c9ccd4")
im.save("docs/og.png")
