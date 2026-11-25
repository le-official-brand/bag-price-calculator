"""
Bag Price Calculator - @le_official_brand
Founder: [Your Real Name]
Business: Handmade crochet bags in UAE

Calculates the true cost, profit and profit margin for each bag.
Yarn cost is fixed. Other materials (hook, lock, lining, chain)
change for every bag design.
"""

class CrochetBag:
    def __init__(self, name, yarn_cost=32.0, other_materials=0.0,
                 labour_hours=0.0, labour_rate=20.0, selling_price=0.0):
        self.name = name
        self.yarn_cost = yarn_cost
        self.other_materials = other_materials
        self.labour_hours = labour_hours
        self.labour_rate = labour_rate
        self.selling_price = selling_price

    def total_cost(self):
        """Total cost = yarn + other materials + labour"""
        labour_cost = self.labour_hours * self.labour_rate
        return self.yarn_cost + self.other_materials + labour_cost

    def profit(self):
        """Profit = Selling Price - Total Cost"""
        return self.selling_price - self.total_cost()

    def profit_margin(self):
        """Profit Margin % = Profit / Selling Price * 100"""
        if self.selling_price == 0:
            return 0
        return (self.profit() / self.selling_price) * 100

    def summary(self):
        print(f"\n--- {self.name} ---")
        print(f"Yarn Cost:            {self.yarn_cost:.2f} AED")
        print(f"Other Materials:      {self.other_materials:.2f} AED (hook, lock, lining)")
        print(f"Labour: {self.labour_hours}h x {self.labour_rate} AED = {self.labour_hours * self.labour_rate:.2f} AED")
        print(f"Total Cost:           {self.total_cost():.2f} AED")
        print(f"Selling Price:        {self.selling_price:.2f} AED")
        print(f"Profit:               {self.profit():.2f} AED")
        print(f"Profit Margin:        {self.profit_margin():.1f}%")
        if self.profit_margin() < 30:
            print("⚠️  Margin too low - consider increasing price or reducing cost")
        else:
            print("✅  Healthy margin for a handmade business")

# --- Real Examples from @le_official_brand ---
# Bag 1: Simple bag, cheap lock, sold for 140 AED
bag1 = CrochetBag(
    name="Classic Bag - 140 AED",
    yarn_cost=32.0,
    other_materials=18.0,  # simple lock + lining
    labour_hours=3.0,
    selling_price=140.0
)

# Bag 2: Premium bag, expensive lock + chain, sold for 200 AED
bag2 = CrochetBag(
    name="Premium Bag - 200 AED",
    yarn_cost=32.0,
    other_materials=45.0,  # premium lock + chain + lining
    labour_hours=4.0,
    selling_price=200.0
)

bag1.summary()
bag2.summary()
