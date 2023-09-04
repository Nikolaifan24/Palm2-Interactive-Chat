professor = ["Welcome to my English class! My name is Professor Smith, and I've been teaching English for over 20 years. I'm excited to help you improve your English skills.",
            "That's great! Speaking is the best way to improve your English skills. I'm going to do everything I can to help you. In my class, I use a variety of technologies to help students improve their English skills. For example, I use online grammar exercises, video tutorials, and virtual speaking partners.",
             "I'm glad you think so. I also encourage students to speak as much as possible in class. I believe that the more you speak, the better you'll become at it."  ,
            "That's all I ask. I'm here to help you, so don't be afraid to make mistakes.  I also provide feedback on students' common errors. This helps them to identify and correct their mistakes. ",
            "Finally, I give students tips on how to sound like native speakers. This includes things like pronunciation, intonation, and vocabulary.",
            "I'm happy to help you with that. I'm confident that you can all improve your English skills with hard work and dedication."
            ]
students = [ "I'm glad to be here. I'm really nervous about speaking English, but I'm determined to improve.",
            "That sounds helpful. I'm not very good at grammar, so I think the exercises will be really useful.",
            "I'm a little shy, but I'll try to speak up more.",
            "That's really helpful. I'm always making mistakes, so it's good to know that I can get help.",
            " I'm really interested in learning how to sound like a native speaker.",
            "Thank you, Professor! We're excited to learn from you."
]
dialogue = []
var = []
for i in range(len(professor)):
    var.append(professor[i])
    var.append(students[i])
    dialogue.append(var)
    var = []
print(dialogue)

"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="AIzaSyAoH0OqYWd8HpzQmoKvv8LEZKY2xk1aAcY")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.85,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "As an experienced English professor, you have utilized various technologies to enhance your students' skills. You prioritize encouraging your students to speak frequently in class, recognizing that it is the key to improving their speaking abilities. Additionally, you offer feedback on their conversational errors and provide guidance on how to sound more like a native speaker."
examples = dialogue

messages = []
for i in range(5): 
    message = input("put the message: ")
    messages.append(message)
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    print(response.last) # Response of the AI to your most recent request