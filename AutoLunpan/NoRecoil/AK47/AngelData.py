yaw1_ = 0.000000
yaw2_ = -0.143000
yaw3_ = 0.110000
yaw4_ = -0.132000
yaw5_ = -0.099000
yaw6_ = 0.638000
yaw7_ = 0.440000
yaw8_ = 0.704000
yaw9_ = -0.759000
yaw10_ = -2.310000
yaw11_ = -1.210000
yaw12_ = 0.616000
yaw13_ = -0.770000
yaw14_ = -1.364000
yaw15_ = -0.374000
yaw16_ = 1.936000
yaw17_ = 1.144000
yaw18_ = 0.902000
yaw19_ = 1.320000
yaw20_ = 1.936000
yaw21_ = -0.660000
yaw22_ = 0.110000
yaw23_ = -0.286000
yaw24_ = -0.418000
yaw25_ = 0.550000
yaw26_ = 0.440000
yaw27_ = -0.748000
yaw28_ = -1.672000
yaw29_ = -3.087920
yaw30_ = -0.000000

pitch1_ = 0.000000
pitch2_ = 0.198000
pitch3_ = 1.100000
pitch4_ = 1.606000
pitch5_ = 1.650000
pitch6_ = 1.804000
pitch7_ = 1.650000
pitch8_ = 1.144000
pitch9_ = 0.990000
pitch10_ = 0.000000
pitch11_ = 0.132000
pitch12_ = 0.528000
pitch13_ = 0.264000
pitch14_ = -0.220000
pitch15_ = 0.154000
pitch16_ = 0.374000
pitch17_ = 0.242000
pitch18_ = 0.220000
pitch19_ = 0.176000
pitch20_ = -0.528000
pitch21_ = 0.176000
pitch22_ = 0.110000
pitch23_ = 0.220000
pitch24_ = 0.220000
pitch25_ = 0.000000
pitch26_ = 0.110000
pitch27_ = 0.000000
pitch28_ = -0.110000
pitch29_ = -0.671000
pitch30_ = 0.000000


def format_six_decimal_places(number):
    # 使用 round 函数保留六位小数
    rounded_number = round(number, 6)

    # 使用字符串格式化来确保结果保留六位小数，即使小数部分为零
    return rounded_number

def get_numeric_input(prompt):
    while True:
        value = input(prompt)
        try:
            # 尝试将输入转换为浮点数
            value = float(value)
            return value
        except ValueError:
            print("请输入数值")

# 获取用户输入的 sensitivity 和 m_yaw
sensitivity = get_numeric_input("请输入你的游戏内 sensitivity: ")
m_yaw = get_numeric_input("请输入 m_yaw: ")
m_pitch = get_numeric_input("请输入 m_pitch: ")

print(f"sensitivity: {sensitivity}, m_yaw: {m_yaw}, m_pitch: {m_pitch}")


divider1 = m_yaw * sensitivity
divider2 = m_pitch * sensitivity

yaw1 = format_six_decimal_places(yaw1_ / divider1)
yaw2 = format_six_decimal_places(yaw2_ / divider1)
yaw3 = format_six_decimal_places(yaw3_ / divider1)
yaw4 = format_six_decimal_places(yaw4_ / divider1)
yaw5 = format_six_decimal_places(yaw5_ / divider1)
yaw6 = format_six_decimal_places(yaw6_ / divider1)
yaw7 = format_six_decimal_places(yaw7_ / divider1)
yaw8 = format_six_decimal_places(yaw8_ / divider1)
yaw9 = format_six_decimal_places(yaw9_ / divider1)
yaw10 = format_six_decimal_places(yaw10_ / divider1)
yaw11 = format_six_decimal_places(yaw11_ / divider1)
yaw12 = format_six_decimal_places(yaw12_ / divider1)
yaw13 = format_six_decimal_places(yaw13_ / divider1)
yaw14 = format_six_decimal_places(yaw14_ / divider1)
yaw15 = format_six_decimal_places(yaw15_ / divider1)
yaw16 = format_six_decimal_places(yaw16_ / divider1)
yaw17 = format_six_decimal_places(yaw17_ / divider1)
yaw18 = format_six_decimal_places(yaw18_ / divider1)
yaw19 = format_six_decimal_places(yaw19_ / divider1)
yaw20 = format_six_decimal_places(yaw20_ / divider1)
yaw21 = format_six_decimal_places(yaw21_ / divider1)
yaw22 = format_six_decimal_places(yaw22_ / divider1)
yaw23 = format_six_decimal_places(yaw23_ / divider1)
yaw24 = format_six_decimal_places(yaw24_ / divider1)
yaw25 = format_six_decimal_places(yaw25_ / divider1)
yaw26 = format_six_decimal_places(yaw26_ / divider1)
yaw27 = format_six_decimal_places(yaw27_ / divider1)
yaw28 = format_six_decimal_places(yaw28_ / divider1)
yaw29 = format_six_decimal_places(yaw29_ / divider1)
yaw30 = format_six_decimal_places(yaw30_ / divider1)


