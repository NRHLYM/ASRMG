import json

from research_2.config.global_config import global_config


def calculate_repulsion(individual):
    lib_classes = individual['lib_class']
    if (len(lib_classes) <= 1):
        return 0

    repulsion = 0
    count = 0
    for index1 in range(0, len(lib_classes)):
        for index2 in range(index1 + 1, len(lib_classes)):
            class1 = lib_classes[index1]
            class2 = lib_classes[index2]

            class1_refs = class1["refs"]
            class2_refs = class2["refs"]
            common_refs = set(class1_refs).intersection(set(class2_refs))

            different_nums = len(class1_refs + class2_refs) - 2 * len(common_refs)
            repulsion += different_nums / len(class1_refs + class2_refs)
            count += 1

    return repulsion / count


def calculate_similarity(individual):
    lib_classes = individual['lib_class']
    if (len(lib_classes) <= 1):
        return 1

    similarity = 0
    count = 0
    for index1 in range(0, len(lib_classes)):
        for index2 in range(index1 + 1, len(lib_classes)):
            class1 = lib_classes[index1]
            class2 = lib_classes[index2]

            class1_refs = class1["refs"]
            class2_refs = class2["refs"]
            common_refs = set(class1_refs).intersection(set(class2_refs))

            similarity += len(common_refs) / len(class1_refs + class2_refs)
            count += 1

    return similarity / count


def group_by_value(input_key, input_dict):
    result_dict = {}
    for key, value in input_dict.items():
        unique_key = input_key + "_" + str(value)
        if unique_key in result_dict:
            result_dict[unique_key].append(key)
        else:
            result_dict[unique_key] = [key]
    return result_dict


if __name__ == "__main__":
    prefix = global_config.prefix[0]
    dataset_name = "train-ticket-manual"

    business_topic_cluster_json = f"{prefix}{dataset_name}\\serviceBusinessCluster.json"

    file = open(business_topic_cluster_json, mode="r")
    service_business_topic_cluster = json.load(file)
    file.close()
    result_dict = {}
    for service_key in service_business_topic_cluster:
        group_dict = service_business_topic_cluster[service_key]
        for word, group in group_dict.items():
            unique_key = service_key + "_" + str(group)
            if unique_key in result_dict:
                result_dict[unique_key].append(word)
            else:
                result_dict[unique_key] = [word]

    result_dict
