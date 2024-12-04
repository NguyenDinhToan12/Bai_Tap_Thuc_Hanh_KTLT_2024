input_string = input("nhap chuoi: ")
result_string = ''.join([char for char in input_string if not char.isdigit()])
print("chuoi sau khi bi loai bo cac chu so:", result_string)
