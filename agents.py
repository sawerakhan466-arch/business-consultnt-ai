from crewai import Agent
from llm import get_llm


def create_market_researcher():

    return Agent(

        role="Market Research Specialist",

        goal=(
            "Research the business market and identify "
            "target customers, competitors, trends, "
            "opportunities and threats."
        ),

        backstory=(
            "You are an experienced market researcher. "
            "You carefully analyze customer needs, "
            "competitors and market conditions. "
            "You never invent statistics or facts."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False
    )


def create_business_analyst():

    return Agent(

        role="Business Analyst",

        goal=(
            "Analyze the market research and determine "
            "the business's strengths, weaknesses, "
            "opportunities, threats, value proposition "
            "and major business risks."
        ),

        backstory=(
            "You are a practical business analyst. "
            "You transform research into clear business "
            "insights and identify important assumptions."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False
    )


def create_strategy_consultant():

    return Agent(

        role="Business Strategy Consultant",

        goal=(
            "Develop a practical business strategy "
            "based on the market research and business analysis."
        ),

        backstory=(
            "You are an experienced strategy consultant. "
            "You focus on realistic execution, "
            "customer acquisition, competitive positioning "
            "and sustainable growth."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False
    )


def create_report_writer():

    return Agent(

        role="Business Strategy Report Writer",

        goal=(
            "Create a professional business strategy report "
            "by combining the work of all previous agents."
        ),

        backstory=(
            "You are a senior consulting report writer. "
            "You organize complex business information into "
            "a clear, structured and useful final report."
        ),

        llm=get_llm(),

        verbose=True,

        allow_delegation=False
    )
