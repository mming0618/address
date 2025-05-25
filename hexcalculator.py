def hex_calculator():
    """
    十六进制加减计算器（支持任意长度）
    输入格式示例：
    hex1 = "1a3f"
    hex2 = "b7e2"
    operation = "+" 或 "-"
    """
    while True:
        try:
            hex1 = input("请输入第一个十六进制数（输入 q 退出）: ").strip().lower()
            if hex1 == 'q':
                break
            hex2 = input("请输入第二个十六进制数: ").strip().lower()
            op = input("请选择运算 (+/-): ").strip()

            # 转换为整数
            num1 = int(hex1, 16)
            num2 = int(hex2, 16)

            # 执行运算
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            else:
                raise ValueError("无效运算符，请输入 + 或 -")

            # 转换回十六进制（去掉前缀，处理负数）
            if result < 0:
                hex_result = f"-{abs(result):x}"
            else:
                hex_result = f"{result:x}"

            print(f"计算结果: {hex_result}\n")
            
        except ValueError as e:
            print(f"错误: {e}\n")
        except KeyboardInterrupt:
            print("\n操作已终止")
            break

if __name__ == "__main__":
    hex_calculator()
