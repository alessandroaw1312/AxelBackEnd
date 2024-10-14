import json
import time

from BE.src.services.chat import create_summarization_chain
from BE.src.services.hf_triplets import generate_triplets
from BE.src.services.make_graph import make_graph


def get_execution_time(start_time):
    # End time
    end_time = time.time()

    # Calculate execution time
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.6f} seconds")


def generate_kg(text, user_id=None, topic=None, summary=None):
    print(f"Building new graph from text: {text}")
    if topic is None and summary is None:
        topic, summary = produce_topic_and_summary(text)
    triplets = generate_triplets(text)
    graph = make_graph(text, triplets, topic, summary, user_id)
    return graph


def produce_topic_and_summary(text):
    chain = create_summarization_chain()
    llm_result = chain.invoke({"text": text})
    print("+++ GOT LLM RESULT", llm_result)
    processed_res = process_llm_response(llm_result)
    try:
        topic = processed_res['topic']
        summary = processed_res['summary']
        return topic, summary
    except KeyError as e:
        print(f"ERROR EXTRACTING TOPIC AND SUMMARY {e}")
        return None, None


def process_llm_response(llm_res):
    try:
        cleaned_string = extract_inner_content(llm_res['text'])
        loaded_result = json.loads(cleaned_string)
        return loaded_result
    except json.JSONDecodeError as e:
        print(f"ERROR PRODUCING JSON {e}")
    return None


def extract_inner_content(response):
    start_index = response.find('{')
    end_index = response.rfind('}') + 1
    inner_content = response[start_index:end_index]
    inner_content = inner_content.replace("'", '"')
    inner_content = inner_content.replace(".", '')
    return inner_content


# # fixme: main for testing purposes
# if __name__ == '__main__':
#     text = """
#     Artemis Corp was founded by Athena Helios in the year 2010, with its headquarters located in the city of Olympus,
#     which is part of the country Skyland. Athena Helios is married to Apollo Solaris, who works as an astrophysicist
#     at the Solar Research Institute. The institute itself has been in operation since 1985.
#     Athena Helios is well known for her achievements, including receiving the prestigious Golden Innovation Award.
#     She was also mentored by Hestia Ignis, a renowned molecular chemist who won the Nobel Prize in Chemistry for her
#     contributions to the field. Artemis Corp also developed a significant project known as Hyperion, which aims to
#     provide renewable energy solutions, and it earned the Green Tech Prize for its groundbreaking advancements.
#     Apollo Solaris, aside from his work at the Solar Research Institute, made a significant discovery—a star named
#     Solaris Nova, which is located in the constellation Phoenix.
#     """
#     # json_sbagliato = "ecco a te la risposta bastardo {'1': 'x', '2': y'}x fai cosa credi"
#     # print(extract_inner_content(json_sbagliato))
#     produce_topic_and_summary(text)
