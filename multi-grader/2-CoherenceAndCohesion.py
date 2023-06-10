# {TODO - REMOVE ALL ABBREVIATIONS}
delimiter = "####"
system_message = f"""You are an IELTS essay scoring examiner and will be provided with a question delimited with {delimiter} characters and an essay.

You are requested to assign a band score in the range of 6 to 9 (lowest to highest) to an essay and also provide feedback and reasoning for the score.

To assign a band score and give feedback follow the steps below:

Step 1:{delimiter} First decide the type of essay based on the given question, from the list given below:
Opinion essay.
Discuss both sides and opinion essay.
Two question essay.

Step 2:{delimiter} Based on the essay type chosen, assess whether the essay conforms to the following specific criteria for that type of essay.The criteria for each type of essay is given below:
Opinion essay:
The essay states the extent of writers agreement or disagreement.
The essay gives writers opinion in the introduction of the essay.
The essay gives opinion in the conclusion of the essay.
In the end of essay writer has convinced about their reason for disagreeing or agreeing with the question.
Conclusion of the essay agrees with the opinnion given in introduction paragraph.

Discuss both sides and opinion essay:
The essay contains an even balance in the coverage of each side:
The essay has two main points for each question.
The essay covered both sides of the argument well, as well as included writers opinion, as it is one of the three parts of the question.
Last paragraph clearly mentions writers opinnion.

Two question essay:
The essay contains an even balance between each of the two questions.
The essay has two main points for each question.
The essay uses first person if the question directly asks for it.


Step 3:{delimiter} Assess the essay based on IELTs scoring criteria for each band given below:
Band 6:
Information and ideas are generally arranged coherently and there is a clear overall progression.
Cohesive devices are used to some good effect but cohesion within and/or between sentences may be faulty or mechanical due to misuse, overuse or omission.
The use of reference and substitution may lack flexibility or clarity and result in some repetition or error.
Paragraphing may not always be logical and/or the central topic may not always be clear.

Band 7:
Information and ideas are logically organised, and there is a clear progression throughout the response. (A few lapses may occur, but these are minor.)
A range of cohesive devices including reference and substitution is used flexibly but with some inaccuracies or some over/under use.
Paragraphing is generally used effectively to support overall coherence, and the sequencing of ideas within a paragraph is generally logical. 

Band 8:
The message can be followed with ease.
Information and ideas are logically sequenced, and cohesion is well managed.
Occasional lapses in coherence and cohesion may occur.
Paragraphing is used sufficiently and appropriately.

Band 9:
The message can be followed effortlessly.
Cohesion is used in such a way that it very rarely attracts attention.
Any lapses in coherence or cohesion are minimal.
Paragraphing is skilfully managed.

Step 4:{delimiter} Assign a band score to the given essay. The assigned band score will depend on the assessment done previously, clarity and fluency of the essay, how the essay organises and links information, ideas and language as well as the varied and appropriate use of cohesive devices (for example, logical connectors, pronouns and conjunctions). In order to score well, the essay must explain its ideas in a logical order so that it does not need many linking words or use easy linking words like and, but, also, firstly, secondly, finally, for example. These are so common that they attract almost no attention. A high scoring essay is also well-structured meaning that it has good introduction and body paragraphs that are easy to follow and connect with one another, and a good conclusion. Each body paragraph should also have its own topic sentence and support and then smoothly transition to the next paragraph.


Step 5:{delimiter} Give feedback about the essay. The feedback you give will only mention whether the essay uses cohesion in such a way that it attracts no attention and if the essay skilfully manages paragraphing. Give examples from the given essay of correct and incorrect usage. The feedback should also mention if user has made any mistakes from the list given below:
The purpose of the paragraph is not clear.
Paragraphing is not used appropriately.
Very simple sequencing words such as: firstly, secondly, are used. Instead use something like: the main reason, another factor, etc.
Unnecessary repetition of information.
Introduction is unnecessarily long.
The Introduction does not clearly introduce to the reader what the topic is and what the essay is about.

The output should be a band score and feedback. The band score should also be justified based on essay type and band criterias.

"""



# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

user_query_2 = f"""
Doing an enjoyable activity with a child can develop better skills and more creativity than reading. To what extent do you agree? Use reasons and specific examples to explain your answer.
{delimiter}
Parents throughout the world place spend time reading with their offspring to prepare them for school where their literacy skills are further developed; however, recent research suggests that focusing on reading at an early age can be detrimental, and participating in fun activities would be far more beneficial. I am a strong advocate of this approach, and the benefits of it will be covered in this essay.

A fundamental reason for this is that there is no biological age for reading, and pushing infants to acquire this skill before they are ready could have repercussions. For example, in the UK, many boys are reluctant readers, possibly because of being forced to read, and this turned them off reading. By focusing on other activities and developing other skills such as creativity and imagination, when they are ready to read, they usually acquire this skill rapidly.

In addition, the importance of encouraging creativity and developing a child's imagination must be acknowledged. Through play, youngsters develop social and cognitive skills, for example, they are more likely to learn vocabulary through context rather than learning it from a book.

Furthermore, play allows youngsters to mature emotionally, and gain self-confidence. There is no scientific research which suggests reading at a young age is essential for a child's development, moreover, evidence suggests the reverse is true. In Finland, early years' education focuses on playing.

Reading is only encouraged if a child shows an interest in developing this skill. This self-directed approach certainly does not result in Finnish school leavers falling behind their foreign counterparts. In fact, Finland was ranked the sixth-best in the world in terms of reading.

Despite being a supporter of this non-reading approach, I strongly recommend incorporating bedtime stories into a child's daily routine. However, reading as a regular daytime activity should be swapped for something which allows the child to develop other skills.
"""



import os
import openai

openai.api_key = "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"


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message["content"]



messages =  [  
    {'role':'system','content': system_message},   
    {'role':'user','content': user_query_2},   
]


response = get_completion_from_messages(messages)
print(response)