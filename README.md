# OSG
## Mô phỏng các cơ chế đồng bộ I/O

### 1. Giới thiệu
- Chương trình này mô phỏng các cơ chế đồng bộ trong hệ điều hành khi làm việc với I/O
- Bao gồm:
  + Mutex
  + Semaphore
  + Condition Variable
- Mục tiêu:
  + Hiểu cách các tiến trình đồng bộ khi truy cập tài nguyên dùng chung
  + Tránh xung đột và đảm bảo tính đúng đắn của dữ liệu

---

## MUTEX

### 1. Giới thiệu
- Mô phỏng cơ chế Mutex
- Nguyên tắc:
  + Chỉ một tiến trình được truy cập thiết bị I/O tại một thời điểm
- Là cơ chế loại trừ lẫn nhau

### 2. Thuật toán
- Tạo mutex (Lock)
- Tạo nhiều tiến trình (threads)
- Mỗi tiến trình:
  + Chờ I/O
  + Khi vào vùng tới hạn:
    - Khóa mutex
    - Thực hiện I/O
    - Mở khóa mutex

### 3. Ví dụ chạy chương trình

- Chạy:
  ```
  python io_sync.py
  ```
- Chọn:
  ```
  1
  ```

- Output:
  ```
  --- MÔ PHỎNG MUTEX ---
  Process-1: Đang chờ thiết bị I/O...
  Process-2: Đang chờ thiết bị I/O...
  Process-3: Đang chờ thiết bị I/O...

  Process-1: Đang sử dụng thiết bị I/O
  Process-1: Hoàn thành I/O

  Process-2: Đang sử dụng thiết bị I/O
  Process-2: Hoàn thành I/O

  Process-3: Đang sử dụng thiết bị I/O
  Process-3: Hoàn thành I/O
  ```

### 4. Nhận xét
- Các tiến trình chạy tuần tự
- Không có 2 tiến trình nào chạy cùng lúc

---

## SEMAPHORE

### 1. Giới thiệu
- Mô phỏng Semaphore
- Cho phép nhiều tiến trình sử dụng I/O nhưng có giới hạn (ở đây là 2)

### 2. Thuật toán
- Khởi tạo semaphore = 2
- Mỗi tiến trình:
  + Chờ quyền truy cập
  + Khi có slot:
    - Thực hiện I/O
    - Giải phóng slot

### 3. Ví dụ chạy chương trình

- Chọn:
  ```
  2
  ```

- Output:
  ```
  --- MÔ PHỎNG SEMAPHORE ---
  Process-1: Đang chờ cấp quyền I/O...
  Process-2: Đang chờ cấp quyền I/O...
  Process-3: Đang chờ cấp quyền I/O...
  Process-4: Đang chờ cấp quyền I/O...
  Process-5: Đang chờ cấp quyền I/O...

  Process-1: Đang thực hiện I/O
  Process-2: Đang thực hiện I/O

  Process-1: Hoàn thành I/O
  Process-3: Đang thực hiện I/O

  Process-2: Hoàn thành I/O
  Process-4: Đang thực hiện I/O

  Process-3: Hoàn thành I/O
  Process-5: Đang thực hiện I/O
  ```

### 4. Nhận xét
- Có 2 tiến trình chạy song song
- Các tiến trình còn lại phải chờ

---

## CONDITION VARIABLE

### 1. Giới thiệu
- Mô phỏng Condition Variable
- Theo mô hình Producer - Consumer

### 2. Thuật toán
- Producer tạo dữ liệu
- Consumer:
  + Nếu chưa có dữ liệu → wait()
  + Khi có dữ liệu → xử lý

### 3. Ví dụ chạy chương trình

- Chọn:
  ```
  3
  ```

- Output:
  ```
  --- MÔ PHỎNG CONDITION VARIABLE ---
  Process đang chờ dữ liệu...

  Thiết bị I/O tạo dữ liệu: Data-1
  Process xử lý dữ liệu: Data-1

  Thiết bị I/O tạo dữ liệu: Data-2
  Process xử lý dữ liệu: Data-2

  Thiết bị I/O tạo dữ liệu: Data-3
  Process xử lý dữ liệu: Data-3
  ```

### 4. Nhận xét
- Consumer phải chờ dữ liệu
- Khi có dữ liệu → được đánh thức và xử lý

---

## MENU CHƯƠNG TRÌNH

### 1. Giao diện
```
1. Mô phỏng Mutex
2. Mô phỏng Semaphore
3. Mô phỏng Condition Variable
4. Mô phỏng tất cả
0. Thoát
```

---

## 5. Cách chạy chương trình

- Cài Python (>= 3.x)
- Chạy:
  ```
  python io_sync.py
  ```
- Chọn chức năng mong muốn

---

## 6. Kết luận

- Mutex:
  + Đảm bảo chỉ 1 tiến trình truy cập tài nguyên
- Semaphore:
  + Cho phép nhiều tiến trình nhưng có giới hạn
- Condition Variable:
  + Đồng bộ theo điều kiện (chờ dữ liệu)

→ Ba cơ chế này rất quan trọng trong hệ điều hành để:
- Tránh race condition
- Đồng bộ tiến trình
- Tối ưu xử lý I/O

---
