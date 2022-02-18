def find_neareset(paragraph):
    word_to_latest_index, min_distance = {}, float("inf")

    for i, word in enumerate(paragraph):
        if word in word_to_latest_index:
            difference = i - word_to_latest_index[word]
            # if difference < min_distance:
            #     min_distance = difference
            min_distance = min(difference, min_distance)

        word_to_latest_index[word] = i

    return min_distance if min_distance != float("inf") else -1


paragraph = "all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no"
print(find_neareset(paragraph))
