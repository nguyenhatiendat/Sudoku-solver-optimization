import pandas as pd
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    os.makedirs("figures", exist_ok=True)
    df = pd.read_csv("results/benchmark_results.csv")

    # 1. Vẽ biểu đồ so sánh thời gian (4 cột)
    plt.figure(figsize=(10, 6))
    mean_times = df.groupby("Level")[["Base_Time", "MRV_Time", "CSP_Time", "FC_Time"]].mean()
    mean_times.plot(kind="bar", logy=True, color=["#f87171", "#facc15", "#34d399", "#60a5fa"])
    plt.title("So sánh thời gian giải trung bình (ms) - Log Scale")
    plt.ylabel("Thời gian (ms)")
    plt.xticks(rotation=0)
    plt.legend(["Baseline", "MRV Scan", "CSP Bitmask", "Forward Checking"])
    plt.tight_layout()
    plt.savefig("figures/fig_runtime_comparison.png")
    plt.close()

    # 2. Vẽ biểu đồ so sánh số Nodes (4 cột)
    plt.figure(figsize=(10, 6))
    mean_nodes = df.groupby("Level")[["Base_Nodes", "MRV_Nodes", "CSP_Nodes", "FC_Nodes"]].mean()
    mean_nodes.plot(kind="bar", logy=True, color=["#f87171", "#facc15", "#34d399", "#60a5fa"])
    plt.title("So sánh số Nodes trung bình - Log Scale")
    plt.ylabel("Số Nodes")
    plt.xticks(rotation=0)
    plt.legend(["Baseline", "MRV Scan", "CSP Bitmask", "Forward Checking"])
    plt.tight_layout()
    plt.savefig("figures/fig_nodes_comparison.png")
    plt.close()

    print("Đã xuất 2 hình biểu đồ vào thư mục figures/")