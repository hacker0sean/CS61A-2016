"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    i, sum, pigout = 0, 0, False
    numone = 0
    while i < num_rolls:
        k = dice()
        if k == 1:
            numone += 1
            pigout = True
        else:
            sum += k
        i += 1
    if pigout:
        return numone
    else:
        return sum
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    return max(opponent_score // 10, opponent_score % 10) + 1
    # END PROBLEM 2


# Write your prime functions here!
def isPrime(n):
    if n == 1 or n == 0:
        return False
    count = 0
    for i in range(n):
        if i == 0 or i == 1:
            continue
        if n % i == 0:
            break
    if i == n - 1:
        return True
    else:
        return False


def nextPrime(n):
    while True:
        n = n + 1
        if isPrime(n):
            return n


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    if num_rolls == 0:
        sum = free_bacon(opponent_score)
    else:
        sum = roll_dice(num_rolls, dice)
    if isPrime(sum):
        sum = nextPrime(sum)
    if sum < 25 - num_rolls:
        return sum
    else:
        return 25 - num_rolls

    # END PROBLEM 2


take_turn(2, 0, make_test_dice(4, 6, 1))


def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""

    def rerolled():
        # BEGIN PROBLEM 3
        count = 0
        while True:
            roll = roll_dice(1, dice)
            if roll % 2 == 1 and count == 0:
                count = 1
                continue
            if roll % 2 == 1 and count == 1:
                count = 0
                return roll
            if roll % 2 == 0:
                return roll
        # END PROBLEM 3

    return rerolled


test_dice = reroll(make_test_dice(2, 4, 6))
test_dice()


def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    # BEGIN PROBLEM 4
    if dice_swapped == False:
        dice = six_sided
    if dice_swapped == True:
        dice = four_sided
    # END PROBLEM 4
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    # dice = select_dice(score0, score1, dice_swapped)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        # dice = select_dice(score0, score1, dice_swapped)
        if player == 0:
            score0_times = strategy0(score0, score1)
            if score0_times == -1:
                score0_add = 1
                dice_swapped = not dice_swapped
            dice = select_dice(score0, score1, dice_swapped)
            if score0_times != -1:
                score0_add = take_turn(score0_times, score1, dice)
            score0 = score0 + score0_add
            if score0 == 2 * score1 or score1 == 2 * score0:
                score0, score1 = score1, score0
            player = other(player)
            continue
        if player == 1:
            score1_times = strategy1(score1, score0)
            if score1_times == -1:
                score1_add = 1
                dice_swapped = not dice_swapped
            dice = select_dice(score1, score0, dice_swapped)
            if score1_times != -1:
                score1_add = take_turn(score1_times, score0, dice)
            score1 = score1 + score1_add
            if score0 == 2 * score1 or score1 == 2 * score0:
                score0, score1 = score1, score0
            player = other(player)

    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """

    def strategy(score, opponent_score):
        return n

    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    try:
        for i in range(goal):
            for j in range(goal):
                check_strategy_roll(i, j, strategy(i, j))
    except:
        raise AssertionError
    return None
    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    result = 0
    temp = num_samples
    def average_roll_dice(*args):
        nonlocal temp
        nonlocal result
        while temp > 0:
            result = result + fn(*args)
            temp = temp - 1
        return (result / num_samples)
    return average_roll_dice
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    max_roll = 0
    average_score = 0
    for i in range(1, 11):
        average = make_averaged(roll_dice, num_samples)
        temp = average(i, dice)
        if temp >= average_score:
            max_roll = i
            average_score = temp
    return max_roll
    # END PROBLEM 8

def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(4) win rate:', average_win_rate(always_roll(4)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True:  # Change to True to test swap_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    scor = free_bacon(opponent_score)
    if isPrime(scor):
        scor = nextPrime(scor)
    if scor >= margin:
        return 0
    else:
        return num_rolls
    # END PROBLEM 9


check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    "*** REPLACE THIS LINE ***"
    if score * 2 < opponent_score and opponent_score % 2 != 1:
        return 0
    elif bacon_strategy(score, opponent_score, margin, num_rolls) == 0:
        return 0
    else:
        return num_rolls
    # END PROBLEM 10


check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    *** YOUR DESCRIPTION HERE ***
    The program starts out by rolling -1 dice and taking advantage of the
    pork chop roll. By rolling -1 and converting the dice to 4 sided, the
    strategy limits the maximum and average amount of points the opponent could
    potentially receive. The always_roll strategy also does not have the
    ability to swap the dice settings back.
    The next segment of code deals with edge cases and attempts to force
    favorable rolls. The reason for optimal roll is due to the following:
    (When Pigs Fly)
    Rolls       Maximum Possible Score          Average Dice Value Needed
    10          25 - 10 = 15                    1.5
    7           25 - 7 = 18                     2.57
    4           25 - 4 = 21                     5.25
    Four rolls seems to be optimal b/c while the game is mostly played using
    the four sided dice and therefore cannot achieve the average dice value, the
    risk of rolling a one is minimized while eliminating any possibility of the
    maximum score rule cutting off the raw roll value.

    rollZero is a temporary variable that represents the points you'd receive
    if you rolled a zero that turn. The first conditional checks if score is
    free bacon points away from winning, and then uses free bacon to ensure a
    win. The following conditionals test for swine swap and hog wild, and the
    conditionals are meant to either force favorable and avoid unfavorable
    swaps.
    The last set of conditionals deal with general strategy, in the case that
    none of the edge case opportunities are presented. If I am currently in the
    lead, if my score is greater than 75, I try to hinder the opponent by
    changing up the type of dice that is used if I cannot acheve a score
    higher than 2. Otherwise, I return a swap strategy that determines whether
    I'm rolling the defaultRoll value unless I can achieve a value of 7, which
    is a more conservative value than the same default swap strategy in the
    case I'm behind (margin is 11 instead of 7). Finally, the last return
    statement is only called if the scores are equal, in which I roll 4
    in an attempt to break the tie.
    """
    # BEGIN PROBLEM 11
    if score == 0:
        return -1

    defaultRoll = 4
    rollZero = take_turn(0, opponent_score)
    # Conditional that tries to close out game efficiently with hog wild
    if score + rollZero >= 100:
        return 0
    # following conditionals check if hog wild and swine swap strategies are
    # available and whether I'm on the favorable or unfavorable end of the deal
    if (score + rollZero) * 2 == opponent_score:
        return 0
    if opponent_score * 2 == score - 1:
        if rollZero > 1:
            return 0
    if (score + opponent_score) % 7 == 0:
        return defaultRoll + 2
    if rollZero > defaultRoll + 2:
        return 0

    # If I am currently in the lead
    if score > opponent_score:
        if score > 75:
            # If the game is almost ending because scores are high
            return swap_strategy(score, opponent_score, 2, -1)
        else:
            # default strategy
            return swap_strategy(score, opponent_score, 7, defaultRoll)
    # If I am currently behind
    if score < opponent_score:
        # margin is greater than lead default strategy for more aggressive approach
        return swap_strategy(score, opponent_score, 11, defaultRoll)
    return defaultRoll
    # END PROBLEM 11


check_strategy(final_strategy)
run_experiments()
##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()


