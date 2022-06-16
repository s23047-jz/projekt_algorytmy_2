data = {}
done_item = {}
routes = {}


# I didn't use heap sort because sorted works the same and doesn't take up that much code space
# And I didn't want to modify it.

def set_text_file_to_string():
    # read text from file and convert into string
    text = ""
    with open('text_file.txt', 'r') as file:
        text = file.read().rstrip()

    return text


def read_text(text):
    # read whole text
    for character in text.replace('\r', '').replace('\n', ''):
        if character in data:
            data[character]['counts'] += 1
        else:
            data[character] = {'counts': 1}
    sorted_array = sorted(data, key=lambda x: data[x]['counts'], reverse=True)
    return sorted_array


def merge_items(array):
    # take first and second item from array and merge them into one item
    # next we send deleted items to another array to build a tree with this array
    while len(array) != 1:
        first_item = array.pop()
        second_item = array.pop()
        first_item_value = data[first_item]['counts']
        second_item_value = data[second_item]['counts']
        merged_items_value = first_item_value + second_item_value
        done_item[first_item], done_item[second_item] = data[first_item], data[second_item]
        del data[first_item], data[second_item]
        data[str(first_item) + str(second_item)] = {'counts': merged_items_value, 'left': first_item,
                                                    'right': second_item}
        array = sorted(data, key=lambda x: data[x]['counts'], reverse=True)
        done_item[list(data.keys())[0]] = list(data.values())[0]

    return array


def tree(node, char, route):
    # create tree
    if 'left' in done_item[node]:
        if char in done_item[node]['left']:
            new_route = route + '0'
            tree(done_item[node]['left'], char, new_route)
    if 'right' in done_item[node]:
        if char in done_item[node]['right']:
            new_route = route + '1'
            tree(done_item[node]['right'], char, new_route)
    # without this we got KeyError
    if 'left' not in done_item[node]:
        if 'right' not in done_item[node]:
            routes[char] = route


def create_root_node(text):
    encoded_text = ""
    root_node = list(data.keys())[0]
    for char in root_node:
        tree(root_node, char, '')

    for char in text.replace('\r', '').replace('\n', ''):
        encoded_text += routes[char]

    # print('\n Routes: ', routes)
    # print('\n \n: ', encoded_text)

    # write to files
    with open('text_file.bin', 'wb') as f:
        f.write(str.encode(encoded_text))
        f.close()

    with open('text_file_compressed.txt', 'w') as f:
        f.write(str(routes))
        f.close()


def main():
    text = set_text_file_to_string()
    sorted_array = read_text(text)
    merge_items(sorted_array)
    create_root_node(text)


main()
