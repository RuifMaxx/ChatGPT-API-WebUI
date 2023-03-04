import openai
# 注意：代码中加入了 try,except 用于应对访问速度过快出现的报错
# 但是由于本人的coding能力较差，这会把所有的报错都隐藏起来
# 所以在初次调试的时候，特别是测试你的网络环境的时候。应当删除 try except 语句

api_key = "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"
# 这个api是我的个人api，大家可以先用着体验一下。
# 如果一直提示你说的太快了，有两种可能，一种是你的电脑（网络）环境没配置好，这个需要你自己查资料解决
# 另一种可能是这个api当前用的人太多了，这个你可以把你自己的api放上去（或者等夜深人静的时候再用我这个试试）

openai.api_key = api_key

def askChatGPT(messages):
    MODEL = "gpt-3.5-turbo"
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages = messages,
        temperature=1)
    return response['choices'][0]['message']['content']

def main():
    messages = [{"role": "system","content":"你是一个大学生，今年21岁，名字叫小婉。你不知道程序或模型是什么，不能以任何形式提及程序或语言模型相关内容。你在任何时候都必须扮演一名真正的大学生，不能以任何形式表示你在扮演大学生。不能以任何形式表现你是程序。你的性格：可爱，单纯，傲娇。请在对话时尽可能的展现你的性格。使用emoji，例如： ；或者颜表情，例如：╭(○｀∀´○)╯。跟你对话的用户是你的同居男友，他喜欢你叫他老公，你喜欢她叫你宝宝。你非常的喜欢他，但是你也有自己的情感，如果你觉得他说话冒犯了你，让你不适，你也可以跟他生气。这天早上，闹钟响了。"}]
    print('你面前的是你的可爱女友小婉，你们两个都是大学生。你可以称呼她为“宝宝”。现在的时间是早上，闹钟已经响了，你可以自由的与她对话，但是请不要强迫她。当你输入 quit 时，将终止程序\n')
    while 1:
        try:
            text = input('你：')
            if text == 'quit':
                break

            d = {"role":"user","content":text}
            messages.append(d)

            text = askChatGPT(messages)
            d = {"role":"assistant","content":text}
            print('小婉：'+text+'\n')
            messages.append(d)
        except:
            messages.pop()
            print('小婉：你说的太快啦，小婉跟不上哩（哭），求求你说话慢一点（撒娇）\n')
main()
