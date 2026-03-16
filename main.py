import threading
import time
import random

# =========================================
# MÔ PHỎNG CÁC CƠ CHẾ ĐỒNG BỘ I/O
# Nguyễn Đình Quyết
# =========================================

def showTitle():
    print("\n" + "=" * 60)
    print("      MÔ PHỎNG CÁC CƠ CHẾ ĐỒNG BỘ I/O")
    print("           Nguyễn Đình Quyết")
    print("=" * 60)


# =================================================
# MUTEX
# =================================================
def simulateMutex():
    print("\n--- MÔ PHỎNG MUTEX ---")
    print("Chỉ 1 tiến trình được truy cập thiết bị I/O tại một thời điểm.\n")

    mutex = threading.Lock()

    def ioTask(name):
        print(f"{name}: Đang chờ thiết bị I/O...")
        with mutex:
            print(f"{name}: Đang sử dụng thiết bị I/O")
            time.sleep(random.uniform(1,2))
            print(f"{name}: Hoàn thành I/O")

    threads = []

    for i in range(3):
        t = threading.Thread(target=ioTask, args=(f"Process-{i+1}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# =================================================
# SEMAPHORE
# =================================================
def simulateSemaphore():
    print("\n--- MÔ PHỎNG SEMAPHORE ---")
    print("Cho phép tối đa 2 tiến trình sử dụng I/O cùng lúc.\n")

    semaphore = threading.Semaphore(2)

    def ioTask(name):
        print(f"{name}: Đang chờ cấp quyền I/O...")
        with semaphore:
            print(f"{name}: Đang thực hiện I/O")
            time.sleep(random.uniform(1.5,3))
            print(f"{name}: Hoàn thành I/O")

    threads = []

    for i in range(5):
        t = threading.Thread(target=ioTask, args=(f"Process-{i+1}",))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# =================================================
# CONDITION VARIABLE / MONITOR
# =================================================
def simulateConditionVariable():
    print("\n--- MÔ PHỎNG CONDITION VARIABLE ---")
    print("Tiến trình phải chờ đến khi có dữ liệu từ thiết bị I/O.\n")

    buffer = []
    condition = threading.Condition()

    def producer():
        for i in range(5):
            time.sleep(random.uniform(1,2))
            with condition:
                item = f"Data-{i+1}"
                buffer.append(item)
                print(f"Thiết bị I/O tạo dữ liệu: {item}")
                condition.notify()

    def consumer():
        for i in range(5):
            with condition:
                while not buffer:
                    print("Process đang chờ dữ liệu...")
                    condition.wait()

                item = buffer.pop(0)
                print(f"Process xử lý dữ liệu: {item}")

    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


# =================================================
# MENU
# =================================================
def showMenu():

    while True:

        showTitle()

        print("1. Mô phỏng Mutex")
        print("2. Mô phỏng Semaphore")
        print("3. Mô phỏng Condition Variable")
        print("4. Mô phỏng tất cả")
        print("0. Thoát")

        choice = input("\nNhập lựa chọn: ")

        if choice == "1":
            simulateMutex()

        elif choice == "2":
            simulateSemaphore()

        elif choice == "3":
            simulateConditionVariable()

        elif choice == "4":
            simulateMutex()
            simulateSemaphore()
            simulateConditionVariable()

        elif choice == "0":
            print("Thoát chương trình")
            break

        else:
            print("Lựa chọn không hợp lệ")

        input("\nNhấn Enter để quay lại menu...")


if __name__ == "__main__":
    showMenu()