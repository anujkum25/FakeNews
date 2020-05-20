from models import standard_model
from datetime import datetime


start=datetime.now()
print(standard_model())
end=datetime.now()
duration=end-start
print(duration)