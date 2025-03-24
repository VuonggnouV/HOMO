raw_text = """
Tải lớn
Ba gác
Tải lớn
"""

# Chuyển thành danh sách Python
name_list = raw_text.split("\n")
formatted_names = "names = [\n    " + ",\n    ".join(f'"{name}"' for name in name_list) + "\n]"

print(formatted_names)