pitch1 = format_six_decimal_places(pitch1_ / divider2)
pitch2 = format_six_decimal_places(pitch2_ / divider2)
pitch3 = format_six_decimal_places(pitch3_ / divider2)
pitch4 = format_six_decimal_places(pitch4_ / divider2)
pitch5 = format_six_decimal_places(pitch5_ / divider2)
pitch6 = format_six_decimal_places(pitch6_ / divider2)
pitch7 = format_six_decimal_places(pitch7_ / divider2)
pitch8 = format_six_decimal_places(pitch8_ / divider2)
pitch9 = format_six_decimal_places(pitch9_ / divider2)
pitch10 = format_six_decimal_places(pitch10_ / divider2)
pitch11 = format_six_decimal_places(pitch11_ / divider2)
pitch12 = format_six_decimal_places(pitch12_ / divider2)
pitch13 = format_six_decimal_places(pitch13_ / divider2)
pitch14 = format_six_decimal_places(pitch14_ / divider2)
pitch15 = format_six_decimal_places(pitch15_ / divider2)
pitch16 = format_six_decimal_places(pitch16_ / divider2)
pitch17 = format_six_decimal_places(pitch17_ / divider2)
pitch18 = format_six_decimal_places(pitch18_ / divider2)
pitch19 = format_six_decimal_places(pitch19_ / divider2)
pitch20 = format_six_decimal_places(pitch20_ / divider2)
pitch21 = format_six_decimal_places(pitch21_ / divider2)
pitch22 = format_six_decimal_places(pitch22_ / divider2)
pitch23 = format_six_decimal_places(pitch23_ / divider2)
pitch24 = format_six_decimal_places(pitch24_ / divider2)
pitch25 = format_six_decimal_places(pitch25_ / divider2)
pitch26 = format_six_decimal_places(pitch26_ / divider2)
pitch27 = format_six_decimal_places(pitch27_ / divider2)
pitch28 = format_six_decimal_places(pitch28_ / divider2)
pitch29 = format_six_decimal_places(pitch29_ / divider2)
pitch30 = format_six_decimal_places(pitch30_ / divider2)




# 模版内容
template = rf"""
alias angel angel1
alias angel1 "start_gun;yaw {yaw1} 1 1; pitch {pitch1} 1 1;alias angel angel2"
alias angel2 "start_gun;yaw {yaw2} 1 1; pitch {pitch2} 1 1;alias angel angel3"
alias angel3 "start_gun;yaw {yaw3} 1 1; pitch {pitch3} 1 1;alias angel angel4"
alias angel4 "start_gun;yaw {yaw4} 1 1; pitch {pitch4} 1 1;alias angel angel5"
alias angel5 "start_gun;yaw {yaw5} 1 1; pitch {pitch5} 1 1;alias angel angel6"
alias angel6 "start_gun;yaw {yaw6}  1 1; pitch {pitch6} 1 1;alias angel angel7"
alias angel7 "start_gun;yaw {yaw7}  1 1; pitch {pitch7} 1 1;alias angel angel8"
alias angel8 "start_gun;yaw {yaw8}  1 1; pitch {pitch8} 1 1;alias angel angel9"
alias angel9 "start_gun;yaw {yaw9}  1 1; pitch {pitch9} 1 1;alias angel angel10"
alias angel10 "start_gun;yaw {yaw10}  1 1; pitch {pitch10} 1 1;alias angel angel11"
alias angel11 "start_gun;yaw {yaw11}  1 1; pitch {pitch11} 1 1;alias angel angel12"
alias angel12 "start_gun;yaw {yaw12}  1 1; pitch {pitch12} 1 1;alias angel angel13"
alias angel13 "start_gun;yaw {yaw13}  1 1; pitch {pitch13} 1 1;alias angel angel14"
alias angel14 "start_gun;yaw {yaw14}  1 1; pitch {pitch14} 1 1;alias angel angel15"
alias angel15 "start_gun;yaw {yaw15}  1 1; pitch {pitch15} 1 1;alias angel angel16"
alias angel16 "start_gun;yaw {yaw16}  1 1; pitch {pitch16} 1 1;alias angel angel17"
alias angel17 "start_gun;yaw {yaw17}  1 1; pitch {pitch17} 1 1;alias angel angel18"
alias angel18 "start_gun;yaw {yaw18}  1 1; pitch {pitch18} 1 1;alias angel angel19"
alias angel19 "start_gun;yaw {yaw19}  1 1; pitch {pitch19} 1 1;alias angel angel20"
alias angel20 "start_gun;yaw {yaw20}  1 1; pitch {pitch20} 1 1;alias angel angel21"
alias angel21 "start_gun;yaw {yaw21}  1 1; pitch {pitch21} 1 1;alias angel angel22"
alias angel22 "start_gun;yaw {yaw22}  1 1; pitch {pitch22} 1 1;alias angel angel23"
alias angel23 "start_gun;yaw {yaw23}  1 1; pitch {pitch23} 1 1;alias angel angel24"
alias angel24 "start_gun;yaw {yaw24}  1 1; pitch {pitch24} 1 1;alias angel angel25"
alias angel25 "start_gun;yaw {yaw25}  1 1; pitch {pitch25} 1 1;alias angel angel26"
alias angel26 "start_gun;yaw {yaw26}  1 1; pitch {pitch26} 1 1;alias angel angel27"
alias angel27 "start_gun;yaw {yaw27}  1 1; pitch {pitch27} 1 1;alias angel angel28"
alias angel28 "start_gun;yaw {yaw28}  1 1; pitch {pitch28} 1 1;alias angel angel29"
alias angel29 "start_gun;yaw {yaw29}  1 1; pitch {pitch29} 1 1;alias angel angel30"
alias angel30 "start_gun;yaw {yaw30}  1 1; pitch {pitch30} 1 1;alias angel "
"""





with open("AngelData.cfg", "w", encoding="utf-8") as f:
    f.writelines(template)
    f.close()