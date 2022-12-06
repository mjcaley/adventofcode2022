def start_of_packet(line: str, length: int) -> int:
    for i in range(len(line)):
        sub = {char for char in line[i:i+length]}
        if len(sub) == length:
            return i + length


def first_start_of_packet(line: str) -> int:
    return start_of_packet(line, 4)


def first_start_of_message_packet(line: str) -> int:
    return start_of_packet(line, 14)


def parse1(line: str) -> int:
    return first_start_of_packet(line)


def parse2(line: str) -> int:
    return first_start_of_message_packet(line)
