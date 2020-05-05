
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
    if fitsPlan(ingredients, factors, max_kcal, min_kcal, max_cup, min_cup):
      return factors
    else:
      return []


def fitsPlan(ingredients, factors, max_kcal, min_kcal, max_cup, min_cup):
  """
  Fit recipe.
  """

  kcal_avgs = {
    'fruit': 100,
    'grain': 200,
    'nuts': 800
  }

  kcals = 0
  cups = 0
  for i in range(len(ingredients)):
    kcals += kcal_avgs[ingredients[i]['list']] + factors[i]
    cups += factors[i]

  return min_kcal <= kcals <= max_kcal and min_cup <= cups <= max_cup


if __name__ == "__main__":
  ingredients = [{
    'title': 'oatmeal',
    'list': 'grain'
  }, {
    'title': 'fruit',
    'list': 'fruit'
  }, {
    'title': 'peanuts',
    'list': 'nuts'
  }]
  meals = 1

  meal_plans = mealPlans(ingredients, meals)
  print(meal_plans)
