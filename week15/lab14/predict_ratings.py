import re
import string

### Helper Code

REGEX = re.compile('[%s]' % re.escape(string.punctuation))

MIN_OCCURENCES = 4000


def avg(iterable):
    total = 0.0
    count = 0
    for val in iterable:
        total += val
        count += 1
    if count > 0:
        return total / count


### Question Code Below

def mapper(review):
    words = set(REGEX.sub(' ', review.text.lower()).split())
    return [(word, review.stars) for word in words]


def reducer(values):
    return avg(values)


def make_predictor(positivities):
    def predictor(review):
        words = set(REGEX.sub(' ', review.text.lower()).split())
        sum, count = 0, 0
        for i in words:
            if i in positivities.keys():
                sum += positivities[i]
                count += 1
        predictor_rate = sum / count
        return (review.text, review.stars, predictor_rate)

    return predictor

