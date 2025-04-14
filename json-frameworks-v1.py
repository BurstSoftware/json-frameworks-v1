import streamlit as st

# Data: Dictionary of languages and their JSON frameworks
json_frameworks = {
    "JavaScript": [
        {"name": "Native JSON", "description": "Built-in JSON.parse() and JSON.stringify()"},
        {"name": "Lodash", "description": "Enhances JSON manipulation"}
    ],
    "Python": [
        {"name": "json (stdlib)", "description": "Built-in module for JSON encoding/decoding"},
        {"name": "simplejson", "description": "Faster alternative to json"},
        {"name": "ujson", "description": "Ultra-fast JSON parsing"}
    ],
    "Java": [
        {"name": "Jackson", "description": "High-performance JSON processing"},
        {"name": "Gson", "description": "Lightweight, by Google"},
        {"name": "FastJSON", "description": "Optimized for speed"},
        {"name": "org.json", "description": "Simple, minimalistic"}
    ],
    "C#": [
        {"name": "System.Text.Json", "description": "Built-in, lightweight, and fast"},
        {"name": "JSON.NET (Newtonsoft.Json)", "description": "Feature-rich, widely used"}
    ],
    "C++": [
        {"name": "RapidJSON", "description": "Fast and efficient"},
        {"name": "jsoncpp", "description": "Simple and portable"},
        {"name": "nlohmann/json", "description": "Modern, header-only library"}
    ],
    "PHP": [
        {"name": "json_encode/json_decode", "description": "Built-in JSON functions"}
    ],
    "Ruby": [
        {"name": "json (stdlib)", "description": "Standard library for JSON parsing"},
        {"name": "Oj", "description": "Optimized JSON parsing"}
    ],
    "Go": [
        {"name": "encoding/json", "description": "Standard library for JSON handling"},
        {"name": "jsoniter", "description": "Faster alternative"}
    ],
    "Rust": [
        {"name": "serde_json", "description": "Efficient JSON serialization/deserialization"},
        {"name": "rustc_serialize", "description": "Alternative with JSON support"}
    ],
    "Scala": [
        {"name": "Circe", "description": "Functional, type-safe JSON processing"},
        {"name": "Play JSON", "description": "Flexible, part of Play Framework"}
    ]
    # Add more languages from the previous lists as needed
}

# Streamlit app
st.title("JSON Frameworks by Language")

# Dropdown at the top
selected_language = st.selectbox(
    "Select a Programming Language",
    options=list(json_frameworks.keys()),
    index=0  # Default to the first language
)

# Display the list of frameworks for the selected language
st.subheader(f"JSON Frameworks for {selected_language}")
frameworks = json_frameworks[selected_language]

for framework in frameworks:
    st.write(f"**{framework['name']}**: {framework['description']}")

# Optional: Add a note about expanding the list
st.write("Note: This is a sample list. More languages and frameworks can be added!")
