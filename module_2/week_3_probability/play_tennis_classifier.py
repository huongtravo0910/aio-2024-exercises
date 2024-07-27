import numpy as np


def create_train_data():
    data = [
        ['Sunny', 'Hot', 'High', 'Weak', 'no'],
        ['Sunny', 'Hot', 'High', 'Strong', 'no'],
        ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
        ['Rain', 'Mild', 'High', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
        ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
        ['Overcast', 'Mild', 'High', 'Weak', 'no'],
        ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
        ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    return np.array(data)


train_data = create_train_data()
# print(train_data)


def compute_prior_probability(train_data):
    prior_probability = {}
    x = 0
    y = 0

    for list in train_data:
        if (list[len(list) - 1] == 'no'):
            x += 1
        else:
            y += 1

    prior_probability['no'] = x/len(train_data)
    prior_probability['yes'] = y/len(train_data)
    return prior_probability


prior_probablity = compute_prior_probability(train_data)
print("P( play tennis = No)", prior_probablity['no'])
print("P( play tennis = Yes)", prior_probablity['yes'])


def compute_conditional_probability(train_data):
    y_unique = ["no", "yes"]
    conditional_probability = []
    list_x_name = []
    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = {}
        for x in x_unique:
            for y in y_unique:
                num_x_and_y = np.sum(
                    (train_data[:, i] == x) & (train_data[:, -1] == y))
                num_y = np.sum(train_data[:, -1] == y)
                x_conditional_probability[(
                    x, y)] = num_x_and_y / num_y if num_y != 0 else 0

        conditional_probability.append(x_conditional_probability)

    return conditional_probability, list_x_name


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


def get_index_from_value(feature_name, list_features):
    # Tìm vị trí của feature_name trong list_features và trả về index
    index = np.nonzero(np.array(list_features) == feature_name)[0][0]
    return index


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)

train_data = create_train_data()
conditional_probability, list_x_name = compute_conditional_probability(
    train_data)
# Compute P(" Outlook "=" Sunny "| Play Tennis "=" Yes ")
print('conditional_probability',
      conditional_probability[0][np.str_('Sunny'), 'no'])


def train_naive_bayes(train_data):
    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probability(train_data)
    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(event, list_x_name, prior_probability, conditional_probability):
    # X: [Outlook, Temperature, Humidity, Wind]
    x1 = get_index_from_value(event[0], list_x_name[0])
    x2 = get_index_from_value(event[1], list_x_name[1])
    x3 = get_index_from_value(event[2], list_x_name[2])
    x4 = get_index_from_value(event[3], list_x_name[3])

    # Initialize probabilities
    p0 = prior_probability['no']
    p1 = prior_probability['yes']

    # Calculate conditional probabilities
    p0 *= conditional_probability[0][(list_x_name[0][x1], 'no')]
    p0 *= conditional_probability[1][(list_x_name[1][x2], 'no')]
    p0 *= conditional_probability[2][(list_x_name[2][x3], 'no')]
    p0 *= conditional_probability[3][(list_x_name[3][x4], 'no')]

    p1 *= conditional_probability[0][(list_x_name[0][x1], 'yes')]
    p1 *= conditional_probability[1][(list_x_name[1][x2], 'yes')]
    p1 *= conditional_probability[2][(list_x_name[2][x3], 'yes')]
    p1 *= conditional_probability[3][(list_x_name[3][x4], 'yes')]

    # Compare probabilities
    if p0 > p1:
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']

data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(X, list_x_name, prior_probability,
                              conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
