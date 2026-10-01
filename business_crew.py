from crewai import Crew, Process

from agents import (
    create_market_researcher,
    create_business_analyst,
    create_strategy_consultant,
    create_report_writer
)

from tasks import (
    create_market_task,
    create_analysis_task,
    create_strategy_task,
    create_report_task
)


def run_business_consulting(
    business_name,
    business_idea,
    target_market,
    location,
    budget
):

    # -----------------------------
    # Create Agents
    # -----------------------------

    market_researcher = (
        create_market_researcher()
    )

    business_analyst = (
        create_business_analyst()
    )

    strategy_consultant = (
        create_strategy_consultant()
    )

    report_writer = (
        create_report_writer()
    )


    # -----------------------------
    # Create Tasks
    # -----------------------------

    market_task = create_market_task(
        market_researcher
    )

    analysis_task = create_analysis_task(
        business_analyst,
        market_task
    )

    strategy_task = create_strategy_task(
        strategy_consultant,
        market_task,
        analysis_task
    )

    report_task = create_report_task(
        report_writer,
        market_task,
        analysis_task,
        strategy_task
    )


    # -----------------------------
    # Create Crew
    # -----------------------------

    consulting_crew = Crew(

        agents=[
            market_researcher,
            business_analyst,
            strategy_consultant,
            report_writer
        ],

        tasks=[
            market_task,
            analysis_task,
            strategy_task,
            report_task
        ],

        process=Process.sequential,

        verbose=True
    )


    # -----------------------------
    # Run Crew
    # -----------------------------

    result = consulting_crew.kickoff(

        inputs={

            "business_name": business_name,

            "business_idea": business_idea,

            "target_market": target_market,

            "location": location,

            "budget": budget
        }
    )


    return result.raw
