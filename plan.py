
def mealPlans(ingredients, recipe = []):
  """
  Make meal plans.
  """

  servings = {
    'start': 0,
    'end': 3,
    'step': 0.25,
    # 'kcal': {
    #   'max': 900,
    #   'min': 850
    # },
    'kcal': { # 70% rice, 30% dressing
      'max': 630,
      'min': 595
    },
    'cup': {
      'max': 3,
      'min': 2
    }
  }

  # Mutate ingredients
  if len(recipe) == 0:
    recipe += [ingredients[0]]
  if 'cups' not in recipe[-1]:
    recipe[-1]['cups'] = servings['start']

  # Recursion base cases
  if recipe[-1]['cups'] > servings['end']:
    return []

  recipe_left = [r for r in recipe]
  recipe_left[-1]['cups'] += servings['step']
  if len(recipe) < len(ingredients):
    recipe_right = [r for r in recipe]
    recipe_right += [ingredients[len(recipe_right)]]
    return mealPlans(ingredients, recipe_left) + mealPlans(ingredients, recipe_right)
  else:
    if fitsPlan(recipe):
      return recipe + mealPlans(ingredients, recipe_left)
    else:
      return mealPlans(ingredients, recipe_left)


# def fitsPlan(ingredients, factors):
def fitsPlan(recipe):
  """
  Fit recipe.
  """

  servings = {
    'start': 0,
    'end': 3,
    'step': 0.25,
    # 'kcal': {
    #   'max': 900,
    #   'min': 850
    # },
    'kcal': { # 70% rice, 30% dressing
      'max': 630,
      'min': 595
    },
    'cup': {
      'max': 3,
      'min': 2
    }
  }
  kcal_avgs = { # kcal / cup
    'beans': 200,
    'fruit': 100,
    'grain': 200,
    'nuts': 800,
    'oil': 1600,
    'spices': 0,
    'vegetables': 100
  }

  kcal = 0
  cup = 0
  for ingredient in recipe:
    kcal += kcal_avgs[ingredient['type']] * ingredient['cups']
    cup += ingredient['cups']

  return servings['kcal']['min'] <= kcal <= servings['kcal']['max'] and servings['cup']['min'] <= cup <= servings['cup']['max']


if __name__ == '__main__':
  # ingredients = [{ # Breakfast
  #   'title': 'fruit',
  #   'type': 'fruit'
  # }, {
  #   'title': 'oatmeal',
  #   'type': 'grain'
  # }, {
  #   'title': 'peanuts',
  #   'type': 'nuts'
  # }]
  ingredients = [{ # Lunch
    'title': 'brown rice',
    'type': 'grain'
  }, {
    'title': 'vegetables',
    'type': 'vegetables'
  }, {
    'title': 'olive oil',
    'type': 'oil'
  }, {
    'title': 'beans',
    'type': 'beans'
  }]

  meal_plans = mealPlans(ingredients)
  size = len(ingredients)
  meal_plans = [meal_plans[i:i + size] for i in range(0, len(meal_plans), size)]
  print('meal_plans', meal_plans)
