import cv2
import pyautogui
import tkinter as tk
from PIL import ImageTk, Image

# 创建一个窗口
window = tk.Tk()
window.title("自动点击")
window.geometry("400x300")

# 创建一个标签用于显示目标图片a
label_a = tk.Label(window)
label_a.pack()

# 创建一个标签用于显示目标图片b
label_b = tk.Label(window)
label_b.pack()

# 读取目标图片a和目标图片b
# target_image_a = cv2.imread('target_image_a.png')
# target_image_b = cv2.imread('target_image_b.png')
target_image_a = cv2.imread('a.png')
target_image_b = cv2.imread('b.png')

# 获取屏幕尺寸
screen_width, screen_height = pyautogui.size()

# 初始化标志变量
is_clicked_a = False


def update_images():
    global is_clicked_a

    # 在屏幕上查找目标图片a
    result_a = pyautogui.locateOnScreen(target_image_a,confidence=0.8)

    # 如果找到目标图片a
    if result_a is not None:
        # 获取目标图片a的中心坐标
        target_x_a, target_y_a, target_width_a, target_height_a = result_a
        target_center_x_a = target_x_a + target_width_a / 2
        target_center_y_a = target_y_a + target_height_a / 2
        print("target_center_x_a:", target_center_x_a, "target_center_y_a:", target_center_y_a)

        # 移动鼠标到目标图片a的中心坐标并进行点击
        pyautogui.moveTo(target_center_x_a, target_center_y_a)
        pyautogui.click()
        print("点击了a")
        # 弹窗提示信息
        label_a.config(text="点击了a")

        # 更新标志变量
        is_clicked_a = True

        # 如果已经点击了图片a，则继续查找目标图片b
    if is_clicked_a:
        # 在屏幕上查找目标图片b
        result_b = pyautogui.locateOnScreen(target_image_b,confidence=0.8)

        # 如果找到目标图片b
        if result_b is not None:
            # 获取目标图片b的中心坐标
            target_x_b, target_y_b, target_width_b, target_height_b = result_b
            target_center_x_b = target_x_b + target_width_b / 2
            target_center_y_b = target_y_b + target_height_b / 2
            print("target_center_x_b:", target_center_x_b, "target_center_y_b:", target_center_y_b)

            # 移动鼠标到目标图片b的中心坐标并进行点击
            pyautogui.moveTo(target_center_x_b, target_center_y_b)
            pyautogui.click()
            print("点击了b")
            # 弹窗提示信息
            label_b.config(text="点击了b")

            # 重置标志变量
            is_clicked_a = False

            # 更新目标图片a的标签
    img_a = Image.fromarray(cv2.cvtColor(target_image_a, cv2.COLOR_BGR2RGB))
    img_a = img_a.resize((100, 100))
    img_a = ImageTk.PhotoImage(img_a)
    # label_a.configure(image=img_a)
    label_a.image = img_a

    # 更新目标图片b的标签
    img_b = Image.fromarray(cv2.cvtColor(target_image_b, cv2.COLOR_BGR2RGB))
    img_b = img_b.resize((100, 100))
    img_b = ImageTk.PhotoImage(img_b)
    # label_b.configure(image=img_b)
    label_b.image = img_b

    # 每隔一段时间更新图片
    window.after(1000, update_images)


# 启动图片更新
update_images()

# 启动窗口的主循环
window.mainloop()