from typing import Tuple


def parse_college(value: str) -> Tuple[str, str]:
    value = value.replace(" ", "")
    value = value.replace(")", "")
    college, detail = value.split("(")
    if college == "泰达物理":
        college = "物理学院"
    elif college == "泰达生物":
        college = "生物学院"
    elif college == "环科":
        college = "环境科学与工程学院"
    elif college == "药学院":
        college = "药学院"

    return college, detail


def parse_dorm(value: str) -> Tuple[str, str, str, str]:
    """
    build, door_id, room_id, singleRoom_id
    """
    value = value.strip()
    if len(value) == 0:
        return "", "", "", ""
    if not value[0].isnumeric():
        return "", "", "", ""

    line_count = value.count("-")
    if line_count == 0:
        return value[0], "", value[1:], ""
    elif line_count == 3:
        data = value.split("-")
        build = data[0]
        door_id = data[1]
        room_id = data[2]
        singleRoom_id = data[3]
        return build, door_id, room_id, singleRoom_id



