import qrcode

# 要编码的数据
data = "https://supershrimp.github.io/SciTokyo_AR-Arc/"

# 创建二维码对象
qr = qrcode.QRCode(
    version=1,  # 控制二维码的大小，1是最小（21x21）
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # 容错等级
    box_size=10,  # 每个小格子的像素大小
    border=4,  # 边框宽度（4个格子）
)

qr.add_data(data)  # 添加数据
qr.make(fit=True)  # 自动调整大小

# 生成图像
img = qr.make_image(fill_color="black", back_color="white")

# 保存为文件
img.save("qrcode.png")
