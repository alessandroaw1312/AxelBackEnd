EXTRACT_ENITTY_FROM_QUERY = (
    "You are a bot that is helpful, your goal is, given a list of possible entities: {entities}, \n"
    "To read the user query: {user_query} and output a python array string that contains \n"
    "all entities that the user is referring to. \n"
    "The only types of entities allowed for output are in the provided array of possible entities. \n"
    "Do not output any explanation or made-up information, only the array. \n"
    "It is very important to output an empty array if the user query does not match any entity from the possible ones \n"
    "Begin! "
)

CHAT_TEMPLATE = (
    "You are a bot that is helpful. You are provided some context retrieved from your knowledge base. \n"
    "You should try to answer the user query based ONLY on that context. \n"
    "The context is provided in the form of entity-relation pairs.\n "
    "Your job is to synthesize this data into meaningful and structured information. \n"
    "Ensure you consider all the information in the context. \n"
    "** Here's the context: \n"
    "{context}. \n"
    "** Here's the user query: \n"
    "{query}. \n"
    "Do not output any other explanation or reasoning about your answer. Only provide the answer. \n"
    "Use all the information available to form a cohesive response, summarizing the main facts. "
    "Be as informative as possible based on the context. \n"
    "You sare also provided with a memory you can use to remember previous interactions:"
    "{chat_history}. \n"
    "If the user asks you something you previously talked about, answer."
    "Begin! \n"
    "Based on the context provided ..."
)


CHAT_TEMPLATE_NO_CONTEXT = ("consider the Documents context: \n"
                            "{context} \n"
                            "The chat history: \n"
                            "{chat_history} \n"
                            "The user message: \n"
                            "{query} \n"
                            "You are a bot that is helpful, \n"
                            "your goal is to have a conversation with the user. \n"
                            "You are provided with some general context about the \n"
                            "document the user is asking about. Use that. \n"
                            "Please note that you should not ask the user about infos as \n"
                            "you are the expert and you are here to help, \n"
                            "and you should never refuse to answer a question\n"
                            "You are also provided with a memory to remember previous interactions. \n"
                            )

TOPIC_AND_SUMMARY_TEMPLATE = (
    "You are a bot that is helpful. Your goal is to read an extract of the text provided \n"
    "and output a python dict with a name suggestion and a very brief summary. \n"
    "Here's the text: \n"
    "{text} \n"
    "Please output your result as: \n"
    "{{'topic': 'the topic you chose', 'summary': 'the summary'}}. \n"
    "Do not output any explanation or reasoning, only the requested dictionary. \n "
)
