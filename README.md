
<div align="center">

# 🧩 SUDOKU SOLVER OPTIMIZATION

### Đồ án Nhập môn Tối ưu hóa
### Tối ưu hóa thuật toán giải Sudoku bằng Backtracking kết hợp MRV và Forward Checking

**Trường Đại học Văn Lang — Khoa Công nghệ Thông tin**  
**Nhóm thực hiện: Nhóm 09**

![Optimization](https://img.shields.io/badge/Topic-Optimization-blue)
![Algorithms](https://img.shields.io/badge/Algorithms-Backtracking%20%7C%20MRV%20%7C%20Bitmask-green)
![Language](https://img.shields.io/badge/Language-Python%20%7C%20JavaScript-yellow)
![Dataset](https://img.shields.io/badge/Benchmark-100%20Sudoku-orange)

</div>

---

## 📖 1. Giới thiệu đề tài

Sudoku là bài toán thỏa mãn ràng buộc (*Constraint Satisfaction Problem – CSP*). Bàn cờ tiêu chuẩn gồm 9 hàng, 9 cột và 9 khối 3×3. Mỗi ô trống cần được điền một chữ số từ 1 đến 9 sao cho không có chữ số nào bị lặp trong cùng hàng, cột hoặc khối 3×3.

Dự án xây dựng và đánh giá các phương pháp giải Sudoku bằng Python. Các thuật toán được so sánh dựa trên thời gian thực thi, số nút tìm kiếm và tỷ lệ giải thành công trên bộ dữ liệu gồm 100 đề Sudoku được sinh tự động.

## 🎯 2. Mục tiêu

- Mô hình hóa Sudoku dưới dạng bài toán CSP gồm biến, miền giá trị và các ràng buộc.
- Cài đặt và so sánh các phương pháp giải Sudoku.
- Sinh dữ liệu Sudoku theo bốn mức độ: Easy, Medium, Hard và Expert.
- Đánh giá hiệu năng bằng thời gian giải, số nút tìm kiếm và trạng thái giải thành công.
- Trực quan hóa kết quả thực nghiệm bằng biểu đồ.

## 🧮 3. Mô hình hóa bài toán

### 3.1. Biến và miền giá trị

Mỗi ô ở hàng `r`, cột `c` được biểu diễn bởi biến `x[r,c]`. Bàn Sudoku có tổng cộng 81 biến.

- Ô đã có số trong đề bài được giữ cố định.
- Ô trống có miền giá trị từ 1 đến 9.
- Các giá trị có thể điền phải thỏa mãn ràng buộc hàng, cột và khối 3×3.

### 3.2. Các ràng buộc

- **Ràng buộc hàng:** Các chữ số trong cùng một hàng không được trùng nhau.
- **Ràng buộc cột:** Các chữ số trong cùng một cột không được trùng nhau.
- **Ràng buộc khối:** Các chữ số trong cùng một khối 3×3 không được trùng nhau.
- **Ràng buộc dữ liệu gốc:** Các ô đã được cho sẵn không được thay đổi.

### 3.3. Tiêu chí đánh giá

Các thuật toán được đánh giá bằng ba chỉ số:

- **Thời gian giải (ms):** Thời gian thuật toán cần để tìm lời giải.
- **Số nút tìm kiếm (Nodes):** Số lần thử gán giá trị trong quá trình tìm kiếm.
- **Tỷ lệ giải thành công:** Số đề giải thành công trên tổng số đề được kiểm tra.

Thời gian và số nút tìm kiếm được báo cáo riêng vì chúng có đơn vị đo khác nhau.

## ⚙️ 4. Các thuật toán

### 4.1. Baseline Backtracking

Duyệt các ô theo thứ tự hàng trước, cột sau. Với mỗi ô trống, thuật toán thử lần lượt các số từ 1 đến 9. Nếu lựa chọn không dẫn đến nghiệm, thuật toán quay lui để thử giá trị khác.

### 4.2. MRV Scan

MRV (*Minimum Remaining Values*) chọn ô trống có ít giá trị hợp lệ nhất trước. Chiến lược này ưu tiên các ô bị ràng buộc nhiều, giúp phát hiện nhánh không khả thi sớm hơn.

### 4.3. CSP Bitmask + MRV

Kết hợp chiến lược MRV với cách biểu diễn trạng thái hàng, cột và khối bằng bitmask. Các phép toán bit được sử dụng để xác định nhanh những chữ số còn có thể điền vào một ô.

### 4.4. Forward Checking

Forward Checking cập nhật miền giá trị của các ô chưa điền sau mỗi lần gán số. Nếu một ô liên quan không còn giá trị hợp lệ, thuật toán phát hiện nhánh không khả thi và quay lui.

## 🗂️ 5. Cấu trúc dự án

```text
Sudoku-solver-optimization/
├── README.md
├── requirements.txt
├── run_experiments.py
├── analyze.py
├── data/
├── figures/
├── notebooks/
├── report/
├── results/
│   └── benchmark_results.csv
└── src/
    ├── generator.py
    └── solvers.py
```

| Tệp/thư mục | Chức năng |
|---|---|
| `src/solvers.py` | Cài đặt các thuật toán giải Sudoku |
| `src/generator.py` | Sinh đề Sudoku và kiểm tra số lượng nghiệm |
| `run_experiments.py` | Chạy thực nghiệm và ghi kết quả vào CSV |
| `analyze.py` | Đọc CSV và tạo biểu đồ so sánh |
| `results/benchmark_results.csv` | Lưu kết quả thực nghiệm của 100 đề |
| `figures/` | Lưu các biểu đồ được tạo từ dữ liệu benchmark |
| `notebooks/` | Lưu notebook phục vụ quá trình thực hiện |
| `data/` | Thư mục dữ liệu của dự án |
| `report/` | Lưu tài liệu và nội dung báo cáo |

## 📊 6. Dữ liệu thực nghiệm

Dữ liệu benchmark nằm tại `results/benchmark_results.csv`, gồm **100 đề Sudoku**, chia đều thành bốn mức độ:

| Mức độ | Số lượng đề |
|---|---:|
| Easy | 25 |
| Medium | 25 |
| Hard | 25 |
| Expert | 25 |
| **Tổng cộng** | **100** |

Các đề được sinh bởi `src/generator.py`. Số ô gợi ý mục tiêu được thiết lập như sau:

| Mức độ | Số ô gợi ý mục tiêu |
|---|---:|
| Easy | 45 |
| Medium | 35 |
| Hard | 28 |
| Expert | 21 |

Bộ sinh kiểm tra số lượng nghiệm và chỉ giữ lại các đề có đúng một nghiệm.

### 6.1. Các trường dữ liệu trong CSV

| Cột | Ý nghĩa |
|---|---|
| `Level` | Mức độ đề Sudoku |
| `Puzzle_ID` | Mã đề trong từng mức |
| `Seed` | Giá trị seed dùng để sinh đề |
| `Base_Time`, `Base_Nodes`, `Base_Solved` | Thời gian, số nút và trạng thái giải của Baseline |
| `MRV_Time`, `MRV_Nodes`, `MRV_Solved` | Thời gian, số nút và trạng thái giải của MRV Scan |
| `CSP_Time`, `CSP_Nodes`, `CSP_Solved` | Thời gian, số nút và trạng thái giải của CSP Bitmask |
| `FC_Time`, `FC_Nodes`, `FC_Solved` | Thời gian, số nút và trạng thái giải của Forward Checking |

Các cột thời gian có đơn vị mili giây. Các cột `*_Solved` thể hiện thuật toán có giải thành công đề tương ứng hay không.

### 6.2. Kết quả giải thành công từ CSV hiện tại

Dựa trên 100 dòng dữ liệu trong file CSV được lưu trên repository:

| Thuật toán | Số đề giải thành công |
|---|---:|
| Baseline Backtracking | 99/100 |
| MRV Scan | 100/100 |
| CSP Bitmask + MRV | 100/100 |
| Forward Checking | 100/100 |

Một đề ở mức Expert không được Baseline giải thành công trong giới hạn thời gian. Ba phương pháp còn lại giải thành công toàn bộ 100 đề trong dữ liệu hiện tại.

> Kết quả trên là trạng thái của file CSV hiện được lưu trong repository. Nếu chạy lại thực nghiệm, thời gian và số nút có thể thay đổi theo dữ liệu sinh ra, phần cứng và môi trường chạy.

## 📈 7. Phân tích và trực quan hóa

Chạy `analyze.py` để đọc `results/benchmark_results.csv` và tạo hai biểu đồ:

- `figures/fig_runtime_comparison.png`: So sánh thời gian giải trung bình của bốn thuật toán theo từng mức độ.
- `figures/fig_nodes_comparison.png`: So sánh số nút tìm kiếm trung bình của bốn thuật toán theo từng mức độ.

Các biểu đồ sử dụng thang logarit (`log scale`) để thể hiện chênh lệch hiệu năng giữa các thuật toán.

## 🚀 8. Cài đặt và chạy chương trình

### 8.1. Yêu cầu

- Python 3.8 trở lên.
- Các thư viện được liệt kê trong `requirements.txt`.

### 8.2. Cài đặt thư viện

Mở terminal tại thư mục gốc dự án và chạy:

```bash
pip install -r requirements.txt
```

### 8.3. Chạy thực nghiệm

Sau khi bảo đảm `src/solvers.py` có đủ bốn hàm giải tương ứng với các hàm được import trong `run_experiments.py`, chạy:

```bash
python run_experiments.py
```

Chương trình sinh 25 đề cho mỗi mức độ, chạy bốn thuật toán và ghi kết quả vào:

```text
results/benchmark_results.csv
```

### 8.4. Tạo biểu đồ

Sau khi có file CSV với đầy đủ các cột kết quả, chạy:

```bash
python analyze.py
```

Hai biểu đồ sẽ được lưu trong thư mục `figures/`.

## ⚠️ 9. Giới hạn và hướng phát triển

- Bộ dữ liệu thực nghiệm hiện gồm 100 đề, phù hợp để so sánh trong phạm vi bài tập.
- Thời gian chạy phụ thuộc cấu hình phần cứng và môi trường thực thi.
- Số ô gợi ý là mục tiêu khi sinh đề; số ô thực tế có thể phụ thuộc điều kiện giữ đề có nghiệm duy nhất.
- Nên chạy thực nghiệm nhiều lần để có đánh giá ổn định hơn.
- Có thể mở rộng số lượng đề, bổ sung thống kê trung vị và độ lệch chuẩn.
- Cần bảo đảm mã nguồn của cả bốn thuật toán đồng bộ với script chạy thực nghiệm và dữ liệu CSV.

## 👥 10. Thành viên thực hiện

**Nhóm 09 — Khoa Công nghệ Thông tin, Trường Đại học Văn Lang**

| Họ và tên | Mã số sinh viên |
|---|---|
| Nguyễn Hà Tiến Đạt | 2474802010077 |
| Nguyễn Bảo Lâm | 2474802010209 |
| Lâm Hữu Lộc | 2474802010221 |

## 📚 11. Tài liệu tham khảo

- Russell, S. và Norvig, P. — *Artificial Intelligence: A Modern Approach*, nội dung về Constraint Satisfaction Problems.
- [Python Documentation](https://docs.python.org/3/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)
- [Sudoku Solver Optimization — GitHub Repository](https://github.com/nguyenhatiendat/Sudoku-solver-optimization)
