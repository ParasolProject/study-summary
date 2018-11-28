import re

unit = ['', '拾', '佰', '千']
sep = ['', '万', '亿', '兆']
accDigits = list('零壹贰叁肆伍陆柒捌玖')
digits = list('0123456789')
acc_dict = dict(zip(digits, accDigits))


def turn_float(num):
    if len(num) == 1:
        if num == "0":
            return "圆整"
        else:
            return acc_dict[num] + "角"
    else:
        if num[0] == "0" and num[1] == "0":
            return "圆整"
        elif num[0] == '0' and num[1] != "0":
            return acc_dict[num[1]] + "分"
        else:
            return acc_dict[num[0]] + "角" + acc_dict[num[1]] + "分"


def four_digit_block(num):
    zero_fill_counter = len(num) % 4
    num = ('0' * (4 - zero_fill_counter) + num) if zero_fill_counter != 0 else num
    block_num = len(num) // 4
    block_list = [num[4 * i:4 * (i + 1)] for i in range(block_num)]
    return block_list


def convert(num):
    block_list = four_digit_block(num)
    result = ''
    for blockIndex in range(len(block_list)):
        block = block_list[blockIndex]
        for index in range(len(block)):
            # 转换成大写财务数字，如果最大是十位那壹就省略
            if not (index == 2 and block[index] == '1' and blockIndex == 0):
                result += acc_dict[block[index]]
            # 加上单位‘千佰拾’等
            if block[index] != '0':
                result += unit[3 - index]
        # 把多个连续的零合并成一个
        result = re.sub(r'(零+)', r'零', result)
        # 去除两头的零
        result = result.strip('零')
        # 加上4位分隔单位‘万，亿’等
        result += sep[len(block_list) - blockIndex - 1]

    return result


def digit_split(num):
    digit_list = str(num).split('.')
    if len(digit_list) == 2:
        big_num = digit_list[0]
        small_num = digit_list[1]
        str1 = turn_float(small_num)
        str2 = convert(big_num)
        return str2 + str1
    else:
        big_num = digit_list[0]
        if big_num[-1] == "0":
            str3 = "圆整"
            return convert(big_num) + str3
        return convert(big_num)


if __name__ == '__main__':
    print(digit_split(2200.20))

