import streamlit as st

st.set_page_config(
    page_title="CampusNav AI",
    page_icon="🧭",
    layout="wide"
)

# -----------------------------
# CAMPUS DATA
# -----------------------------

campus = {
    "Engineering Block": {
        "purpose": "Department and HOD related work",
        "documents": "Student ID"
    },
    "Student Section": {
        "purpose": "Forms, certificates and student documents",
        "documents": "Application form + Student ID"
    },
    "Accounts Office": {
        "purpose": "Fees and payment related work",
        "documents": "Fee receipt + Student ID"
    },
    "Library": {
        "purpose": "Books and learning resources",
        "documents": "Student ID"
    },
    "Computer Lab": {
        "purpose": "Practical and computer related work",
        "documents": "Student ID"
    }
}


# -----------------------------
# MISSION PLANNER
# -----------------------------

def find_mission(task):

    task = task.lower()

    if "scholarship" in task:
        return {
            "title": "🎓 Scholarship Submission",
            "steps": [
                "1. Engineering Block → Get department/HOD verification",
                "2. Student Section → Submit scholarship application"
            ],
            "documents": [
                "Scholarship application form",
                "Student ID",
                "Required supporting documents"
            ],
            "route": "Engineering Block → Student Section"
        }

    elif "fee" in task or "fees" in task:
        return {
            "title": "💳 Fee Payment",
            "steps": [
                "1. Accounts Office → Complete fee/payment process"
            ],
            "documents": [
                "Student ID",
                "Fee receipt/payment details"
            ],
            "route": "Accounts Office"
        }

    elif "certificate" in task or "bonafide" in task:
        return {
            "title": "📄 Certificate Request",
            "steps": [
                "1. Student Section → Request the required certificate"
            ],
            "documents": [
                "Student ID",
                "Certificate application"
            ],
            "route": "Student Section"
        }

    elif "library" in task or "book" in task:
        return {
            "title": "📚 Library Visit",
            "steps": [
                "1. Library → Search or issue the required book"
            ],
            "documents": [
                "Student ID"
            ],
            "route": "Library"
        }

    elif "lab" in task or "practical" in task:
        return {
            "title": "💻 Computer Lab",
            "steps": [
                "1. Computer Lab → Complete your practical/lab work"
            ],
            "documents": [
                "Student ID"
            ],
            "route": "Computer Lab"
        }

    else:
        return None


# -----------------------------
# HEADER
# -----------------------------

st.title("🧭 CampusNav AI")
st.subheader("Your AI Guide Inside the Campus")

st.write(
    "Tell us what you need to accomplish, and CampusNav AI "
    "will help you find where to go, what to do, and what you need."
)

st.divider()


# -----------------------------
# MISSION INPUT
# -----------------------------

st.header("🎯 Mission Mode")

task = st.text_area(
    "What do you need to accomplish?",
    placeholder="Example: I need to submit my scholarship form."
)

if st.button("🚀 Plan My Mission"):

    if task:

        mission = find_mission(task)

        if mission:

            st.success("Mission identified!")

            st.subheader(mission["title"])

            # Mission progress
            st.markdown("### 🗺️ Your Mission Route")

            route_parts = mission["route"].split(" → ")

            for i, place in enumerate(route_parts):

                if i < len(route_parts) - 1:
                    st.info(f"📍 {place}  ➜")
                else:
                    st.success(f"🏁 {place} — Mission Complete")

            st.markdown("### 📋 What to do")

            for step in mission["steps"]:
                st.write(step)

            st.markdown("### 📑 What you need")

            for document in mission["documents"]:
                st.write("✅", document)

        else:

            st.warning(
                "I couldn't identify this campus task yet. "
                "Try scholarship, fees, certificate, library or lab."
            )

    else:
        st.warning("Please enter a task first.")


# -----------------------------
# CAMPUS LOCATIONS
# -----------------------------

st.divider()

st.header("🏫 Campus Locations")

columns = st.columns(3)

for i, (location, details) in enumerate(campus.items()):

    with columns[i % 3]:

        st.markdown(f"### 📍 {location}")

        st.write(details["purpose"])

        st.caption(
            f"Requirement: {details['documents']}"
        )