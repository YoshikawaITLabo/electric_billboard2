from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont
import time

# LEDマトリクスの設定
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.gpio_slowdown = 4  # GPIOの速度を遅くする

matrix = RGBMatrix(options=options)

# フォントとテキストの設定
#font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
font = ImageFont.truetype("/usr/share/fonts/truetype/sazanami/sazanami-gothic.ttf", 30)
#text = "This is a long scrolling text example for a 32x64 LED matrix!"
#text = "こんにちは　日本語で表示するとこうなります"
#text_bbox = font.getbbox(text)
#text_width = text_bbox[2] - text_bbox[0]
#text_height = text_bbox[3] - text_bbox[1]

text_part1 = "こんにちわ、"
text_part2 = "日本語"
text_part3 = "で表示するとこうなります"

text_bbox_part1 = font.getbbox(text_part1)
text_bbox_part2 = font.getbbox(text_part2)
text_bbox_part3 = font.getbbox(text_part3)
text_width_part1 = text_bbox_part1[2] - text_bbox_part1[0]
text_width_part2 = text_bbox_part2[2] - text_bbox_part2[0]
text_width_part3 = text_bbox_part3[2] - text_bbox_part3[0]
text_height = max(text_bbox_part1[3] - text_bbox_part1[1], text_bbox_part2[3] - text_bbox_part2[1], text_bbox_part3[3] - text_bbox_part3[1])
text_width = text_width_part1 + text_width_part2 + text_width_part3

# 画像の作成
#image = Image.new("RGB", (text_width + 0, 32))
#draw = ImageDraw.Draw(image)
#draw.text((0, 0), text, fill=(255, 255, 255), font=font)

# 画像の作成
image_width = text_width + 256
image = Image.new("RGB", (text_width_part1 + text_width_part2 + text_width_part3, 30))
draw = ImageDraw.Draw(image)

# テキストを描画
drp = 64
draw.text((drp, 0), text_part1, fill=(255, 255, 255), font=font)  # 「こんにちわ、」を白色に

drp += text_width_part1
draw.text((drp, 0), text_part2, fill=(255, 0, 0), font=font)  # 「日本語」を赤色に

drp += text_width_part2
draw.text((drp, 0), text_part3, fill=(255, 255, 255), font=font)  # 「で表示するとこうなります」を白色に

# スクロールの設定
x_pos = 1

# 無限ループでスクロール表示
try:
    while True:
        # 画像の一部を切り取って表示
        matrix.SetImage(image.crop((x_pos, 0, x_pos + 64, 32)).convert('RGB'))
        x_pos += 1
        if x_pos > image_width:
            x_pos = 1
        time.sleep(0.05)  # スクロール速度を調整
except KeyboardInterrupt:
    pass

