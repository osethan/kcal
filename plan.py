
def mealPlans(ingredients, meals, factors = [], start = 0, end = 2, step = 1/8, max_kcal = 900, min_kcal = 850, max_cup = 3, min_cup = 2):
  """
  Make meal plans.
  """

  # Recursion base cases
  if factors[-1] > max_cup:
    return []
  if len(factors) > len(ingredients):
    return []

  if len(factors) < len(ingredients):
    factors_left = [f for f in factors]
    factors_left[-1] += step
    factors_right = [f for f in factors]
    factors_right += [start]
    return mealPlans(ingredients, meals, factors_left, start, end, step, max_kcal, min_kcal, max_cup, min_cup) + mealPlans(ingredients, meals, factors_right, start, end, step, max_kcal, min_kcal, max_cup, min_cup)
  else:
    if fitsPlan(factors, max_kcal, min_kcal, max_cup, min_cup):
      return factors
    else:
      return []
