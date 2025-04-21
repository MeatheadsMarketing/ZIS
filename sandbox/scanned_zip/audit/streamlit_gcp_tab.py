import streamlit as st
from clients.google_drive_client import upload_file_to_drive
from clients.google_sheets_client import append_to_sheet
from clients.vertex_client import call_vertex

st.title("🧠 GCP Assistant Panel")

st.subheader("📁 Upload File to Google Drive")
file = st.file_uploader("Select a file to upload")
if file:
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    file_id = upload_file_to_drive(file.name)
    st.success(f"Uploaded! File ID: {file_id}")

st.subheader("📄 Append to Google Sheet")
spreadsheet_id = st.text_input("Spreadsheet ID")
sheet_range = st.text_input("Range (e.g. Sheet1!A1)")
row_data = st.text_area("Comma-separated values (e.g. value1,value2,value3)")
if st.button("Append Row"):
    values = [row_data.split(",")]
    result = append_to_sheet(spreadsheet_id, sheet_range, values)
    st.success("Row appended")

st.subheader("🧠 Run Prompt in Vertex AI")
prompt = st.text_area("Enter prompt for Vertex AI")
if st.button("Run Vertex Prompt"):
    output = call_vertex(prompt)
    st.code(output)