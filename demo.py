import sys
from module.description import Description

if __name__ == "__main__":
    desc = Description()
    state, description = desc.init()
    print(state, description)
    if state < 0:
        sys.exit(0)

    sentence_list = [
        
        '这朵花真香呀，像蜜一样'
    ]
    state, desc_info = desc.get_all_descriptions(sentence_list)
    if desc_info['num'] == 1:
        print("是嗅觉描写")
    else:
        print("不是嗅觉描写")
