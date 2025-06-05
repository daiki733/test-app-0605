import random

# ダミーの選手名リスト（日本人名風）
names = [
    "佐藤 大輔", "鈴木 一郎", "高橋 健太", "田中 翔太", "伊藤 直樹",
    "渡辺 拓海", "山本 亮", "中村 優斗", "小林 海斗", "加藤 大地",
    "吉田 颯太", "山田 陽斗", "佐々木 陸", "山口 悠真", "松本 颯",
    "井上 智也", "木村 悠斗", "林 大和", "斎藤 陽向", "清水 悠人",
    "山崎 陸斗", "森 拓真", "池田 智樹", "橋本 大翔", "阿部 悠生",
    "石川 陽太", "山下 颯太", "中島 陸", "小川 悠真", "前田 大輝",
    "藤田 陽斗", "後藤 拓海", "岡田 智也", "長谷川 陸斗", "村上 大地",
    "近藤 颯", "石井 陽向", "坂本 悠斗", "遠藤 陸", "青木 大和",
    "藤井 拓真", "西村 智樹", "福田 大翔", "太田 悠生", "三浦 陽太",
    "岡本 颯太", "松田 陸斗", "中野 悠真", "原田 大輝", "小島 陽斗"
]

# 選手データ生成
runners = []
for name in names:
    time = round(random.uniform(9.56, 12.99), 2)
    age = random.randint(18, 35)
    runners.append({"name": name, "time": time, "age": age})

# バブルソートでタイム順に並び替え（アルゴリズムの過程を表示）
n = len(runners)
print("バブルソートによる並び替えの過程：")
for i in range(n):
    for j in range(0, n-i-1):
        if runners[j]["time"] > runners[j+1]["time"]:
            # 並び替えの様子を表
            # print(f'入れ替え: {runners[j]["name"]}({runners[j]["time"]}) <-> {runners[j+1]["name"]}({runners[j+1]["time"]})')
            runners[j], runners[j+1] = runners[j+1], runners[j]

# 上位5名を表示
print("\n上位5名のタイムと年齢：")
for i in range(5):
    r = runners[i]
    print(f'{i+1}位: {r["name"]} - タイム: {r["time"]}秒, 年齢: {r["age"]}歳')