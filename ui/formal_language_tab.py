import streamlit as st


def render():
    st.subheader("Formal Language Specification")

    st.markdown(
        """
**Master alphabet (15 symbols):**

`0 1 2 3 4 5 6 7 8 9 : ␣ A M P`  (␣ = one literal space)

**Languages:**

- L24 = { h ":" m | h = 00-23, m = 00-59 }
- L12 = { h ":" m ␣ r | h = 01-12, m = 00-59, r in {AM, PM} }
- L_TIME = L24 ∪ L12 (no mode selection)
"""
    )

    st.markdown("**Programming regex (implementation reference):**")
    st.code(r"^((([01][0-9]|2[0-3]):[0-5][0-9])|((0[1-9]|1[0-2]):[0-5][0-9] (AM|PM)))$")

    st.markdown(
        """
**Accepted examples:** `00:00`, `12:49`, `23:59`, `01:05 AM`, `12:00 PM`

**Rejected examples:** `24:00`, `12:60`, `13:00 PM`, `00:30 AM`, `09:30AM`, `ab:cd`

Full details: `docs/FORMAL_SPECIFICATION.md`
"""
    )