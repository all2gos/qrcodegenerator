import streamlit as st
import qrcode
from PIL import Image

st.set_page_config(page_title='QR Code Generator', page_icon=':link:')

st.title("QR Code Generator by all2")
st.write('Yes, it is possible to create a QR code generator which is free, easy to use, without any watermarks, exactly as you wish that this kind of tool should work.')

st.header("Enter the text or URL to generate a QR code:")
st.write('Of course, I trust your intelligence, and I assume I don’t need to tell you that pasting sensitive or illegal data here is entirely your responsibility, and you do so at your own risk. Normal links are welcome.')
input_text = st.text_area("Input Text or URL", "")

if "generate" not in st.session_state:
    st.session_state.generate = False

if st.button("Generate QR Code"):
    st.session_state.generate = True

if st.session_state.generate:
    BOX_SIZE = st.number_input('Image size', min_value=1, max_value=20, value=4, step=1)
    BORDER = st.number_input('Border size', min_value=1, max_value=20, value=3, step=1)
    col1, col2 = st.columns(2)

    with col1:
        BACKGROUND_COLOR = st.color_picker("Background Color", "#FFFFFF")
    with col2:
        QR_COLOR = st.color_picker("QR Code Color", "#000000")
    TYPE_OF_QR = st.number_input('Size of Matrix (1-20)', min_value=1, max_value=20, value=1, step=1)

    if input_text.strip() == "":
        st.error("Please enter some text or URL to generate a QR code.")
    else:

        qr = qrcode.QRCode(
            version=TYPE_OF_QR,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=BOX_SIZE,
            border=BORDER,
        )

        qr.add_data(input_text)
        qr.make(fit=True)
        img = qr.make_image(fill_color=QR_COLOR, back_color=BACKGROUND_COLOR).convert('RGB')

        st.image(img, caption="Generated QR Code")
        st.success("QR Code generated successfully!")
        st.button("Download QR Code (.png format)", on_click=lambda: img.save("qrcode.png"))

        if st.success:
            st.markdown("I hope everything worked out! I'm glad I could help. As I mentioned, the service is free—there are no hidden fees or watermarks. However, if you’d like, **you can buy me a coffee [here](https://buymeacoffee.com/all2).**")


        



