
def mealPlans(ingredients, meals, factors = [0]):
  """
  Make meal plans.
  """

  # print('factors', factors)
  servings = {
    'start': 0,
    'end': 1,
    'step': 0.25,
    'kcal': {
      'max': 900,
      'min': 850
    },
    'cup': {
      'max': 3,
      'min': 2
    }
  }

  # Recursion base cases
  if factors[-1] > servings['end']:
    return []
  if len(factors) > len(ingredients):
    return []

  # print('factors', factors)
  factors_left = [f for f in factors]
  factors_left[-1] += servings['step']
  factors_right = [f for f in factors]
  factors_right += [servings['start']]
  meal_plans = mealPlans(ingredients, meals, factors_left) + mealPlans(ingredients, meals, factors_right)
  if len(factors) < len(ingredients):
    return meal_plans
  else:
    if fitsPlan(ingredients, factors):
      return factors + meal_plans
    else:
      return meal_plans


def fitsPlan(ingredients, factors):
  """
  Fit recipe.
  """

  servings = {
    'start': 0,
    'end': 1,
    'step': 1/4,
    'kcal': {
      'max': 900,
      'min': 850
    },
    'cup': {
      'max': 3,
      'min': 2
    }
  }
  kcal_avgs = {
    'fruit': 100,
    'grain': 200,
    'nuts': 800
  }

  kcals = 0
  cups = 0
  for i in range(len(ingredients)):
    kcals += kcal_avgs[ingredients[i]['list']] * factors[i]
    cups += factors[i]

  return servings['kcal']['min'] <= kcals <= servings['kcal']['max'] and servings['cup']['min'] <= cups <= servings['cup']['max']


if __name__ == '__main__':
  ingredients = [{
    'title': 'fruit',
    'list': 'fruit'
  }, {
    'title': 'oatmeal',
    'list': 'grain'
  }, {
    'title': 'peanuts',
    'list': 'nuts'
  }]
  meals = 1

  meal_plans = mealPlans(ingredients, meals)
  size = len(ingredients)
  meal_plans = [meal_plans[i:i + size] for i in range(0, len(meal_plans), size)]
  print('meal_plans', meal_plans)
