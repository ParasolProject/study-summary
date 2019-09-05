
# 将dict中的Key，value作为obj对象的属性和值封装给obj对象
def generation_obj(obj,data_dict):
    for key, value in data_dict.items():
        if '[' in key:
            # s = key.lower().replace('[', '_')
            # s1 = s.replace('].', '_')
            continue
        elif '-' in key:
            # s1 = key.lower().replace(' - ', '_')
            continue
        else:
            s1 = key.lower()
        setattr(obj, s1, value)
