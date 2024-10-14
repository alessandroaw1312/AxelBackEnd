from BE.src.llm.prompts import EXTRACT_ENITTY_FROM_QUERY, CHAT_TEMPLATE, TOPIC_AND_SUMMARY_TEMPLATE, \
    CHAT_TEMPLATE_NO_CONTEXT


def get_entity_recognition_template():
    return EXTRACT_ENITTY_FROM_QUERY


def get_chat_template():
    return CHAT_TEMPLATE


def get_chat_template_no_context():
    return CHAT_TEMPLATE_NO_CONTEXT


def get_topic_and_summary_template():
    return TOPIC_AND_SUMMARY_TEMPLATE
