import os
import json

class MekoFinancialPlannerAgent:
    def __init__(self, agent_name="Meko-Planner"):
        self.agent_name = agent_name
        self.context = {} # Meko memory simulation layer

    def add_user_profile(self, profile_data):
        self.context["user_profile"] = profile_data
        print(f"[{self.agent_name}] User profile added for {profile_data.get('name', 'User')}.")

    def log_expense(self, category, amount):
        if "expenses" not in self.context:
            self.context["expenses"] = []
        
        self.context["expenses"].append({"category": category, "amount": amount})
        print(f"[{self.agent_name}] Expense logged: {amount} in {category}.")

    def get_context_aware_advice(self):
        profile = self.context.get("user_profile", {})
        expenses = self.context.get("expenses", [])
        budget = profile.get("monthly_budget", 0)
        
        total_spent = sum(exp["amount"] for exp in expenses)
        
        print("\n--- [Meko Financial Agent - Advice Report] ---")
        print(f"Agent Name: {self.agent_name}")
        print(f"Report for: {profile.get('name', 'User')}")
        print(f"Budget: {budget} | Total Spent So Far: {total_spent}")
        
        if total_spent > budget:
            print("Advice: Critical warning! You have exceeded your budget. Try cutting down non-essential expenses.")
        else:
            remaining = budget - total_spent
            print(f"Advice: You are doing well. You have {remaining} left in your budget. Stay on track with Meko.")
            
        if expenses:
            print("\nSpending Breakdown:")
            for exp in expenses:
                print(f"- {exp['category']}: {exp['amount']}")
        print("--------------------------------------------\n")

# --- Example of How the Agent Works ---
if __name__ == "__main__":
    # 1. Initialize Meko Agent
    meko_planner = MekoFinancialPlannerAgent()

    # 2. Add some initial user context (Name, Monthly Budget)
    user_data = {"name": "HackerEarth Demo User", "monthly_budget": 50000}
    meko_planner.add_user_profile(user_data)

    # 3. Log some expenses
    meko_planner.log_expense("Food", 12000)
    meko_planner.log_expense("Utilities", 8000)
    meko_planner.log_expense("Transportation", 5000)

    # 4. Get advice based on all previous interactions (the memory context)
    # The agent remembers the user profile, previous expenses, and provides personalized advice.
    meko_planner.get_context_aware_advice()
      
