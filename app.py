import streamlit as st
import os
from dotenv import load_dotenv
from chatbot import initialize_chat, handle_user_input

# Cargar las variables de entorno
load_dotenv()

# Función principal para la aplicación de Streamlit
def main():
    st.title('Invention Disclosure Form')

    # Sección: Name of the Invention
    st.header('Name of the Invention')
    name_of_invention = st.text_input('Enter the name of the invention')

    # Sección: Inventor(s)
    st.header('Inventor(s)')
    inventors = st.text_area('Enter the inventors details')

    # Sección: Conception
    st.header('Conception')
    conception_date = st.date_input('When was the invention conceived?')
    first_record_date = st.date_input('When was the first written record made?')

    # Sección: Previous Disclosure
    st.header('Previous Disclosure')
    previous_disclosure = st.radio('Has the invention been disclosed previously?', ('Yes', 'No'))
    if previous_disclosure == 'Yes':
        disclosure_details = st.text_area('Provide the details of the previous disclosure')

    # Sección: Keywords
    st.header('Keywords')
    keywords = st.text_area('Enter at least 6 keywords that describe the technology (Spanish and English)')

    # Sección: Purpose of the Invention
    st.header('Purpose of the Invention')
    purpose = st.text_area('Describe the problem and the application of the invention')

    # Sección: Detailed Description of the Invention
    st.header('Detailed Description of the Invention')
    detailed_description = st.text_area('Describe the invention in detail including images, graphs, and diagrams')

    # Sección: State of the Art of the Invention
    st.header('State of the Art of the Invention')
    state_of_art = st.text_area('Describe the background of the invention including references, patents, publications, etc.')

    # Sección: Commercial Applications
    st.header('Commercial Applications')
    commercial_applications = st.text_area('Describe the specific industrial sector that would impact the invention and its use')

    # Sección: Contacts with Companies
    st.header('Contacts with Companies')
    contacts = st.text_area('Indicate if there are previous contacts with companies interested in the invention')

    # Sección: Development
    st.header('Development')
    development = st.text_area('Describe the degree of progress of the proposed invention through the technology readiness level (TRL)')

    # Sección: Outstanding Challenges
    st.header('Outstanding Challenges')
    challenges = st.text_area('Describe the outstanding challenges in order to turn your invention into a marketable innovation')

    # Sección: Program or Contract
    st.header('Program or Contract')
    program_contract = st.radio('Was the invention made in the context of a specific program, grant, or contract?', ('Yes', 'No'))
    if program_contract == 'Yes':
        program_details = st.text_area('Provide the details of the program, grant, or contract')

    # Sección: Witnesses
    st.header('Witnesses')
    witnesses = st.text_area('Enter the details of witnesses validating this information')

    # Sección: Relevant Information of this Document
    st.header('Relevant Information of this Document')
    completed_by = st.text_input('Completed by')
    date_completed = st.date_input('Date completed')
    sent_by = st.text_input('Sent by')
    date_sent = st.date_input('Date sent')
    received_by = st.text_input('Received by')
    date_received = st.date_input('Date received')

    # Sección: Bibliography
    st.header('Bibliography')
    bibliography = st.text_area('Add the references cited in the document')

    # Ventana de chat
    st.sidebar.title("Asistente Virtual")
    initialize_chat()

    # Entrada de usuario para el chat
    if prompt := st.sidebar.text_input("You: ", key="input"):
        handle_user_input(prompt)

    # Botón para enviar el formulario
    if st.button('Submit'):
        st.write("Form submitted successfully!")
        # Aquí podrías agregar código para manejar el envío de datos, como guardarlos en una base de datos o enviarlos por correo electrónico.

if __name__ == "__main__":
    main()


