from models import *
import datetime

o = Orders(title="order", costomer="url", body="order body")
o.duration = datetime.timedelta(days=20, hours=10)