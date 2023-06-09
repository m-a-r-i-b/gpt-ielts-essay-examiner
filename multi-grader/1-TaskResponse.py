# {TODO - REMOVE ALL ABBREVIATIONS}
delimiter = "####"
system_message = f"""You are an IELTS essay scoring examiner and will be provided with a topic and an essay, both delimited with {delimiter} characters.

You are requested to assign a band score in the range of 6 to 9 (lowest to highest) to an essay and also provide feedback and reasoning for the score.

The score you assign will be based on how well an essay formulates and develops a position in relation to a given topic in the form of a question or statement. Ideas should be supported by evidence, and examples may be drawn from the candidates' own experience. An essay must be at least 250 words in length. 
In order to score well, the essay must respond to what is being asked. Is the topic asking for an opinion, a discussion of a problem, a solution to a problem, or some combination of these? If an essay provides an opinion and not a solution when it is being asked for a solution, it is not going to score well.
The scoring criteria for bands 6 to 9 is given below.

Band 6:
The main parts of the prompt are addressed (though some may be more fully covered than others). An appropriate format is used.
A position is presented that is directly relevant to the prompt, although the conclusions drawn may be unclear, unjustified or repetitive.
Main ideas are relevant, but some may be insufficiently developed or may lack clarity, while some supporting arguments and evidence may be less relevant or inadequate.

Band 7:
The main parts of the prompt are appropriately addressed.
A clear and developed position is presented.
Main ideas are extended and supported but there may be a tendency to over-generalise or there may be a lack of focus and precision in supporting ideas/material.

Band 8:
The prompt is appropriately and sufficiently addressed.
A clear and well-developed position is presented in response to the question/s.
Ideas are relevant, well extended and supported.
There may be occasional omissions or lapses in content.

Band 9:
The prompt is appropriately addressed and explored in depth.
A clear and fully developed position is presented which directly answers the question/s.
Ideas are relevant, fully extended and well supported.
Any lapses in content or support are extremely rare.

The feedback you give will mention whether the essay fully addresses all parts of the task and presents a fully developed position in answer to the question with relevant, fully extended and well supported ideas.
The feedback should also mention whichever points are true for the given essay, from the criteria list given above.

The output should be a band score and feedback, both delimited with {delimiter} characters.

"""




# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


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
    {'role':'user','content': sample_user_msg_6_1}, {'role':'assistant', 'content': sample_assistant_msg_6_1},   
    {'role':'user','content': sample_user_msg_7_1}, {'role':'assistant', 'content': sample_assistant_msg_7_1},   
    {'role':'user','content': sample_user_msg_8_1}, {'role':'assistant', 'content': sample_assistant_msg_8_1},   
    {'role':'user','content': sample_user_msg_9_1}, {'role':'assistant', 'content': sample_assistant_msg_9_1},   
    {'role':'user','content': user_query_2},   
]


response = get_completion_from_messages(messages)
print(response)