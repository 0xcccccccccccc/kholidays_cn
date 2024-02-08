import calendar
import datetime
import math
from typing import List, Iterator, Tuple

from chinese_calendar.constants import holidays, workdays, Holiday


def format_date(d: datetime.date):
    return f"{calendar.month_name[d.month].lower()} {d.day} {d.year}"


def wide_char_len(s: str):
    acc = 0
    for ch in s:
        if ord(ch) in range(0x20, 0x7f):
            acc += 1
        else:
            acc += 1.6
    return int(math.ceil(acc))


def render(ls: List[Tuple[str]]) -> Iterator[str]:
    max_line_width: int = max(map(lambda x: wide_char_len(x[0] + x[1]) + 3, ls))
    for i in ls:
        yield i[0] + i[1].rjust(max_line_width - wide_char_len(i[0]), ' ')


if __name__ == "__main__":
    days: List[datetime.date] = [*holidays.keys(), *workdays.keys()]
    lines = []
    for d in sorted(days):
        if d in holidays:
            lines.append((f'"{Holiday(holidays[d]).chinese}({holidays[d]})"', f'public on {format_date(d)}'))
        if d in workdays:
            lines.append(
                (f'"法定工作日-{Holiday(workdays[d]).chinese}调休 (Workday)"', f'public on {format_date(d)}'))

    with open("holiday_cn_zh-cn", "w") as f_output, open("template", "r") as f_template:
        template = f_template.read()
        f_output.write(template.replace(
            "{build_date}", datetime.datetime.now().isoformat()
        ).replace(
            "{extra_lines}", "\n".join(render(lines))
        ))
