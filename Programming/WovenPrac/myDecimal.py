from dataclasses import dataclass
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
import calendar

def money(amount: Decimal) -> Decimal:
    return amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

def days_in_month(d: date) -> int:
    return calendar.monthrange(d.year, d.month)[1]

def overlap_days(start1: date, end1: date, start2: date, end2: date) -> int:
    overlap_start = max(start1, start2)
    overlap_end = min(end1, end2)
    return max(0, (overlap_end - overlap_start).days)

@dataclass
class InvoiceLine:
    description: str
    amount: Decimal

def generate_invoice_line(
    period_start: date,
    period_end: date,
    service_start: date,
    service_end: date,
    monthly_price: Decimal,
) -> InvoiceLine:
    active_days = overlap_days(period_start, period_end, service_start, service_end)
    total_days = days_in_month(period_start)
    amount = money(monthly_price * Decimal(active_days) / Decimal(total_days))
    return InvoiceLine(
        description=f"Prorated service for {active_days} day(s)",
        amount=amount,
    )


a = 5

_counters = {}
todayDate = date.today().strftime("%Y%m%d")

todayInvNum = _counters.get(todayDate,0) + 1
invoice_number= f"INV-{todayDate}-{todayInvNum:03d}"

print(invoice_number)