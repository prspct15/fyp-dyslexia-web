# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Dyslexic Handwriting Detection Using Machine Learning",
        page_icon="✏️",
    )

    st.title("Dyslexic Handwriting Detection Using Machine Learning")

    st.sidebar.title("CS259 Final Year Project")

    st.sidebar.success("Navigate between pages using the sidebar.")

    st.markdown(
        """
        Dyslexic Handwriting Detection Using Machine Learning is a project made by Adam Fahim.
        \\
        \\
        **This project is made in partial fulfilment of the requirements for the degree of Bachelor of Information Systems (Hons.) Intelligent Systems Engineering**.
        ### Want to discover more about the project?
        - Check out the [GitHub repository](https://github.com/prspct15/fyp-dyslexia)
        - View the [FN](https://vadubacoco.one)
        - Hello bro.. have you heard of [Temu](https://temu.com)
    """
    )


if __name__ == "__main__":
    run()
