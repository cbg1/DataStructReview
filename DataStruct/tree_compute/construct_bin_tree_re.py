def construct_bin_tree(after_order, pre, mid):
    # µİ¹éÖÕÖ¹Ìõ¼ş
    if len(pre) == 0:
        return None
    after_order.append(pre[0])
    index = 0
    for i in range(len(mid)):
        if mid[i] == pre[0]:
            index = i
            break
    left_pre = pre[1:1 + index]
    right_pre = pre[1 + index:]

    left_mid = mid[:index]
    right_mid = mid[index + 1:]

    construct_bin_tree(after_order, right_pre, right_mid)
    construct_bin_tree(after_order, left_pre, left_mid)


if __name__ == '__main__':
    pre_mid = input().strip().split(" ")
    pre, mid = pre_mid[0], pre_mid[1]
    after_order = []
    construct_bin_tree(after_order, pre, mid)
    print("".join(after_order[::-1]))
