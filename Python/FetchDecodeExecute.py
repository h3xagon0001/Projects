processor = {
    "processor_step": [
        "copy_PC_to_MAR",
        "copy_MAR_to_MDR",
        "copy_MDR_to_CIR",
        "increment_PC",
        "decode"
    ],
    "memory": None,
    "current_step": None,
    "program_counter": None,
    "memory_address_register": None,
    "memory_data_register": None,
    "current_instruction_register": None,
}

def processorInfo(processor):
    info = ""
    info += "[Memory]\n"

    for addressData in processor["memory"]:
        info += f"{addressData[0]} {addressData[1]}\n"

    info += "\n"
    info += f'[Current Step]: {processor["current_step"]}\n'
    info += f'[PC]: {processor["program_counter"]}\n'
    info += f'[MAR]: {processor["memory_address_register"]}\n'
    info += f'[MDR]: {processor["memory_data_register"]}\n'
    info += f'[CIR]: {processor["current_instruction_register"]}\n'

    return info

processor["memory"] = [
    [0, "read"],
    [1, "read"],
    [2, "read"],
    [3, "read"],
    [4, ""]
]
processor["current_step"] = "copy_PC_to_MAR"
processor["program_counter"] = 0

print(processorInfo(processor))
input()

while True:
    if processor["current_step"] == "copy_PC_to_MAR":
        