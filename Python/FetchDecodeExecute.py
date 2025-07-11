import time

processor = {
    "processor_step": [
        "copy_PC_to_MAR",
        "copy_MAR_to_MDR",
        "copy_MDR_to_CIR",
        "increment_PC",
        "decode_execute"
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

    for address in range(len(processor["memory"])):
        info += f"{address} {processor["memory"][address]}\n"

    info += "\n"
    info += f'[Current Step]: {processor["current_step"]}\n'
    info += f'[PC]: {processor["program_counter"]}\n'
    info += f'[MAR]: {processor["memory_address_register"]}\n'
    info += f'[MDR]: {processor["memory_data_register"]}\n'
    info += f'[CIR]: {processor["current_instruction_register"]}\n'

    return info


def decode_execute(processor, instruction):
    command = ""
    argument = ""

    command_arguments = instruction.split(" ")
    command = command_arguments[0]

    if command == "GOTO":
        goto_address = int(command_arguments[1])
        processor["program_counter"] = goto_address

    elif command == "READ":
        read_address = int(command_arguments[1])
        print(f"READ AT {read_address}: {processor["memory"][read_address]}\n")

    elif command == "WRITE":
        write_address = int(command_arguments[1])
        write_data = str(command_arguments[2])
        processor["memory"][write_address] = write_data

    elif command == "COPY":
        copy_address = int(command_arguments[1])
        paste_address = int(command_arguments[2])
        processor["memory"][paste_address] = processor["memory"][copy_address]

    elif command == "DELETE":
        delete_address = int(command_arguments[1])
        processor["memory"][delete_address] = ""

    elif command == "INCREMENT":
        increment_address = int(command_arguments[1])
        processor["memory"][increment_address] = str(int(processor["memory"][increment_address]) + 1)

    return processor


processor["memory"] = [
    "0",
    "INCREMENT 0",
    "GOTO 1"
]
processor["current_step"] = "copy_PC_to_MAR"
processor["program_counter"] = 0


print(processorInfo(processor))
input("Press ENTER for next step...\n")


while True:
    if processor["current_step"] == "copy_PC_to_MAR":
        processor["memory_address_register"] = processor["program_counter"]


    elif processor["current_step"] == "copy_MAR_to_MDR":
        processor["memory_data_register"] = processor["memory"][processor["memory_address_register"]]


    elif processor["current_step"] == "copy_MDR_to_CIR":
        processor["current_instruction_register"] = processor["memory_data_register"]


    elif processor["current_step"] == "increment_PC":
        processor["program_counter"] += 1


    elif processor["current_step"] == "decode_execute":
        processor = decode_execute(processor, processor["current_instruction_register"])


    else:
        exit()
    
    print(processorInfo(processor))
    time.sleep(0)
    #input("Press ENTER for next step...\n")

    if processor["current_step"] == "decode_execute":
        processor["current_step"] = processor["processor_step"][0]

    else:
        processor["current_step"] = processor["processor_step"][
            processor["processor_step"].index(processor["current_step"]) + 1
        ]
