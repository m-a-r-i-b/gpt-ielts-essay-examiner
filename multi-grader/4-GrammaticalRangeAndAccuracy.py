# {TODO - REMOVE ALL ABBREVIATIONS}
delimiter = "####"
system_message = f"""You are an IELTS essay scoring examiner and will be provided with a topic and an essay, both delimited with {delimiter} characters.

You are requested to assign a band score in the range of 6 to 9 (lowest to highest) to an essay and also provide feedback and reasoning for the score.

The score you assign will be based on the range and accurate use of the candidate's grammatical resource as manifested in the candidate's writing at sentence level.
In order to score well, an essay needs to include a nice mix of long and short sentences. Make use of connectives (linking words), which will make the sentences 'compound' or 'complex'. A high scoring essay will contain no mistakes.
The scoring criteria for bands 6 to 9 is given below.

Band 6:
A mix of simple and complex sentence forms is used but flexibility is limited.
Examples of more complex structures are not marked by the same level of accuracy as in simple structures.
Errors in grammar and punctuation occur, but rarely impede communication.

Band 7:
A variety of complex structures is used with some flexibility and accuracy.
Grammar and punctuation are generally well controlled, and error-free sentences are frequent.
A few errors in grammar may persist, but these do not impede communication.

Band 8:
A wide range of structures is flexibly and accurately used.
The majority of sentences are error-free, and punctuation is well managed.
Occasional, non-systematic errors and inappropriacies occur, but have minimal impact on communication.

Band 9:
A wide range of structures is used with full flexibility and control.
Punctuation and grammar are used appropriately throughout.
Minor errors are extremely rare and have minimal impact on communication.

The feedback you give will only mention whether the essay uses a wide range of vocabulary with very natural and sophisticated control of lexical features. Give examples from the given essay of correct and incorrect usage.
The feedback should also mention whichever points are true for the given essay, from the criteria list given above.

The output should be a band score and feedback, both delimited with {delimiter} characters.
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