from crewai import Task


def create_market_task(agent):

    return Task(

        description="""

Analyze the following business:

Business Name:
{business_name}

Business Idea:
{business_idea}

Target Market:
{target_market}

Location:
{location}

Budget:
{budget}


Research and analyze:

1. Target customer segments
2. Customer problems
3. Customer needs
4. Direct competitors
5. Indirect competitors
6. Market trends
7. Opportunities
8. Threats
9. Market barriers
10. Important assumptions

Do not invent precise statistics.

Clearly identify information
that needs further validation.

""",

        expected_output="""

A structured market research report
covering customers, competitors,
trends, opportunities, threats
and assumptions.

""",

        agent=agent
    )


def create_analysis_task(
    agent,
    market_task
):

    return Task(

        description="""

Using the market research from the
previous agent, perform a detailed
business analysis.

Analyze:

1. Problem-solution fit
2. Value proposition
3. Target customer
4. Competitive position
5. Strengths
6. Weaknesses
7. Opportunities
8. Threats
9. Revenue logic
10. Cost considerations
11. Business risks
12. Validation requirements

Be analytical and realistic.

Do not treat assumptions as facts.

""",

        expected_output="""

A detailed business analysis including
value proposition, competitive position,
SWOT-style analysis, revenue considerations,
risks and validation priorities.

""",

        agent=agent,

        context=[market_task]
    )


def create_strategy_task(
    agent,
    market_task,
    analysis_task
):

    return Task(

        description="""

Develop a practical business strategy
using the market research and business analysis.

The strategy should include:

1. Business positioning
2. Customer acquisition
3. Marketing channels
4. Pricing/revenue approach
5. Operations
6. Competitive differentiation
7. 30-day action plan
8. 90-day action plan
9. Growth opportunities
10. KPIs
11. Risk mitigation

Make the strategy realistic for the
target market, location and budget.

""",

        expected_output="""

A practical business strategy containing
positioning, marketing, customer acquisition,
revenue approach, operations, growth plan,
KPIs and risk mitigation.

""",

        agent=agent,

        context=[
            market_task,
            analysis_task
        ]
    )


def create_report_task(
    agent,
    market_task,
    analysis_task,
    strategy_task
):

    return Task(

        description="""

Create the final business strategy report
using the outputs of all previous agents.

Use this structure:

# Executive Summary

# Business Overview

# Target Customers

# Market Research

# Competitive Landscape

# Business Analysis

# Value Proposition

# Business Strategy

# Marketing and Customer Acquisition

# Revenue and Pricing Approach

# Operations

# 30-Day Action Plan

# 90-Day Action Plan

# Key Performance Indicators

# Risks and Mitigation

# Assumptions and Validation Questions

# Conclusion


The report must be:

- Clear
- Practical
- Specific
- Professional

Do not invent statistics or unsupported
competitor information.

""",

        expected_output="""

A complete professional business
strategy report in Markdown format.

""",

        agent=agent,

        context=[
            market_task,
            analysis_task,
            strategy_task
        ]
    )
