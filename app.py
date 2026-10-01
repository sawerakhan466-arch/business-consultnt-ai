import streamlit as st
from business_crew import run_business_consulting


st.set_page_config(
    page_title="AI Business Consulting Team",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI Business Consulting Team")

st.write(
    "A multi-agent AI system that researches, analyzes, "
    "and creates a business strategy report."
)


# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.header("Business Information")

    business_name = st.text_input(
        "Business / Product Name",
        placeholder="e.g. StudyMate AI"
    )

    business_idea = st.text_area(
        "Business Idea",
        placeholder="Describe your business idea...",
        height=150
    )

    target_market = st.text_input(
        "Target Market",
        placeholder="e.g. University students in Pakistan"
    )

    location = st.text_input(
        "Location / Region",
        placeholder="e.g. Pakistan"
    )

    budget = st.text_input(
        "Approximate Budget",
        placeholder="e.g. PKR 500,000"
    )

    generate = st.button(
        "🚀 Generate Strategy",
        use_container_width=True
    )


# -----------------------------
# Generate Report
# -----------------------------

if generate:

    if not business_idea.strip():

        st.error("Please enter a business idea.")

        st.stop()


    business_name = (
        business_name.strip()
        or "Unnamed Business"
    )

    target_market = (
        target_market.strip()
        or "Not specified"
    )

    location = (
        location.strip()
        or "Not specified"
    )

    budget = (
        budget.strip()
        or "Not specified"
    )


    with st.spinner(
        "🤖 AI consulting team is working..."
    ):

        try:

            result = run_business_consulting(
                business_name,
                business_idea,
                target_market,
                location,
                budget
            )

        except Exception as e:

            st.error(
                f"Something went wrong: {e}"
            )

            st.stop()


    st.success(
        "✅ Business strategy generated!"
    )

    st.subheader(
        "📊 Business Strategy Report"
    )

    st.markdown(result)


else:

    st.info(
        "Enter your business information "
        "and click Generate Strategy."
    )

    st.markdown(
        """
### 🤖 AI Consulting Team

**🔎 Market Researcher**

Researches:
- Target customers
- Competitors
- Market trends
- Opportunities
- Threats

**📊 Business Analyst**

Analyzes:
- Business model
- Customer needs
- Value proposition
- Strengths and weaknesses
- Risks

**🎯 Strategy Consultant**

Develops:
- Business positioning
- Marketing strategy
- Pricing strategy
- Customer acquisition
- Growth strategy

**📝 Report Writer**

Creates the final:
- Business analysis
- Strategy
- Action plans
- KPIs
- Risk analysis
"""
    )
