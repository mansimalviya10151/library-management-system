from datetime import datetime

def parse_date(date_str):
    if not date_str:
        return None
    return datetime.strptime(date_str, "%Y-%m-%d").date()

def format_date(date_obj):
    if not date_obj:
        return "N/A"
    return date_obj.strftime("%Y-%m-%d")

def calculate_fine(due_date_str, return_date=None, fine_per_day=5):
    if not due_date_str:
        return 0
    due_date = parse_date(due_date_str)
    current_date = return_date if return_date else datetime.now().date()
    if current_date > due_date:
        overdue_days = (current_date - due_date).days
        return overdue_days * fine_per_day
    return 0