PAGE_SIZE = 1024

page_table = {
    0: 5,
    1: 2,
    2: None,
    3: 7,
}

virtual_addresses = [500, 1500, 2500, 3500]

print(f"{'Virtual address':>16} | {'Page':>4} | {'Offset':>6} | {'Frame':>5} | Result")
print("-" * 65)

for virtual_address in virtual_addresses:
    page_number = virtual_address // PAGE_SIZE
    offset = virtual_address % PAGE_SIZE
    frame = page_table.get(page_number)

    if frame is None:
        print(f"{virtual_address:>16} | {page_number:>4} | {offset:>6} | {'—':>5} | Page fault")
    else:
        physical_address = frame * PAGE_SIZE + offset
        print(f"{virtual_address:>16} | {page_number:>4} | {offset:>6} | {frame:>5} | {physical_address}")