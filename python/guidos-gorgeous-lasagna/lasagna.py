EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """"
    Return expected_bake_time value
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """"
    Return the multiply for expected_bake_time per layer
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers,  elapsed_bake_time):
    """
    Return elapsed cooking time.
    This function takes two numbers representing the number of layers & the time already
    spent baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
