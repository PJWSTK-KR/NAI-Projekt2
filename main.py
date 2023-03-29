import math
import random
import sys


def calculate(inputs: [], weights: [], threshold: float = 0):
    input_sum = 0
    for index in range(0, len(inputs)):
        input_sum += int(inputs[index]) * int(weights[index])
    if input_sum >= threshold:
        return 1
    return 0


def calculate_delta(inputs: [], weights: [], alfa: float, result: float, correct_result: float):
    new_inputs = []
    for value in inputs:
        new_inputs.append(int(value) * alfa * (correct_result - result))
    new_weights = []
    for index in range(0, len(new_inputs)):
        new_weights.append(int(weights[index]) + int(new_inputs[index]))
    return new_weights


def main():
    train_file_path, test_file_path, alfa, epoch_number = sys.argv[1:5]
    alfa = float(alfa)
    train_file = open(train_file_path, "r")
    test_file = open(test_file_path, "r")
    train_data = []
    n = 0
    for line in train_file:
        line = line.split(",")
        if len(line) == 0 or len(line) == 1:
            break
        line[len(line) - 1] = line[len(line) - 1].strip()
        train_data.append(line)
        n += 1
    weights = []
    for i in range(0, len(train_data[0]) - 1):
        weights.append(0)
    test_data = []
    for line in test_file:
        line = line.split(",")
        if len(line) == 0 or len(line) == 1:
            break
        line[len(line) - 1] = line[len(line) - 1].strip()
        test_data.append(line)
    threshold = -5
    total = len(test_data)
    for epoch in range(0, int(epoch_number)):
        for data in train_data:
            y = calculate(data[0:len(data) - 1], weights, threshold)
            if y != int(data[len(data) - 1]):
                weights = calculate_delta(data[0:len(data) - 1], weights, alfa, y, float(data[len(data) - 1]))
        random.shuffle(train_data)
        correct_count = 0
        for t_data in test_data:
            y_test = calculate(t_data[0:len(t_data) - 1], weights, threshold)
            if y_test == int(t_data[len(t_data) - 1]):
                correct_count += 1
            print("Epoch " + str(epoch) + " " + str((correct_count / float(total)) * 100) + "%")
    # while True:
    #     print("1. Własna obserwacja\n2. Obserwacje w pliku testowym\n3. Zmiana k\n4. Koniec")
    #     action = input("> ")
    #     if action == "1":
    #         print(k_nearest_neighbours(train_data, input("obserwacja>").split(","), k))
    #     elif action == "2":
    #         find_all_k_nearest_neighbours(train_data, test_data, k)
    #     elif action == "3":
    #         k = int(input("k> "))
    #         find_all_k_nearest_neighbours(train_data, test_data, k)
    #     elif action == '4':
    #         sys.exit(0)


if __name__ == "__main__":
    main()
