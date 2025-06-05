16# 身長と体重を入力すると平均体重が出てくるプログラム

def main():
    weights = []
    while True:
        try:
            height = float(input("身長をcmで入力してください（終了するには0を入力）："))
            if height == 0:
                break
            weight = float(input("体重をkgで入力してください："))
            weights.append(weight)
        except ValueError:
            print("数値を入力してください。")
            continue

    if weights:
        avg_weight = sum(weights) / len(weights)
        print(f"\n入力された人数: {len(weights)}人")
        print(f"平均体重: {avg_weight:.2f}kg")
    else:
        print("データがありません。")

if __name__ == "__main__":
    main()