address_field = 200
r1 = 40
memory = {200: 500, 240: 900}
immediate_value = 25

print("a) Immediate addressing")
print("Rule: The operand is included in the instruction.")
print(f"Operand = {immediate_value}; no effective address is calculated.")

print("\nb) Direct addressing")
print("Rule: EA = address field.")
direct_ea = address_field
print(f"EA = {direct_ea}; operand = Memory[{direct_ea}] = {memory[direct_ea]}")

print("\nc) Indirect addressing")
print("Rule: EA = Memory[address field].")
indirect_ea = memory[address_field]
print(f"EA = Memory[{address_field}] = {indirect_ea}")
print(f"Operand at Memory[{indirect_ea}] is not given.")

print("\nd) Indexed addressing")
print("Rule: EA = address field + index register.")
indexed_ea = address_field + r1
print(f"EA = {address_field} + {r1} = {indexed_ea}")
print(f"Operand = Memory[{indexed_ea}] = {memory[indexed_ea]}")