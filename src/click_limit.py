```python
class ClickLimit:
    def __init__(self):
        self.unlimited = True
        self.limit = 0

    def set_unlimited(self):
        self.unlimited = True

    def set_limit(self, limit):
        self.unlimited = False
        self.limit = limit

    def get_limit(self):
        if self.unlimited:
            return "Unlimited"
        else:
            return self.limit
```