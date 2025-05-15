import sys
import time
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append("modules")
import modules.a2_earthquake_info
import modules.a3_MySQL
import modules.a4_向量資料庫
import modules.a5_typesetting



def main(user_input):
    total_start = time.time()
    step_log = []

    # 步驟 1：地震即時資訊
    start = time.time()
    earthquake_info = modules.a2_earthquake_info.main()
    step_log.append(("地震即時資訊", time.time() - start))

    # 步驟 2：數學模型運算與資源決策
    start = time.time()
    mysql_summarize = modules.a3_MySQL.main()
    step_log.append(("資源部屬分析", time.time() - start))

    # 步驟 3：歷史資料匹配與應變建議
    start = time.time()
    strategy_summarize = modules.a4_向量資料庫.vectorize_and_decide()
    step_log.append(("匹配歷史災害並給予決策建議", time.time() - start))

    # 步驟 4：打印報告
    start = time.time()
    disaster_report = f"""
    一、即時地震資訊\n
    {earthquake_info}\n

    二、資源分配規劃\n
    {mysql_summarize}\n

    三、綜合決策建議\n
    {strategy_summarize}
    """

    print(disaster_report)


    # disaster_report_after_typesetting = modules.a5_typesetting.generate_typesetting(disaster_report)
    # print(disaster_report_after_typesetting)
    # step_log.append(("報告排版輸出", time.time() - start))

    # 顯示總耗時
    total_time = time.time() - total_start
    print(f"\n🔧 執行總耗時：{round(total_time, 2)} 秒")

    # 顯示耗時表格
    df = pd.DataFrame(step_log, columns=["模組", "耗時（秒）"])
    print("\n📊 各模組執行耗時：")
    print(df)

    # # 可視化
    # plt.barh(df["模組"], df["耗時（秒）"])
    # plt.xlabel("耗時（秒）")
    # plt.title("各模組執行時間")
    # plt.tight_layout()
    # plt.show()

    return disaster_report


if __name__ == "__main__":
    user_input = "身為台南市災防指揮官，針對剛剛台南市發生的地震，該如何調度資源因應"
    main(user_input)
