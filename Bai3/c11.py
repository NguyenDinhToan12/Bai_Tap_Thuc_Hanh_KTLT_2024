def benefit(t, n, k):
    # Tính sô tiên nhận được sau k tháng
    S = n * (1 + t / 100) ** k
    return S

# Nhập lãi suất, số vốn ban đầu và số tháng gửi từ bàn phím
t = float(input("Nhập lãi suất (t%) mỗi tháng: "))
n = float(input("Nhập số vốn ban đầu (n): "))
k = int(input("Nhập số tháng gửi (k): "))

# Tính và in ra số tiền nhận được
result = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {result:.2f}")
