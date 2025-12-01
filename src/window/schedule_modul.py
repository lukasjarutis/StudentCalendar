from datetime import date, timedelta


class ScheduleModel:
    def __init__(self):
        self.timetable = {}
        self.recurring_lessons = []

    def clear(self):
        self.timetable.clear()
        self.recurring_lessons.clear()

    def add_recurring_lesson(self, weekday, row, repeat, base_monday, subject, type_, room, teacher, notes, exam=False):
        self.recurring_lessons.append(
            {
                "weekday": weekday,
                "row": row,
                "repeat": repeat,
                "base_monday": base_monday,
                "subject": subject,
                "type": type_,
                "room": room,
                "teacher": teacher,
                "notes": notes,
                "exam": bool(exam),
            }
        )

    def set_single_lesson(self, iso_date, row, data):
        self.timetable[(iso_date, row)] = data

    def remove_single_lesson(self, iso_date, row):
        self.timetable.pop((iso_date, row), None)

    def get_single_lesson(self, iso_date, row):
        return self.timetable.get((iso_date, row))

    def build_week_cells(self, current_monday, day_count, time_slots_len):
        grid = [[None for _ in range(day_count)] for _ in range(time_slots_len)]

        for lesson in self.recurring_lessons:
            weekday = lesson["weekday"]
            row = lesson["row"]
            repeat = lesson["repeat"]
            base_monday = lesson["base_monday"]

            week_diff = (current_monday - base_monday).days // 7
            if week_diff < 0:
                continue
            if repeat == "biweekly" and (week_diff % 2) == 1:
                continue
            if 0 <= weekday < day_count and 0 <= row < time_slots_len:
                data = {
                    "subject": lesson["subject"],
                    "type": lesson.get("type", ""),
                    "room": lesson["room"],
                    "teacher": lesson["teacher"],
                    "notes": lesson["notes"],
                    "exam": lesson.get("exam", False),
                }
                grid[row][weekday] = data

        for (iso, row), data in self.timetable.items():
            try:
                d = date.fromisoformat(iso)
            except Exception:
                continue
            delta = (d - current_monday).days
            if 0 <= delta < day_count and 0 <= row < time_slots_len:
                grid[row][delta] = data

        return grid

    def to_dict(self):
        timetable_list = []
        for (iso_date, row), data in self.timetable.items():
            timetable_list.append(
                {
                    "date": iso_date,
                    "row": row,
                    "data": data,
                }
            )

        recurring_list = []
        for lesson in self.recurring_lessons:
            rec = lesson.copy()
            rec["base_monday"] = rec["base_monday"].isoformat()
            recurring_list.append(rec)

        return {
            "timetable": timetable_list,
            "recurring_lessons": recurring_list,
        }

    def from_dict(self, payload):
        self.clear()

        for item in payload.get("timetable", []):
            iso_date = item.get("date")
            row = item.get("row")
            data = item.get("data", {})
            if iso_date is None or row is None:
                continue
            self.timetable[(iso_date, row)] = data

        for lesson in payload.get("recurring_lessons", []):
            base_monday_str = lesson.get("base_monday")
            if not base_monday_str:
                continue
            try:
                base_monday = date.fromisoformat(base_monday_str)
            except Exception:
                continue

            self.recurring_lessons.append(
                {
                    "weekday": lesson.get("weekday", 0),
                    "row": lesson.get("row", 0),
                    "repeat": lesson.get("repeat", "weekly"),
                    "base_monday": base_monday,
                    "subject": lesson.get("subject", ""),
                    "type": lesson.get("type", ""),
                    "room": lesson.get("room", ""),
                    "teacher": lesson.get("teacher", ""),
                    "notes": lesson.get("notes", ""),
                    "exam": lesson.get("exam", False),
                }
            )